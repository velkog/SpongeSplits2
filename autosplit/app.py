from core.frame_collector import FrameCollector
from core.frame_processor import FrameProcessor
from core.result_handler import ResultHandler
from system.base_window import BaseWindow
from system.win.window import Window


def select_window() -> BaseWindow:
    windows = Window.get_windows()
    print(f"\nSelect a window (1-{len(windows)}):")
    for i, window in enumerate(windows):
        print(f"\t{i + 1}. {window.name}")
    window_index = int(input())
    assert window_index > 0 and window_index <= len(windows)
    return windows[window_index - 1]


if __name__ == "__main__":
    window = select_window()
    frame_collector = FrameCollector(window)

    # print("Creating Processes")
    frame_processor = FrameProcessor()
    result_handler = ResultHandler()

    # print("Starting Collector...")
    frame_processor.start()
    frame_collector.start()
    result_handler.start()

    input("Press enter to exit.\n\n")
