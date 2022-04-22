from typing import Type

from network.message.frame_pb2 import Frame
from network.message_service.generic_message_service import GenericMessageService
from PIL import Image  # type: ignore


class FrameMessageService(GenericMessageService):
    @classmethod
    def _message_type(cls) -> Type[Frame]:
        return Frame

    @classmethod
    def from_data(
        cls, image_data: bytes, width: int, height: int, mode: str
    ) -> "FrameMessageService":
        frame = cls._new_message()
        assert isinstance(frame, cls._message_type())
        frame.image_data = image_data
        frame.width = width
        frame.height = height
        frame.mode = mode
        return cls(frame)

    @property
    def image(self) -> Image:
        frame = self.message
        assert isinstance(frame, self._message_type())
        return Image.frombytes(
            frame.mode, (frame.width, frame.height), frame.image_data
        )
