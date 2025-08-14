from collections.abc import Collection
from datetime import datetime

from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from conduit.core.exceptions import UserNotFoundException
from conduit.domain.dtos.user import CreateUserDTO, UserDTO
from conduit.domain.mapper import IModelMapper
from conduit.domain.repositories.user import IUserRepository
from conduit.infrastructure.models import User
from conduit.services.password import get_password_hash


class UserRepository(IUserRepository):
    """Repository for User model."""

    def __init__(self, user_mapper: IModelMapper[User, UserDTO]):
        self._user_mapper = user_mapper

    async def add(self, session: AsyncSession, create_item: CreateUserDTO) -> UserDTO:
        query = (
            insert(User)
            .values(
                username=create_item.username,
                email=create_item.email,
                password_hash=get_password_hash(create_item.password),
                image_url="https://api.realworld.io/images/smiley-cyrus.jpeg",
                bio="",
                created_at=datetime.now(),
            )
            .returning(User)
        )
        result = await session.execute(query)
        return self._user_mapper.to_dto(result.scalar())

    async def get_by_email_or_none(
        self, session: AsyncSession, email: str
    ) -> UserDTO | None:
        query = select(User).where(User.email == email)
        if user := await session.scalar(query):
            return self._user_mapper.to_dto(user)

    async def get_by_email(self, session: AsyncSession, email: str) -> UserDTO:
        query = select(User).where(User.email == email)
        if not (user := await session.scalar(query)):
            raise UserNotFoundException()
        return self._user_mapper.to_dto(user)

    async def get_or_none(self, session: AsyncSession, user_id: int) -> UserDTO | None:
        query = select(User).where(User.id == user_id)
        if user := await session.scalar(query):
            return self._user_mapper.to_dto(user)

    async def get(self, session: AsyncSession, user_id: int) -> UserDTO:
        query = select(User).where(User.id == user_id)
        if not (user := await session.scalar(query)):
            raise UserNotFoundException()
        return self._user_mapper.to_dto(user)

    async def list_by_users(
        self, session: AsyncSession, user_ids: Collection[int]
    ) -> list[UserDTO]:
        query = select(User).where(User.id.in_(user_ids))
        users = await session.scalars(query)
        return [self._user_mapper.to_dto(user) for user in users]

    async def get_by_username_or_none(
        self, session: AsyncSession, username: str
    ) -> UserDTO | None:
        query = select(User).where(User.username == username)
        if user := await session.scalar(query):
            return self._user_mapper.to_dto(user)

    async def get_by_username(self, session: AsyncSession, username: str) -> UserDTO:
        query = select(User).where(User.username == username)
        if not (user := await session.scalar(query)):
            raise UserNotFoundException()
        return self._user_mapper.to_dto(user)
