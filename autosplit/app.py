from core.frame_processor import FrameProcessor
from core.frame_collector import FrameCollector
from core.result_handler import ResultHandler

r = ResultHandler()
w1 = FrameProcessor()
w2 = FrameProcessor()
a = FrameCollector()

r.start()
a.start()
w1.start()
w2.start()

input("------ Press enter to exit -----\n\n")
