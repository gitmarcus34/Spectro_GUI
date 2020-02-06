from PyQt5 import QtCore, QtGui, QtWidgets # Import the PyQt4 module we'll need
import sys # We need sys so that we can pass argv to QApplication
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
#import matplotlib

import numpy as np
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
		self.EntranceSlitSlider.valueChanged.connect(self.sliderEntranceSlit_Change)
		self.ExitSlitSlider.valueChanged.connect(self.sliderExitSlit_Change)
		self.IntegrationTimeSlider.valueChanged.connect(self.sliderIntegrationTime_Change)
		self.StepSizeSlider.valueChanged.connect(self.sliderStepSize_Change)
		
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
		self.IntegrationTimeSlider.setMinimum(1)
		self.IntegrationTimeSlider.setMaximum(self.maxIntTime_ms)
		self.IntegrationTimeSlider.setTickInterval(self.tickInterval)
		
		self.maxStepSize_steps = self.convert_NMtoSTEPS(self.grating, 5)  #set max step size to 5 nm and increment by step factor (accounted for in slider _Change function)
		self.tickInterval = self.maxStepSize_steps/10
		self.StepSizeSlider.setMinimum(1) #make the smallest increment the step factor for the set grating
		self.StepSizeSlider.setMaximum(self.maxStepSize_steps)
		self.StepSizeSlider.setTickInterval(self.tickInterval)
		
		###Buttons
		#signals
		self.ApplySettings_Button.clicked.connect(self.applysettings)
		self.StartScan_Button.clicked.connect(self.startscan)
		self.EndScan_Button.clicked.connect(self.endscan)
		
		#spectrometer initialize button (use upon HR460 power up for spectrometer to be calibrated to base grating.)
		#self.Initialize_Button.clicked.connect(self.HR460_Initialize)
		
		###Error Messages
		self.error_inputNotNum = QtWidgets.QErrorMessage()
		self.error_inputNotInRange =QtWidgets.QErrorMessage()
		
	
	def sliderEntranceSlit_Change(self, slider_val):
		self.lcdNum_EntranceSlider.display(slider_val)
		
	def sliderExitSlit_Change(self, slider_val):
		self.lcdNum_ExitSlider.display(slider_val)
	
	def sliderIntegrationTime_Change(self, slider_val):
		self.lcdNum_IntTimeSlider.display(slider_val)
		
	def sliderStepSize_Change(self, slider_val):
		stepFactor = self.convert_NMtoSTEPS(self.grating, getFactor = True)
		incremented_val = float(slider_val*stepFactor)
		
		#display step sizes in increments of the step factor for the given grating
		self.lcdNum_StepSizeSlider.display(incremented_val)
	
	###funtions/slots 
	def applysettings(self):
		print('Applying Settings!')
		
		
		self.intTime = self.IntegrationTimeSlider.value()
		self.entSize = self.EntranceSlitSlider.value()
		self.exitSize = self.ExitSlitSlider.value()
		self.stepSize_nm = self.StepSizeSlider.value()
		self.lowerWavelen_nm = self.lowerWavelength_input.text()
		self.upperWavelen_nm = self.upperWavelength_input.text()
		
		print('Detector:', self.detector, '; Gain:', self.gain, '; Grating:', self.grating)
		
		print('Entrance Width:', self.entSize)
		print('Exit width:', self.exitSize)
		print('Integration time:', self.intTime)
		print('Step Size:', self.stepSize_nm)
		
		###Before doing calculations and applying settings make sure inputs are valid. Display error messages where necessary.
		
		#If user hides the error message and tries same bad input make sure to display the hidden error message again (delete window and remake it so that copies are not made)
		self.error_inputNotNum.done(1) #delete error message
		if not (self.is_number(self.lowerWavelen_nm) and  self.is_number(self.upperWavelen_nm)):
			print('Displaying Error Message')
			self.error_inputNotNum.showMessage("ERROR: Wavelength input is not a number!") #make/remake error message
			#self.error_dialog.activateWindow()
			
			return #do not continue to calculations
			
		self.lowerWavelen_nm = float(self.lowerWavelen_nm) #We all float down here
		self.upperWavelen_nm = float(self.upperWavelen_nm)			
		
			
		self.error_inputNotInRange.done(1) #delete error message
		if self.lowerWavelen_nm < 0:
			print('Displaying Error Message')
			self.error_inputNotInRange.showMessage("ERROR: Wavelength input must be a positive number!") #make/remake error message
			return #do not continue to calculations and settings application	
			
		elif self.lowerWavelen_nm >= self.upperWavelen_nm: #make sure  lower is less than upper
			print('Displaying Error Message')
			self.error_inputNotInRange.showMessage("ERROR: Lower wavelength input must be less than upper wavelength input!") #make/remake error message
			return #do not continue to calculations and settings application
			
		elif (self.lowerWavelen_nm < 300 or self.upperWavelen_nm > 870) and self.grating == '1800 l/mm (Vis)': #check if in suggested range for detector and grating currently in use (may need to update for new sensors/gratings)
			print('Displaying Error Message')
			self.error_inputNotInRange.showMessage("Warning: For accurate results, scanning range should be between 300 and 870 for the grating and detector in use! \n Uncheck the box below and press 'OK' if you would like to continue with your current input.") #make/remake error message
			return #do not continue to calculations and settings application
		
		elif (self.lowerWavelen_nm < 300 or self.upperWavelen_nm > 1000) and self.grating == '600 l/mm (IR)': #check if in suggested range for detector and grating currently in use (may need to update for new sensors/gratings)
			print('Displaying Error Message')
			self.error_inputNotInRange.showMessage("Warning: For accurate results, scanning range should be between 300 and 1000 for the grating and detector in use! \n Uncheck the box below and press 'OK' if you would like to continue with your current input.") #make/remake error message
			return #do not continue to calculations and settings application
		
		self.lowerWave_steps, self.upperWave_steps = [self.convert_NMtoSTEPS(self.grating, self.lowerWavelen_nm), self.convert_NMtoSTEPS(self.grating, self.upperWavelen_nm)]
		self.stepFactor_nm_step = self.convert_NMtoSTEPS(self.grating, getFactor = True) #setting getFactor param to true returns the step factor of the given grating
		self.stepIncrement_steps = np.round(self.stepSize_nm/self.stepFactor_nm_step)
		print("lowStep: {}, highStep: {}, stepIncrement: {}".format(self.lowerWave_steps, self.upperWave_steps, self.stepIncrement_steps))
		#self.spectrometer.setScanGUI('0','0','0',str(intTime),str(int(entSize/12.5)),str(int(extSize/12.5)),str(gain),grating,detector,'3',str(gratingPos),str(incTime),str(totalTime)):
		
		
	def startscan(self):
		print('Starting Scan!')
		#self.spectrometer.startScan()
		
	def endscan(self):
		print('Ending Scan!')
		#Used to stop the current time base scan
		endFlag = True
		totalTime = 0
		while endFlag:
			try:
				#response_end = a.scanStop()
				print('Scan Ended')
				endFlag = False
			except serial.serialutil.SerialException:
				   time.sleep(0.001)
				   totalTime += 0.001
	

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
			
		#set the check mark next to the new detector setting
			for act in self.detectorOptions:
				if act.isChecked():
					act.setChecked(False)
					
			action.setChecked(True)
			
		elif action in self.gainOptions:
			self.gain = self.gainOptions[action]
			print('Gain Changed to "{}"!'.format(self.gain))
			
		#set the check mark next to the new detector setting
			for act in self.gainOptions:
				if act.isChecked():
					act.setChecked(False)
					
			action.setChecked(True)
			
		elif action in self.gratingOptions:
			self.grating = self.gratingOptions[action]
			
			#step size changes for different gratings. Certain related properties must be therefore be changed correspondingly.
			self.maxStepSize_steps = self.convert_NMtoSTEPS(self.grating, 5)
			self.tickInterval = self.maxStepSize_steps/5
			self.StepSizeSlider.setMinimum(self.convert_NMtoSTEPS(self.grating, getFactor = True)) #make the smallest increment the step factor for the set grating
			self.StepSizeSlider.setMaximum(self.maxStepSize_steps)
			self.StepSizeSlider.setTickInterval(self.tickInterval)
			
			if self.grating == '600 l/mm (IR)':
				self.upperWavelength_input.setPlaceholderText("1000")
			elif self.grating == '1800 l/mm (Vis)':
				self.upperWavelength_input.setPlaceholderText("870")
			
			print('Grating changed to "{}"!'.format(self.grating))
			
			#set the check mark next to the new detector setting
			for act in self.gratingOptions:
				if act.isChecked():
					act.setChecked(False)
					
			action.setChecked(True)
			
			
	def convert_NMtoSTEPS(self, grating, nm_val = 0, getFactor = False):
		"""Converts a nm_val (which may be a desired nanometer value of wavelength or step size for example) to the grating motor step position knowing that the 
		HR460 spectrometer - if initialized after powerup - has a base grating calibration setting for 1200 l/mm grating with 160 steps/nm factor (or .00625 nm/step resolution descreibed 
		in user manual PDF page 41).  
		
		The step position is calculated by dividing the nm_val by the new grating's step factor which is found using the formula described in the handbook (equation (3)).
		Essentially: (nm/step factor) = (0.00625 nm)*((1200 l/mm)/(new grating l/mm)) which is just the inverse of the steps/nm factor.  
		
		Note that this can currently only be called for the '1800 l/mm (Vis)' and '600 l/mm (IR)' grating else get a print response.
		
		Note that if get factor is True then this function only returns the step/nm factor for the given grating and ignores the 
		"""
		
		if float(nm_val) < 0:
			print("{} is not positive number".format(nm_val))
		
		nm_val = float(nm_val)
		if grating == '1800 l/mm (Vis)':
			stepFactor = float(0.00625*((1200)/(1800)))
			if getFactor == True:
				return stepFactor
				
			stepPos = np.round(nm_val/stepFactor)
			return stepPos
			
		elif grating == '600 l/mm (IR)':
			stepFactor = float(0.00625*((1200)/(600)))
			if getFactor == True:
				return stepFactor
				
			stepPos = np.round(nm_val/stepFactor)
			return stepPos
			
		else:
			print("Grating is not '1800 l/mm (Vis) or 600 l/mm (IR)")
		return 
	
	def is_number(self,a):
		"""Function used to check if input from user is a number.
		"""
		try:
			float(a)
			return True
		except ValueError:
			pass

		return False
		
		
def main():
	app = QtWidgets.QApplication(sys.argv)  # A new instance of QApplication
	form = ScanningMenu()				 # We set the form to be our ExampleApp (StartUpMenu)
	form.show()						 # Show the form
	app.exec_()						 # and execute the app


if __name__ == '__main__':			  # if we're running file directly and not importing it
	main()							  # run the main function