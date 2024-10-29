from obswebsocket import obsws, requests
import json

source_name_text = "Text"
source_name_image = "pngwing.com.png"


def connect():
    host = "localhost"
    port = 4455
    password = "adeXWrJJMlMwdfb8"
    global ws
    ws = obsws(host, port, password)
    ws.connect()


def set_text(message: str):
    ws.call(requests.SetInputSettings(
        inputName=source_name_text, inputSettings={"text": message}))


def set_image_enabled(enabled: bool):
    sceneItemId = ws.call(requests.GetSceneItemId(
        sceneName="Scene", sourceName=source_name_image)).datain['sceneItemId']

    ws.call(requests.SetSceneItemEnabled(sceneName="Scene",
            sceneItemId=sceneItemId, sceneItemEnabled=enabled))


connect()
