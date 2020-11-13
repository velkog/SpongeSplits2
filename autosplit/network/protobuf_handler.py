from __future__ import annotations

from network.frame_pb2 import Frame
from network.frame_result_pb2 import FrameResult


class FrameHandler:
    def __init__(self, frame_id: int) -> None:
        self.frame = Frame()
        self.frame.id = frame_id

    def serialize(self) -> bytes:
        serialized_frame: bytes = self.frame.SerializeToString()
        return serialized_frame

    @classmethod
    def deserialize(cls, serialized_frame: bytes) -> FrameHandler:
        frame = Frame()
        frame.ParseFromString(serialized_frame)
        return cls(frame.id)
        return FrameHandler(frame)

    @property
    def frame_id(self) -> int:
        frame_id: int = self.frame.id
        return frame_id


class FrameResultHandler:
    def __init__(self, prediction: str) -> None:
        self.frame_result = FrameResult()
        self.frame_result.prediction = prediction

    def serialize(self) -> bytes:
        serialized_frame_result: bytes = self.frame_result.SerializeToString()
        return serialized_frame_result

    @classmethod
    def deserialize(cls, serialized_frame_result: bytes) -> FrameResultHandler:
        frame_result = FrameResult()
        frame_result.ParseFromString(serialized_frame_result)
        return cls(frame_result.prediction)

    @property
    def prediction(self) -> str:
        prediction: str = self.frame_result.prediction
        return prediction
