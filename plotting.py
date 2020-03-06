#data plot
from matplotlib import pyplot as plt

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import noiseFilter

class Canvas(FigureCanvas):
	"""Note that FigureCanvas is a matplotlib designed QObject so it can be treated correspondignly - we can add it to sublayors like a widget using sublayor.addWidget(Canvas) 
	"""
	def __init__(self, scanData, width = 5, height = 5, dpi = 100, parent = None):
		self.figure = Figure(figsize=(width, height), dpi=dpi)
		self.axes = self.figure.add_subplot(111)

		FigureCanvas.__init__(self, self.figure)
		#self.setParent(parent)
		self.steps, self.intensities = scanData
		self.plot()
		
	
	def getFigure(self):
		"""return the figure so that we could export it as png/jpg
		"""
		return self.figure	
 
	def plot(self):
		#randNum = random.random()
		#y = np.array([random.random(), random.random(),random.random()])
		#x = [1, 2, 3]
		#print('intensities from canvas class: ', self.intensities)
		ax = self.figure.add_subplot(111)
		ax.plot(self.steps, self.intensities)
		mu = r'$\mu$'
		ax.set_title('Intensity vs Wavelength')

		ax.set_xlabel('Wavelength (nm)')
		ax.set_ylabel('Intensity (counts)')
		plt.show()

def plotData(MA_Size, lowerLim, upperLim, limFind):
	filename = input('filename: ')
	with open(filename, 'r') as dataFile:
		dataFile.readline()
		data = dataFile.read()
		dataLines = data.split('\n')

		wavelengths = []
		intensities = []
		
		for line in dataLines:
			if len(line) > 1:
				wavelength, intensity = line.split(',')
				wavelengths.append(float(wavelength))
				intensities.append(float(intensity))
				
				intensities_fil = noiseFilter.movingAverage(intensities, MA_Size, lowerLim, upperLim, limFind)
		scanData = (wavelengths, intensities)
		dataFile.close()

	fig = plt.figure(figsize = [15, 10])
	ax1 = fig.add_subplot(1,1,1)

	ax1.set_title('Intensity vs Wavelength')
	ax1.set_ylabel('Intensity (counts)')
	ax1.set_xlabel('Wavelength (nm)')
	ax1.plot(scanData[0], scanData[1])
	plt.show()


