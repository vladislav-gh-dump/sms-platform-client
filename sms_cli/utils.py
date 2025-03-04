import tomllib


def load_toml(file_path: str) -> dict:
    """Загрузка данных из TOML файла."""
    
    with open(file_path, 'rb') as toml_file:
        return tomllib.load(toml_file)
