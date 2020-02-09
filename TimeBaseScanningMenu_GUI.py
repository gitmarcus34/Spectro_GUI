from PyQt5 import QtCore, QtGui, QtWidgets # Import the PyQt4 module we'll need
import sys # We need sys so that we can pass argv to QApplication
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import numpy as np

import time

import TimeBaseScanningMenu_Design as TBS_Design # This file holds our scanning menu and scanning related things like time base scanning and range scanning options
			  # it also keeps events etc that we defined in Qt Designer
			  
class SetScan_Thread(QThread):
	actionSignal = pyqtSignal()
	def __init__(self, spectrometer, wavelength_steps, intTime, timeInc, totalTime, entSize, exitSize, gain, grating, detector, parent = None):
		super(SetScan_Thread, self).__init__(parent)
		
		self.spectrometer = spectrometer
		self.intTime = intTime
		self.entSize = entSize
		self.exitSize = exitSize
		self.timeInc = timeInc
		self.totalTime = totalTime
		self.wavelength_steps = wavelength_steps
		self.detector = detector
		self.gain = gain
		self.grating = grating
		
	
	def run(self):
		time.sleep(2)
		#responseApply = self.spectrometer.setScanGUI(str(lowerWave_steps),str(upperWave_steps),str(stepIncrement_steps),str(intTime),str(int(entSize/12.5)),str(int(extSize/12.5)),str(gain),grating,detector)
		#print("Apply Settings Response: ", responseApply)
		responseApply = True
		if responseApply:
			print('Settings Applied - Ready to start scan!') 
		return
		
			  
class Error_Message(QMessageBox):
	def __init__(self, title, text = 'Error', checked = False, parent = None):
		super(Error_Message, self).__init__(parent)
		self.setWindowTitle(title)
		self.setText(text)
		self.checked = checked
		
		self.setGeometry(QtCore.QRect(800, 500, 600, 300))
		self.setMinimumSize(QtCore.QSize(600, 300))
		#self.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:0, stop:0.328358 rgba(159, 212, 255, 127), stop:1 rgba(255, 255, 255, 255));")

		self.checkBox = QCheckBox()
		if self.checked:
			self.checkBox = QCheckBox()
			self.setCheckBox(self.checkBox)
			
	def setChecked(self, newBox = True):
		"""set checked to True so that checkbox is created, or set checked to false to remove the widget"
		"""
		if newBox:
			self.setCheckBox(self.checkBox)
			
		elif newBox == False:
			#remove the check box but be sure to not destroy an instance of checkbox
			self.checkBox.setEnabled(False) #ths ensures that self.checkBox exists the next time setChecked is called 
	
	def run():
		app = QtWidgets.QApplication(sys.argv)  # A new instance of QApplication
		form = ErrorMessage()				 # We set the form to be our ExampleApp (StartUpMenu)
		form.show()						 # Show the form
		app.exec_()	


