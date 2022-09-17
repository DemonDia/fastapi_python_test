
from fastapi import Response, Depends
from Schema.TrackSchema import Track
from database import *
from sqlmodel import Session, select, delete
from config import  app
from Models.TrackModel import TrackModel
from HelperFunctions import *

# ===========================test functions===========================
@app.delete("/tracks/deleteall")
def deleteAll(session:Session = Depends(get_session)):
    return deleteAllData(TrackModel)

@app.post("/tracks/seedall")
def addSeedData(session:Session = Depends(get_session)):
    return seedInitialData("track",TrackModel)


# ===========================actual CRUD functions===========================
@app.get('/tracks/')
def getTracks(session: Session = Depends(get_session)):
    stmt = select(TrackModel)
    result = session.exec(stmt).all()
    # return result
    return {
        "success": True,
        "data": result
    }

@app.get("/tracks/{track_id}/")
def track(track_id: int, response: Response, session: Session = Depends(get_session)):
    track = session.get(TrackModel, track_id)
    if not track:
        response.status_code = 404
        return {
            "success": False,
            "message": "Track not found"
        }
    # return track
    return {
        "success": True,
        "data": track
    }

@app.post("/tracks/")
def createTrack(track: TrackModel, session: Session = Depends(get_session)):
    session.add(track)
    session.commit()
    session.refresh(track)
    session.close()
    return {
        "success": True,
        "message": "Successfully added"
    }


@app.put("/tracks/{track_id}/")
def updateTrack(track_id: int, updated_track: Track, session: Session = Depends(get_session)):
    track = session.get(TrackModel, track_id)
    if not track:
        return {
            "success": False,
            "message": "Track not found"
        }
    if updated_track.title:
        track.title = updated_track.title
    if updated_track.artist:
        track.artist = updated_track.artist
    if updated_track.duration:
        track.duration = updated_track.duration
    if updated_track.last_play:
        track.last_play = updated_track.last_play
    session.add(track)
    session.commit()
    session.refresh(track)
    session.close()
    return {
        "success": True,
        "message": "Successfully updated"
    }


@app.delete("/tracks/{track_id}/")
def deleteTrack(track_id: int, session: Session = Depends(get_session)):
    track = session.get(TrackModel, track_id)
    if not track:
        return {
            "success": False,
            "message": "Track not found"
        }
    session.delete(track)
    session.commit()
    session.close()
    return {
        "success": True,
        "message": "Successfully deleted"
    }
