from abc import ABC, abstractmethod
from multiprocessing import Process
from typing import Type

from network.message_service.generic_message_service import GenericMessageService
from network.socket import AsyncMessageSocket
from zmq import PULL, PUSH


class GenericProcess(Process, ABC):
    def __init__(self) -> None:
        Process.__init__(self, daemon=True)

    def _create_generic_socket(
        self,
        message_service: Type[GenericMessageService],
        port: int,
        socket_direction: int,
    ) -> AsyncMessageSocket:
        assert (
            socket_direction is PUSH or socket_direction is PULL
        ), f"Unexpected socket direction '{socket_direction}' given."
        return AsyncMessageSocket(message_service, port, socket_direction)

    @abstractmethod
    def run(self) -> None:
        raise NotImplementedError


class ClientProcess(GenericProcess, ABC):
    @property
    @abstractmethod
    def CLIENT_PORT(self) -> int:
        raise NotImplementedError

    @property
    @abstractmethod
    def CLIENT_MSG_SERVICE(self) -> Type[GenericMessageService]:
        raise NotImplementedError

    def __init__(self) -> None:
        ABC.__init__(self)
        GenericProcess.__init__(self)

    def _create_client_socket(self) -> AsyncMessageSocket:
        socket = self._create_generic_socket(
            self.CLIENT_MSG_SERVICE, self.CLIENT_PORT, PULL
        )
        socket.bind()
        return socket


class ServerProcess(GenericProcess, ABC):
    @property
    @abstractmethod
    def SERVER_PORT(self) -> int:
        raise NotImplementedError

    @property
    @abstractmethod
    def SERVER_MSG_SERVICE(self) -> Type[GenericMessageService]:
        raise NotImplementedError

    def __init__(self) -> None:
        ABC.__init__(self)
        GenericProcess.__init__(self)

    def _create_server_socket(self) -> AsyncMessageSocket:
        socket = self._create_generic_socket(
            self.SERVER_MSG_SERVICE, self.SERVER_PORT, PUSH
        )
        socket.connect()
        return socket


class HybridProcess(ClientProcess, ServerProcess, ABC):
    def __init__(self) -> None:
        ABC.__init__(self)
        ClientProcess.__init__(self)
        ServerProcess.__init__(self)
