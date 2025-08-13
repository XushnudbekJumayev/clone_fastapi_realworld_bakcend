import logging

from pydantic import computed_field
from sqlalchemy import NullPool

from conduit.core.settings.app import AppSettings


class TestAppSettings(AppSettings):
    """
    Test application settings.
    """

    debug: bool =True
    title: str = "[Test] Conduit API"

    logging_level: int = logging.DEBUG

    class Config(AppSettings):
        env_file = ".env.test"

    @computed_field
    @property
    def sqlalchemy_engine_props(self) -> dict:
        return dict(
            url=self.sql_db_uri,
            echo= False,
            poolclass = NullPool,
            isolation_level="AUTOCOMMIT",
        )
