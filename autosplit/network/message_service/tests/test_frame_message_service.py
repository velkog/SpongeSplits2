from unittest import TestCase

from network.message.frame_pb2 import Frame
from network.message_service.frame_message_service import FrameMessageService
from PIL import Image


class TestFrameMessageService(TestCase):
    IMAGE_DATA = b"\xff\xed\xad\xff\xe5\x8c\xff\xe5\x8c\xff\xc9\x0e\xff\xe3\xed\xff\xd8\xe5\xb4\xca\xb1\x95\xb0\x8d"
    WIDTH = 2
    HEIGHT = 4
    MODE = "RGB"

    def setUp(self) -> None:
        self.frame = Frame()
        self.frame.image_data = self.IMAGE_DATA
        self.frame.width = self.WIDTH
        self.frame.height = self.HEIGHT
        self.frame.mode = self.MODE
        self.message_service = FrameMessageService(self.frame)

    def test_message(self) -> None:
        self.assertEqual(self.message_service.message, self.frame)

    def test_message_type(self) -> None:
        self.assertEqual(FrameMessageService._message_type(), Frame)

    def test_serialize(self) -> None:
        self.assertEqual(
            self.message_service.serialize(), self.frame.SerializeToString()
        )

    def test_deserialize(self) -> None:
        serialized_frame = self.frame.SerializeToString()
        self.assertEqual(FrameMessageService.deserialize(serialized_frame), self.frame)

    def test_new_message(self) -> None:
        self.assertEqual(FrameMessageService._new_message(), Frame())

    def test_from_data(self) -> None:
        message_service = FrameMessageService.from_data(
            self.IMAGE_DATA, self.WIDTH, self.HEIGHT, self.MODE
        )
        self.assertEqual(message_service.message, self.message_service.message)

    def test_get_image(self) -> None:
        image = Image.frombytes(self.MODE, (self.WIDTH, self.HEIGHT), self.IMAGE_DATA)
        self.assertEqual(image, self.message_service.image)
