from typing import Optional

from pydantic import BaseModel

data = {
    "name": "Michael Kennedy",
    "age": "28",
    "location": {
        "city": "Portland",
        "state": "Oregon"
    },
    "bike": "KTM Duke 690",
    "rides": [7, 103, 22, "70", 1000]
}


class Location(BaseModel):
    city: str
    state: str
    country: Optional[str]


class User(BaseModel):
    name: str
    age: int
    location: Location
    bike: str
    rides: list[int] = []


user = User(**data)

print(f"Found a user: {user}")
