from sqlmodel import  SQLModel, create_engine, Session
from config import database_route
from Models.TrackModel import TrackModel
engine = create_engine(database_route,echo=True)

# to create a database table
def create_tables():
    SQLModel.metadata.create_all(engine)

if __name__ == "__main__":
    create_tables()

def get_session():
    with Session(engine) as session:
        yield session