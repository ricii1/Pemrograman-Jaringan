'''
Response Header Extraction
Description: Write a Python program that sends a GET request to
https://httpbin.org/response-headers?Content-Type=text/
html&Server=Domjudge and prints the value of the Server response
header. Use the socket module to solve this problem.


Output (with unit test):
connect called with: call(('httpbin.org', 80))
send called with: call(b'GET /response-headers?Content-Type=text/
html&Server=Domjudge HTTP/1.1\r\nHost: httpbin.org\r\nConnection:
close\r\n\r\n')
recv called with: call(1024)
test attribute passed: Domjudge is equal to Domjudge'''

import socket
import sys
import unittest
from io import StringIO
from unittest.mock import patch, MagicMock

def get_headers(header_text):
    headers = {}
    lines = header_text.split("\r\n")
    for line in lines:
        if ": " in line:
            key, value = line.split(": ",1)
            headers[key] = value
    return headers


def fetch_server_header():
    host = 'httpbin.org'
    port = 80
    request = b'GET /response-headers?Content-Type=text/html&Server=Domjudge HTTP/1.1\r\nHost: httpbin.org\r\nConnection: close\r\n\r\n'

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(3) #KALO KENAK TIMELIMIT
        s.connect((host, port))
        s.send(request)
        response = b''
        while True:
            temp = s.recv(1024)
            if not temp:
                break
            response += temp
    header_text = response.decode()
    header_temp = header_text.split("\r\n\r\n")[0]
    headers = get_headers(header_temp)
    return headers.get("Server", "")


# A 'null' stream that discards anything written to it
class NullWriter(StringIO):
    def write(self, txt):
        pass


def assert_equal(parameter1, parameter2):
    if parameter1 == parameter2:
        print(f'test attribute passed: {parameter1} is equal to {parameter2}')
    else:
        print(f'test attribute failed: {parameter1} is not equal to {parameter2}')


class TestFetchServerHeader(unittest.TestCase):
    @patch('socket.socket')
    def test_fetch_server_header(self, mock_socket):
        # Setup the mocked socket instance
        mock_sock_instance = MagicMock()
        mock_socket.return_value.__enter__.return_value = mock_sock_instance

        # Define the mock response from the server
        http_response = (
            "HTTP/1.1 200 OK\r\n"
            "Content-Type: text/html\r\n"
            "Server: Domjudge\r\n"
            "\r\n"
            "body content"
        )
        mock_sock_instance.recv.side_effect = [http_response.encode('utf-8'), b'']

        # Call the function
        server = fetch_server_header()

        # Assertions to check if the correct server header was returned
        mock_sock_instance.connect.assert_called_once_with(('httpbin.org', 80))
        print(f"connect called with: {mock_sock_instance.connect.call_args}")

        mock_sock_instance.send.assert_called_once()
        print(f"send called with: {mock_sock_instance.send.call_args}")

        mock_sock_instance.recv.assert_called()
        print(f"recv called with: {mock_sock_instance.recv.call_args}")

        assert_equal(server, 'Domjudge')

if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == 'run':
        header = fetch_server_header()
        print(header)

    # run unit test to test locally
    # or for domjudge
    runner = unittest.TextTestRunner(stream=NullWriter())
    unittest.main(testRunner=runner, exit=False)
