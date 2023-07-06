from fastapi import FastAPI
from redis_om import get_redis_connection
from dotenv import load_dotenv
import os
load_dotenv()
app = FastAPI()



redis = get_redis_connection(
    host =os.environ.get("REDIS_KEY"), 
    port = 18465,
    password=os.environ.get("REDIS_PASSWORD")

)


@app.get("/")
async def root():
    return {"message" : "Hello World"}