import psutil
from win32 import win32gui, win32process
from ctypes import windll
import win32ui
from settings import config
import numpy as np


def get_visible_processes():
    """ Returns a list of processes with a valid hwnd """
    processes = []
    for proc in psutil.process_iter():
        hwnd = 0
        try:
            # Get process name & pid from process object.
            process_name = proc.name()
            process_id = proc.pid

            if process_id is not None:
                def callback(h, additional):
                    if win32gui.IsWindowVisible(h) and win32gui.IsWindowEnabled(h):
                        _, p = win32process.GetWindowThreadProcessId(h)
                        if p == process_id:
                            additional.append(h)
                        return True
                    return True

                additional = []
                win32gui.EnumWindows(callback, additional)

                if additional:
                    hwnd = additional[0]

            if hwnd and process_name not in config.EXCLUSION_LIST:
                processes.append((proc, hwnd))

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return processes

def get_hwnd_from_list(process_name, process_list):
    """ Given a list of processes, return process with given name """
    for p in process_list:
        if p[0].name() == process_name:
            return p[1]


def capture(hwnd):
    """
    https://stackoverflow.com/a/24352388
    """
    left, top, right, bot = win32gui.GetWindowRect(hwnd)
    w = right - left
    h = bot - top


    hwnd_dc = win32gui.GetWindowDC(hwnd)
    mfc_dc = win32ui.CreateDCFromHandle(hwnd_dc)
    save_dc = mfc_dc.CreateCompatibleDC()

    save_bitmap = win32ui.CreateBitmap()
    save_bitmap.CreateCompatibleBitmap(mfc_dc, w, h)

    save_dc.SelectObject(save_bitmap)

    result = windll.user32.PrintWindow(hwnd, save_dc.GetSafeHdc(), 0)

    bmp_info = save_bitmap.GetInfo()
    bmp_str = save_bitmap.GetBitmapBits(True)

    image = np.fromstring(bmp_str, np.uint8).reshape(bmp_info['bmHeight'], bmp_info['bmWidth'], 4)[:,:,:3]

    win32gui.DeleteObject(save_bitmap.GetHandle())
    save_dc.DeleteDC()
    mfc_dc.DeleteDC()
    win32gui.ReleaseDC(hwnd, hwnd_dc)

    return image


def get_capture_size(hwnd):
    left, top, right, bot = win32gui.GetWindowRect(hwnd)

    return [right - left, bot - top]

from PIL import Image as im

# processes = get_visible_processes()
# for process, hwnd in processes:
#     print(process)
#     imgage_array = capture(hwnd)
#     image = im.fromarray(imgage_array)
#     image.show()
#     input("waiting for next process")


from PIL import ImageGrab
import win32gui

toplist, winlist = [], []
def enum_cb(hwnd, results):
    winlist.append((hwnd, win32gui.GetWindowText(hwnd)))

win32gui.EnumWindows(enum_cb, toplist)

# for hwnd, title in winlist:
#     print(hwnd)
#     print(title)
#     print("----")

firefoxes = [(hwnd, title) for hwnd, title in winlist if 'firefox' in title.lower()]
for firefox in firefoxes:
    # just grab the hwnd for first window matching firefox
    hwnd = firefox[0]

    win32gui.SetForegroundWindow(hwnd)
    bbox = win32gui.GetWindowRect(hwnd)
    img = ImageGrab.grab(bbox)
    img.show()