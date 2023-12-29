import json
import time
import hashlib
import hmac
import base64
import uuid
import requests
from os import environ as env

TOKEN = env['SWITCHBOT_API_TOKEN']
SECRET = env['SWITCHBOT_API_SECRET']
GARAGE_DEVICE_ID = env['GARAGE_DEVICE_ID']

nonce = uuid.uuid4()
t = int(round(time.time() * 1000))
string_to_sign = '{}{}{}'.format(TOKEN, t, nonce)
string_to_sign = bytes(string_to_sign, 'utf-8')
secret = bytes(SECRET, 'utf-8')
sign = base64.b64encode(hmac.new(secret, msg=string_to_sign, digestmod=hashlib.sha256).digest())
API_HEADER = {
    'Authorization': TOKEN,
    'Content-Type': 'application/json',
    'charset': 'utf8',
    't': str(t),
    'sign': str(sign, 'utf-8'),
    'nonce': str(nonce)

}

def get_devices():
    get_url = "https://api.switch-bot.com/v1.1/devices"
    r = requests.get(get_url, headers=API_HEADER)
    return r



def trigger_garage_switch():
    post_url = f"https://api.switch-bot.com/v1.1/devices/{GARAGE_DEVICE_ID}/commands"
    post_body = {
        "command": "press",
        "parameter": "default",
        "commandType": "command"
    }
    r = requests.post(post_url, headers=API_HEADER, json=post_body)
    return r