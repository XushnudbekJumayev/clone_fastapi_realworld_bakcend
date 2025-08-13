from functools import lru_cache

from conduit.core.settings.app import AppSettings
from conduit.core.settings.base import AppEnvTypes, BaseAppSettings
from conduit.core.settings.development import DevAppSettings
from conduit.core.settings.production import ProdAppSettings
from conduit.core.settings.test import TestAppSettings

AppEnvType = DevAppSettings | TestAppSettings | ProdAppSettings

enviroment: dict[str, type[AppEnvTypes]] = {
    AppEnvTypes.development: DevAppSettings,
    AppEnvTypes.testing: TestAppSettings,
    AppEnvTypes.production: ProdAppSettings,
}

@lru_cache
def get_app_settings():
    """
    Return application configuration
    """
    app_env = BaseAppSettings().app_env
    config = enviroment[app_env]
    return config() #type ignore
