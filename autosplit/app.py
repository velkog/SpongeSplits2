import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
from PyQt5 import QtGui


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QtGui.QIcon('/Users/kvel/personal/BfBB/SpongeSplits2/res/SpongeSplits.png'))

        self.show()


def main():

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()


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
