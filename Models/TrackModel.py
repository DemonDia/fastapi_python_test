from typing import Optional
from datetime import datetime
from sqlmodel import Field, SQLModel


class TrackModel(SQLModel,table=True):
    __tablename__: "trackmodel"
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    artist: str
    duration: float
    last_play: datetime