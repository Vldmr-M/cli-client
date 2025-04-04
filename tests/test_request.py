import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
import pytest
from models import HttpRequest

def test_http_request_creation():
    # Test the creation of the HttpRequest object
    path = "/send_sms"
    auth_header = "someAuthTokenHere"
    body = '{"sender": "12345", "recipient": "67890", "message": "Hello"}'

    request = HttpRequest(path, auth_header, body)

    # Verify the request path, headers, and body
    assert request.path == path
    assert request.body == body
    assert request.headers["Authorization"] == "Basic someAuthTokenHere"
    assert request.headers["Host"] == "localhost"
    assert request.headers["Content-Type"] == "application/json"
    assert request.headers["Content-Length"] == len(body)

def test_http_request_to_bytes():
    # Test the conversion of HttpRequest to bytes
    path = "/send_sms"
    auth_header = "someAuthTokenHere"
    body = '{"sender": "12345", "recipient": "67890", "message": "Hello"}'

    request = HttpRequest(path, auth_header, body)
    request_bytes = request.to_bytes()

    # Verify that the byte conversion is correct
    expected_request = f'POST {path} HTTP/1.1\r\n' + \
                       'Authorization:Basic someAuthTokenHere\r\n' + \
                       'Host:localhost\r\n' + \
                       'Content-Type:application/json\r\n' + \
                       f'Content-Length:{len(body)}\r\n\n' + body
    expected_bytes = expected_request.encode("utf-8")

    assert request_bytes == expected_bytes

def test_http_request_repr():
    # Test the __repr__ method of HttpRequest
    path = "/send_sms"
    auth_header = "someAuthTokenHere"
    body = '{"sender": "12345", "recipient": "67890", "message": "Hello"}'

    request = HttpRequest(path, auth_header, body)

    # Verify the string representation
    repr_str = repr(request)
    assert 'HTTP REQUEST:' in repr_str
    assert 'POST /send_sms HTTP/1.1' in repr_str
    assert 'BODY: {"sender": "12345", "recipient": "67890", "message": "Hello"}' in repr_str
