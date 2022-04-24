from unittest import TestCase

from network.message.pineapple_result_pb2 import PineappleResult
from network.message_service.pineapple_result_message_service import (
    PineappleResultMessageService,
)


class TestPineappleResultMessageService(TestCase):
    PREDICTION = "prediction = 10"

    def setUp(self) -> None:
        self.sample_id = "sample_id"
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
        message_service = PineappleResultMessageService.from_data(self.sample_id, self.PREDICTION)

        result = message_service.message
        original_result = self.message_service.message
        assert isinstance(result, PineappleResult)
        assert isinstance(original_result, PineappleResult)

        self.assertEqual(result.id, self.sample_id)
        self.assertEqual(result.prediction, original_result.prediction)

    def test_get_prediction(self) -> None:
        self.assertEqual(self.PREDICTION, self.message_service.prediction)
