from ctypes import windll
from typing import List, Sequence

from PIL import Image
from psutil import AccessDenied, NoSuchProcess, ZombieProcess, process_iter
from settings import config
from system.base_window import BaseWindow
from win32.win32gui import (
    DeleteObject,
    EnumWindows,
    GetClientRect,
    GetWindowDC,
    IsWindowEnabled,
    IsWindowVisible,
    ReleaseDC,
)
from win32.win32process import GetWindowThreadProcessId
from win32ui import CreateBitmap, CreateDCFromHandle


def hi(f) -> str:
    return 4


class Window(BaseWindow):
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
                        windows.append(Window(process.name(), hwnds[0]))

            except (NoSuchProcess, AccessDenied, ZombieProcess):
                pass

        return windows

    def capture(self) -> Image:
        # https://stackoverflow.com/a/24352388

        windll.user32.SetProcessDPIAware()
        left, top, right, bottom = GetClientRect(self.win_id)
        width = right - left
        height = bottom - top

        hwndDC = GetWindowDC(self.win_id)
        mfcDC = CreateDCFromHandle(hwndDC)
        saveDC = mfcDC.CreateCompatibleDC()

        saveBitMap = CreateBitmap()
        saveBitMap.CreateCompatibleBitmap(mfcDC, width, height)
        saveDC.SelectObject(saveBitMap)
        windll.user32.PrintWindow(self.win_id, saveDC.GetSafeHdc(), 1)

        bmpinfo = saveBitMap.GetInfo()
        bmpstr = saveBitMap.GetBitmapBits(True)
        image = Image.frombuffer(
            "RGB",
            (bmpinfo["bmWidth"], bmpinfo["bmHeight"]),
            bmpstr,
            "raw",
            "BGRX",
            0,
            1,
        )

        DeleteObject(saveBitMap.GetHandle())
        saveDC.DeleteDC()
        mfcDC.DeleteDC()
        ReleaseDC(self.win_id, hwndDC)

        return image
