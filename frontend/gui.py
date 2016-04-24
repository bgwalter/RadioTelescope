from qt5gui import Ui_RadioTelescope
from telescope import Telescope
from allsky import AllSky

import sys
import time

# matplotlib imports for graphs and figures
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigattionToolbar)

# PyQt 5 imports for GUI
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QTableWidgetItem, QApplication
from PyQt5.uic import loadUiType
Ui_MainWindow, QMainWindow = loadUiType('qt5gui.ui')


class RadioGUI(QMainWindow, Ui_MainWindow):
    def __init__(self, Telescope, SkyMap):
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
        self.parkBtn.clicked.connect(self.park)
        self.recordBtn.stateChanged.connect(self.record)

        # get values from telescope class
        self.telescope = Telescope
        self.siteName = self.telescope.Observer.name
        self.latitude = self.telescope.Observer.location.latitude
        self.longitude = self.telescope.Observer.location.longitude
        self.elevation = self.telescope.Observer.location.height

        # get allsky map
        self.skyMap = SkyMap

        self.populateInfo()
        self.addSkyMap(self.skyMap)

    def populateInfo(self):
        '''
        Add information about the telescope to the window
        '''

        def addToTable(row, string):
            self.telescopeInfo.setItem(row, 1, QTableWidgetItem(string))

        addToTable(0, self.siteName)
        addToTable(1, str(self.latitude))
        addToTable(2, str(self.longitude))
        addToTable(3, str(self.elevation))

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

        if self.telescope.isMoving or self.telescope.isTracking:
            return

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

    def record(self):
        outFile = self.outFile.text()
        self.recordThread = recordThread(outFile, self.telescope, self)

    def addSkyMap(self, skymap):
        fig = skymap.draw(self.telescope.Observer)
        self.canvas = FigureCanvas(fig)
        self.figvl.addWidget(self.canvas)
        self.canvas.draw()


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


class recordThread(QThread):
    def __init__(self, outFile, telescope, qwindow):
        QThread.__init__(self)
        self.outFile = outFile
        self.qwindow = qwindow

    def record(self):
        self.telescope.record(outFile=self.outFile, qwindow=qwindow)


def run(telescope, skymap):
    app = QApplication(sys.argv)
    radiogui = RadioGUI(telescope, skymap)
    radiogui.show()
    sys.exit(app.exec_())
