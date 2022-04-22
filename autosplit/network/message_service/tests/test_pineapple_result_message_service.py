from unittest import TestCase

from network.message.pineapple_result_pb2 import PineappleResult
from network.message_service.pineapple_result_message_service import (
    PineappleResultMessageService,
)


class TestPineappleResultMessageService(TestCase):
    PREDICTION = "prediction = 10"

    def setUp(self) -> None:
        self.result = PineappleResult()
        self.result.prediction = self.PREDICTION
        self.message_service = PineappleResultMessageService(self.result)

    def test_message(self) -> None:
        self.assertEqual(self.message_service.message, self.result)

    def test_message_type(self) -> None:
        self.assertEqual(PineappleResultMessageService._message_type(), PineappleResult)

    def test_serialize(self) -> None:
        self.assertEqual(
            self.message_service.serialize(), self.result.SerializeToString()
        )

    def test_deserialize(self) -> None:
        serialized_result = self.result.SerializeToString()
        self.assertEqual(
            PineappleResultMessageService.deserialize(serialized_result), self.result
        )

    def test_new_message(self) -> None:
        self.assertEqual(
            PineappleResultMessageService._new_message(), PineappleResult()
        )

    def test_from_data(self) -> None:
        message_service = PineappleResultMessageService.from_data(self.PREDICTION)
        self.assertEqual(message_service.message, self.message_service.message)

    def test_get_prediction(self) -> None:
        self.assertEqual(self.PREDICTION, self.message_service.prediction)
