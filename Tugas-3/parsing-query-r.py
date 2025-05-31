#CONNECTION CALLED WITH
'''
Parsing Query Parameters (http.client)
Description: Write a Python program that sends a GET request to
jsonplaceholder.typicode.com/comments with a query parameter
postId=1 and prints the number of comments for that post. Use
http.client module to connect to the server.


Output (with unit test):
test attribute passed: 1 is equal to 1
test attribute passed: 1 is equal to 1
test attribute passed: 1 is equal to 1
test attribute passed: John Doe is equal to John Doe
test attribute passed: johndoe@example.com is equal to
johndoe@example.com
test attribute passed: Great post! is equal to Great post!
connection called with: call('jsonplaceholder.typicode.com')
request called with: call('GET', '/comments?postId=1')
read called: b'[{"postId": 1, "id": 1, "name": "John Doe", "email":
"johndoe@example.com", "body": "Great post!"}]'
connection closed: call()'''

import http.client
import json
import sys
import unittest
from unittest import mock
from io import StringIO




def get_comments():
    conn = http.client.HTTPSConnection("jsonplaceholder.typicode.com")
    conn.request('GET', '/comments?postId=1')
    response = conn.getresponse()

    if response.status == 200:
        data = response.read()
        comments = json.loads(data)
        conn.close()
        return comments
    else:
        conn.close()
        return []


# A 'null' stream that discards anything written to it
class NullWriter(StringIO):
    def write(self, txt):
        pass


def assert_equal(parameter1, parameter2):
    if parameter1 == parameter2:
        print(f'test attribute passed: {parameter1} is equal to {parameter2}')
    else:
        print(f'test attribute failed: {parameter1} is not equal to {parameter2}')


class TestSolution(unittest.TestCase):
    @mock.patch('http.client.HTTPSConnection')
    def test_get_comments(self, mock_conn):
        # Mock the response
        mock_response = mock.Mock()
        mock_response.status = 200
        mock_response.read.return_value = b'[{"postId": 1, "id": 1, "name": "John Doe", "email": "johndoe@example.com", "body": "Great post!"}]'
        mock_conn.return_value.getresponse.return_value = mock_response

        # Call the function to be tested
        comments = get_comments()

        # Assertions
        assert_equal(len(comments), 1)
        assert_equal(comments[0]['postId'], 1)
        assert_equal(comments[0]['id'], 1)
        assert_equal(comments[0]['name'], "John Doe")
        assert_equal(comments[0]['email'], "johndoe@example.com")
        assert_equal(comments[0]['body'], "Great post!")

        # Assert the HTTP connection is called with the correct arguments
        mock_conn.assert_called_once_with("jsonplaceholder.typicode.com")
        print(f"connection called with: {mock_conn.call_args}")

        mock_conn.return_value.request.assert_called_once_with("GET", "/comments?postId=1")
        print(f"request called with: {mock_conn.return_value.request.call_args}")

        mock_response.read.assert_called_once()
        print(f"read called: {mock_response.read.return_value}")

        conn_close = mock_conn.return_value.close
        conn_close.assert_called_once()
        print(f"connection closed: {conn_close.call_args}")


if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == 'run':
        comments = get_comments()
        print(comments)

    # run unit test to test locally
    # or for domjudge
    runner = unittest.TextTestRunner(stream=NullWriter())
    unittest.main(testRunner=runner, exit=False)