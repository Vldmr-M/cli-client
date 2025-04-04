import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
import pytest
from models import HttpResponse

def test_http_response_creation():
    # Test the creation of the HttpResponse object
    status = "HTTP/1.1 200 OK"
    headers = "Content-Type: application/json"
    body = '{"status": "success"}'

    response = HttpResponse(status, headers, body)

    # Verify the response status, headers, and body
    assert response.status == status
    assert response.headers == headers
    assert response.body == body

def test_http_response_from_bytes():
    # Test the conversion of response bytes to HttpResponse object
    response_bytes = b"HTTP/1.1 200 OK\r\nContent-Type: application/json\r\n\r\n{\"status\": \"success\"}"

    response = HttpResponse.from_bytes(response_bytes)

    # Verify that the HttpResponse object was created correctly
    assert response.status == "HTTP/1.1 200 OK\r"
    assert response.headers == "Content-Type: application/json\r\n\r"
    assert response.body == '{"status": "success"}'

def test_http_response_repr():
    # Test the __repr__ method of HttpResponse
    status = "HTTP/1.1 200 OK"
    headers = "Content-Type: application/json"
    body = '{"status": "success"}'

    response = HttpResponse(status, headers, body)

    # Verify the string representation
    repr_str = repr(response)
    assert 'HTTP RESPONSE:' in repr_str
    assert 'STATUS_CODE: 200' in repr_str
    assert 'BODY: {"status": "success"}' in repr_str
