#from backend.scheme import Item
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pymongo import results
from scheme import *
import pymongo
from bson.objectid import ObjectId
import uvicorn
import datetime
from pydantic import BaseModel



client = pymongo.MongoClient('...')
db = client.sbercatDB

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/user")
async def createUser(user: User):
    if db.users.find_one({"UserId": user.UserId}) == None:
        _id = db.users.insert_one(dict(user)).inserted_id
        return str(_id)
    else:
        return "0"

#функция обновления 
@app.put("/user")
async def updateUser(params: Item):
    db.users.update_one({"UserId": params.UserId},
    {"$set":
    {'name': params.name,
    'foodLevel': params.foodLevel,
    'playLevel': params.playLevel,
    'sleepLevel': params.sleepLevel,
    'timeOfExit': params.timeOfExit,
    'sec': params.sec,
    'min': params.min,
    'hour': params.hour,
    'kusua': params.kusua,
    'flag': params.flag}})



@app.get("/user")
async def getUser(UserId: str):
    response = db.users.find_one({"UserId": UserId})
    result = {}
    result["UserId"] = response["UserId"]
    result["name"] = response["name"]
    result["foodLevel"] = response["foodLevel"]
    result["sleepLevel"] = response["sleepLevel"]
    result["playLevel"] = response["playLevel"]
    result["timeOfExit"] = response["timeOfExit"]
    result["sec"] = response["sec"]
    result["min"] = response["min"]
    result["hour"] = response["hour"]
    result["kusua"] = response["kusua"]
    result["flag"] = response["flag"]
    return result


