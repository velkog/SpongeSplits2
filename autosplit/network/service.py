from typing import Optional, Type

from network.protobuf.message import ProtobufMessage
from zmq import Context
from zmq.sugar.socket import Socket


class AsyncMessageSocket:
    HOST: str = "127.0.0.1"
    TRANSPORT: str = "tcp"
    PORT: int

    def __init__(
        self, message_type: Type[ProtobufMessage], port: int, socket_type: int
    ) -> None:
        self.message_type = message_type
        self.socket: Optional[Socket] = None
        self.socket_type = socket_type
        self.PORT = port

    @property
    def connection_addr(self) -> str:
        return f"{self.TRANSPORT}://{self.HOST}:{self.PORT}"

    def _create_socket(self) -> Socket:
        return Context().socket(self.socket_type)  # type: ignore

    def bind(self) -> None:
        self.socket = self._create_socket()
        self.socket.bind(self.connection_addr)  # type: ignore

    def connect(self) -> None:
        self.socket = self._create_socket()
        self.socket.connect(self.connection_addr)  # type: ignore

    def send_message(self, message: ProtobufMessage) -> None:
        assert self.socket is not None
        serialized_msg = message.serialize()
        self.socket.send(serialized_msg)  # type: ignore

    def recv_message(self) -> ProtobufMessage:
        assert self.socket is not None
        serialized_msg = self.socket.recv()
        return self.message_type.deserialize(serialized_msg)  # type: ignore
