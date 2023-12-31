from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from switchbot import get_devices, trigger_garage_switch
from os import environ as env
from pydantic import BaseModel

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
    "https://sams-auto-home-react-3js6vcbkca-uw.a.run.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

class TriggerGarageRequest(BaseModel):
    password: str


@app.post("/garage")
def trigger_garage(request: TriggerGarageRequest, response: Response):
    if invalid_password(request.password):
        response.status_code = 401
        return response
    
    result = trigger_garage_switch().json()
    if result['statusCode'] != 100:
        # something went wrong with triggering the switchbot. it's not important to the user what the error was so we will just return a 500 error
        response.status_code = 500
        return response
    return {"message": 'success'}

def invalid_password(password):
    return password != env['GARAGE_PASSWORD']