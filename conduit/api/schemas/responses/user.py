from pydantic import BaseModel
from conduit.domain.dtos.user import CreatedUserDTO, UserDTO

class UserIDData(BaseModel):
    id: int

class UserBaseData(BaseModel):
    email: str
    username: str
    bio: str
    image: str
    token: str

class RegisteredUserData(UserIDData, UserBaseData):
    pass

class UserRegistrationResponse(BaseModel):
    user: RegisteredUserData

    @classmethod
    def from_dto(cls, dto: CreatedUserDTO) -> "UserRegistrationResponse":
        return UserRegistrationResponse(
            user=RegisteredUserData(
                id=dto.id,
                email=dto.email,
                username=dto.username,
                bio=dto.bio,
                image=dto.image,
                token=dto.token,
            )
        )

class CurrentUserData(UserIDData, UserBaseData):
    pass

class CurrentUserResponse(BaseModel):
    user: CurrentUserData

    @classmethod
    def from_dto(cls, dto: UserDTO, token: str) -> "CurrentUserResponse":
        return CurrentUserResponse(
            user=CurrentUserData(
                id=dto.id,
                email=dto.email,
                username=dto.username,
                bio=dto.bio,
                image=dto.image_url,
                token=token,
            )
        )
