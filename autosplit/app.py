from learner.models.pineapple_models import SpatulaModel

model = SpatulaModel()
model._train()

# import logging
# import sys
# from typing import Optional

# from PyQt5 import QtWidgets
# from PyQt5.QtWidgets import QDialog

# # Uncomment below for terminal log messages
# # logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(name)s - %(levelname)s - %(message)s')


# class QTextEditLogger(logging.Handler):
#     def __init__(self, parent: QDialog) -> None:
#         super().__init__()
#         print(type(parent))
#         self.widget = QtWidgets.QPlainTextEdit(parent)
#         self.widget.setReadOnly(True)

#     def emit(self, record: logging.LogRecord) -> None:
#         msg = self.format(record)
#         self.widget.appendPlainText(msg)


# class MyDialog(QDialog, QtWidgets.QPlainTextEdit):
#     def __init__(self, parent: Optional[QDialog] = None) -> None:
#         super().__init__(parent)

#         logTextBox = QTextEditLogger(self)
#         # You can format what is printed to text box
#         logTextBox.setFormatter(
#             logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
#         )
#         logging.getLogger().addHandler(logTextBox)
#         # You can control the logging level
#         logging.getLogger().setLevel(logging.DEBUG)

#         self._button = QtWidgets.QPushButton(self)
#         self._button.setText("Test Me")

#         layout = QtWidgets.QVBoxLayout()
#         # Add the new logging box widget to the layout
#         layout.addWidget(logTextBox.widget)
#         layout.addWidget(self._button)
#         self.setLayout(layout)

#         # Connect signal to slot
#         self._button.clicked.connect(self.test)  # type: ignore

#     def test(self) -> None:
#         logging.debug("damn, a bug")
#         logging.info("something to remember")
#         logging.warning("that's not right")
#         logging.error("foobar")


# app = QtWidgets.QApplication(sys.argv)
# dlg = MyDialog()
# dlg.show()
# dlg.raise_()
# sys.exit(app.exec_())

# from core.frame_collector import FrameCollector
# from core.frame_processor import FrameProcessor
# from core.pineapple_result_handler import PineappleResultHandler as ResultHandler

# if __name__ == "__main__":
#     print("Creating Processes")
#     frame_processor = FrameProcessor()
#     frame_collector = FrameCollector()
#     result_handler = ResultHandler()

#     print("Starting Collector...")
#     frame_processor.start()
#     frame_collector.start()
#     result_handler.start()

#     input("Press enter to exit.\n\n")
