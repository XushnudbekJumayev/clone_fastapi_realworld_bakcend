import logging

from pydantic import computed_field

from conduit.core.settings.app import AppSettings

class DevAppSettings(AppSettings):
    """
    DEvelopment application settings.
    """

    debug: bool =True

    title: str = "[DEV] Conduit API"

    loggin_level: int = logging.DEBUG

    class Config(AppSettings.Config):
        env_file = ".env.dev"

    @computed_field  # type: ignore
    @property
    def sqlalchemy_engine_props(self) -> dict:
        return dict(url=self.sql_db_uri, echo=True)
