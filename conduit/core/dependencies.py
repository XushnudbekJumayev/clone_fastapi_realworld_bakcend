from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from conduit.domain.services.auth import IUserAuthService

from conduit.core.container import container

DBSession = Annotated[AsyncSession, Depends(container.session)]
IUserAuthService = Annotated[IUserAuthService, Depends(container.user_auth_service)]
