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

            logging.debug(f"Frame '{frame_msg.id.split('-')[-1]}' sent.")
            if remaining_time < 0:
                logging.warning(
                    f"Unable to collect frames at {config.FRAME_RATE}Hz - {'%.3f' % (remaining_time * 1000)} milliseconds behind."
                )
            else:
                logging.debug(
                    f"Collector sleeping for {'%.3f' % (remaining_time * 1000)} milliseconds."
                )
                sleep(remaining_time)
            sleep(5)  # TODO: remove
