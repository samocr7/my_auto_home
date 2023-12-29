from fastapi import FastAPI
from switchbot import get_devices
from os import environ as env

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World!!!!", 'devices': get_devices().json(), 'env_var': env['MY_VAR']}