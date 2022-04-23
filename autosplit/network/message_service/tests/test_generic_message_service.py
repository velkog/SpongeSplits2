from unittest import TestCase
from unittest.mock import MagicMock, patch

from google.protobuf.message import Message
from network.message_service.generic_message_service import GenericMessageService

TEST_BYTE_STR = b"TEST_BYTES"


class TestGenericMessageService(TestCase):
    # TODO: Move into utility
    @patch(
        "network.message_service.generic_message_service.GenericMessageService.__abstractmethods__",
        set(),
    )
    def setUp(self) -> None:
        self.message = Message()
        self.message_service = GenericMessageService(self.message)  # type: ignore

    def test_message(self) -> None:
        self.assertTrue(self.message_service.message is self.message)

    def test_message_type(self) -> None:
        with self.assertRaises(NotImplementedError):
            GenericMessageService._message_type()

    @patch(
        "google.protobuf.message.Message.SerializeToString", return_value=TEST_BYTE_STR
    )
    def test_serialize(self, magic_mock: MagicMock) -> None:
        self.assertEqual(self.message_service.serialize(), TEST_BYTE_STR)

    def test_deserialize(self) -> None:
        with self.assertRaises(NotImplementedError):
            GenericMessageService.deserialize(TEST_BYTE_STR)

    def test_new_message(self) -> None:
        with self.assertRaises(NotImplementedError):
            GenericMessageService._new_message()
