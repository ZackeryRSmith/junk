# Simple script for creating a file dialog
# ~ ZackeryRSmith

from sys import exit as _exit
from sys import argv as _argv
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 file dialog testing'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.openFileNameDialog()
        self.openFileNamesDialog()
        self.saveFileDialog()
        
        self.show()
    
    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "", options=options)
        if fileName: print(fileName)
    
    def openFileNamesDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(self,"QFileDialog.getOpenFileNames()", "", options=options)
        if files: print(files)
    
    def saveFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()", "", options=options)
        if fileName: print(fileName)

if __name__ == '__main__':
    app = QApplication(_argv)
    ex = App()
    exit(app.exec_())