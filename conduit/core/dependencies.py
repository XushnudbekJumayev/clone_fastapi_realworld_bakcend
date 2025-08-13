from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends

from conduit.core.container import container

DBSession = Annotated[AsyncSession, Depends(container.session)]
IUserAuthService =  Annotated[AsyncSession, Depends(container.user_auth_service)]
