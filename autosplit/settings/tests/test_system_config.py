from unittest import TestCase

from settings.system_config import NetworkConfig


class TestSystemConfig(TestCase):
    def test_network_config(self) -> None:
        network_config = NetworkConfig()
        self.assertEqual(network_config.COLLECTION_PORT, 5557)
        self.assertEqual(network_config.OUTPUT_PORT, 5558)
