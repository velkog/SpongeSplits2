from abc import ABC, abstractmethod
from typing import Type

from google.protobuf.message import Message


class GenericMessageService(ABC):
    def __init__(self, message: Message) -> None:
        self.message = message

    @classmethod
    @abstractmethod
    def _message_type(cls) -> Type[Message]:
        raise NotImplementedError

    def serialize(self) -> bytes:
        return self.message.SerializeToString()

    @classmethod
    def deserialize(cls, serialized_msg: bytes) -> Message:
        message_type = cls._message_type()
        message = message_type()
        message.ParseFromString(serialized_msg)
        return message

    @classmethod
    def _new_message(cls) -> Message:
        message_type = cls._message_type()
        message = message_type()
        return message
