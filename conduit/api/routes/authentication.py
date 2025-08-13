from fastapi import APIRouter

from conduit.api.schemas.requests.user import UserRegistrationRequest
from conduit.api.schemas.responses.user import UserRegistrationResponse

from conduit.core.dependencies import DBSession, IUserAuthService


router = APIRouter()



@router.post("", response_model=UserRegistrationResponse)
async def register_user(
    payload: UserRegistrationRequest,
    session: DBSession,
    user_auth_service: IUserAuthService,
) -> UserRegistrationResponse:
    """
    Process user registration.
    """
    user_dto = await user_auth_service.sign_up_user(
        session=session, user_to_create=payload.to_dto()
    )
    return UserRegistrationResponse.from_dto(dto=user_dto)
