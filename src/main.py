import socket
import json
import logging
from models import HttpResponse, HttpRequest
import cli
import config

logging.basicConfig(level=logging.INFO, filename="./log/py_log.log", filemode="w")


def make_body() -> str:
    sender, recipient, message = cli.parse_args()
    logging.info(f"params from command-line:\n   sender: {sender}\n   recipient: {recipient}\n   message: {message}")
    return json.dumps({"sender": sender, "recipient": recipient, "message": message})


def get_response(s: socket.socket) -> bytes:
    response = b""
    try:
        while True:
            data = s.recv(4096)
            if len(data) == 0:
                break
            response += data
    except Exception as e:
        logging.error(f"Error when receiving the response: {e}")
    return response


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.settimeout(10)

    request = HttpRequest("/send_sms", config.auth_header, make_body()).to_bytes()

    try:
        s.connect((config.config["server"]["host"], config.config["server"]["port"]))
        logging.info("Connection is established")

        s.sendall(request)
        logging.info("The request has been sent")

        response = HttpResponse.from_bytes(get_response(s))
    except socket.timeout:
        logging.error("Error: The time was exceeded when connecting or receiving data")
    except Exception as e:
        logging.error(f"Error when connecting or sending data: {e}")
    else:
        logging.info(f"Response received:\n{response}")
        print(response)
