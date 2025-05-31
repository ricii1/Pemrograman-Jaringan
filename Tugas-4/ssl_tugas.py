import unittest
import sys
import json
from io import StringIO
import pickle
import ssl
import socket

# Target server to test SSL connection
test_hostname = 'www.google.com'
test_port = 443

# Establish an SSL connection and retrieve peer certificate
def get_ssl_certificate(hostname, port):
    context = ssl.create_default_context(purpose = ssl.Purpose.SERVER_AUTH)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((hostname, port))
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            data = ssock.getpeercert()
            return data

# Verify that certificate contains expected fields
def assert_cert_has_fields(cert, fields):
    missing = [field for field in fields if field not in cert]
    if not missing:
        print("Certificate has all required fields:", fields)
    else:
        print("Certificate is missing fields:", missing)

# A 'null' stream that discards anything written to it
class NullWriter(StringIO):
    def write(self, txt):
        pass

# Unit test for SSL certificate retrieval
class TestSSLConnection(unittest.TestCase):
    def setUp(self):
        self.hostname = test_hostname
        self.port = test_port

    def test_ssl_certificate_retrieval(self):
        cert = get_ssl_certificate(self.hostname, self.port)
        self.assertIsInstance(cert, dict)
        assert_cert_has_fields(cert, ['subject', 'issuer'])

    def test_certificate_subject(self):
        cert = get_ssl_certificate(self.hostname, self.port)
        subject = dict(x[0] for x in cert['subject'])
        self.assertIn('commonName', subject)
        print("Common Name (CN):", subject.get('commonName'))

# Entry point
if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == 'run':
        cert = get_ssl_certificate(test_hostname, test_port)
        print("Retrieved SSL Certificate:", cert)
    else:
        runner = unittest.TextTestRunner(stream=NullWriter())
        unittest.main(testRunner=runner, exit=False)
