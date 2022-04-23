from ctypes import windll
from typing import List

from PIL import Image
from psutil import AccessDenied, NoSuchProcess, Process, ZombieProcess, process_iter
from settings import config
from win32 import win32process
from win32.win32gui import (
    DeleteObject,
    EnumWindows,
    GetClientRect,
    GetWindowDC,
    IsWindowEnabled,
    IsWindowVisible,
    ReleaseDC,
)
from win32ui import CreateBitmap, CreateDCFromHandle


class ProcessInfo:
    def __init__(self, process: Process, hwnd: int) -> None:
        self.process = process
        self.hwnd = hwnd

    def capture(self) -> Image:
        # https://stackoverflow.com/a/24352388

        windll.user32.SetProcessDPIAware()
        left, top, right, bottom = GetClientRect(self.hwnd)
        width = right - left
        height = bottom - top

        hwndDC = GetWindowDC(self.hwnd)
        mfcDC = CreateDCFromHandle(hwndDC)
        saveDC = mfcDC.CreateCompatibleDC()

        saveBitMap = CreateBitmap()
        saveBitMap.CreateCompatibleBitmap(mfcDC, width, height)
        saveDC.SelectObject(saveBitMap)
        windll.user32.PrintWindow(self.hwnd, saveDC.GetSafeHdc(), 1)

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
        ReleaseDC(self.hwnd, hwndDC)

        return image

    @staticmethod
    def get_visible_processes() -> List["ProcessInfo"]:
        processes = []
        for proc in process_iter():
            hwnd = 0
            try:
                process_name = proc.name()
                process_id = proc.pid

                if process_id is not None:

                    def callback(hwid: int, hwnds: List[int]) -> bool:
                        if IsWindowVisible(hwid) and IsWindowEnabled(hwid):
                            _, p = win32process.GetWindowThreadProcessId(hwid)
                            if p == process_id:
                                hwnds.append(hwid)
                        return True

                    hwnds: List[int] = []
                    EnumWindows(callback, hwnds)

                    if hwnds:
                        hwnd = hwnds[0]

                if hwnd and process_name not in config.EXCLUSION_LIST:
                    processes.append(ProcessInfo(proc, hwnd))

            except (NoSuchProcess, AccessDenied, ZombieProcess):
                pass

        return processes
