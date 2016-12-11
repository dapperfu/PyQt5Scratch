
# coding: utf-8

# In[1]:

import sys
from mainwindow_test import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets


# In[2]:

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        # Explaining super is out of the scope of this article
        # So please google it if you're not familar with it
        # Simple reason why we use it here is that it allows us to
        # access variables, methods etc in the design.py file
        super(self.__class__, self).__init__()
        self.setupUi(self)  # This is defined in design.py file automatically


# In[3]:

def main():
    app = QtWidgets.QApplication(sys.argv)  # A new instance of QApplication
    form = MainWindow()  # We set the form to be our ExampleApp (design)
    form.show()  # Show the form
    app.exec_()  # and execute the app


# In[5]:

if __name__ == '__main__':  # if we're running file directly and not importing it
    main()  # run the main function

