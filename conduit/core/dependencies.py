from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends

from conduit.core.container import container
from conduit.services.auth import UserAuthService

DBSession = Annotated[AsyncSession, Depends(container.session)]
IUserAuthService = Annotated[UserAuthService, Depends(container.user_auth_service)]
