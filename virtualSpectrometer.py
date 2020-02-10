#virtual spectrometer
import time
import csv

graph_data = open('realTimeData.csv','r').read()
lines = graph_data.split('\n')

	
with open('realTimeDataWrite.csv', mode = 'r+') as liveDataFile:
	liveDataFile.truncate()
	liveData = csv.writer(liveDataFile, delimiter=',', lineterminator = '\n')

	for line in lines:
		if len(line) > 1:
			print(line)
			newDataPos, newIntensity = line.split(',')
			#put the time data that was just acquired with the intensity and its position in the csv file to read to graph from HR460.py
			#row_count = sum(1 for row in liveDataFile) #count number of rows to not overwrite earlier data when writing
			#for i in range(row_count):
			#	liveDataFile.readline()
			liveData.writerow([newDataPos, newIntensity])
			time.sleep(0.001)
		
