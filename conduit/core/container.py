from collections.abc import AsyncIterator
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from conduit.core.settings.base import BaseAppSettings
from conduit.core.config import get_app_settings
from conduit.domain.services.auth import IUserAuthService

from conduit.services.auth import UserAuthService
from conduit.domain.services.user import IUserService
from conduit.domain.services.auth_token import IAuthTokenService
from conduit.domain.mapper import IModelMapper
from conduit.infrastructure.mappers.user import UserModelMapper
from conduit.domain.repositories.user import IUserRepository
from conduit.infrastructure.repositories.user import UserRepository
from conduit.services.auth_token import AuthTokenService
from conduit.services.user import UserService

class Container:
    """Dependency injector project container."""

    def __init__(self, settings: BaseAppSettings) -> None:
        self._settings = settings
        self._engine = create_async_engine(**settings.sqlalchemy_engine_props)
        self._session = async_sessionmaker(bind=self._engine, expire_on_commit=False)

    async def session(self) -> AsyncIterator[AsyncSession]:
        async with self._session() as session:
            try:
                yield session
                await session.commit()
            except Exception:
                await session.rollback()
                raise
            finally:
                await session.close()


    @staticmethod
    def user_model_mapper() -> IModelMapper:
        return UserModelMapper()

    def user_repository(self) -> IUserRepository:
        return UserRepository(user_mapper=self.user_model_mapper())

    def auth_token_service(self) -> IAuthTokenService:
        return AuthTokenService(
            secret_key=self._settings.jwt_secret_key,
            token_expiration_minutes=self._settings.jwt_token_expiration_minutes,
            algorithm=self._settings.jwt_algorithm,
        )

    def user_service(self) -> IUserService:
        return UserService(user_repo=self.user_repository())

    def user_auth_service(self) -> IUserAuthService:
        return UserAuthService(
            user_service=self.user_service(),
            auth_token_service=self.auth_token_service(),
        )

container = Container(settings=get_app_settings())
