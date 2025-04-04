class HttpRequest:
    def __init__(self, path: str, auth_header: str, body: str):
        self.headers = {
            "Authorization": f"Basic {auth_header}",
            "Host": "localhost",
            "Content-Type": "application/json",
            "Content-Length": len(body)
        }
        self.path = path
        self.body = body

    def to_bytes(self) -> bytes:
        http_request = f'POST {self.path} HTTP/1.1\r\n' + \
                       '\r\n'.join([f'{key}:{val}' for key, val in self.headers.items()]) + \
                       '\r\n\n' + self.body
        return http_request.encode("utf-8")

    def __repr__(self):
        return 'HTTP REQUEST:\n' + \
            f'   STATUS: POST {self.path} HTTP/1.1\r\n' + \
            '   BODY: ' + str(self.body)


class HttpResponse:
    def __init__(self, status, headers, body):
        self.status = status
        self.headers = headers
        self.body = body

    @classmethod
    def from_bytes(cls, bts: bytes):
        response = bts.decode("utf-8")
        status, other = response.split("\n", 1)
        headers, body = other.rsplit("\n", 1)
        return cls(status, headers, body)

    def __repr__(self):
        return 'HTTP RESPONSE:\n' + "   STATUS_CODE: " + \
            self.status.split()[1] + "\n" + "   BODY: " + self.body
