import logging

from settings.system_config import NetworkConfig
from settings.user_config import EXCLUSION_LIST, FRAME_RATE


class Config:
    NETWORK = NetworkConfig()
    EXCLUSION_LIST = EXCLUSION_LIST
    FRAME_RATE = FRAME_RATE


config = Config()

logging.basicConfig(
    encoding="utf-8",
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
