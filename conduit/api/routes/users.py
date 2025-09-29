from fastapi import APIRouter

from conduit.api.schemas.responses.user import CurrentUserResponse
from conduit.core.dependencies import JWTToken, CurrentUser
router = APIRouter()

@router.get("", response_model=CurrentUserResponse) # userni tokenini oladi
async def get_current_user(
    token: JWTToken, current_user: CurrentUser
) -> CurrentUserResponse:
    """
    Return current user.
    """
    return CurrentUserResponse.from_dto(dto=current_user, token=token)
