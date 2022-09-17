
from Models.TrackModel import TrackModel
from config import app
from Routes.TrackRoutes import *
from HelperFunctions import *
from ErrorHandler import *
# instantiate the FasAPI app

@app.on_event("startup")
async def startup_event():
    seedInitialData("track",TrackModel)


@app.get("/")
async def hello():
    return "OK"