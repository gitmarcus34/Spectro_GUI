
import time
def getLastDataPos(output):
	"""None -> (last data position, cycle number)
	This method is used to get and return the number of the last data point that was acquired by the
	SpectrAcq or DataScan / DataLink spectrometer controller. The cycle number will also be returned.
	"""
		 
	#self.s.write(b't')
	#output = self.s.readline()
	#output = output.decode('utf-8')
	 
	#note that output is string so must extract desired elements like list
	confirmation = output[0]
	try:
		lastDataPos = int(output[1: len(output)-3]) #(!) Note this will need to be changed if using cycle scanning and if cycle # > 9
		print('position of last data point:', lastDataPos)
		return(lastDataPos)
	except ValueError:
		print('should be int intensity string', output[1: len(output)-3], type(output[1: len(output)-3]))
		time.sleep(0.001)
		lastDataPos = int(output[1: len(output)-3]) #(!) Note this will need to be adjusted if using cycle scanning if cycle # > 9
	print(lastDataPos)
	return lastDataPos
	#cycleNumber = output[len(output)-2:]

