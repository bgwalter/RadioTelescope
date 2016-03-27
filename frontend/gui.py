import sys

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigattionToolbar)

from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.uic import loadUiType
Ui_MainWindow, QMainWindow = loadUiType('qt5gui.ui')

from qt5gui import Ui_RadioTelescope


class RadioGUI(QMainWindow, Ui_MainWindow):
    def __init__(self, location):
        super(RadioGUI, self).__init__();
        self.setupUi(self)

        self.siteName = location["SITE_NAME"]
        self.latitude = location["LATITUDE"]
        self.longitude = location["LONGITUDE"]

        self.slewBtn.clicked.connect(self.slew)
        self.slewBtn.clicked.connect(self.park)

        self.populateInfo();

    def populateInfo(self):
        self.telescopeInfo.addItem("Site: %s" %self.siteName)
        self.telescopeInfo.addItem("Latitude: %s" %self.latitude)
        self.telescopeInfo.addItem("Longitude: %s" %self.longitude)

    def slew(self):
        pass

    def park(self):
        pass

def run(location):
    app = QtWidgets.QApplication(sys.argv)
    radiogui = RadioGUI(location)
    radiogui.show()
#    RadioTelescope = QtWidgets.QMainWindow()
#    ui = Ui_RadioTelescope()
#    ui.setupUi(RadioTelescope)
#    RadioTelescope.show()
    sys.exit(app.exec_())
