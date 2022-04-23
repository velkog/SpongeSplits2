from typing import Type

from network.communication_process import ClientProcess
from network.message_service.pineapple_result_message_service import (
    PineappleResultMessageService,
)
from settings import config


class ResultHandler(ClientProcess):
    @property
    def CLIENT_PORT(self) -> int:
        return config.NETWORK.OUTPUT_PORT

    @property
    def CLIENT_MSG_SERVICE(self) -> Type[PineappleResultMessageService]:
        return PineappleResultMessageService

    def run(self) -> None:
        client_socket = self._create_client_socket()

        while self._is_running:
            pineapple_result_msg = client_socket.recv_message()
            prediction = self.CLIENT_MSG_SERVICE(pineapple_result_msg).prediction
            print(prediction)
