from abc import ABC, abstractmethod
from typing import Sequence

from PIL import Image


class BaseWindow(ABC):
    def __init__(self, name: str, win_id: int):
        self._name = name
        self.win_id = win_id

    @property
    def name(self) -> str:
        return self._name

    @staticmethod
    @abstractmethod
    def get_windows() -> Sequence["BaseWindow"]:
        raise NotImplementedError

    @abstractmethod
    def capture(self) -> Image:
        raise NotImplementedError
