from PyQt5 import QtCore, QtGui, QtWidgets # Import the PyQt4 module we'll need
import sys # We need sys so that we can pass argv to QApplication

import MainMenu_Design
#import ScanningMenu_GUI

class MainMenu(QtWidgets.QFrame, MainMenu_Design.Ui_MainMenu):
	def __init__(self, mdiArea =None, subwindow_dict = None):
		super(self.__class__, self).__init__()
		self.setupUi(self)  # This is defined in MainMenu_Design.p file automatically # It sets up layout and widgets that are defined
		self.subwindow_dict = subwindow_dict
		self.mdiArea = mdiArea
		
		#Subwindows
		self.scanningmenu_sub = self.subwindow_dict['scanningmenu']	
		
		self.ScanningMenu_Button.clicked.connect(self.scanningmenu_path)
		
		"""###Subwindows
		#scanning subwindow
		self.scanningmenu = ScanningMenu_GUI.ScanningMenu()
		self.scanningmenu_sub = QMdiSubWindow()
		self.scanningmenu_sub.setWidget(self.scanningmenu)
		
		"""
		
	def scanningmenu_path(self, action):
		"""#if main menu button is clicked then a subwindow is opened in mdiArea (mdi in coreWindow)
		"""
		print("scanning menu triggered")
		
		#Check if subwindow already exists, show it and its widgets in case user had exited out.
		if self.scanningmenu_sub in self.mdiArea.subWindowList():
			print('returned to scanningmenu')
			self.scanningmenu_sub.show()
			self.scanningmenu_sub.activateWindow()
			self.scanningmenu_sub.raise_()

			self.scanningmenu_sub.widget().show() #must call otherwise widget does not appear in subwindow if user exited out of subwindow onece before
		else:
			print('added scanning menu to mdiArea')
			self.mdiArea.addSubWindow(self.scanningmenu_sub)
			self.scanningmenu_sub.show()
		

def main():
	app = QtWidgets.QApplication(sys.argv)  # A new instance of QApplication
	form = MainMenu()				 # We set the form to be our ExampleApp (StartUpMenu)
	form.show()						 # Show the form
	app.exec_()						 # and execute the app


if __name__ == '__main__':			  # if we're running file directly and not importing it
	main()							  # run the main function