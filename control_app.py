#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 04:50:02 2016

@author: jafrey
"""
from PyQt5.uic import loadUiType
from PyQt5 import QtWidgets
import sys
import numpy as np

from matplotlib.figure import Figure

from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)
    

Ui_MainWindow, QMainWindow = loadUiType('control_gui.ui')

class ControlCanvas(FigureCanvas):
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        
        self.compute_initial_figure()

        #
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QtWidgets.QSizePolicy.Expanding,
                                   QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        

    def compute_initial_figure(self):
        pass
    
class StaticControlCanvas(ControlCanvas):
    """Simple canvas with a sine plot."""

    def compute_initial_figure(self):
        t = np.arange(0.0, 3.0, 0.01)
        s = np.sin(2*np.pi*t)
        self.axes.plot(t, s)
        
class MainWindow(QMainWindow, Ui_MainWindow):  
#class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        # Explaining super is out of the scope of this article
        # So please google it if you're not familar with it
        # Simple reason why we use it here is that it allows us to
        # access variables, methods etc in the design.py file
        super(self.__class__, self).__init__()
        
        self.setupUi(self)
        self.pushButton.clicked.connect(self.makeplot)
        
        self.actionAbout.triggered.connect(self.browse_folder)
        self.actionNew.triggered.connect(self.makeplot)
        self.actionQuit.triggered.connect(self.close)
        
        self.statusBar().showMessage("", 5000)
        
        self.fig = Figure()
        self.plot_axis = self.fig.add_subplot(111)
        
        # Slider changes.
        self.horizontalSlider.valueChanged.connect(self.slider_value_change)
        

    def makeplot(self):
        self.plot_axis.plot(np.random.rand(5))
        
        try:
            self.mplvl.removeWidget(self.canvas)
            self.canvas.close()
        except:
            pass            
            
        self.canvas = FigureCanvas(self.fig)
        self.mplvl.addWidget(self.canvas)
        self.canvas.draw()


    def slider_value_change(self,):
        print(self.horizontalSlider.value())
        self.lineEdit.value=str(self.horizontalSlider.value())
        
    def browse_folder(self,):
        QtWidgets.QMessageBox.about(self, "About", """Copyright 2016 Jed Frey""")

    def actionAbout(self):
        print("Hello World")

    def actionEaster_Eggs(self,):
        print("Hello Easter Egg")
 #       QtWidgets.QMessageBox.about(self, "About",
#                                    """Copyright 2016 Jed Frey
#                                This program is a simple GUI example for controls.""")
        
   
if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)  # A new instance of QApplication
    main = MainWindow() 
    main.show()
    sys.exit(app.exec_())