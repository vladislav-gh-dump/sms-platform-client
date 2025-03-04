import json
from .utils import encode_creds


class HttpRequest:
    
    def __init__(
        self,
        host: str,
        path: str,
        auth: tuple[str, str],
        body: dict[str, str]
    ):

        encoded_creds = encode_creds(*auth)
        body_string = json.dumps(body)
        
        self.request = (
            f"POST {path} HTTP/1.1\r\n"
            f"Host: {host}\r\n"
            f"Authorization: Basic {encoded_creds}\r\n"
            "Content-Type: application/json\r\n"
            f"Content-Length: {len(body_string)}\r\n"
            f"\r\n{body_string}"
        )

    def to_bytes(self) -> bytes:
        return self.request.encode()


class HttpResponse:
    
    @classmethod
    def from_bytes(cls, binary_data: bytes):
        response = binary_data.decode()
        lines = response.split("\r\n")
        status_code = lines[0].split(" ")[1]
        body = json.loads(lines[-1])
        return cls(status_code, body)
    
    def __init__(self, status_code: str, body: dict):
        self.status_code = status_code
        self.body = body
        
    def __str__(self):
        body_string = json.dumps(self.body)
        return f"Status code: {self.status_code}\nBody: {body_string}"
