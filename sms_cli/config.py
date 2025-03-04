from dataclasses import dataclass
from utils import load_toml


_config_path = "config.toml"
_config = load_toml(_config_path)


@dataclass(frozen=True)
class ServerConfig:
    HOST: str = _config["server"]["host"]
    PORT: str = _config["server"]["port"]
    PATH: str = _config["server"]["path"]


@dataclass(frozen=True)
class AuthConfig:
    USERNAME: str = _config["auth"]["username"]
    PASSWORD: str = _config["auth"]["password"]
