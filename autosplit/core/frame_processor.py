import logging
from typing import Type

from network.communication_process import HybridProcess
from network.message_service.frame_message_service import FrameMessageService
from network.message_service.pineapple_result_message_service import (
    PineappleResultMessageService,
)
from settings import config


class FrameProcessor(HybridProcess):
    @property
    def CLIENT_PORT(self) -> int:
        return config.NETWORK.COLLECTION_PORT

    @property
    def CLIENT_MSG_SERVICE(self) -> Type[FrameMessageService]:
        return FrameMessageService

    @property
    def SERVER_PORT(self) -> int:
        return config.NETWORK.OUTPUT_PORT

    @property
    def SERVER_MSG_SERVICE(self) -> Type[PineappleResultMessageService]:
        return PineappleResultMessageService

    def run(self) -> None:
        client_socket = self._create_client_socket()
        server_socket = self._create_server_socket()

        while self._is_running:
            frame_msg = self.CLIENT_MSG_SERVICE(client_socket.recv_message())
            result = (
                f"Frame '{frame_msg.id.split('-')[-1]}' processed, and results sent."
            )
            pineapple_result_msg = PineappleResultMessageService.from_data(result)
            server_socket.send_message(pineapple_result_msg)
            logging.debug(result)
