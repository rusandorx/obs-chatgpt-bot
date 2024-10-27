from obswebsocket import obsws, requests

source_name_text = "Text"


def connect():
    host = "localhost"
    port = 4455
    password = "z3IdMXZ8aV9UfhAJ"
    global ws
    ws = obsws(host, port, password)
    ws.connect()


def set_text(message: str):
    ws.call(requests.SetInputSettings(
        inputName=source_name_text, inputSettings={"text": message}))


connect()
