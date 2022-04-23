from os.base_window import BaseWindow
from typing import List, Sequence

from psutil import AccessDenied, NoSuchProcess, Process, ZombieProcess, process_iter
from settings import config
from win32.win32gui import EnumWindows, IsWindowEnabled, IsWindowVisible
from win32.win32process import GetWindowThreadProcessId


class Window(BaseWindow):
    def __init__(self, process: Process, win_id: int) -> None:
        BaseWindow.__init__(self, win_id)
        self.process = process

    @staticmethod
    def get_windows() -> Sequence[BaseWindow]:
        windows = []
        for process in process_iter():
            try:
                if process.pid is not None:

                    hwnds: List[int] = []

                    def callback(hwid: int, hwnds: List[int]) -> bool:
                        if IsWindowVisible(hwid) and IsWindowEnabled(hwid):
                            _, pid = GetWindowThreadProcessId(hwid)
                            if pid == process.pid:
                                hwnds.append(hwid)
                        return True

                    EnumWindows(callback, hwnds)

                    if hwnds and process.name() not in config.EXCLUSION_LIST:
                        windows.append(Window(process, hwnds[0]))

            except (NoSuchProcess, AccessDenied, ZombieProcess):
                pass

        return windows
