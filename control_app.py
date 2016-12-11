#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 04:50:02 2016

@author: jafrey
"""
from PyQt5.uic import loadUiType

Ui_MainWindow, QMainWindow = loadUiType('control_gui.ui')
        
class MainWindow(QMainWindow, Ui_MainWindow):  
#class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        # Explaining super is out of the scope of this article
        # So please google it if you're not familar with it
        # Simple reason why we use it here is that it allows us to
        # access variables, methods etc in the design.py file
        super(self.__class__, self).__init__()
        self.setupUi(self)  # This is defined in design.py file automatically
        self.actionAbout.toggled.connect(self.actionAbout99)        
        
    def actionAbout99(self):
        QtWidgets.QMessageBox.about(self, "About",
                                    """Copyright 2016 Jed Frey
                                    
This program is a simple GUI example for controls.""")
        
   
if __name__ == '__main__':
    import sys
    from PyQt5 import QtWidgets  
    app = QtWidgets.QApplication(sys.argv)  # A new instance of QApplication
    main = MainWindow() 
    main.show()
    sys.exit(app.exec_())