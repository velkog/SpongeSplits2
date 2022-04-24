from typing import Sequence

from PIL import Image
from system.base_window import BaseWindow


class Window(BaseWindow):
    @staticmethod
    def get_windows() -> Sequence[BaseWindow]:
        pass

    def capture(self) -> Image:
        pass
