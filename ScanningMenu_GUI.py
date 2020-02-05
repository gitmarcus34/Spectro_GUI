from PyQt5 import QtCore, QtGui, QtWidgets # Import the PyQt4 module we'll need
import sys # We need sys so that we can pass argv to QApplication
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
#import matplotlib
import ScanningMenu_Design # This file holds our MainWindow and all StartUpMenu related things
			  # it also keeps events etc that we defined in Qt Designer


class ScanningMenu(QtWidgets.QMainWindow, ScanningMenu_Design.Ui_ScanningMenu):
	def __init__(self, mdiArea = None,spectrometer = None, subwindow_dict = None):
		super(self.__class__, self).__init__()
		self.setupUi(self)  # This is defined in StartUpMenu_Design.py file automatically # It sets up layout and widgets that are defined
		self.mdiArea = mdiArea
		self.spectrometer = spectrometer
		self.subwindow_dict = subwindow_dict
		
		#bar menu
		##window paths
		self.menuMain.triggered[QAction].connect(self.menuBar_action)
		self.menuScan.triggered[QAction].connect(self.menuBar_action)
		
		#scan parameters
		self.detector, self.gain, self.grating = ('Side', 'AUTO', '1800 l/mm (Vis)') #defaultParams
		self.menuDetector.triggered[QAction].connect(self.menuBar_action)
		self.detectorOptions = {self.actionSide: 'Side', self.actionFront: 'Front'}
		
		self.menuGain.triggered[QAction].connect(self.menuBar_action)
		self.gainOptions = {self.actionAuto: 'AUTO', self.action1X: '1X', self.action10X: '10X', self.action100X: '100X', self.action1000X: '1000X'}
		
		self.menuGrating.triggered[QAction].connect(self.menuBar_action)
		self.gratingOptions = {self.action1800Grating: '1800 l/mm (Vis)', self.action600Grating: '600 l/mm (IR)'}
		
		
		#subwindows
		self.mainmenu_sub = self.subwindow_dict['mainmenu']
		self.tbsmenu_sub = self.subwindow_dict['tbsmenu']
		
		###sliders 
		#Signals
		self.EntranceSlitSlider.valueChanged.connect(self.sliderEnt_Change)
		self.ExitSlitSlider.valueChanged.connect(self.sliderExit_Change)
		self.IntegrationTimeSlider.valueChanged.connect(self.sliderInt_Change)
		self.StepSizeSlider.valueChanged.connect(self.sliderStep_Change)
		
		#slider properties
		self.maxEnt_nm = 10000
		self.tickInterval = self.maxEnt_nm/20
		self.EntranceSlitSlider.setMaximum(self.maxEnt_nm)
		self.EntranceSlitSlider.setTickInterval(self.tickInterval)
		
		self.maxExit_nm = 10000
		self.tickInterval = self.maxExit_nm/20
		self.ExitSlitSlider.setMaximum(self.maxExit_nm)
		self.ExitSlitSlider.setTickInterval(self.tickInterval)
		
		self.maxIntTime_ms = 500
		self.tickInterval = self.maxIntTime_ms/20
		self.IntegrationTimeSlider.setMaximum(self.maxIntTime_ms)
		self.IntegrationTimeSlider.setTickInterval(self.tickInterval)
		
		self.maxStepSize_nm = 500
		self.tickInterval = self.maxStepSize_nm/20
		self.StepSizeSlider.setMaximum(self.maxStepSize_nm)
		self.StepSizeSlider.setTickInterval(self.tickInterval)
		
		#Buttons
		self.ApplySettings_Button.clicked.connect(self.applysettings)

		
		"""###define subwindows for CoreWindow that span from widgetActions in this menu.
		#main menu subwindow
		self.mainmenu = MainMenu_GUI.MainMenu()
		self.mainmenu_sub = QMdiSubWindow()
		self.mainmenu_sub.setWidget(self.mainmenu)
		
		#initialize button
		self.Initialize_Button.clicked.connect(self.HR460_Initialize)
		"""
	
	def sliderEnt_Change(self, slider_val):
		self.lcdNum_EntranceSlider.display(slider_val)
		
	def sliderExit_Change(self, slider_val):
		self.lcdNum_ExitSlider.display(slider_val)
	
	def sliderInt_Change(self, slider_val):
		self.lcdNum_IntTimeSlider.display(slider_val)
		
	def sliderStep_Change(self, slider_val):
		self.lcdNum_StepSizeSlider.display(slider_val)
		
	def applysettings(self):
		print('Applying Settings!')
		self.intTime = self.IntegrationTimeSlider.value()
		self.entSize = self.EntranceSlitSlider.value()
		self.exitSize = self.ExitSlitSlider.value()
		self.stepSize = self.StepSizeSlider.value()
		print('Detector:', self.detector, '; Gain:', self.gain, '; Grating:', self.grating)
		
		print('Entrance Width:', self.entSize)
		print('Exit width:', self.exitSize)
		print('Integration time:', self.intTime)
		print('Step Size:', self.stepSize)
		#self.spectrometer.setScanGUI('0','0','0',str(intTime),str(int(entSize/12.5)),str(int(extSize/12.5)),str(gain),grating,detector,'3',str(gratingPos),str(incTime),str(totalTime)):

	
	def menuBar_action(self, action):
		"""#if main menu button is clicked then a subwindow is opened in mdiArea (mdi in coreWindow)
		"""
		print("menu bar action triggered")
		if action == self.actionMainMenu:
			#Check if subwindow already exists, show it and its widgets in case user had exited out.
			if self.mainmenu_sub in self.mdiArea.subWindowList():
				print('returned to main menu')
				self.mainmenu_sub.show()
				self.mainmenu_sub.raise_() #bring the menu into view
				self.mainmenu_sub.activateWindow() #set as active window (only really important if usr has to use keyboard on the menu.
				self.mainmenu_sub.widget().show() #must call otherwise widget does not appear in subwindow if user exited out of subwindow onece before
			else:
				print('added main menu to mdiArea')
				self.mdiArea.addSubWindow(self.mainmenu_sub)
				self.mainmenu_sub.show()
		
		elif action == self.actionTimeMenu:
			print('Triggered time base scanning')
		#Check if subwindow already exists, show it and its widgets in case user had exited out.
			if self.tbsmenu_sub in self.mdiArea.subWindowList():
				print('returned to time menu')
				self.tbsmenu_sub.show()
				self.tbsmenu_sub.raise_() #bring the menu into view
				self.tbsmenu_sub.activateWindow() #set as active window (only really important if usr has to use keyboard on the menu.
				self.tbsmenu_sub.widget().show() #must call otherwise widget does not appear in subwindow if user exited out of subwindow onece before
			else:
				print('added time menu to mdiArea')
				self.mdiArea.addSubWindow(self.tbsmenu_sub)
				self.tbsmenu_sub.show()
				
		elif action in self.detectorOptions:
			self.detector = self.detectorOptions[action]
			print('Detector changed to "{}"!'.format(self.detector))
			
		elif action in self.gainOptions:
			self.gain = self.gainOptions[action]
			print('Gain Changed to "{}"!'.format(self.gain))
			
		elif action in self.gratingOptions:
			self.grating = self.gratingOptions[action]
			print('Grating changed to "{}"!'.format(self.grating))
		

		
def main():
	app = QtWidgets.QApplication(sys.argv)  # A new instance of QApplication
	form = ScanningMenu()				 # We set the form to be our ExampleApp (StartUpMenu)
	form.show()						 # Show the form
	app.exec_()						 # and execute the app


if __name__ == '__main__':			  # if we're running file directly and not importing it
	main()							  # run the main function