from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends

from conduit.core.container import container
from conduit.services.auth import UserAuthService
from conduit.services.auth_token import AuthTokenService
from conduit.core.security import HTTPTokenHeader
from conduit.domain.dtos.user import UserDTO
from conduit.services.user import UserService


token_security= HTTPTokenHeader(
    name= "Authorization",
    scheme_name = "JWT Token",
    description = "Token Format: `Token xxxxxx.yyyyyyy.zzzzzz`",
    raise_error=True
)


JWTToken = Annotated[str, Depends(token_security)]
DBSession = Annotated[AsyncSession, Depends(container.session)]


IUserAuthService = Annotated[UserAuthService, Depends(container.user_auth_service)]
IAuthTokenService = Annotated[AuthTokenService, Depends(container.auth_token_service)]
IUserService = Annotated[UserService, Depends(container.user_service)]

async def get_current_user(
    token: JWTToken,
    session: DBSession,
    auth_token_service: IAuthTokenService,
    user_service: IUserService,
) -> UserDTO:
    jwt_user = auth_token_service.parse_jwt_token(token=token)
    current_user_dto = await user_service.get_user_by_id(
        session=session, user_id=jwt_user.user_id
    )
    return current_user_dto

CurrentUser = Annotated[UserDTO, Depends(get_current_user)]
