from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/data")
def create_data(data: dict):
    # Process the data here
    return {"message": "Data created successfully"}





import logging
from fastapi import FastAPI

app = FastAPI()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.get("/")
def read_root():
    logger.info("Root endpoint called")
    return {"Hello": "World"}

@app.post("/data")
def create_data(data: dict):
    logger.info("Data creation endpoint called")
    # Process the data here
    return {"message": "Data created successfully"}
