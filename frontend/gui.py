from qt5gui import Ui_RadioTelescope
from telescope import Telescope

import sys
import time

# matplotlib imports for graphs and figures
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigattionToolbar)

# PyQt 5 imports for GUI
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import QThread
from PyQt5.uic import loadUiType
Ui_MainWindow, QMainWindow = loadUiType('qt5gui.ui')

class slewingThread(QThread):
    def __init__(self, ra, dec, telescope, qwindow):
        QThread.__init__(self)
        self.ra = ra
        self.dec = dec
        self.telescope = telescope
        self.qwindow = qwindow

    def slewToCoord(self):
        self.telescope.slewToCoord(self.ra, self.dec, qwindow=self.qwindow)
        while self.qwindow.trackBtn.isChecked():
            time.sleep(1)
            self.telescope.slewToCoord(self.ra, self.dec, qwindow=self.qwindow)
        self.quit()

    def run(self):
        self.slewToCoord()

    def __del__(self):
        self.wait()


class RadioGUI(QMainWindow, Ui_MainWindow):
    def __init__(self, Telescope):
        '''
        Initialize the GUI

        Parameters
        ----------
        telescope : `~telescope.Telescope`
            The telescope object to control
        '''

        # setup PyQt5 class
        super(RadioGUI, self).__init__()
        self.setupUi(self)

        # configure buttons to call functions
        self.slewBtn.clicked.connect(self.slewToCoord)
        self.slewBtn.clicked.connect(self.park)

        # get values from telescope class
        self.telescope = Telescope
        self.siteName = self.telescope.Observer.name
        self.latitude = self.telescope.Observer.location.latitude
        self.longitude = self.telescope.Observer.location.longitude

        self.populateInfo()

    def populateInfo(self):
        '''
        Add information about the telescope to the window
        '''

        self.telescopeInfo.addItem("Site: %s" % self.siteName)
        self.telescopeInfo.addItem("Latitude: %s" % self.latitude)
        self.telescopeInfo.addItem("Longitude: %s" % self.longitude)

    def printInfo(self, string):
        '''
        Print information to the command output box

        Parameters
        ----------
        string : str
            String to print to the window
        '''

        self.commandOutput.addItem(string)

    def slewToCoord(self):
        '''
        Slew to the RA/Dec coordinates given as user input in the window
        '''

        # get the coordinates from the input box
        ra = self.ra.text()
        dec = self.dec.text()

        self.slewThread = slewingThread(ra, dec, self.telescope, self)
        self.slewThread.start()

    def track(self):
        ra = self.ra.text()
        dec = self.dec.text()
        self.slewThread = slewingThread(ra, dec, self.telescope, self)
        self.slewThread.start()

    def park(self):
        pass


def run(telescope):
    app = QtWidgets.QApplication(sys.argv)
    radiogui = RadioGUI(telescope)
    radiogui.show()
    sys.exit(app.exec_())
