#virtual spectrometer 
import serial
import time

class Vitual_Spectrometer():
    def__init__(self, integrationTime, timeIncrement, totalTime, command):
        self.data = []
        self.intTime = integrationTime
        self.timeInc = timeIncrement
        self.totalTime = totalTime
    
    def sendDataReal():
        with open('realCopy.csv', mode = 'r') as streamFile:
            data_toStream = csv.writer(fullDataFile, delimiter=',')
            data_toStream = data_toStream.readlines()
            
            for line in data_toStream:
                self.data
            #dataPosEnc = str(dataPos)
            #dataPosEnc = str.encode(dataPosEnc)

            #self.s.write(b'u' + dataPosEnc + b'\r')
            #output = self.s.read_until(b'\r',15)
            #output = output.decode('utf-8')
            

            #put the time data that was just acquired with the intensity and its position in the csv file to read to graph from HR460.py
            intensity = output[1: len(output)-3]

            row_count = sum(1 for row in liveDataFile) #count number of rows not to overwrite when writing
            for i in range(row_count):
                liveDataFile.readline()
            liveData.writerow([dataPos, intensity])
            
    def run