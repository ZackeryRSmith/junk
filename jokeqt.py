# Simple script for creating a uncloseable window
# ~ ZackeryRSmith

from sys import exit as _exit
from sys import argv as _argv
from PyQt5.QtWidgets import QApplication, QWidget

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Window title here'
        self.left = self.top = 10
        self.width, self.height = (640, 480)
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.show()

    def closeEvent(self, evnt): 
        try: evnt.ignore()
        except: pass

if __name__ == '__main__':
    app = QApplication(_argv)
    ex = App()
    exit(app.exec_())