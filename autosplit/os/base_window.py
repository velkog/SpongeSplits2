from abc import ABC, abstractmethod
from typing import Sequence


class BaseWindow(ABC):
    def __init__(self, win_id: int):
        self.win_id = win_id

    @staticmethod
    @abstractmethod
    def get_windows() -> Sequence["BaseWindow"]:
        raise NotImplementedError
