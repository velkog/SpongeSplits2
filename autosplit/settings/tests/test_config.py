from unittest import TestCase

from settings import config
from settings.system_config import NetworkConfig


class TestConfig(TestCase):
    def test_config(self) -> None:
        network_config = config.NETWORK
        self.assertIsInstance(network_config, NetworkConfig)
