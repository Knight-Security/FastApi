import random
from fastapi import FastAPI,HTTPException,Response
from datetime import datetime
from typing import Any
data=[
    {
        "campaign_id":1,
        "name":"Summer launch",
        "due_date": datetime.now(),
        "created _at":datetime.now()
    },
    {
        "campaign_id":2,
        "name":"black friday",
        "due_date": datetime.now(),
        "created _at":datetime.now()
    }
]
app= FastAPI(root_path="/api/v1")
@app.get("/")
async def root():
    return {"message":"Hello World"} 
@app.get("/campaigns")
async def read_campaigns():
    return {"campaign":data}

#retrieving specific value by id
@app.get("/campaigns/{id}")
async def read_campains(id:int):
    for campaign in data:
        if campaign.get("campaign_id")==id:
            return {"campaign":campaign}
    raise HTTPException(status_code=404)

# creating values 
@app.post("/campaign",status_code=201)
async def create_campaign(body:dict[str,Any]):
    new : Any ={
        "capaign_id":random.randint(100,1000),
        "name":body.get("name"),   
        "due_date":body.get("due date"),
         "created _at":datetime.now()
        }
    data.append(new);
    return  {"campaign:": new}

# updating value by id
@app.put("/campaign/{id}")
async def update_campaign(id:int,body:dict[str,Any]):
    for index, campaign in enumerate(data):
        if campaign.get("campaign_id")==id:
            updated : Any ={
            "campaign_id":id,
            "name":body.get("name"),   
            "due_date":body.get("due date"),
            "created _at":campaign.get("created_at")
            }
            data[index]=updated
            return {"campaign":updated}
        
    raise HTTPException(status_code=404)

# deleting our data
@app.delete("/campaign/{id}")
async def delete_id(id:int):
    for index,campaign in enumerate(data):
        if campaign.get("campaign_id")==id:
            data.pop(index)
            return Response(status_code=204)
    raise HTTPException(status_code=404)
