import json
import pathlib
from sqlmodel import Session, select, delete
from database import *

# seed data for given entity
def seedInitialData(fileName,model):
    try:
        fileName = fileName+".json"
        DATAFILE = pathlib.Path() / "data" / fileName
        print(DATAFILE)

        session = Session(engine)
        stmt = select(model)
        result = session.exec(stmt).first()
        # check if duplicates
        print(result)
        if result is None:
            # autogen data
            with open(DATAFILE, "r") as f:
                items = json.load(f)
                for item in items:
                    session.add(model(**item))
            session.commit()
        session.close()
        return {
            "success":True,
            "message":"Data is seeded"
        }
    except Exception as e:
        return {
            "success":False,
            "messaage":e
        }

# delete all data for given entity
def deleteAllData(model):
    session = Session(engine)
    stmt = delete(model)
    result = session.exec(stmt)
    session.commit()
    session.close()
    if result:
        return {
            "success":True,
            "message":"Everything is deleted"
        }
    return {
        "success":False,
        "message":"Failed to delete"
    }
