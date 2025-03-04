import json
from sms_cli.http_messages import HttpRequest
from sms_cli.utils import encode_creds


def test_http_request_to_bytes():
    host = "host"
    path = "/path"
    
    username = "uname"
    password = "pwd"
    auth = (username, password)
    
    body = {
        "sender": "89207456123", 
        "recipient": "89107156170", 
        "message": "Hello!"
    }
    
    request = HttpRequest(host, path, auth, body)
    decoded_request_string = request.to_bytes().decode()

    encoded_creds = encode_creds(*auth)
    body_string = json.dumps(body)
    
    request_lines = decoded_request_string.split("\r\n")
    
    assert request_lines[0] == f"POST {path} HTTP/1.1"
    assert request_lines[1] == f"Host: {host}"     
    assert request_lines[2] == f"Authorization: Basic {encoded_creds}"
    assert request_lines[3] == "Content-Type: application/json"
    assert request_lines[4] == f"Content-Length: {len(body_string)}"
    assert request_lines[5] == ""
    assert request_lines[6] == body_string
    
    assert json.loads(request_lines[6]) == body
