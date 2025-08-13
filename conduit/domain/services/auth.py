import abc
from typing import Any

from conduit.domain.dtos.user import (
    CreatedUserDTO,
    CreateUserDTO,

)


class IUserAuthService(abc.ABC):

    @abc.abstractmethod
    async def sign_up_user(
        self, session: Any, user_to_create: CreateUserDTO
    ) -> CreatedUserDTO: ...
