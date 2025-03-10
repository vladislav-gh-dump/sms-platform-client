import socket

from .config import ServerConfig, AuthConfig
from .http_messages import HttpRequest, HttpResponse
from .logger import logger


def send_sms(sender: str, recipient: str, message: str):
    body = {
        "sender": sender,
        "recipient": recipient,
        "message": message
    }
    auth = (
        AuthConfig.USERNAME,
        AuthConfig.PASSWORD
    )
    
    request = HttpRequest(
        ServerConfig.HOST, ServerConfig.PATH,
        auth, body
    )
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((
                ServerConfig.HOST,
                ServerConfig.PORT
            ))
            s.sendall(request.to_bytes())
            
            response_data = s.recv(1024)
            response = HttpResponse.from_bytes(response_data)
            
            logger.info(f"Response:\n{response}")
            print(response)
            
        except socket.error as ex:
            logger.error(f"Connection error: {ex}")
            print(f"Connection error: {ex}")
