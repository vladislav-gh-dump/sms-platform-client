import tomllib
from base64 import b64encode


def load_toml(file_path: str) -> dict:
    """Загрузка данных из TOML файла."""
    
    with open(file_path, 'rb') as toml_file:
        return tomllib.load(toml_file)


def encode_creds(username: str, password: str) -> str:
    """Кодирование учетных данных в Base64."""
    
    creds_bytes = f"{username}:{password}".encode()
    return b64encode(creds_bytes).decode()
