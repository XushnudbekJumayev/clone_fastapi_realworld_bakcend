import logging
from typing import ClassVar

from pydantic import computed_field
from sqlalchemy import NullPool


from conduit.core.settings.app import AppSettings


class TestAppSettings(AppSettings):
    """
    Test application settings.
    """

    debug: bool = True

    title: str = "[TEST] Conduit API"

    logging_level: int = logging.DEBUG

    class Config(AppSettings.Config):
        env_file: ClassVar[str] = ".env.test" #bu qator o'zgartirildi chunki Pydantic v2 da barcha atributlar uchun type annotation talab qilinadi.
        #eski versiyasi: env_file = ".env.test"

    @computed_field  # type: ignore
    @property
    def sqlalchemy_engine_props(self) -> dict:
        return dict(
            url=self.sql_db_uri,
            echo=False,
            poolclass=NullPool,
            isolation_level="AUTOCOMMIT",
        )
