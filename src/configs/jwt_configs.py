import os

def __get_env(key: str) -> str:
    value = os.getenv(key)
    if value is None:
        raise ValueError(f"Variável de ambiente {key} não configurada")
    return value

jwt_infos = {
    "KEY": __get_env("JWT_KEY"),
    "ALGORITHM": __get_env("JWT_ALGORITHM"),
    "JWT_HOURS": __get_env("JWT_HOURS"),
}
