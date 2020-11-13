from network.protobuf_handler import (
    FrameHandler as Frame,
    FrameResultHandler as FrameResult,
)
from typing import Optional
from zmq import Context
from zmq.sugar.socket import Socket


class AsyncMessageSocket:
    HOST: str = "127.0.0.1"
    TRANSPORT: str = "tcp"
    PORT: int = 5555

    def __init__(self, socket_type: int, port: int = 5555) -> None:
        self.socket_type = socket_type
        self.PORT = port
        self.socket: Optional[Socket] = None

    @property
    def connection_addr(self) -> str:
        return f"{self.TRANSPORT}://{self.HOST}:{self.PORT}"

    def _create_socket(self) -> Socket:
        return Context().socket(self.socket_type)

    def bind(self) -> None:
        self.socket = self._create_socket()
        self.socket.bind(self.connection_addr)

    def connect(self) -> None:
        self.socket = self._create_socket()
        self.socket.connect(self.connection_addr)

    def send_frame(self, frame_id: int) -> None:
        assert self.socket is not None
        serialized_frame = Frame(frame_id).serialize()
        self.socket.send(serialized_frame)

    def send_result(self, prediction: str) -> None:
        assert self.socket is not None
        serialized_frame_result = FrameResult(prediction).serialize()
        self.socket.send(serialized_frame_result)

    def recv_frame(self) -> int:
        assert self.socket is not None
        serialized_frame = self.socket.recv()
        frame = Frame.deserialize(serialized_frame)
        return frame.frame_id

    def recv_result(self) -> str:
        assert self.socket is not None
        serialized_frame_result = self.socket.recv()
        frame_result = FrameResult.deserialize(serialized_frame_result)
        return frame_result.prediction
