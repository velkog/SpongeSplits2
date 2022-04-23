from core.frame_collector import FrameCollector
from core.frame_processor import FrameProcessor
from core.result_handler import ResultHandler

if __name__ == "__main__":
    print("Creating Processes")
    frame_processor = FrameProcessor()
    frame_collector = FrameCollector()
    result_handler = ResultHandler()

    print("Starting Collector...")
    frame_processor.start()
    frame_collector.start()
    result_handler.start()

    input("Press enter to exit.\n\n")
