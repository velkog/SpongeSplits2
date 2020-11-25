from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton
from sys import exit
from PyQt5 import Qt
from PyQt5 import QtCore
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget

from conf import constants

class HelloWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(640, 480))    
        self.setWindowTitle("Hello world - pythonprogramminglanguage.com") 

        centralWidget = QWidget(self)          
        self.setCentralWidget(centralWidget)   

        gridLayout = QGridLayout(self)     
        centralWidget.setLayout(gridLayout)

        title = QLabel("Hello World from PyQt", self) 
        title.setAlignment(QtCore.Qt.AlignCenter) 
        gridLayout.addWidget(title, 0, 0)

class Application(QApplication):
    def __init__(self):
        super().__init__([])
        self.addWidgets()
        self.title = "woo"

    class MainWindow(QMainWindow):
        def __init__(self) -> None:
            super().__init__()
            
            print(constants)
            self.setMinimumSize(QSize(constants.WIN_HEIGHT, constants.WIN_WIDTH))    
            self.setWindowTitle(self.title()) 

            centralWidget = QWidget(self)          
            self.setCentralWidget(centralWidget)   

            gridLayout = QGridLayout(self)     
            centralWidget.setLayout(gridLayout)  

            title = QLabel("Hello World from PyQt", self) 
            title.setAlignment(QtCore.Qt.AlignCenter) 
            gridLayout.addWidget(title, 0, 0)
        
        @staticmethod
        def title() -> str:
            return f"{constants.TITLE} {version}"

    def addWidgets(self):
        """ In this method, we're adding widgets and connecting signals from 
            these widgets to methods of our class, the so-called "slots" 
        """
        self.mainWin = self.MainWindow()
        self.mainWin.show()

        # self.hellobutton = Qt.QPushButton("Say 'Hello world!'")
        # self.hellobutton.clicked.connect(self.slotSayHello)
        # self.hellobutton.show()

    def slotSayHello(self):
        """ This is an example slot, a method that gets called when a signal is 
            emitted """
        print ("Hello, World!")
    
    def exec(self) -> None:
        self.exec_()


# class Application(QApplication):
#     def __init__(self) -> None:
#         super().__init__([])
#         root = QWidget()
#         root.resize(320, 240)
#         root.setWindowTitle("hello")
#         root.show
    
#     def exec(self):
#         self.exec_()

# class Application(QMainWindow):
#     def __init__(self, parent = None) -> None:
#         super().__init__(parent=parent)
#         self.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
#         self.width = 365
#         self.height = 259
#         self.initialize()
#         self.show()

#     @property
#     def title(self) -> str:
#         return f"{constants.TITLE} {version}"
