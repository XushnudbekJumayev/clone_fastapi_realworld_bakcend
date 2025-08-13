import datetime

from dataclasses import dataclass, field

@dataclass
class UserDTO:
    id: int = field(init=False)
    username: str
    email: str
    password_hash: str
    bio: str
    image_url: str
    created_at: datetime.datetime

@dataclass(frozen=True)
class CreateUserDTO:
    username: str
    email: str
    password: str

@dataclass(frozen=True)
class CreatedUserDTO:
    id: int
    email: str
    username: str
    bio: str
    image: str
    token: str
