from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from fastap.encoders import jsonable_encoder
from pydantic import BaseModel
from enum import Enum, unique, IntEnum
from kafka import KafkaProducer
import datetime as dt 
import json

PER_UNIT_PRICE =  300.0

#messages will be serialized as JSON
def serializer(message):
    return json.dumps(message).encode('utf-8')


    