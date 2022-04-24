from typing import Type

from network.message.pineapple_result_pb2 import PineappleResult
from network.message_service.generic_message_service import GenericMessageService


class PineappleResultMessageService(GenericMessageService):
    @classmethod
    def _message_type(cls) -> Type[PineappleResult]:
        return PineappleResult

    @classmethod
    def from_data(cls, id: str, prediction: str) -> "PineappleResultMessageService":
        result = PineappleResultMessageService._new_message()
        assert isinstance(result, cls._message_type())
        result.id = id
        result.prediction = prediction
        return PineappleResultMessageService(result)

    @property
    def prediction(self) -> str:
        result = self.message
        assert isinstance(result, self._message_type())
        return result.prediction

    @property
    def id(self) -> str:
        result = self.message
        assert isinstance(result, self._message_type())
        return result.id