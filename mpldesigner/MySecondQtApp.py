
# coding: utf-8

# In[1]:

from PyQt5.uic import loadUiType

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)


# In[2]:

from control.matlab import *


# In[3]:

s=tf([1,0],[1])


# In[4]:

a=3
b=2
c=1
Plant = a/(b*s+c)

t=0
t_final = 100
dt = 0.01
T = np.arange(t, t_final+dt, dt)


# In[5]:

X0 = 0.0


# In[6]:

yout, T = step(Plant, T=T, X0=X0)


# In[2]:

Ui_MainWindow, QMainWindow = loadUiType('window.ui')
        
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, ):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.fig_dict = {}

        self.mplfigs.itemClicked.connect(self.changefig)

        fig = Figure()
        self.addmpl(fig)

    def changefig(self, item):
        text = item.text()
        print("item.text: "+text)
        self.rmmpl()
        self.addmpl(self.fig_dict[text])

    def addfig(self, name, fig):
        self.fig_dict[name] = fig
        self.mplfigs.addItem(name)

    def addmpl(self, fig):
        self.canvas = FigureCanvas(fig)
        self.mplvl.addWidget(self.canvas)
        self.canvas.draw()
        self.toolbar = NavigationToolbar(self.canvas, 
                self.mplwindow, coordinates=True)
        self.mplvl.addWidget(self.toolbar)
# This is the alternate toolbar placement. Susbstitute the three lines above
# for these lines to see the different look.
#        self.toolbar = NavigationToolbar(self.canvas,
#                self, coordinates=True)
#        self.addToolBar(self.toolbar)

    def rmmpl(self,):
        self.mplvl.removeWidget(self.canvas)
        self.canvas.close()
        self.mplvl.removeWidget(self.toolbar)
        self.toolbar.close()


# In[ ]:

if __name__ == '__main__':
    import sys
    from PyQt5 import QtWidgets
    from pylab import *
    from control.matlab import *
    
    yout, T = step(Plant, T=T, X0=X0)
    fig1 = Figure()
    ax1f1 = fig1.add_subplot(111)
    ax1f1.plot(T,yout)

    fig2 = Figure()
    ax1f2 = fig2.add_subplot(121)
    ax1f2.plot(np.random.rand(5))
    ax2f2 = fig2.add_subplot(122)
    ax2f2.plot(np.random.rand(10))

    fig3 = Figure()
    ax1f3 = fig3.add_subplot(111)
    ax1f3.pcolormesh(np.random.rand(20,20))

    app = QtWidgets.QApplication(sys.argv)  # A new instance of QApplication
    main = MainWindow() 
    main.addfig('One plot', fig1)
    main.addfig('Two plots', fig2)
    main.addfig('Pcolormesh', fig3)
    main.show()
    sys.exit(app.exec_())

