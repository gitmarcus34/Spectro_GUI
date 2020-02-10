#Core Window

from PyQt5 import QtCore, QtGui, QtWidgets # Import the PyQt4 module we'll need
import sys # We need sys so that we can pass argv to QApplication
import Spectrometer

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import StartUpMenu_GUI # This file holds our MainWindow and all StartUpMenu related things
			  # it also keeps events etc that we defined in Qt Designer
import MainMenu_GUI
import ScanningMenu_GUI
import TimeBaseScanningMenu_GUI as TBS_GUI
import StartUpMenu_GUI
import multiDoc_Design
usb = input("Enter the USB port name for the Spectrometer: ")
class CoreWindow(QtWidgets.QMainWindow, multiDoc_Design.Ui_CoreWindow):
	count = 0
	def __init__(self, parent = None):
		#super(self.__class__, self).__init__()
		super(CoreWindow, self).__init__(parent)
		self.setupUi(self)	# This is defined in multiDoc_Design.py file automatically # It sets up layout and widgets that are defined
		self.spectrometer = Spectrometer.Spectrometer(usb)	

		#menu bar
		self.menufiles.triggered[QAction].connect(self.menuBar_action)
		self.menubar.setNativeMenuBar(False)

		####subwindows: start with startmenu when user chooses 'start' from files drop down menu
		#dictionary of sub_windows to pass to and reference from subwindows to avoid importing modules to each subwindow (leads to snake eating own tail bug)
		self.subwindow_dict = {}
		self.startmenu_sub = QMdiSubWindow()
		self.mainmenu_sub = QMdiSubWindow()
		self.scanningmenu_sub = QMdiSubWindow()
		self.tbsmenu_sub = QMdiSubWindow()
		
		self.subwindow_dict['startmenu'] = self.startmenu_sub
		self.subwindow_dict['mainmenu'] = self.mainmenu_sub
		self.subwindow_dict['scanningmenu'] = self.scanningmenu_sub
		self.subwindow_dict['tbsmenu'] = self.tbsmenu_sub
				
		#start menu subwindow
		self.startmenu = StartUpMenu_GUI.StartMenu(mdiArea = self.mdiArea,spectrometer = self.spectrometer, subwindow_dict = self.subwindow_dict)
		#self.startmenu_sub = QMdiSubWindow()
		self.startmenu_sub.setWidget(self.startmenu)
		self.subwindow_dict['startmenu'] = self.startmenu_sub
		
		#main menu subwindow
		self.mainmenu = MainMenu_GUI.MainMenu(mdiArea = self.mdiArea, subwindow_dict = self.subwindow_dict)
		#self.mainmenu_sub = QMdiSubWindow()
		self.mainmenu_sub.setWidget(self.mainmenu)
		self.subwindow_dict['mainmenu'] = self.mainmenu_sub
		
		#scanning menu subwindow
		self.scanningmenu = ScanningMenu_GUI.ScanningMenu(mdiArea = self.mdiArea, spectrometer = self.spectrometer, subwindow_dict = self.subwindow_dict)
		#self.scanningmenu_sub = QMdiSubWindow()
		self.scanningmenu_sub.setWidget(self.scanningmenu)
		self.subwindow_dict['scanningmenu'] = self.scanningmenu_sub
		
		#scanning menu subwindow
		self.tbsmenu = TBS_GUI.TBS_Menu(mdiArea = self.mdiArea,spectrometer = self.spectrometer, subwindow_dict = self.subwindow_dict)
		#self.scanningmenu_sub = QMdiSubWindow()
		self.tbsmenu_sub.setWidget(self.tbsmenu)
		self.subwindow_dict['tbsmenu'] = self.tbsmenu_sub
		

		
	
	def menuBar_action(self, action):
		print("start menu triggered")
		
		if action == self.actionstart:
			if self.startmenu_sub in self.mdiArea.subWindowList():
				print('returned to start menu')
				self.startmenu_sub.show()
				self.startmenu_sub.raise_()
				self.startmenu_sub.activateWindow()
				self.startmenu.show() #must call otherwise widget does not appear in subwindow
			else:
				print('added start menu to mdiArea')
				self.mdiArea.addSubWindow(self.startmenu_sub)
				self.startmenu_sub.show()
				

			
		if action == self.actioncascade:
			self.mdiArea.cascadeSubWindows()
			print('cascade triggered')

		if action == self.actiontiled:
			self.mdiArea.tileSubWindows()
			print('tiled triggered')

		
def main():
	app = QtWidgets.QApplication(sys.argv)	# A new instance of QApplication
	form = CoreWindow()			  # We set the form to be our ExampleApp (StartUpMenu)
	form.show()					  # Show the form
	app.exec_()					  # and execute the app


if __name__ == '__main__':			# if we're running file directly and not importing it
	main()							# run the main function
