import json
import pathlib
from Models.TrackModel import TrackModel
from database import *
from sqlmodel import Session, select
from config import app
from Routes.TrackRoutes import *
# instantiate the FasAPI app



@app.on_event("startup")
async def startup_event():
    DATAFILE = pathlib.Path() / "data" / "track.json"
    print(DATAFILE)

    session = Session(engine)
    stmt = select(TrackModel)
    result = session.exec(stmt).first()
    # check if duplicates
    print(result)
    if result is None:
        # autogen data
        with open(DATAFILE, "r") as f:
            tracks = json.load(f)
            for track in tracks:
                session.add(TrackModel(**track))
        session.commit()
    session.close()

