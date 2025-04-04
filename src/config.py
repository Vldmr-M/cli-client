import tomllib
import base64

config = tomllib.load(open("./config/config.toml", 'rb'))

credentials = f"{config['auth']['username']}:{config['auth']['password']}".encode("utf-8")
auth_header = base64.b64encode(credentials).decode("utf-8")
