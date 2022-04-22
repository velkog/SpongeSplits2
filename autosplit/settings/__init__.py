from settings.system_config import NetworkConfig
from settings.user_config import EXCLUSION_LIST


class Config:
    NETWORK = NetworkConfig()
    EXCLUSION_LIST = EXCLUSION_LIST


config = Config()
