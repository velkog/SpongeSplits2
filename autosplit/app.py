from core.frame_collector import FrameCollector
from core.frame_processor import FrameProcessor
from core.result_handler import ResultHandler
from system.system_window import SystemWindow


def select_window() -> SystemWindow:
    windows = SystemWindow.get_windows()
    print(f"\nSelect a window (1-{len(windows)}):")
    for i, window in enumerate(windows):
        print(f"\t{i + 1}. {window.name}")
    window_index = int(input())
    assert window_index > 0 and window_index <= len(windows)
    window = windows[window_index - 1]
    assert isinstance(window, SystemWindow)
    return window


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
    frame_processor.terminate()
    frame_collector.terminate()
    result_handler.terminate()
