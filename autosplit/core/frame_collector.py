from typing import Type

from network.communication_process import ServerProcess
from network.message_service.frame_message_service import FrameMessageService
from PIL import Image  # type: ignore
from settings import config
from abc import ABC, abstractmethod


class FrameCollector(ServerProcess):
    @property
    def SERVER_PORT(self) -> int:
        return config.NETWORK.COLLECTION_PORT

    @property
    def SERVER_MSG_SERVICE(self) -> Type[FrameMessageService]:
        return FrameMessageService

    def run(self) -> None:
        server_socket = self._create_server_socket()

        image = Image.open("autosplit/reset_frame.jpg")
        image_mode = image.mode
        image_height = image.height
        image_width = image.width
        image_data = image.tobytes()

        while True:
            frame_msg = FrameMessageService.from_data(
                image_data, image_width, image_height, image_mode
            )
            server_socket.send_message(frame_msg)
            # TODO: remove
            from time import sleep

            sleep(0.01666666666)
