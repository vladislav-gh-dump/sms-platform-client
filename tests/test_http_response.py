from sms_cli.http_messages import HttpResponse


def test_http_response_ok():
    raw_response = (
        b"HTTP/1.1 200 OK\r\n"
        b"Access-Control-Allow-Origin: *\r\n"
        b"Access-Control-Allow-Headers: *\r\n"
        b"Access-Control-Allow-Credentials: true\r\n"
        b"Access-Control-Expose-Headers: *\r\n"
        b"Content-type: application/json\r\n"
        b"Content-Length: 42\r\n"
        b"Date: Tue, 04 Mar 2025 01:51:42 GMT\r\n"
        b"Connection: keep-alive\r\n"
        b"Keep-Alive: timeout=5\r\n"
        b'\r\n{"status":"success","message_id":"123456"}'
    )

    response = HttpResponse.from_bytes(raw_response)
    
    assert response.status_code == "200"
    assert response.body["status"] == "success"
    assert response.body["message_id"] == "123456"
    
    assert str(response) == 'Status code: 200\nBody: {"status": "success", "message_id": "123456"}'


def test_http_response_bad():
    raw_response = (
        b"HTTP/1.1 400 Bad Request\r\n"
        b"Access-Control-Allow-Origin: *\r\n"
        b"Access-Control-Allow-Headers: *\r\n"
        b"Access-Control-Allow-Credentials: true\r\n"
        b"Access-Control-Expose-Headers: *\r\n"
        b'sl-violations: [{"location":["request","body"],"severity":"Error","code":"required","message":"Request body must have required property \'message\'"}]\r\n'
        b"Content-type: application/json\r\n"
        b"Content-Length: 30\r\n"
        b"Date: Tue, 04 Mar 2025 01:55:57 GMT\r\n"
        b"Connection: keep-alive\r\n"
        b"Keep-Alive: timeout=5\r\n"
        b'\r\n{"error":"Invalid parameters"}'
    )
    
    response = HttpResponse.from_bytes(raw_response)
    
    assert response.status_code == "400"
    assert response.body["error"] == "Invalid parameters"
    
    assert str(response) == 'Status code: 400\nBody: {"error": "Invalid parameters"}'
