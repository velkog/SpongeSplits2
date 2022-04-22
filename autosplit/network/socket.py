from typing import Type

from google.protobuf.message import Message
from network.message_service.generic_message_service import GenericMessageService
from zmq import Context
from zmq.sugar.socket import Socket


class AsyncMessageSocket:
    # TODO: Move to configuration
    HOST: str = "127.0.0.1"
    TRANSPORT: str = "tcp"
    PORT: int

    def __init__(
        self, message_service: Type[GenericMessageService], port: int, socket_type: int
    ) -> None:
        self.message_service = message_service
        self.PORT = port
        self.socket_type = socket_type
        self.socket: Socket = Context().socket(self.socket_type)  # type: ignore
        assert self.socket is not None

    @property
    def connection_addr(self) -> str:
        return f"{self.TRANSPORT}://{self.HOST}:{self.PORT}"

    def bind(self) -> None:
        self.socket.bind(self.connection_addr)  # type: ignore

    def connect(self) -> None:
        self.socket.connect(self.connection_addr)  # type: ignore

    def send_message(self, message: GenericMessageService) -> None:
        serialized_msg = message.serialize()
        self.socket.send(serialized_msg)  # type: ignore

    def recv_message(self) -> Message:
        serialized_msg = self.socket.recv()
        return self.message_service.deserialize(serialized_msg)  # type: ignore
