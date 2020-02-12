#plot builder
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import time
import noiseFilter
class AnimatedPlot:
	def __init__(self):
		style.use('fivethirtyeight')

		self.fig = plt.figure()
		self.ax1 = self.fig.add_subplot(1,1,1)

	def animate(self, i):
		graph_data = open('realTimeData.csv','r').read()
		lines = graph_data.split('\n')
		positions = []
		intensities = []

		for line in lines:
			if len(line) > 1:
				pos, intensity = line.split(',')
				positions.append(float(pos))
				intensities.append(float(intensity))

				#intensities = noiseFilter.movingAverage(intensities, MA_Size = 6, lowerLim= 2000, upperLim = 2500, limFind = True)
		self.ax1.clear()
		self.ax1.plot(positions, intensities)


	def runAnimate(self, animTime = 20):
		ani = animation.FuncAnimation(self.fig, self.animate, interval=100)
		plt.show()
		

