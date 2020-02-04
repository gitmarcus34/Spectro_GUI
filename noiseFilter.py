#Data noise filters
import numpy as np

def average(measurements):
	return sum(measurements)/len(measurements)

def movingAverage(measurements, MA_Size, lowerLim, upperLim, limFind = False):
	lastMeasurement = measurements[-1]
	movingAverage = lastMeasurement #in case next condition is not met

	if limFind and (len(measurements) >= MA_Size):
		lowerLim = min(measurements[len(measurements)-MA_Size:])
		upperLim = max(measurements[len(measurements)-MA_Size:])

	if (lowerLim < lastMeasurement < upperLim) and len(measurements) >= MA_Size:
		group = measurements[(len(measurements)-MA_Size):]
		movingAverage = average(group)
	else:
		movingAverage = average(measurements)

	measurements[-1] = movingAverage
	return measurements
