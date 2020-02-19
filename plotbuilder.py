#plot builder
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import time
import noiseFilter
class AnimatedPlot:
	def __init__(self, timeInc = 1):
		style.use('fivethirtyeight')
		self.timeInc = timeInc

		self.fig = plt.figure(figsize = [15, 10])
		self.ax1 = self.fig.add_subplot(2,1,1)
		self.ax2 = self.fig.add_subplot(2,1,2)

	def animate(self, i):
		graph_data = open('realTimeData.csv','r').read()
		lines = graph_data.split('\n')
		positions = []
		intensities = []

		for line in lines:
			if len(line) > 1:
				pos, intensity = line.split(',')
				positions.append(float(pos)*self.timeInc)
				intensities.append(float(intensity))
				
				#intensities_fil = intensities[:]
				#positions_fil = positions[:]
				#intensities_fil = noiseFilter.movingAverage(intensities_fil, MA_Size = 6, lowerLim= 10000, upperLim =16000 , limFind = False)
		self.ax1.clear()
		self.ax1.set_title('Intensity vs Time')
		self.ax1.set_ylabel('Intensity')
		self.ax1.set_xlabel('Time (seconds)')
		self.ax1.plot(positions, intensities)

	def animate_fil(self, i):
		graph_data = open('realTimeData.csv','r').read()
		lines = graph_data.split('\n')
		positions = []
		intensities = []

		for line in lines:
			if len(line) > 1:
				pos, intensity = line.split(',')
				positions.append(float(pos)*self.timeInc)
				intensities.append(float(intensity))
				
				intensities_fil = noiseFilter.movingAverage(intensities, MA_Size = 6, lowerLim= 20000, upperLim =30000 , limFind = True)
		self.ax2.clear()
		self.ax2.set_title('Filtered Intensity vs Time')
		self.ax2.set_ylabel('Intensity')
		self.ax2.set_xlabel('Time (seconds)')
		self.ax2.plot(positions, intensities_fil)



	def runAnimate(self):
		anim1 = animation.FuncAnimation(self.fig, self.animate, interval=(self.timeInc*1000))
		anim2 = animation.FuncAnimation(self.fig, self.animate_fil, interval=(self.timeInc*1000))
		plt.show()
		

