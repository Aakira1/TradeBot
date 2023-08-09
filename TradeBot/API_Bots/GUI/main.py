import typing
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QLayout

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        #MENU BAR
        bar = self.menuBar()
        file = bar.addMenu("File")
        settings = bar.addMenu("Settings")
        file.addAction("New")
        settings.addAction("Properties")

        save = QAction("Save", self)
        save.setShortcut("Ctrl+S")
        file.addAction(save)

        #TABS

    def layout():
        layout = QHBoxLayout()
        return
    
    def label():
        return
    
    def MBar(self):
        return
        
        

def mainWindow():
    app = QApplication(sys.argv)
    app.setApplicationName("Trade Bot")

    main = MainWindow()
    main.setGeometry(100,100,920,720)
    main.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    mainWindow()

    



