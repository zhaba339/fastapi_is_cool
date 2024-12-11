from datetime import date
from fastapi import FastAPI, Query, Depends
from pydantic import BaseModel
from typing_extensions import Optional

app = FastAPI()

class HotelsSearchArgs:
    def __init__(
        self,
        location: str,
        date_from: date,
        date_to: date,
        has_spa: Optional[bool] = None,
        stars: Optional[int] = Query(None, ge=1, le=5),
    ):
        self.location = location
        self.date_from = date_from
        self.date_to = date_to
        self.has_spa = has_spa
        self.stars = stars

@app.get("/hotels")
async def get_hotels(
        search_args: HotelsSearchArgs = Depends()
        ):
    return search_args


class SBooking(BaseModel):
    room_id: int
    date_from: date
    date_to: date


@app.post("/booking")
async def booking(booking: SBooking):
    return booking