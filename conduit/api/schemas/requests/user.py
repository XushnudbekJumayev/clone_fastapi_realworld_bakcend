from pydantic import BaseModel
from conduit.domain.dtos.user import CreateUserDTO
class UserRegistrationData(BaseModel):
    email: str
    password: str
    username: str

class UserRegistrationRequest(BaseModel):
    user: UserRegistrationData

    def to_dto(self) -> CreateUserDTO:
        return CreateUserDTO(
            username=self.user.username,
            email=self.user.email,
            password=self.user.password,
        )
