from PyQt5 import QtCore, QtGui, QtWidgets # Import the PyQt4 module we'll need
import sys # We need sys so that we can pass argv to QApplication
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import StartUpMenu_Design # This file holds our MainWindow and all StartUpMenu related things
			  # it also keeps events etc that we defined in Qt Designer
#import MainMenu_GUI

class StartMenu(QtWidgets.QMainWindow, StartUpMenu_Design.Ui_StartUp_Menu):
	def __init__(self, mdiArea = None,spectrometer = None, subwindow_dict = None):
		super(self.__class__, self).__init__()
		self.setupUi(self)  # This is defined in StartUpMenu_Design.py file automatically # It sets up layout and widgets that are defined
		self.mdiArea = mdiArea
		self.spectrometer = spectrometer
		self.subwindow_dict = subwindow_dict
		
		#subwindows
		print(self.subwindow_dict)
		self.mainmenu_sub = self.subwindow_dict['mainmenu']


		"""###define subwindows for CoreWindow that span from widgetActions in this menu.
		#main menu subwindow
		self.mainmenu = MainMenu_GUI.MainMenu()
		self.mainmenu_sub = QMdiSubWindow()
		self.mainmenu_sub.setWidget(self.mainmenu)
		
		"""
		
		self.MainMenu_Button.clicked.connect(self.mainmenu_path)
		
		#initialize button
		self.Initialize_Button.clicked.connect(self.HR460_Initialize)
		
		###Progress Bar
		self.progressSignal = self.spectrometer.getProgressSignal()
		self.progressSignal.connect(self.updateProgressBar)
		self.progressIncrement = 100/12

	def updateProgressBar(self, message, startUp):
		if startUp != 'start up':
			return
		self.progressBar.setFormat(message)
		currentVal = self.progressBar.value()
		self.progressBar.setValue(currentVal+self.progressIncrement)

	
	def mainmenu_path(self, action):
		"""#if main menu button is clicked then a subwindow is opened in mdiArea (mdi in coreWindow)
		"""
		print("main menu triggered")
		
		#Check if subwindow already exists, show it and its widgets in case user had exited out.
		if self.mainmenu_sub in self.mdiArea.subWindowList():
			print('returned to main menu')
			self.mainmenu_sub.show()
			self.mainmenu_sub.raise_()
			self.mainmenu_sub.activateWindow()
			self.mainmenu_sub.widget().show() #must call otherwise widget does not appear in subwindow if user exited out of subwindow onece before
		else:
			print('added main menu to mdiArea')
			self.mdiArea.addSubWindow(self.mainmenu_sub)
			self.mainmenu_sub.show()
			
	def HR460_Initialize(self):
		"""When Inititalize button is pressed, initialize the spectrometer and update the progress bar. 
		Opens Main Menu subwindow when done
		"""
		self.progressBar.reset()
		
		####initialize the spectrometer when intialize button is pressed.
		print('spectrometer is initializing')
		self.spectrometer.on(fromStartUpMenu = True)


		self.progressSignal.emit('Setting monochromator motor speed', 'start up')
		self.spectrometer.setMotorSpeed()

		self.progressSignal.emit('Setting front (axial) entrance slit motor speed', 'start up')
		self.spectrometer.setSlitSpeed('0')

		self.progressSignal.emit('Setting side (lateral) entrance slit motor speed', 'start up')
		self.spectrometer.setSlitSpeed('1')

		self.progressSignal.emit('Setting front (axial) exit slit motor speed', 'start up')
		self.spectrometer.setSlitSpeed('2')

		self.progressSignal.emit('Setting front (lateral) exit slit motor speed', 'start up')
		self.spectrometer.setSlitSpeed('3')

		self.progressSignal.emit('Initializing: autocalibrating monochromator to base grating (1200 l/mm)', 'start up')
		self.spectrometer.initialize()

		self.progressSignal.emit('Spectrometer is Initialized and ready for scanning!', 'start up')
		print('spectrometer is initialized')
		self.progressBar.setValue(100)
		
		

		
def main():
	app = QtWidgets.QApplication(sys.argv)  # A new instance of QApplication
	form = StartMenu()				 # We set the form to be our ExampleApp (StartUpMenu)
	form.show()						 # Show the form
	app.exec_()						 # and execute the app


if __name__ == '__main__':			  # if we're running file directly and not importing it
	main()							  # run the main function
