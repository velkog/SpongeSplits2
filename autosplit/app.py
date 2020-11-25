from gui.application import Application

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton
import sys

import sys
from PyQt5 import Qt


# Only actually do something if this script is run standalone, so we can test our 
# application, but we're also able to import this program without actually running
# any code.
if __name__ == "__main__":
    app = Application()
    app.exec()

    # app.exec()



    # app = QApplication([])

    # w = QWidget()

    # grid = QGridLayout(w)
    # grid.addWidget(QPushButton("Button one"),0,0)
    # grid.addWidget(QPushButton("Button two"),0,1)
    # grid.addWidget(QPushButton("Button three"),1,0)
    # grid.addWidget(QPushButton("Button four"),1,1)


    # w.show()
    # sys.exit(app.exec_())

# from core.frame_processor import FrameProcessor
# from core.frame_collector import FrameCollector
# from core.result_handler import ResultHandler

# r = ResultHandler()
# w1 = FrameProcessor()
# w2 = FrameProcessor()
# a = FrameCollector()

# r.start()
# a.start()
# w1.start()
# w2.start()

# input("------ Press enter to exit -----\n\n")
