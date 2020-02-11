#virtual spectrometer
import time
import csv

from PyQt5 import QtCore, QtGui, QtWidgets # Import the PyQt4 module we'll need
import sys # We need sys so that we can pass argv to QApplication
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class LiveWrite_Thread(QThread):
	triggerWrite = pyqtSignal()
	def __init__(self, timeIncrement, parent = None):
		super(LiveWrite_Thread, self).__init__(parent)
		self.timeIncrement = timeIncrement
		self.triggerWrite.connect(self.writeRecentData)
	
	def run(self):
		print('live write should begin')
		graph_data = open('realTimeData.csv','r').read()
		lines = graph_data.split('\n')

			
		with open('realTimeDataWrite.csv', mode = 'r+') as liveDataFile:
			liveDataFile.truncate()
			self.liveData = csv.writer(liveDataFile, delimiter=',', lineterminator = '\n')

			for line in lines:
				if len(line) > 1:
					print(line)
					self.newDataPos, self.newIntensity = line.split(',')
					#put the time data that was just acquired with the intensity and its position in the csv file to read to graph from HR460.py
					#row_count = sum(1 for row in liveDataFile) #count number of rows to not overwrite earlier data when writing
					#for i in range(row_count):
					#	liveDataFile.readline()
					#liveData.writerow([newDataPos, newIntensity])
					self.triggerWrite.emit()					
					time.sleep(self.timeIncrement)

	
	def writeRecentData(self):
		liveDataFile = open('realTimeData.csv','w')
		self.liveData = csv.writer(liveDataFile, delimiter=',', lineterminator = '\n')
		self.liveData.writerow([self.newDataPos, self.newIntensity])
		
