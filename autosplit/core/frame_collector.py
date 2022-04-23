import logging
from time import perf_counter, sleep
from typing import Type

from network.communication_process import ServerProcess
from network.message_service.frame_message_service import FrameMessageService
from settings import config
from system.base_window import BaseWindow


class FrameCollector(ServerProcess):
    def __init__(self, window: BaseWindow):
        ServerProcess.__init__(self)
        self.window = window

    @property
    def SERVER_PORT(self) -> int:
        return config.NETWORK.COLLECTION_PORT

    @property
    def SERVER_MSG_SERVICE(self) -> Type[FrameMessageService]:
        return FrameMessageService

    def run(self) -> None:
        server_socket = self._create_server_socket()

        while self._is_running:
            start_time = perf_counter()
            image = self.window.capture()
            frame_msg = FrameMessageService.from_data(
                image.tobytes(), image.width, image.height, image.mode
            )
            server_socket.send_message(frame_msg)
            remaining_time = 1 / config.FRAME_RATE - (perf_counter() - start_time)

            if remaining_time < 0:
                logging.warning("Unable to collect frames at 60Hz.")
            else:
                logging.debug(f"Frame sent, sleeping for {remaining_time} seconds.")
                sleep(1)  # TODO: remove
                sleep(remaining_time)
