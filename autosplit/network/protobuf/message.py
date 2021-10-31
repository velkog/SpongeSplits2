from __future__ import annotations

from google.protobuf.message import Message
from network.protobuf.pineapple_frame_pb2 import PineappleFrame
from network.protobuf.pineapple_result_pb2 import PineappleResult
from typing import Any, Optional


class ProtobufMessage:
    MESSAGE_TYPE: Optional[Message] = None

    def __init__(self, message: Message) -> None:
        self.message = message

    @classmethod
    def deserialize(cls, serialized_msg: bytes) -> ProtobufMessage:
        if cls.MESSAGE_TYPE is None:
            raise NotImplementedError
        # "Message" not callable
        message = cls.MESSAGE_TYPE()  # type: ignore
        message.ParseFromString(serialized_msg)
        return cls(message)

    def serialize(self) -> bytes:
        serialized_object: bytes = self.message.SerializeToString()
        return serialized_object

    @staticmethod
    def from_data(data: Any) -> ProtobufMessage:
        raise NotImplementedError


class PineappleFrameMessage(ProtobufMessage):
    MESSAGE_TYPE: Optional[Message] = PineappleFrame

    @staticmethod
    def from_data(frame_id: int) -> PineappleFrameMessage:
        frame = PineappleFrame()
        frame.id = frame_id
        return PineappleFrameMessage(frame)

    @property
    def frame_id(self) -> int:
        # "Message" has no attribute "id"
        frame_id: int = self.message.id  # type: ignore
        return frame_id


class PineappleResultMessage(ProtobufMessage):
    MESSAGE_TYPE: Optional[Message] = PineappleResult

    @staticmethod
    def from_data(prediction: str) -> PineappleResultMessage:
        result = PineappleResult()
        result.prediction = prediction
        return PineappleResultMessage(result)

    @property
    def prediction(self) -> str:
        # "Message" has no attribute "id"
        prediction: str = self.message.prediction  # type: ignore
        return prediction
