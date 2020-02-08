from PyQt5 import QtCore, QtGui, QtWidgets # Import the PyQt4 module we'll need
import sys # We need sys so that we can pass argv to QApplication
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from matplotlib import animation
from matplotlib.figure import Figure

class Window(QtWidgets.QDialog): #or QtGui.QWidget ???

	def __init__(self):
		super(Window, self).__init__()
		self.fig = Figure(figsize=(5,4),dpi=100)
		self.canvas = FigureCanvas(self.fig)
		self.button = QtGui.QPushButton('Animate')
		self.button.clicked.connect(self.animate)

		# set the layout
		layout = QtGui.QVBoxLayout()
		layout.addWidget(self.canvas)
		layout.addWidget(self.button)
		self.setLayout(layout)

	def animate(self):
		self.ax = self.fig.add_subplot(111)  # create an axis
		self.ax.hold(False)  # discards the old graph
		self.circle = Circle((0,0), 1.0)
		self.ax.add_artist(self.circle)
		self.ax.set_xlim([0,10])
		self.ax.set_ylim([-2,2])

		self.anim = animation.FuncAnimation(self.fig,self.animate_loop,frames=10,interval=100,repeat=False,blit=False)
		#plt.show()
		self.canvas.draw()

	def animate_loop(self,i):
		self.circle.center=(i,0)
		return self.circle, 

w = Window()
w.show()