class TBS_Menu(QtWidgets.QMainWindow, TBS_Design.Ui_TBSMenu):
	def __init__(self, mdiArea = None,spectrometer = None, subwindow_dict = None):
		super(self.__class__, self).__init__()
		self.setupUi(self)  # This is defined in StartUpMenu_Design.py file automatically # It sets up layout and widgets that are defined
		self.mdiArea = mdiArea
		self.spectrometer = spectrometer
		self.subwindow_dict = subwindow_dict
		
		
		###Subwindows
		#subwindows of Core Window
		self.mainmenu_sub = self.subwindow_dict['mainmenu']
		self.scanningmenu_sub = self.subwindow_dict['scanningmenu']
		
		#scanning plot subwindows
		self.sub_mdiArea.addSubWindow(self.plot_subwindowD)
		self.sub_mdiArea.addSubWindow(self.plot_subwindowC)
		self.sub_mdiArea.addSubWindow(self.plot_subwindowB)
		self.sub_mdiArea.addSubWindow(self.plot_subwindowA)
		
		self.plot_subwindowA.setWindowTitle('Plot Subwindow A')
		self.plot_subwindowB.setWindowTitle('Plot Subwindow B')
		self.plot_subwindowC.setWindowTitle('Plot Subwindow C')
		self.plot_subwindowD.setWindowTitle('Plot Subwindow D')
		
		#bar menu
		self.menuMain.triggered[QAction].connect(self.menuBar_action)
		self.menuScan.triggered[QAction].connect(self.menuBar_action)
		
		#scan parameters menus
		self.detector, self.gain, self.grating = ('Side', 'AUTO', '1800 l/mm (Vis)') #defaultParams
		self.menuDetector.triggered[QAction].connect(self.menuBar_action)
		self.detectorOptions = {self.actionSide: 'Side', self.actionFront: 'Front'}
		
		self.menuGain.triggered[QAction].connect(self.menuBar_action)
		self.gainOptions = {self.actionAuto: 'AUTO', self.action1X: '1X', self.action10X: '10X', self.action100X: '100X', self.action1000X: '1000X'}
		
		self.menuGrating.triggered[QAction].connect(self.menuBar_action)
		self.gratingOptions = {self.action1800Grating: '1800 l/mm (Vis)', self.action600Grating: '600 l/mm (IR)'}
		
		#subwindow control options menu
		self.menu_SubwindowPlots.triggered[QAction].connect(self.menuBar_action)
		self.subPlotOptions = {self.actionTiled: 'tiled', self.actionCascade: 'cascade', self.actionPlotA: self.subLayoutA, self.actionPlotB: self.subLayoutB, self.actionPlotC: self.subLayoutC, self.actionPlotD: self.subLayoutD}
		
		
		####sliders
		#Slider Signals
		self.EntranceSlitSlider.valueChanged.connect(self.sliderEntranceSlit_Change)
		self.ExitSlitSlider.valueChanged.connect(self.sliderExitSlit_Change)
		self.IntegrationTimeSlider.valueChanged.connect(self.sliderIntegrationTime_Change)
		self.TimeIncrementSlider.valueChanged.connect(self.sliderTimeIncrement_Change)
		self.TotalTimeSlider.valueChanged.connect(self.sliderTotalTime_Change)
		
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
		
		self.maxTimeInc_ms = 500
		self.tickInterval = self.maxTimeInc_ms/20
		self.TimeIncrementSlider.setMaximum(self.maxTimeInc_ms)
		self.TimeIncrementSlider.setTickInterval(self.tickInterval)
		
		self.maxTotalTime_sec = 100
		self.tickInterval = self.maxTotalTime_sec/20
		self.IntegrationTimeSlider.setMinimum(1)
		self.TotalTimeSlider.setMaximum(self.maxTotalTime_sec)
		self.TotalTimeSlider.setTickInterval(self.tickInterval)
		
		###Buttons
		#Apply setings button
		self.ApplySettings_Button.clicked.connect(self.applysettings) 
		self.StartScan_Button.clicked.connect(self.startscan)
		self.EndScan_Button.clicked.connect(self.endscan)
		
		#initialize button
		#self.Initialize_Button.clicked.connect(self.HR460_Initialize)
		
		###Error messages
		###Error Messages
		self.warning_suggestedRange1800 = Error_Message('Warning: Range Suggestion')
		self.warning_suggestedRange1800.setGeometry(QtCore.QRect(800, 500, 600, 300))
		self.warning_suggestedRange1800.setIcon(QMessageBox.Warning)
		self.warning_suggestedRange1800.setChecked(True)
		
		self.warning_suggestedRange600 = Error_Message('Warning: Range Suggestion')
		self.warning_suggestedRange600.setGeometry(QtCore.QRect(800, 500, 600, 300))
		self.warning_suggestedRange600.setIcon(QMessageBox.Warning)
		self.warning_suggestedRange600.setChecked(True)
		
		self.error_inputNotNum = Error_Message('Not Number Error')
		self.error_inputNotNum.setIcon(QMessageBox.Critical)
		
		self.error_inputNotInRange = Error_Message('Not In Range Error')
		self.error_inputNotInRange.setIcon(QMessageBox.Critical)
		
		self.error_invalidTimeInput = Error_Message('Invalid Time Input')
		self.error_invalidTimeInput.setIcon(QMessageBox.Critical)
		
		self.error_dataOverload = Error_Message('Data Overload')
		self.error_dataOverload.setIcon(QMessageBox.Critical)
		
		
		
	def sliderEntranceSlit_Change(self, slider_val):
		self.lcdNum_EntranceSlider.display(slider_val)
		
	def sliderExitSlit_Change(self, slider_val):
		self.lcdNum_ExitSlider.display(slider_val)
	
	def sliderIntegrationTime_Change(self, slider_val):
		maxIntTime_ms = 200
		self.lcdNum_IntTimeSlider.display(slider_val)
		
	def sliderTimeIncrement_Change(self, slider_val):
		maxTimeInc_ms = 500
		self.lcdNum_TimeIncrementSlider.display(slider_val)

	def sliderTotalTime_Change(self, slider_val):
		maxTotalTime_sec = 200
		totalTime = 200
		self.lcdNum_TotalTimeSlider.display(slider_val)	
		
	#Button slots/funcs
	def applysettings(self):
		"""Slot for ApplySettings_Button
		"""
		
		print('Applying Settings!')
		self.intTime = self.IntegrationTimeSlider.value()/1000
		self.entSize = self.EntranceSlitSlider.value()
		self.exitSize = self.ExitSlitSlider.value()
		self.timeInc = self.TimeIncrementSlider.value()/1000
		self.totalTime = self.TotalTimeSlider.value()
		self.wavelength_nm = self.wavelength_input.text()
		print('Detector:', self.detector, '; Gain:', self.gain, '; self.grating:', self.grating)
		

		print('Entrance Width:', self.entSize)
		print('Exit width:', self.exitSize)
		print('Integration time:', self.intTime)
		print('Time Increment:', self.timeInc)
		print('Total Time:', self.totalTime)
		
		self.error_inputNotNum.done(1) #delete error message
		if not (self.is_number(self.wavelength_nm)):
			print('Displaying Error Message')
			self.error_inputNotNum.setText("ERROR: Wavelength input is not a number!") #make/remake error message
			
			self.error_inputNotNum.exec() 
			return #do not continue to calculations
			
		self.wavelength_nm = float(self.wavelength_nm) #We all float down here
		
		
		self.error_inputNotInRange.done(1) #delete error message
		if self.wavelength_nm < 0:
			print('Displaying Error Message')
			self.error_inputNotInRange.setText("ERROR: Wavelength input must be a positive number!") #make/remake error message
			self.error_inputNotInRange.exec()
			return #do not continue to calculations and settings application	
			
		elif (self.wavelength_nm < 300 or self.wavelength_nm > 870) and self.grating == '1800 l/mm (Vis)': #check if in suggested range for detector and grating currently in use (may need to update for new sensors/gratings)
			print('Displaying Error Message')
			self.warning_suggestedRange1800.setText("Warning: For accurate results, scanning range should be between 300 and 870 for the grating and detector in use! \n Uncheck the box below and press 'OK' if you would like to continue with your current input.") #make/remake error message
			if self.warning_suggestedRange1800.checkBox.isChecked() == False:
				self.warning_suggestedRange1800.exec() #only execute the error message if the error box is unchecked
			return #do not continue to calculations and settings application
		
		elif (self.wavelength_nm < 300 or self.wavelength_nm > 1000) and self.grating == '600 l/mm (IR)': #check if in suggested range for detector and grating currently in use (may need to update for new sensors/gratings)
			print('Displaying Error Message')
			self.warning_suggestedRange600.setText("Warning: For accurate results, scanning range should be between 300 and 1000 for the grating and detector in use! \n Uncheck the box below and press 'OK' if you would like to continue with your current input.") #make/remake error message
			if self.warning_suggestedRange600.checkBox.isChecked() == False:
				self.warning_suggestedRange600.exec() #make/remake error message #make/remake error message
			return #do not continue to calculations and settings application
		
		elif (self.timeInc < self.intTime) and self.timeInc != 0:
			print('Displaying Error Message')
			self.error_invalidTimeInput.setText("Error: 'Time Increment' must be less than 'Integration Time'\nTime Increment is the time between integration starts. (see illustration on left side of time base scanning menu.")
			self.error_invalidTimeInput.exec()
			
		elif (self.timeInc > self.totalTime) or (self.intTime > self.totalTime): #this should never really be possible as long as max integration time and time increment sliders are 500 ms and min total time slider is 1 second
			print('Displaying Error Message')
			self.error_invalidTimeInput.setText("Error: 'Time Increment' and 'Integration Time' must be less than 'Total Time'\n.(see illustration on left side of time base scanning menu.")
			self.error_invalidTimeInput.exec()
			
		elif (self.timeInc == 0 and self.totalTime/self.intTime >= 5000):
			print('Displaying Error Message')
			self.error_dataOverload.setText("The total number of data points acquired during the scan must be less than 5000 points.\n\nTry decreasing the 'Total Time' or increasing the 'Time Increment' to decrease number of data points")  
			self.error_dataOverload.exec()
			
		elif self.timeInc != 0:
			if (self.totalTime/self.timeInc >= 5000):		
				print('Displaying Error Message')
				self.error_dataOverload.setText("The total number of data points acquired during the scan must be less than 5000 points.\n\nTry decreasing the 'Total Time' or increasing the 'Time Increment' to decrease number of data points")  
				self.error_dataOverload.exec()		
				
		self.wavelength_steps = self.convert_NMtoSTEPS(self.grating, self.wavelength_nm)
		print("wavelength position in steps: {}".format(self.wavelength_steps))
		
		print('Applying Settings and Preparing monochromator for scanning')		
		self.setscan_thread = SetScan_Thread('spectrometer', self.wavelength_steps, self.intTime, self.timeInc, self.totalTime, self.entSize, self.exitSize, self.gain, self.grating, self.detector)
		self.setscan_thread.start()
		#time.sleep(5)
		#responseApply = self.spectrometer.setScanGUI('0','0','0',str(intTime),str(int(entSize/12.5)),str(int(extSize/12.5)),str(gain),grating,detector,'3',str(gratingPos),str(incTime),str(totalTime)):
		
		#self.setscan_thread.quit()
		#self.setscan_thread.wait()
		self.setscan_thread.finished.connect(self.applythreadFinished)
		
	def applythreadFinished(self):
		print('Thread is finished!')
		#self.progressBar.setFormat('Monochromator ready to scan over range (from {}nm to {}nm)'.format(self.lowerWavelen_nm, self.upperWavelen_nm))
		#self.progressBar.setValue(100)
		#self.busyMessageThread.triggerFinish()#trigger the busydots_thread to end and stop appending '...' to end of message.
		time.sleep(0.5)#wait a little bit before reseting busy thread so that the trigger can fully end the previous run of BusyDots_Thread	

		
	def startscan(self):
		"""Slot for StartScan_Button
		"""
		
		print('Starting Scan!')
		#self.spectrometer.startScan()
		
	def endscan(self):
		"""Slot for endScan_Button
		"""
		
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
	
		
		#self.spectrometer.setScanGUI('0','0','0',str(intTime),str(int(entSize/12.5)),str(int(extSize/12.5)),str(gain),grating,detector,'3',str(gratingPos),str(timeInc),str(totalTime)):


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
		
		elif action == self.actionScanningMenu:
			print('Triggered time base scanning menu')
		#Check if subwindow already exists, show it and its widgets in case user had exited out.
			if self.scanningmenu_sub in self.mdiArea.subWindowList():
				print('returned to time menu')
				self.scanningmenu_sub.show()
				self.scanningmenu_sub.raise_() #bring the menu into view
				self.scanningmenu_sub.activateWindow() #set as active window (only really important if usr has to use keyboard on the menu.
				self.scanningmenu_sub.widget().show() #must call otherwise widget does not appear in subwindow if user exited out of subwindow onece before
			else:
				print('added time menu to mdiArea')
				self.mdiArea.addSubWindow(self.scanningmenu_sub)
				self.scanningmenu_sub.show()

				
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
			
			if self.grating == '600 l/mm (IR)':
				self.wavelength_input.setPlaceholderText("300 - 1000")
				
			print('Grating changed to "{}"!'.format(self.grating))
            
			#set the check mark next to the new detector setting
			for act in self.gratingOptions:
				if act.isChecked():
					act.setChecked(False)
					
			action.setChecked(True)
			
		elif action in self.subPlotOptions:
			if action == self.actionCascade:
				self.sub_mdiArea.cascadeSubWindows()
				print('cascade triggered')

			elif action == self.actionTiled:
				self.sub_mdiArea.tileSubWindows()
				print('tiled triggered')
			
			elif action == self.actionPlotA:
				print('set view to subwindow plot A')
			elif action == self.actionPlotB:
				print('set view to subwindow plot B')
			elif action == self.actionPlotC:
				print('set view to subwindow plot C')
			elif action == self.actionPlotD:
				print('set view to subwindow plot D')
				
			for act in self.subPlotOptions:
				if act.isChecked() and (action != self.actionTiled and action != self.actionCascade):
					act.setChecked(False)
			action.setChecked(True)				
			
	def convert_NMtoSTEPS(self, grating, nm_val, getFactor = False):
		"""Converts a nm_val to the grating motor step position corresponding to the nm_val (which may be a desired nanometer value of wavelength or step size for example) knowing that the 
		HR460 spectrometer - if initialized after powerup - has a base grating calibration setting for 1200 l/mm grating with 160 steps/nm factor (or .00625 nm/step wavelength drive step size described 
		in usermanual PDF page 41).  
		
		The step position is calculated by dividing the nm_val by the new grating's step factor which is found using the formula described in the handbook PDF (equation (3)).
		Essentially: (nm/step factor) = (0.00625 nm)*((1200 l/mm)/(new grating l/mm)) which is just the inverse of the steps/nm factor.  
		
		Note that if getFactor parameter is True then this function only returns the step/nm factor for the given grating and ignores the wavelength parameter.
		"""
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
	form = TBS_Menu()				 # We set the form to be our ExampleApp (StartUpMenu)
	form.show()						 # Show the form
	app.exec_()						 # and execute the app


if __name__ == '__main__':			  # if we're running file directly and not importing it
	main()							  # run the main function