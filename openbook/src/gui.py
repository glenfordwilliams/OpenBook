from PySide.QtGui import *
from PySide.QtCore import *
from operations import Operations, rowCount as rowcount
#from PySide import QtCore, QtSql


class GUI(QMainWindow):
    """
    Handling of all the different aspects of the user interface, menus,
     buttons etc..
    """
    def __init__(self):
        super(GUI, self).__init__()
        self.setupMenu()
        self.setWindowIcon(QIcon("./book.ico"))
        self.setWindowTitle("OpenBook")

        self.setGeometry(10, 50 , 1000, 600)

        from database import Database

        self.data = Database()
        self.show()

    def setupMenu(self):
        #setup of the user menu
        menu = self.menuBar()
        self.status = self.statusBar()
        closeAction = QAction("&Quit", self)
        closeAction.setShortcut("Ctrl + q")
        closeAction.setStatusTip("Close OpenBook")
        closeAction.triggered.connect(self.close)
        fileMenu = menu.addMenu("&File")
        editMenu = menu.addMenu("&Edit")

        viewMenu = menu.addMenu("&View")
        addAction = QAction("&Add Entry", self)
        addAction.triggered.connect(self.addEntry)
        gridAction = QAction("&Sheet View", self)
        gridAction.triggered.connect(self.Grid)
        aboutMenu = menu.addMenu("&About")
        aboutAction = QAction("&About OpenBook", self)
        cutAction = QAction("&Cut", self)

        fileMenu.addAction(closeAction)
        viewMenu.addAction(addAction)
        viewMenu.addAction(gridAction)
        aboutMenu.addAction(aboutAction)
        editMenu.addAction(cutAction)

    def addEntry(self):

        from PySide.QtUiTools import QUiLoader

        loader = QUiLoader()

        File = QFile("base.ui")
        File.open(QFile.ReadOnly)
        self.basic = loader.load(File, self)
        File.close()
        self.setCentralWidget(self.basic)
        self.basic.submit.clicked.connect(self.addCon)

    def Grid(self):
        from PySide.QtUiTools import QUiLoader

        loader = QUiLoader()

        File = QFile("gui.ui")
        File.open(QFile.ReadOnly)
        self.widg = loader.load(File, self)
        File.close()

        self.setCentralWidget(self.widg)
        self.widg.tableView.setModel(self.data.show())
        self.widg.submit.clicked.connect(self.gridCon)
        self.widg.updatabase.clicked.connect(self.data.show())
        self.widg.tableView.setSortingEnabled(True)
        self.widg.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)

    def addCon(self):
        Operations(self.basic.firstE.text(), self.basic.middleE.text(),
                   self.basic.lastE.text(), self.basic.ygE.text(),
                    self.basic.idE.text(), self.basic.titleE.text(),
                    self.basic.isdnE.text(), self.basic.authorE.text(),
                    self.basic.dbE.text(), self.basic.drE.text()
                    )

    def gridCon(self):
        Operations(self.widg.firstE.text(), self.widg.middleE.text(),
                   self.widg.lastE.text(), self.widg.ygE.text(),
                    self.widg.idE.text(), self.widg.titleE.text(),
                    self.widg.isdnE.text(), self.widg.authorE.text(),
                    self.widg.dbE.text(), self.widg.drE.text()
                    )


import sys
app = QApplication(sys.argv)
gui = GUI()
sys.exit(app.exec_())
