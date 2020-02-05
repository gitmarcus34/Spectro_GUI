#Code written by Justin deMattos (MIIP Optics Track '20)
#Designed for use with Jobin Yvon-Spex HR460 Spectrometer
#Advanced Project Lab University of Oregon
#Function: Creates the graphical user interface to run and operate spectrometer

#Multiple packages needed:
import tkinter as tk
import csv
import time
import math
from tkinter import filedialog
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from PIL import ImageTk
from PIL import Image
#from test import test
from Spectrometer import Spectrometer
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import threading
import serial

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

import plotbuilder
import noiseFilter

#Prompt the user for the name of the USB port to communicate with
usb = input("Enter the USB port name for the Spectrometer: ")



class HR460App(tk.Tk):

	def __init__(self, *args, **kwargs):

		#Create tkinter window container
		tk.Tk.__init__(self,*args,**kwargs)
		container = tk.Frame(self)

		container.pack(side='top', fill='both', expand=True)

		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		#Defined this as a global to manage window size in other classes
		global window

		window=self

		#Don't allow user to change the size of the window (stretches things out and makes it messy)
		self.resizable(width=False,height=False)

		#Create a frames dictionary and set the title of the app
		self.frames = {}
		self.title("Jobin-Yvon HR460")

		#Create the different window frames. Add other windows here!
		for F in (StartPage, MainMenu, Information, Scanning, Tools, timeBaseScanning):
			frame = F(container, self)
			self.frames[F] = frame
			frame.grid(row=0, column=0, sticky='nsew')

		#Show the start page first
		self.show_frame(StartPage)

	#Function used to show the window requested
	def show_frame(self,cont):

		frame = self.frames[cont]
		frame.tkraise()

#Our start page class
class StartPage(tk.Frame):

	def __init__(self,parent,controller):
		self.controller = controller
		imageName = 'Slide1.jpeg'

		#Set specific window size. Can change if needed but will throw off placement
		w = 900
		h = 507
		tk.Frame.__init__(self,parent)
		
		#Create a canvas on the window to store the background image and pack it into the window
		self.canvas = tk.Canvas(self, width=w, height=h)
		self.image = ImageTk.PhotoImage(file=imageName)
		self.canvas.create_image(0,0,image=self.image,anchor='nw')
		self.canvas.pack()

		#Create the opening initialize button
		self.buttonFont = ("jua",15,'bold')
		self.init_button = tk.Button(self, text = "Initialize", command = self.initializeButton, anchor = 'center', width = 20, activebackground = '#ffffff')
		self.init_button.config(font=self.buttonFont)

		#Create the opening non-initializing button
		self.buttonFont = ("jua",15,'bold')
		self.menuButton = tk.Button(self, text = "Main Menu", command = self.mainMenu, anchor = 'center', width = 20, activebackground = '#ffffff')
		self.menuButton.config(font=self.buttonFont)
		
		#Note: because of the way pack() works, I had to create a window over the original window to store the buttons
		self.init_button_window = self.canvas.create_window(w/2,0.35*h,anchor='center',window=self.init_button)

		self.menuButton_window = self.canvas.create_window(w/2,0.50*h,anchor='s',window=self.menuButton)
		#self.init_button_window.place(relx=0.24,rely=0.27,anchor=tk.CENTER)
	
	#Function for handling initialize button press
	def initializeButton(self):
		
		#Set up a progress bar
		self.progress=ttk.Progressbar(self,orient='horizontal',length=300,mode='determinate')
		self.init_button_window = self.canvas.create_window(900/2,0.35*507,anchor='center',window=self.progress)

		#Destroy the initialize button since it gets replaced by the progress bar
		self.init_button.destroy()

		#Define a as our global variable to communicate with the eter
		global a

		a=Spectrometer(usb)

		#Set up spectrometer and update the progress bar through each step
		a.on()

	#wait message (NOTE: background covers this so this is commented out until solution is found)
		#self.waitMessage = tk.Label(self,text = "Please wait, this may take a while...")
		#self.plottingMenuFont = ("jua",12)
		#self.waitMessage.config(font=self.plottingMenuFont)
		#self.waitMessage.place(relx=0.5,rely=0.5,anchor=tk.CENTER)	
	
		self.progress['value']=25
		self.progress.update()
		a.initialize()
		self.progress['value']=50
		self.progress.update()
		a.setMotorSpeed()
		self.progress['value']=60
		self.progress.update()
		a.setSlitSpeed('0')
		self.progress['value']=70
		self.progress.update()
		a.setSlitSpeed('1')
		self.progress['value']=80
		self.progress.update()
		a.setSlitSpeed('2')
		self.progress['value']=90
		self.progress.update()
		a.setSlitSpeed('3')
		self.progress['value']=100
		self.progress.update()

		#When finished, go to the main menu
		self.controller.show_frame(MainMenu)

	def mainMenu(self):

		#Define a as our global variable to communicate with the spectrometer
		global a

		a=Spectrometer(usb)

		#Set up spectrometer and update the progress bar through each step
		a.on()

		self.controller.show_frame(MainMenu)

#Our main menu class
class MainMenu(tk.Frame):
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)
		self.controller=controller

		#Main Menu Text Label
		self.label = tk.Label(self,text = "Main Menu")
		self.MainMenuFont = ("jua",40,"bold")
		self.label.config(font=self.MainMenuFont)
		self.label.place(relx=0.5,rely=0.1,anchor=tk.CENTER)
		
		#Create a label for each button (Information, Scanning, Tool Control) and place them evenly spaced apart 
		self.button1Frame = ttk.Label(self)
		self.button1Frame.place(relx=0.24,rely=0.27,anchor=tk.CENTER)

		self.button1 = tk.Button(self.button1Frame, text="Information",command=self.infoButton)
		self.buttonFont = ("jua",15,'bold')
		self.button1.config(font=self.buttonFont)
		self.button1.grid(column=0,row=1)
		self.button1.config(height=2,width=25)

		self.button2Frame = ttk.Label(self)
		self.button2Frame.place(relx=0.24,rely=0.54,anchor=tk.CENTER)

		self.button2 = tk.Button(self.button2Frame, text="Scanning",command=self.scanButton)
		self.buttonFont = ("jua",15,'bold')
		self.button2.config(font=self.buttonFont)
		self.button2.grid(column=0,row=3)
		self.button2.config(height=2,width=25)

		self.button3Frame = ttk.Label(self)
		self.button3Frame.place(relx=0.24,rely=0.81,anchor=tk.CENTER)

		self.button3 = tk.Button(self.button3Frame, text="Tool Control",command=self.toolButton)
		self.buttonFont = ("jua",15,'bold')
		self.button3.config(font=self.buttonFont)
		self.button3.grid(column=0,row=3)
		self.button3.config(height=2,width=25)

		#Place images to the right of the buttons for design purposes
		self.image1 = Image.open("Main1.png")
		self.image1 = self.image1.resize((250,200),Image.ANTIALIAS)
		self.imageHold1 = tk.Canvas(self)
		self.image1 = ImageTk.PhotoImage(self.image1)
		self.imageHold1.create_image(0,0,image=self.image1,anchor='nw')
		self.imageHold1.place(relx=0.7,rely=0.47,anchor=tk.CENTER)

		self.image2 = Image.open("Main2.png")
		self.image2 = self.image2.resize((250,200),Image.ANTIALIAS)
		self.imageHold2 = tk.Canvas(self)
		self.image2 = ImageTk.PhotoImage(self.image2)
		self.imageHold2.create_image(0,0,image=self.image2,anchor='nw')
		self.imageHold2.place(relx=0.88,rely=0.77,anchor=tk.CENTER)

	#Functions for handling button presses from main menu
	def infoButton(self):
		self.controller.show_frame(Information)

	def scanButton(self):
		#Make the window bigger for the scanning menu so the user can see the plot well enough
		window.geometry('1500x900')
		self.controller.show_frame(Scanning)

	def toolButton(self):
		#Make the window bigger for the tool menu so the user can see the plot well enough
		window.geometry('1500x900')
		self.controller.show_frame(Tools)



#Our information page (Not finished as of week of 12/2)
class Information(tk.Frame):

	def __init__(self,parent,controller):
		self.controller = controller
		imageName = 'Slide1.jpeg'
		w = 900
		h = 507
		tk.Frame.__init__(self,parent)

		#Button for returning to main menu
		self.mainMenuFrame = ttk.Label(self)
		self.mainMenuFrame.place(relx=0.062,rely=0.07,anchor=tk.CENTER)
		self.menuButton = tk.Button(self.mainMenuFrame, text="Main Menu",command=self.menuButton)
		self.buttonFont = ("jua",10,'bold')
		self.menuButton.config(font=self.buttonFont)
		self.menuButton.grid(column=0,row=1)
		self.menuButton.config(height=2,width=10)
		
	#Function to handle main menu button push
	def menuButton(self):
		window.geometry('900x507')
		self.controller.show_frame(MainMenu)

#Our scanning page
class Scanning(tk.Frame):

	def __init__(self,parent,controller):
		self.controller = controller
		tk.Frame.__init__(self,parent)

		#If you want the window to be resizeable:
		#window.resizable(width=True,height=True)

		#Scanning Menu Title Label
		self.label = tk.Label(self,text = "Wavelength Scanning")
		self.ScanningMenuFont = ("jua",35,"bold")
		self.label.config(font=self.ScanningMenuFont)
		self.label.place(relx=0.72,rely=0.11,anchor=tk.CENTER)

		#Variables to store step values and intensities
		self.steps = []
		self.intensities = []

		#Read in the sample data for the sample plot and store values
		with open('thorlabsBulb.csv') as csvfile:
			reader = csv.DictReader(csvfile)
			for row in reader:
				self.steps.append(row['wavelength'])
				self.intensities.append(row['intensity'])
		
		#Variables to store plot options
		self.color = 'b'
		self.plotTitle = 'Sample Spectrum'
		self.xlabel = 'Wavelength (nm)'
		self.ylabel = 'Intensity'

		#Plot the sample spectrum	 
		self.f = Figure(figsize=(7,5.4),dpi=100)
		self.sample = self.f.add_subplot(111)
		self.sample.plot(self.steps,self.intensities,self.color)
		self.sample.set_title(self.plotTitle)
		self.sample.set_xlabel(self.xlabel)
		self.sample.set_ylabel(self.ylabel)
		self.xmin, self.xmax = self.sample.get_xlim()
		self.ymin, self.ymax = self.sample.get_ylim()

		#Create canvas for the plot and add it to the window
		self.pltcanvas = FigureCanvasTkAgg(self.f,self)
		self.pltcanvas.draw()
		self.pltcanvas.get_tk_widget().place(relx=0.72,rely=0.5,anchor=tk.CENTER)

#########Buttons
		#Button for returning to main menu
		self.menuFrame = ttk.Label(self)
		self.menuFrame.place(relx=0.062,rely=0.07,anchor=tk.CENTER)
		self.menuButton = tk.Button(self.menuFrame, text="Main Menu",command=self.menuButton)
		self.menuFont = ("jua",10,'bold')
		self.menuButton.config(font=self.menuFont)
		self.menuButton.grid(column=0,row=1)
		self.menuButton.config(height=2,width=10)

		#Button for downloading png image
		self.pngFrame = ttk.Label(self)
		self.pngFrame.place(relx=0.568,rely=0.86,anchor=tk.CENTER)
		self.png = tk.Button(self.pngFrame, text="Export PNG",command=self.pngButton)
		self.buttonFont = ("jua",10,'bold')
		self.png.config(font=self.buttonFont)
		self.png.grid(column=0,row=1)
		self.png.config(height=2,width=11)

		#Button for downloading jpg image
		self.jpgFrame = ttk.Label(self)
		self.jpgFrame.place(relx=0.668,rely=0.86,anchor=tk.CENTER)
		self.jpg = tk.Button(self.jpgFrame, text="Export JPG",command=self.jpgButton)
		self.buttonFont = ("jua",10,'bold')
		self.jpg.config(font=self.buttonFont)
		self.jpg.grid(column=0,row=1)
		self.jpg.config(height=2,width=11)

		#Button for downloading csv file
		self.csvFrame = ttk.Label(self)
		self.csvFrame.place(relx=0.768,rely=0.86,anchor=tk.CENTER)
		self.csv = tk.Button(self.csvFrame, text="Export CSV",command=self.csvButton)
		self.buttonFont = ("jua",10,'bold')
		self.csv.config(font=self.buttonFont)
		self.csv.grid(column=0,row=1)
		self.csv.config(height=2,width=11)

		#Button for opening plot options
		self.pltOptionFrame = ttk.Label(self)
		self.pltOptionFrame.place(relx=0.868,rely=0.86,anchor=tk.CENTER)
		self.pltOption = tk.Button(self.pltOptionFrame, text="Plot Options",command=self.plotMenuButton)
		self.buttonFont = ("jua",10,'bold')
		self.pltOption.config(font=self.buttonFont)
		self.pltOption.grid(column=0,row=1)
		self.pltOption.config(height=2,width=11)

		#Button for opening help window
		self.helpFrame = ttk.Label(self)
		self.helpFrame.place(relx=0.44,rely=0.30,anchor=tk.CENTER)
		self.helpOption = tk.Button(self.helpFrame, text="Help",command=self.helpButton)
		self.helpFont = ("jua",10,'bold')
		self.helpOption.config(font=self.helpFont)
		self.helpOption.grid(column=0,row=1)
		self.helpOption.config(height=2,width=11)

		#Button to apply settings
		self.applyButtonFrame = ttk.Label(self)
		self.applyButtonFrame.place(relx=0.10,rely=0.96,anchor=tk.CENTER)
		self.applyButton = tk.Button(self.applyButtonFrame, text="Apply Settings",command=self.applySettings_threading)
		self.buttonFont = ("jua",14,'bold')
		self.applyButton.config(font=self.buttonFont)
		self.applyButton.grid(column=0,row=1)
		self.applyButton.config(height=2,width=15)

		#Button to start scan and collect all input
		self.startButtonFrame = ttk.Label(self)
		self.startButtonFrame.place(relx=0.32,rely=0.96,anchor=tk.CENTER)
		self.startButton = tk.Button(self.startButtonFrame, text="Start Scan",command=self.startScan_threading)
		self.buttonFont = ("jua",14,'bold')
		self.startButton.config(font=self.buttonFont)
		self.startButton.grid(column=0,row=1)
		self.startButton.config(height=2,width=15)
		self.startButton.config(state=DISABLED)

		#Button to end current scan
		self.endScanButtonFrame = ttk.Label(self)
		self.endScanButtonFrame.place(relx=0.47,rely=0.96,anchor=tk.CENTER)
		self.endButton = tk.Button(self.endScanButtonFrame, text="End Scan",command=self.endScanButton)
		self.buttonFont = ("jua",14,'bold')
		self.endButton.config(font=self.buttonFont)
		self.endButton.grid(column=0,row=1)
		self.endButton.config(height=2,width=15)
		self.endButton.config(state=DISABLED)
		#self.endScanFlag = False #flag for determining whether endScan button has been pressed

		#Button for debugging (commented out if no longer needed)
		self.debugButtonFrame = ttk.Label(self)
		self.debugButtonFrame.place(relx=0.4,rely=0.07,anchor=tk.CENTER)
		self.debugButton = tk.Button(self.debugButtonFrame, text="DEBUG:\n get data",command=self.debugButton)
		self.buttonFont = ("jua",8,'bold')
		self.debugButton.config(font=self.buttonFont)
		self.debugButton.grid(column=0,row=1)
		self.debugButton.config(height=2,width=10)

		#Button for debugging (commented out if no longer needed)
		self.debugButtonFrame2 = ttk.Label(self)
		self.debugButtonFrame2.place(relx=0.4,rely=0.20,anchor=tk.CENTER)
		self.debugButton2 = tk.Button(self.debugButtonFrame2, text="DEBUG:\n scan status",command=self.debugButton2)
		self.buttonFont = ("jua",8,'bold')
		self.debugButton2.config(font=self.buttonFont)
		self.debugButton2.grid(column=0,row=1)
		self.debugButton2.config(height=2,width=10)
		
 
#########Entry Boxes
		#Title label for range options
		self.rangeLabel = tk.Label(self,text = "Range:")
		self.ScanningMenuFont = ("jua",20,"bold")
		self.rangeLabel.config(font=self.ScanningMenuFont)
		self.rangeLabel.place(relx=0.06,rely=0.25,anchor=tk.CENTER)

		#Small label for low input and entry box
		self.lowLabel = tk.Label(self,text = "Low:")
		self.ScanningMenuFont = ("jua",12)
		self.lowLabel.config(font=self.ScanningMenuFont)
		self.lowLabel.place(relx=0.038,rely=0.30,anchor=tk.CENTER)
		self.lowEntry=tk.Entry(self)
		self.lowEntry.place(relx=0.11,rely=0.30,anchor=tk.CENTER)

		#nm label
		self.nmLabel = tk.Label(self,text = "nm")
		self.ScanningMenuFont = ("jua",9)
		self.nmLabel.config(font=self.ScanningMenuFont)
		self.nmLabel.place(relx=0.175,rely=0.30,anchor=tk.CENTER)

		#Small label for high input and entry box
		self.highLabel = tk.Label(self,text = "High:")
		self.ScanningMenuFont = ("jua",12)
		self.highLabel.config(font=self.ScanningMenuFont)
		self.highLabel.place(relx=0.238,rely=0.30,anchor=tk.CENTER)
		self.highEntry=tk.Entry(self)
		self.highEntry.place(relx=0.31,rely=0.30,anchor=tk.CENTER)

		#nm label
		self.nmLabel2 = tk.Label(self,text = "nm")
		self.ScanningMenuFont = ("jua",9)
		self.nmLabel2.config(font=self.ScanningMenuFont)
		self.nmLabel2.place(relx=0.375,rely=0.30,anchor=tk.CENTER)

#########Sliders
		#Title label for entrance slit option
		self.slitEntLabel = tk.Label(self,text = "Entrance Slit Width:")
		self.ScanningMenuFont = ("jua",20,"bold")
		self.slitEntLabel.config(font=self.ScanningMenuFont)
		self.slitEntLabel.place(relx=0.125,rely=0.35,anchor=tk.CENTER)

		#Entrance slit width slider
		self.entSlider = tk.Scale(self, from_=0, to=10000, orient=HORIZONTAL, length=580,resolution=12.5,digits=5)
		self.entSlider.place(relx=0.218,rely=0.40,anchor=tk.CENTER)

		#Micrometer label
		self.mLabel = tk.Label(self,text = "\u03BCm")
		self.ScanningMenuFont = ("jua",9)
		self.mLabel.config(font=self.ScanningMenuFont)
		self.mLabel.place(relx=0.420,rely=0.41,anchor=tk.CENTER)

		#Title label for exit slit option
		self.slitExtLabel = tk.Label(self,text = "Exit Slit Width:")
		self.ScanningMenuFont = ("jua",20,"bold")
		self.slitExtLabel.config(font=self.ScanningMenuFont)
		self.slitExtLabel.place(relx=0.1,rely=0.46,anchor=tk.CENTER)

		#Exit slit width slider
		self.extSlider = tk.Scale(self, from_=0, to=10000, orient=HORIZONTAL, length=580,resolution=12.5,digits=5)
		self.extSlider.place(relx=0.218,rely=0.51,anchor=tk.CENTER)

		#Micrometer label
		self.mLabel2 = tk.Label(self,text = "\u03BCm")
		self.ScanningMenuFont = ("jua",9)
		self.mLabel2.config(font=self.ScanningMenuFont)
		self.mLabel2.place(relx=0.420,rely=0.52,anchor=tk.CENTER)

		#Title label for integration time option
		self.intTimeLabel = tk.Label(self,text = "Integration Time:")
		self.ScanningMenuFont = ("jua",20,"bold")
		self.intTimeLabel.config(font=self.ScanningMenuFont)
		self.intTimeLabel.place(relx=0.113,rely=0.57,anchor=tk.CENTER)

		#Integration time slider
		self.intSlider = tk.Scale(self, from_=1, to=200, orient=HORIZONTAL, length=580,resolution=1)
		self.intSlider.place(relx=0.218,rely=0.62,anchor=tk.CENTER)

		#Seconds label
		self.sLabel = tk.Label(self,text = "ms")
		self.ScanningMenuFont = ("jua",9)
		self.sLabel.config(font=self.ScanningMenuFont)
		self.sLabel.place(relx=0.420,rely=0.63,anchor=tk.CENTER)

		#Title label for step size option
		self.stepLabel = tk.Label(self,text = "Step Size:")
		self.ScanningMenuFont = ("jua",20,"bold")
		self.stepLabel.config(font=self.ScanningMenuFont)
		self.stepLabel.place(relx=0.075,rely=0.68,anchor=tk.CENTER)

		#Step size slider
		self.stepSlider = tk.Scale(self, from_=0.0041666667, to=5, orient=HORIZONTAL, length=580,resolution=0.0041666667,digits=11)
		self.stepSlider.place(relx=0.218,rely=0.73,anchor=tk.CENTER)

		#Nanometers label
		self.nmLabel3 = tk.Label(self,text = "nm")
		self.ScanningMenuFont = ("jua",9)
		self.nmLabel3.config(font=self.ScanningMenuFont)
		self.nmLabel3.place(relx=0.420,rely=0.74,anchor=tk.CENTER)

#########Drop Down Menus
		#Title label for grating option
		self.gratingLabel = tk.Label(self,text = "Grating:")
		self.ScanningMenuFont = ("jua",20,"bold")
		self.gratingLabel.config(font=self.ScanningMenuFont)
		self.gratingLabel.place(relx=0.065,rely=0.79,anchor=tk.CENTER)

		#Drop-down menu for grating options (Note: gratingDefault is the actual menu, I originally thought this was just a way to set the default)
		self.gratingDefault = StringVar(self)
		self.gratingDefault.set('1800 l/mm (Vis)') #This sets the default
		self.gratingBox = OptionMenu(self,self.gratingDefault,'1800 l/mm (Vis)','600 l/mm (IR)', command = self.stepChange)
		self.gratingBox.place(relx=0.065,rely=0.84,anchor=tk.CENTER)

		#Title label for detector option
		self.detectorLabel = tk.Label(self,text = "Detector:")
		self.ScanningMenuFont = ("jua",20,"bold")
		self.detectorLabel.config(font=self.ScanningMenuFont)
		self.detectorLabel.place(relx=0.23,rely=0.79,anchor=tk.CENTER)

		#Drop-down menu for detector options (Note: detectorDefault is the actual menu, I originally thought this was just a way to set the default)
		self.detectorDefault = StringVar(self)
		self.detectorDefault.set('Side')
		self.detectorBox = OptionMenu(self,self.detectorDefault,'Side','Front')
		self.detectorBox.place(relx=0.23,rely=0.84,anchor=tk.CENTER)

		#Title label for the gain option
		self.gainLabel = tk.Label(self,text = "Gain:")
		self.ScanningMenuFont = ("jua",20,"bold")
		self.gainLabel.config(font=self.ScanningMenuFont)
		self.gainLabel.place(relx=0.39,rely=0.79,anchor=tk.CENTER)

		#Drop-down menu for gain options (Note: gainDefault is the actual menu, I originally thought this was just a way to set the default)
		self.gainDefault = StringVar(self)
		self.gainDefault.set('AUTO')
		self.gainBox = OptionMenu(self,self.gainDefault,'AUTO','1x','10x','100x','1000x')
		self.gainBox.place(relx=0.39,rely=0.84,anchor=tk.CENTER)

		#Title label for the "Wavelength Scanning" Menu or "Time Base Scanning" menu option
		self.modeMenuLabel = tk.Label(self,text = "Scanning Menus:")
		self.ScanningMenuFont = ("jua",10,"bold")
		self.modeMenuLabel.config(font=self.ScanningMenuFont)
		self.modeMenuLabel.place(relx=0.078,rely=0.13,anchor=tk.CENTER)

		#Drop-down menu for the "Wavelength Scanning" Menu or "Time Base Scanning" menu option
		self.scanOptionDefault = StringVar(self)
		self.scanOptionDefault.set('Wavelength Scanning') #This sets the default
		self.scanOptionBox = OptionMenu(self,self.scanOptionDefault,'Time Base Scanning', command = self.scanningDropOption)
		self.scanOptionBox.place(relx=0.078,rely=0.17,anchor=tk.CENTER)

#########Error Label Definitions:

		#Low value is nan
		self.errorLabelLow = tk.Label(self,text = "Error: Low range value entered is not a number! Please enter again!")
		self.errorFont = ("jua",12,"bold")
		self.errorLabelLow.config(font=self.errorFont,foreground='red')

		#High value is nan
		self.errorLabelHigh = tk.Label(self,text = "Error: High range value entered is not a number! Please enter again!")
		self.errorLabelHigh.config(font=self.errorFont,foreground='red')

		#Low greater than high
		self.highLow = tk.Label(self,text = "Error: Low range value exceeds or equals high range value!")
		self.highLow.config(font=self.errorFont,foreground='red')

		#Range out of bounds (visible)
		self.outOfRange1800 = tk.Label(self,text = "Error: Range must be between 300nm and 869.5875069567nm \n for 1800 grating!")
		self.outOfRange1800.config(font=self.errorFont,foreground='red')

		#Range out of bounds (IR)
		self.outOfRange600 = tk.Label(self,text = "Error: Range must be between 300nm and 1000nm for 600 grating!")
		self.outOfRange600.config(font=self.errorFont,foreground='red')

		#Can't have just 1 data point or 0 data points
		self.stepRange = tk.Label(self,text = "Error: Step size exceeds or equals scanning range!")
		self.stepRange.config(font=self.errorFont,foreground='red')

		#Spectrometer has 5000 data point capacity limit
		self.dataRange = tk.Label(self,text = "Error: Number of data points exceeds 5000 with selected step size!")
		self.dataRange.config(font=self.errorFont,foreground='red')

		#Something went wrong in set scan function
		self.setScanError = tk.Label(self,text = "Error: Scanning malfunction (Setting Scan)!\nPlease restart device and application!")
		self.setScanError.config(font=self.errorFont,foreground='red')

		#Something went wrong in start scan function
		self.setScanError2 = tk.Label(self,text = "Error: Scanning malfunction (Starting Scan)!\nPlease restart device and application!")
		self.setScanError2.config(font=self.errorFont,foreground='red')

#########Progress messages

		#Successfully started scan
		self.progressStart = tk.Label(self,text = "Starting scan...")
		self.progressStart.config(font=self.errorFont,foreground='red')

		#Setup of parameters
		self.progressSetting = tk.Label(self,text = "Setting scan parameters...")
		self.progressSetting.config(font=self.errorFont,foreground='red')

		#reset of parameters
		self.progressReset = tk.Label(self,text = "Reapplying the scan parameters...")
		self.progressReset.config(font=self.errorFont,foreground='red')

		#parameters are set
		self.progressSetReady = tk.Label(self,text = "Settings applied and ready to start scan!")
		self.progressSetReady.config(font=self.errorFont,foreground='green')

		#parameters are reapplied and ready to scan again
		self.progressResetReady = tk.Label(self,text = "Settings reapplied and ready to start scan again!")
		self.progressResetReady.config(font=self.errorFont,foreground='green')

		#Spectrometer scanning
		self.progressScanning = tk.Label(self,text = "Scanning...")
		self.progressScanning.config(font=self.errorFont,foreground='red')

		#Scan completed! Getting data
		self.progressData = tk.Label(self,text = "Downloading data...")
		self.progressData.config(font=self.errorFont,foreground='red')

		#Re-initializes after each scan
		self.progressInit = tk.Label(self,text = "Re-initializing...")
		self.progressInit.config(font=self.errorFont,foreground='red')

		#Re-initializes after each scan
		self.progressEndScan = tk.Label(self,text = "Scan Ended!")
		self.progressEndScan.config(font=self.errorFont,foreground='red')

		#Initializing the labels for the download success text (Don't know why I didn't add the text yet)
		self.csvDownload = tk.Label(self)
		self.csvDownload.config(font=self.errorFont,foreground='red')

		self.pngDownload = tk.Label(self)
		self.pngDownload.config(font=self.errorFont,foreground='red')

		self.jpgDownload = tk.Label(self)
		self.jpgDownload.config(font=self.errorFont,foreground='red')

		#Initialize the progress bar for when scanning
		self.progress=ttk.Progressbar(self,orient='horizontal',length=300,mode='indeterminate')
	#stepChange function
	def stepChange(self, grating):
		self.stepSlider.destroy()
		if grating == '1800 l/mm (Vis)':
		   self.stepSlider = tk.Scale(self, from_=0.0041666667, to=5, orient=HORIZONTAL, length=580,resolution=0.0041666667,digits=11)
		   self.stepSlider.place(relx=0.218,rely=0.65,anchor=tk.CENTER)
		elif grating == '600 l/mm (IR)':
		   self.stepSlider = tk.Scale(self, from_=0.0125, to=5, orient=HORIZONTAL, length=580,resolution=0.0125,digits=11)
		   self.stepSlider.place(relx=0.218,rely=0.65,anchor=tk.CENTER)
		   
	#Function to handle main menu button push
	def menuButton(self):
		window.geometry('900x507')
		self.controller.show_frame(MainMenu)

	def debugButton(self):
		#a.getScanStatus()
		endFlag = True
		totalTime = 0
		while endFlag:
			try:
				steps, intensity = a.getDataScan()
				print('intensity:', intensity)
				print('total time:', totalTime)
				endFlag = False
				print('done')
			except:
				time.sleep(0.001)
				totalTime += 0.001
		print('done2')

	def debugButton2(self):
		a.getScanStatus()
		self.startButton.config(state=NORMAL)


	def scanningDropOption(self, scanMode):
		#Make the window bigger for the time Base Scanning menu so the user can see the plot well enough
		window.geometry('1500x900')
		self.controller.show_frame(timeBaseScanning)
	
	#function to lock access to all button features
	def lockFeatures(self):
		#Lock all scan features
		self.menuButton.config(state=DISABLED)
		self.applyButton.config(state=DISABLED)
		self.startButton.config(state=DISABLED)
		self.scanOptionBox.config(state=DISABLED)
		self.gainBox.config(state=DISABLED)
		self.detectorBox.config(state=DISABLED)
		self.gratingBox.config(state=DISABLED)
		self.stepSlider.config(state=DISABLED)
		self.intSlider.config(state=DISABLED)
		self.extSlider.config(state=DISABLED)
		self.entSlider.config(state=DISABLED)
		self.highEntry.config(state=DISABLED)
		self.lowEntry.config(state=DISABLED)
		self.csv.config(state=DISABLED)
		self.jpg.config(state=DISABLED)
		self.png.config(state=DISABLED)
		self.pltOption.config(state=DISABLED)
		self.helpOption.config(state=DISABLED)
		self.endButton.config(state=DISABLED)
	
	#button to unlock access to all button features 
	def unlockFeatures(self):
		#Lock all scan features
		self.menuButton.config(state=NORMAL)
		self.applyButton.config(state=NORMAL)
		self.startButton.config(state=NORMAL)
		self.scanOptionBox.config(state=NORMAL)
		self.gainBox.config(state=NORMAL)
		self.detectorBox.config(state=NORMAL)
		self.gratingBox.config(state=NORMAL)
		self.stepSlider.config(state=NORMAL)
		self.intSlider.config(state=NORMAL)
		self.extSlider.config(state=NORMAL)
		self.entSlider.config(state=NORMAL)
		self.highEntry.config(state=NORMAL)
		self.lowEntry.config(state=NORMAL)
		self.csv.config(state=NORMAL)
		self.jpg.config(state=NORMAL)
		self.png.config(state=NORMAL)
		self.pltOption.config(state=NORMAL)
		self.helpOption.config(state=NORMAL)
		self.endButton.config(state=NORMAL)

	#Function for handling plot options button push
	def plotMenuButton(self):

		#Lock all scan features
		self.lockFeatures()

		#Make sure the graphics get caught up
		self.update()

		#Create window for options
		self.win = tk.Toplevel()
		self.win.wm_title("Plot Options")
		self.win.resizable(width=False,height=False)
		
		#Calculations for the values needed to put new window in the center of the screen
		width = 460
		height = 460
		ws = self.winfo_screenwidth()
		hs = self.winfo_screenheight()
		x = int((ws/2) - (width/2))
		y = int((hs/2) - (height/2))
		width = str(width)
		height = str(height)
		x = str(x)
		y = str(y)

		#Position window
		self.win.geometry(width + 'x' + height + '+' + x + '+' + y)

		#Title label for plot options menu
		menuTitle = tk.Label(self.win, text="Plot Options Menu")
		menuTitle.place(relx=0.5,rely=0.1,anchor=tk.CENTER)
		self.plottingTitleFont = ("jua",16,"bold")
		menuTitle.config(font=self.plottingTitleFont)

		#Button for applying changes and collecting user input
		applyButtonFrame = tk.Label(self.win)
		applyButtonFrame.place(relx=0.5,rely=0.91,anchor=tk.CENTER)
		applyButton = tk.Button(applyButtonFrame, text="Apply Changes",command=self.applyChanges)
		buttonFont = ("jua",12,'bold')
		applyButton.config(font=buttonFont, height=1, width=12)
		applyButton.grid(column=0,row=1)

		#Option for changing plot title (Text Entry)
		self.titleLabel = tk.Label(self.win,text = "Plot Title:")
		self.plottingMenuFont = ("jua",12)
		self.titleLabel.config(font=self.plottingMenuFont)
		self.titleLabel.place(relx=0.2,rely=0.22,anchor=tk.CENTER)
		self.titleEntry=tk.Entry(self.win)
		self.titleEntry.config(width=30)
		self.titleEntry.place(relx=0.66,rely=0.22,anchor=tk.CENTER)

		#Option for changing plot type (Drop down)
		self.typeLabel = tk.Label(self.win,text = "Plot Type:")
		self.plottingMenuFont = ("jua",12)
		self.typeLabel.config(font=self.plottingMenuFont)
		self.typeLabel.place(relx=0.2,rely=0.32,anchor=tk.CENTER)
		self.typeDefault = StringVar(self.win)
		self.typeDefault.set('Line Plot')
		self.typeBox = OptionMenu(self.win,self.typeDefault,'Line Plot','Scatter Plot')
		self.typeBox.place(relx=0.495,rely=0.32,anchor=tk.CENTER)

		#Option for changing minimum wavelength on plot (Entry)
		self.xminLabel = tk.Label(self.win,text = "Min Wavelength:")
		self.plottingMenuFont = ("jua",12)
		self.xminLabel.config(font=self.plottingMenuFont)
		self.xminLabel.place(relx=0.2,rely=0.42,anchor=tk.CENTER)
		self.xminEntry=tk.Entry(self.win)
		self.xminEntry.config(width=15)
		self.xminEntry.place(relx=0.532,rely=0.42,anchor=tk.CENTER)

		#Option for changing maximum wavelength on plot (Entry)
		self.xmaxLabel = tk.Label(self.win,text = "Max Wavelength:")
		self.plottingMenuFont = ("jua",12)
		self.xmaxLabel.config(font=self.plottingMenuFont)
		self.xmaxLabel.place(relx=0.2,rely=0.52,anchor=tk.CENTER)
		self.xmaxEntry=tk.Entry(self.win)
		self.xmaxEntry.config(width=15)
		self.xmaxEntry.place(relx=0.532,rely=0.52,anchor=tk.CENTER)

		#Option for changing minimum intensity on plot (Entry)
		self.yminLabel = tk.Label(self.win,text = "Min Intensity:")
		self.plottingMenuFont = ("jua",12)
		self.yminLabel.config(font=self.plottingMenuFont)
		self.yminLabel.place(relx=0.2,rely=0.62,anchor=tk.CENTER)
		self.yminEntry=tk.Entry(self.win)
		self.yminEntry.config(width=15)
		self.yminEntry.place(relx=0.532,rely=0.62,anchor=tk.CENTER)

		#Option for changing maximum intensity on plot (Entry)
		self.ymaxLabel = tk.Label(self.win,text = "Max Intensity:")
		self.plottingMenuFont = ("jua",12)
		self.ymaxLabel.config(font=self.plottingMenuFont)
		self.ymaxLabel.place(relx=0.2,rely=0.72,anchor=tk.CENTER)
		self.ymaxEntry=tk.Entry(self.win)
		self.ymaxEntry.config(width=15)
		self.ymaxEntry.place(relx=0.532,rely=0.72,anchor=tk.CENTER)

		#Option for changing color of plot (Drop-down)
		self.colorLabel = tk.Label(self.win,text = "Plot Color:")
		self.plottingMenuFont = ("jua",12)
		self.colorLabel.config(font=self.plottingMenuFont)
		self.colorLabel.place(relx=0.2,rely=0.82,anchor=tk.CENTER)
		self.colorDefault = StringVar(self.win)
		self.colorDefault.set('Blue')
		self.colorBox = OptionMenu(self.win,self.colorDefault,'Blue','Red','Green','Black','Cyan')
		self.colorBox.place(relx=0.47,rely=0.82,anchor=tk.CENTER)
		
		#Used for if the user closes the window with the red x instead of pressing the apply button
		self.win.protocol("WM_DELETE_WINDOW",self.callback)


	def helpButton(self):
		
		#Lock all scan features
		self.lockFeatures()
		self.update()

		self.win = tk.Toplevel()
		self.win.wm_title("Help Bar")
		self.win.resizable(width=False,height=False)
		
		#Values for positioning of window in center
		width = 620
		height = 150
		ws = self.winfo_screenwidth()
		hs = self.winfo_screenheight()
		x = int((ws/2) - (width/2))
		y = int((hs/2) - (height/2))
		width = str(width)
		height = str(height)
		x = str(x)
		y = str(y)

		#Position window
		self.win.geometry(width + 'x' + height + '+' + x + '+' + y)

		#Buttons and options
		menuTitle = tk.Label(self.win, text="Help")
		menuTitle.place(relx=0.5,rely=0.1,anchor=tk.CENTER)
		self.plottingTitleFont = ("jua",16,"bold")
		menuTitle.config(font=self.plottingTitleFont)
	
	#inform user of possible wavelength ranges for given grating
		grating = self.gratingDefault.get()
		self.titleLabel = tk.Label(self.win,text = "Valid Wavelength Ranges for {}:".format(grating))
		self.titleLabelFont = ("jua",12)
		self.titleLabel.config(font=self.titleLabelFont)
		self.titleLabel.place(relx=0.44,rely=0.30,anchor=tk.CENTER)
		
		#Place ranges for specified grating
		if grating == '1800 l/mm (Vis)':
			self.rangeLabel = tk.Label(self.win,text = 'Choose range between 300nm and 869.5875069567nm')
			self.rangeLabel.place(relx=0.51,rely=0.45,anchor=tk.CENTER)
		elif grating == '600 l/mm (IR)':
			self.rangeLabel = tk.Label(self.win,text = 'Choose range between 300nm and 1000nm')
			self.rangeLabel.place(relx=0.44,rely=0.45,anchor=tk.CENTER)
		self.rangeLabelFont = ("jua",12)
		self.rangeLabel.config(font=self.rangeLabelFont)
	
		#Note that at 300nm actually observing 300.0000024nm due to stepsize limitations
		self.noteLabel = tk.Label(self.win,text = 'Note that observations are not perfectly at set low and high values due to step size limitations')
		self.noteLabel.place(relx=0.50,rely=0.80,anchor=tk.CENTER)
		self.noteLabelFont = ("jua",8)
		self.noteLabel.config(font=self.noteLabelFont)
		
		self.win.protocol("WM_DELETE_WINDOW",self.callback)

	#Function to handle plot options window being closed with red x built in to system
	def callback(self):
		#Re-enable all scan features
		self.unlockFeatures()

		#Catch graphics up
		self.update()

		#Get rid of the pop-up window
		self.win.destroy()

	#Function to handle file select window being closed with red x built in to system
	def callbackExport(self):

		#Turn on buttons again
		self.csv.config(state=NORMAL)
		self.jpg.config(state=NORMAL)
		self.png.config(state=NORMAL)
		self.pltOption.config(state=NORMAL)
		self.helpOption.config(state=NORMAL)

	#Function to handle apply button push in plot options menu
	def applyChanges(self):

		#Collect all the input
		title = self.titleEntry.get()
		ptype = self.typeDefault.get()
		xmin = self.xminEntry.get()
		ymin = self.yminEntry.get()
		xmax = self.xmaxEntry.get()
		ymax = self.ymaxEntry.get()
		color = self.colorDefault.get()

		#If the user doesn't input a title, use the default
		if title=='':
		   title=self.plotTitle
		else:
		   self.plotTitle = title

		#Store the selected color
		if color == 'Blue':
		   self.color='b'
		if color == 'Black':
		   self.color='k'
		if color == 'Red':
		   self.color='r'
		if color == 'Green':
		   self.color='g'
		if color == 'Cyan':
		   self.color='c'

		#If the user didn't input an actual number, use the default
		if self.is_number(xmin)==False:
		   xmin = self.xmin
		else:
		   xmin = float(xmin)
		if self.is_number(xmax)==False:
		   xmax = self.xmax
		else:
		   xmax = float(xmax)
		if self.is_number(ymin)==False:
		   ymin = self.ymin
		else:
		   ymin = float(ymin)
		if self.is_number(ymax)==False:
		   ymax = self.ymax
		else:
		   ymax = float(ymax)

		#If the user wanted a scatter plot, make one and update
		if ptype=="Scatter":
		   
		   #Create and display plot:
		   self.f = Figure(figsize=(7,5.4),dpi=100)
		   self.sample = self.f.add_subplot(111)
		   self.sample.scatter(self.steps,self.intensities,self.color)
		   self.sample.set_title(self.plotTitle)
		   self.sample.set_xlabel(self.xlabel)
		   self.sample.set_ylabel(self.ylabel)
		   self.sample.set_xlim(xmin,xmax)
		   self.sample.set_ylim(ymin,ymax)

		   self.pltcanvas = FigureCanvasTkAgg(self.f,self)
		   self.pltcanvas.show()
		   self.pltcanvas.get_tk_widget().place(relx=0.72,rely=0.5,anchor=tk.CENTER)
		   self.update()

		#If the user wanted a line plot, make one and update
		else:
		   #Create and display plot:
		   self.f = Figure(figsize=(7,5.4),dpi=100)
		   self.sample = self.f.add_subplot(111)
		   self.sample.plot(self.steps,self.intensities,self.color)
		   self.sample.set_title(self.plotTitle)
		   self.sample.set_xlabel(self.xlabel)
		   self.sample.set_ylabel(self.ylabel)
		   self.sample.set_xlim(xmin,xmax)
		   self.sample.set_ylim(ymin,ymax)

		   self.pltcanvas = FigureCanvasTkAgg(self.f,self)
		   self.pltcanvas.show()
		   self.pltcanvas.get_tk_widget().place(relx=0.72,rely=0.5,anchor=tk.CENTER)
		   self.update()
		   
		#Clear the plot options window
		self.win.destroy()
		
		#Re-enable all scan features
		self.unlockFeatures()

		#Make sure graphics catch up
		self.update()

	#Function to handle png download button push
	def pngButton(self):

		#Don't allow user to double click or select others
		self.csv.config(state=DISABLED)
		self.jpg.config(state=DISABLED)
		self.png.config(state=DISABLED)
		self.pltOption.config(state=DISABLED)
		self.helpOption.config(state=DISABLED)

		#Forget old message
		self.csvDownload.place_forget()
		self.pngDownload.place_forget()
		self.jpgDownload.place_forget()

		#Make sure graphics catch up
		self.update()

		#Give user the option for file location
		f = filedialog.asksaveasfile(mode='w',defaultextension='.png')

		#As long as there was a file name entered...
		if not f is None:
		   self.f.savefig(f.name)

		   f.close()

		   #Display message that download successful
		   self.pngDownload = tk.Label(self, text='Downloaded PNG as:\n ' + f.name)
		   self.exportFont = ("jua",8,"bold")
		   self.pngDownload.config(font=self.exportFont)
		   self.pngDownload.place(relx=0.721,rely=0.91,anchor=tk.CENTER)

		#Turn on buttons again
		self.csv.config(state=NORMAL)
		self.jpg.config(state=NORMAL)
		self.png.config(state=NORMAL)
		self.pltOption.config(state=NORMAL)
		self.helpOption.config(state=NORMAL)

	#Function to handle jpg download button push
	def jpgButton(self):

		#Don't allow user to double click
		self.csv.config(state=DISABLED)
		self.jpg.config(state=DISABLED)
		self.png.config(state=DISABLED)
		self.pltOption.config(state=DISABLED)
		self.helpOption.config(state=DISABLED)

		#Forget old message
		self.csvDownload.place_forget()
		self.pngDownload.place_forget()
		self.jpgDownload.place_forget()
		self.update()

		#Give user the option for file location
		f = filedialog.asksaveasfile(mode='w',defaultextension='.jpg')

		#As long as there was a file name entered...
		if not f is None:
		   self.f.savefig(f.name)

		   f.close()

		   #Display message that download successful
		   self.jpgDownload = tk.Label(self, text='Downloaded JPG as:\n ' + f.name)
		   self.exportFont = ("jua",8,"bold")
		   self.jpgDownload.config(font=self.exportFont)
		   self.jpgDownload.place(relx=0.721,rely=0.91,anchor=tk.CENTER)

		#Turn on buttons again
		self.csv.config(state=NORMAL)
		self.jpg.config(state=NORMAL)
		self.png.config(state=NORMAL)
		self.pltOption.config(state=NORMAL)
		self.helpOption.config(state=NORMAL)

	#Function to handle csv download button push
	def csvButton(self):

		#Don't allow user to double click
		self.csv.config(state=DISABLED)
		self.jpg.config(state=DISABLED)
		self.png.config(state=DISABLED)
		self.pltOption.config(state=DISABLED)
		self.helpOption.config(state=DISABLED)

		#Forget old message
		self.csvDownload.place_forget()
		self.pngDownload.place_forget()
		self.jpgDownload.place_forget()
		self.update()

		#Give user the option for file location
		f = filedialog.asksaveasfile(mode='w',defaultextension='.csv')

		#As long as file name entered...
		if not f is None:
		   f.write('Wavelength(nm),Intensities\n')
		   for i in range(len(self.steps)):
			   f.write(str(self.steps[i]))
			   f.write(',')
			   f.write(str(self.intensities[i]))
			   f.write('\n')

		   f.close()

		   #Display message that download successful
		   self.csvDownload = tk.Label(self, text='Downloaded CSV as: \n ' + f.name)
		   self.exportFont = ("jua",8,"bold")
		   self.csvDownload.config(font=self.exportFont)
		   self.csvDownload.place(relx=0.721,rely=0.91,anchor=tk.CENTER)

		#Turn on buttons again
		self.csv.config(state=NORMAL)
		self.jpg.config(state=NORMAL)
		self.png.config(state=NORMAL)
		self.pltOption.config(state=NORMAL)
		self.helpOption.config(state=NORMAL)
		
	#Function used to check if input from user is a number (Used in scanning menu; plot options menu)
	def is_number(self,a):
		try:
			float(a)
			return True
		except ValueError:
			pass

		return False

	#Function used to clear all possible errors and progress messages
	def clearErrors(self):

		#Clear all errors
		self.errorLabelLow.place_forget()
		self.errorLabelHigh.place_forget()
		self.outOfRange1800.place_forget()
		self.outOfRange600.place_forget()
		self.highLow.place_forget()
		self.stepRange.place_forget()
		self.dataRange.place_forget()
		self.setScanError.place_forget()
		self.setScanError2.place_forget()

		#Clear all progress messages
		self.progressStart.place_forget()
		self.progressSetting.place_forget()
		self.progressReset.place_forget()
		self.progressSetReady.place_forget()
		self.progressResetReady.place_forget()
		self.progressScanning.place_forget()
		self.progressData.place_forget()
		self.progressInit.place_forget()
		self.progressEndScan.place_forget()

		#clear all export messages
		self.csvDownload.place_forget()
		self.pngDownload.place_forget()
		self.jpgDownload.place_forget()

	##############################Wavlength Scanning Menu Buttons##############################################################################
	def applySettingsButton(self, reset = False):#reset = True when called after scan is completed and resetting monochromator
		#Make sure all errors cleared and graphics caught up
		self.clearErrors()
		self.update()

		#Collect all the user input
		low = self.lowEntry.get()
		high = self.highEntry.get()
		gain = self.gainDefault.get()
		grating = self.gratingDefault.get()
		detector = self.detectorDefault.get()
		entSize = self.entSlider.get()
		extSize = self.extSlider.get()
		stepSize = self.stepSlider.get()
		intTime = self.intSlider.get()

		#Check if low value is a number:
		if self.is_number(low)==False:

			#If it isn't throw an error at user:
			self.errorLabelLow.place(relx=0.76,rely=0.94, anchor=tk.CENTER)
			#Reset buttons and exit this function to allow user to try again
			return

		#If the low value IS a number, clear the error
		self.errorLabelLow.place_forget()

		#Check if high value is a number:
		if self.is_number(high)==False:

			#If it isn't, throw an error
			self.errorLabelHigh.place(relx=0.76,rely=0.94,anchor=tk.CENTER)

			#Reset buttons and exit function to allow user to try again
			return

		#If high value was a number, clear the error
		self.errorLabelHigh.place_forget()

		#Check if the low value is larger than the high value
		if float(low) >= float(high):

			#Throw error if it is
			self.highLow.place(relx=0.76,rely=0.94,anchor=tk.CENTER)
	   
			#Reset all buttons and exit function to allow user to try again
			return

		#Clear the error if the low value is indeed less than the high value
		self.highLow.place_forget()

		#Check if out of range for 1800 grating
		if grating=='1800 l/mm (Vis)' and (float(high)>869.5875069567 or float(low)<300): #note that at 300 nm you are actually observing 300.0000024nm
			#If out of range, throw error
			self.outOfRange1800.place(relx=0.76,rely=0.94,anchor=tk.CENTER)

			#Reset buttons and exit function to allow user to try again
			return
		
		#Clear the error if the range is okay
		self.outOfRange1800.place_forget()

		#Check if out of range for 600 grating
		if grating=='600 l/mm (IR)' and (float(high)>1000 or float(low)<300):

			#If out of range, throw error
			self.outOfRange600.place(relx=0.76,rely=0.94,anchor=tk.CENTER)

			#Reset buttons and exit function to allow user to try again
			return

		#Clear error for out of range if within range
		self.outOfRange600.place_forget()

		#If the step size is greater than or equal to the range
		if stepSize >= (float(high)-float(low)):

			#Throw error
			self.stepRange.place(relx=0.76,rely=0.94,anchor=tk.CENTER)

			#Reset buttons and exit function to allow user to try again
			return

		#Clear error for too large of step range
		self.stepRange.place_forget()

		if grating=='1800 l/mm (Vis)':
			#Compute the number of data points with the given step size (0.0041666667nm is the step size given by the manual)
			lowStep = np.round(float(low)/0.0041666667)
			highStep = np.round(float(high)/0.0041666667)
			rangeDif = highStep-lowStep
			stepLength = np.round(stepSize/0.0041666667)
			dataPoints = np.round(rangeDif/stepLength)
		elif grating=='600 l/mm (IR)':
			lowStep = np.round(float(low)/0.0125)
			highStep = np.round(float(high)/0.0125)
			rangeDif = highStep-lowStep
			stepLength = np.round(stepSize/0.0125)
			dataPoints = np.round(rangeDif/stepLength)
		
		#If exceeding 5000 data points:
		if dataPoints>5000:

			#Throw error if over 5000 data points
			self.dataRange.place(relx=0.76,rely=0.94,anchor=tk.CENTER)
			return

		#Clear error for exceeding data point range
		self.dataRange.place_forget()

		#Create progress bar:
		self.progress.place(relx=0.76,rely=0.93,anchor=tk.CENTER)
		self.progress.start()
		self.update()

		#Prepare Gain setting:
		if gain=='AUTO':
			gain=4

		if gain=='1x':
			gain=0

		if gain=='10x':
			gain=1
	 
		if gain=='100x':
			gain=2

		if gain=='1000x':
			gain=3

		#Prepare mirror setting:
		if detector=='Side':
			detector = 's'

		if detector=='Front':
			detector = 'f'

		#Prepare grating setting:
		if grating=='1800 l/mm (Vis)':
			grating = 'vis'

		if grating=='600 l/mm (IR)':
			grating = 'ir'

		#time.sleep(1)

		#Check if settings are applied before or after a scan (this just changes what messages are displayed)
		if reset:

			#Display message that monochromator is getting set up again...
			self.progressReset.place(relx=0.76,rely=0.96,anchor=tk.CENTER)
			self.update()

			#Set the scan parameters for spectrometer, make sure response is good
			response = a.setScanGUI(str(lowStep),str(highStep),str(stepLength),str(intTime),str(int(entSize/12.5)),str(int(extSize/12.5)),str(gain),grating,detector)

			if response==1:
				self.setScanError.place(relx=0.76,rely=0.94,anchor=tk.CENTER)
				return

			#Setting complete! Disable message and display that it is ready to scan:
			self.progressReset.place_forget()
			self.progress.place_forget()
			self.progressResetReady.place(relx=0.76,rely=0.96,anchor=tk.CENTER)
			
			print("DEBUG: set scan response:", response) 
			if response == 0:
			   self.startButton.config(state=NORMAL)

		else:

			#Display message that monochromator is getting set up...
			self.progressSetting.place(relx=0.76,rely=0.96,anchor=tk.CENTER)
			self.update()

			#Set the scan parameters for spectrometer, make sure response is good
			response = a.setScanGUI(str(lowStep),str(highStep),str(stepLength),str(intTime),str(int(entSize/12.5)),str(int(extSize/12.5)),str(gain),grating,detector)
			if response==1:
				self.setScanError.place(relx=0.76,rely=0.94,anchor=tk.CENTER)
				return
		
			#Setting complete! Disable message and display that it is ready to scan:
			self.progressSetting.place_forget()
			self.progress.place_forget()
			self.progressSetReady.place(relx=0.76,rely=0.96,anchor=tk.CENTER)

			if response == 0:
			   self.startButton.config(state=NORMAL)

	#thread the apply settings button so that progress bar works while monochromator is getting set up
	def applySettings_threading(self):
		applySettingsThread = threading.Thread(target=self.applySettingsButton)
		applySettingsThread.start() 

	#Function used to handle start scan button push (LONG!!!)
	def startScanButton(self):

		#clear any errors or messages and place progress bar and scanning message
		self.clearErrors()
		self.progress.place(relx=0.76,rely=0.93,anchor=tk.CENTER)
		self.progress.start()
		self.progressScanning.place(relx=0.76,rely=0.96,anchor=tk.CENTER)
		self.update()

		
		#get essential parameters for downloading data
		low = self.lowEntry.get()
		high = self.highEntry.get()
		grating = self.gratingDefault.get()
		stepSize = self.stepSlider.get()

		#enable access to end scan button during scan
		self.endButton.config(state=NORMAL)

		#Start the scan:
		response_start = a.startScan()

		#Check response from spectrometer
		if response_start == 1:
			self.setScanError2.place(relx=0.76,rely=0.94,anchor=tk.CENTER)
			return

		#sleep for a second in case end scan button was called so that end scan message displays for a moment before initializing
		time.sleep(1) 
		self.progressEndScan.place_forget()

		#Done scanning! Disable message and display that it is downloading data
		self.progressScanning.place_forget()
		self.progressData.place(relx=0.76,rely=0.96,anchor=tk.CENTER) 
		self.update()
		self.endButton.config(state=DISABLED)  

		#Get the data
		self.steps,self.intensities = a.getDataScan()

		#Convert steps to nm
		for i in range(len(self.steps)):
			if math.isnan(float(self.steps[i])):
				self.steps[i]=0.0

			grating = self.gratingDefault.get()
			low = float(low)
			if grating == '1800 l/mm (Vis)':
				startingValue = np.round(low/0.0041666667)*0.0041666667
			elif grating == '600 l/mm (IR)':
				startingValue = np.round(low/0.0125)*0.0125

			if grating == '1800 l/mm (Vis)':
				self.steps[i] = float(startingValue) + ((self.steps[i]-1)*float(stepSize))
			elif grating == '600 l/mm (IR)':
				self.steps[i] = float(startingValue) + ((self.steps[i]-1)*float(stepSize))

		#Check for nans (If nan, make it a 0)
		for i in range(len(self.intensities)):
			if math.isnan(float(self.intensities[i])):
				self.intensities[i] = 0.0

		#Convert steps and intensities to float values for accuracy
		self.steps = self.steps.astype('float64')
		self.intensities = self.intensities.astype('float64')

		#Create and display plot:
		self.f = Figure(figsize=(7,5.4),dpi=100)
		self.sample = self.f.add_subplot(111)
		self.sample.plot(self.steps,self.intensities,self.color)
		self.sample.set_title(self.plotTitle)
		self.sample.set_xlabel(self.xlabel)
		self.sample.set_ylabel(self.ylabel)
		self.xmin, self.xmax = self.sample.get_xlim()
		self.ymin, self.ymax = self.sample.get_ylim()

		self.pltcanvas = FigureCanvasTkAgg(self.f,self)
		self.pltcanvas.show()
		self.pltcanvas.get_tk_widget().place(relx=0.72,rely=0.5,anchor=tk.CENTER)
		self.update()

		#Done getting data! Disable message and display new that device is initializing
		self.progressData.place_forget()

		self.progressInit.place(relx=0.76,rely=0.96,anchor=tk.CENTER)
		self.update()

		#unlock export buttons so that user can export data while reapplying the settings
		self.csv.config(state=NORMAL)
		self.jpg.config(state=NORMAL)
		self.png.config(state=NORMAL) 

		#Re-initialize spectrometer/ reset the spectrometer to user applied settings
		#a.initialize()
		self.applySettingsButton(True)
		self.unlockFeatures()

		#Done with initializing and with progress bar. Clear it all...
		self.progress.place_forget()
		self.progressInit.place_forget()
		self.progress.stop()
		self.update()

		#Reset buttons to allow for new scan
		self.endButton.config(state=DISABLED)


	#Thread the scanning so that user can press the 'end scan' button during scan
	def startScan_threading(self):
		self.lockFeatures()
		scanThread = threading.Thread(target=self.startScanButton)
		scanThread.start()

	def endScanButton(self):
		#Used to stop the current time base scan
		endFlag = True
		totalTime = 0
		while endFlag:
			try:
				response_end = a.scanStop()
				endFlag = False
			except serial.serialutil.SerialException:
				   time.sleep(0.001)
				   totalTime += 0.001

		self.progressScanning.place_forget()
		self.progressEndScan.place(relx=0.76,rely=0.96,anchor=tk.CENTER)



class Tools(tk.Frame):

	def __init__(self,parent,controller):
		self.controller = controller
		tk.Frame.__init__(self,parent)

		#Tool Menu Title Label
		self.label = tk.Label(self,text = "Tool Control")
		self.scanningMenuFont = ("jua",35,"bold")
		self.label.config(font=self.scanningMenuFont)
		self.label.place(relx=0.5,rely=0.07,anchor=tk.CENTER)

		#Button for returning to main menu
		self.mainMenuFrame = ttk.Label(self)
		self.mainMenuFrame.place(relx=0.062,rely=0.07,anchor=tk.CENTER)
		self.menuButton = tk.Button(self.mainMenuFrame, text="Main Menu",command=self.menuButton)
		self.buttonFont = ("jua",10,'bold')
		self.menuButton.config(font=self.buttonFont)
		self.menuButton.grid(column=0,row=1)
		self.menuButton.config(height=2,width=10)

		#Button for initializing
		self.initFrame = ttk.Label(self)
		self.initFrame.place(relx=0.062,rely=0.14,anchor=tk.CENTER)
		self.initButton = tk.Button(self.initFrame, text="Initialize",command=self.initializeButton)
		self.buttonFont = ("jua",10,'bold')
		self.initButton.config(font=self.buttonFont)
		self.initButton.grid(column=0,row=1)
		self.initButton.config(height=2,width=10)


		
	#Function to handle main menu button push
	def menuButton(self):
		window.geometry('900x507')
		self.controller.show_frame(MainMenu)

	def initializeButton(self):
		
		#Set up a progress bar
		self.progress=ttk.Progressbar(self,orient='horizontal',length=300,mode='determinate')
		self.progress.place(relx=0.76,rely=0.93,anchor=tk.CENTER)

	#wait message (NOTE: background covers this so this is commented out until solution is found)
		#self.waitMessage = tk.Label(self,text = "Please wait, this may take a while...")
		#self.plottingMenuFont = ("jua",12)
		#self.waitMessage.config(font=self.plottingMenuFont)
		#self.waitMessage.place(relx=0.5,rely=0.5,anchor=tk.CENTER)	
		self.progress['value']=25
		self.progress.update()
		a.initialize()
		self.progress['value']=50
		self.progress.update()
		a.setMotorSpeed()
		self.progress['value']=60
		self.progress.update()
		a.setSlitSpeed('0')
		self.progress['value']=70
		self.progress.update()
		a.setSlitSpeed('1')
		self.progress['value']=80
		self.progress.update()
		a.setSlitSpeed('2')
		self.progress['value']=90
		self.progress.update()
		a.setSlitSpeed('3')
		self.progress['value']=100
		self.progress.update()
		
#Class for time base Scanning options menu
class timeBaseScanning(tk.Frame):

	def __init__(self,parent,controller):
		self.controller = controller
		tk.Frame.__init__(self,parent)

#########time base scan illustration diagram
		tbsImage = 'tbsDiagram.jpg'

		#Place images to the right of the buttons for design purposes
		self.tbsDiagram = Image.open(tbsImage)
		self.tbsDiagram = self.tbsDiagram.resize((250,200),Image.ANTIALIAS)
		self.imageHold = tk.Canvas(self)
		self.tbsDiagram = ImageTk.PhotoImage(self.tbsDiagram)
		self.imageHold.create_image(0,0,image=self.tbsDiagram,anchor='nw')
		self.imageHold.place(relx=0.40,rely=0.25,anchor=tk.CENTER)

		#Time Base Scanning Menu Title Label
		self.label = tk.Label(self,text = "Time Base Scanning")
		self.scanningMenuFont = ("jua",35,"bold")
		self.label.config(font=self.scanningMenuFont)
		self.label.place(relx=0.72,rely=0.11,anchor=tk.CENTER)


#########Entry boxes
		#Small label for wavelength and create a wavelength entry box
		self.wavelengthLabel = tk.Label(self,text = "Wavelength:")
		self.scanningMenuFont = ("jua",12)
		self.wavelengthLabel.config(font=self.scanningMenuFont)
		self.wavelengthLabel.place(relx=0.058,rely=0.22,anchor=tk.CENTER)
		self.wavelengthEntry=tk.Entry(self)
		self.wavelengthEntry.place(relx=0.12,rely=0.22,anchor=tk.CENTER, width = 70)

		#nm label
		self.nmLabel = tk.Label(self,text = "nm")
		self.ScanningMenuFont = ("jua",9)
		self.nmLabel.config(font=self.ScanningMenuFont)
		self.nmLabel.place(relx=0.155,rely=0.22,anchor=tk.CENTER)

#########Sliders
		#Title label for entrance slit option
		self.slitEntLabel = tk.Label(self,text = "Entrance Slit Width:")
		self.ScanningMenuMenuFont = ("jua",20,"bold")
		self.slitEntLabel.config(font=self.ScanningMenuMenuFont)
		self.slitEntLabel.place(relx=0.125,rely=0.30,anchor=tk.CENTER)

	#Entrance slit width slider
		self.entSlider = tk.Scale(self, from_=0, to=10000, orient=HORIZONTAL, length=580,resolution=12.5,digits=5)
		self.entSlider.place(relx=0.218,rely=0.35,anchor=tk.CENTER)

		#Micrometer label
		self.mLabel = tk.Label(self,text = "\u03BCm")
		self.ScanningMenuMenuFont = ("jua",9)
		self.mLabel.config(font=self.ScanningMenuMenuFont)
		self.mLabel.place(relx=0.420,rely=0.36,anchor=tk.CENTER)

		#Title label for exit slit option
		self.slitExtLabel = tk.Label(self,text = "Exit Slit Width:")
		self.ScanningMenuMenuFont = ("jua",20,"bold")
		self.slitExtLabel.config(font=self.ScanningMenuMenuFont)
		self.slitExtLabel.place(relx=0.1,rely=0.41,anchor=tk.CENTER)

		#Exit slit width slider
		self.extSlider = tk.Scale(self, from_=0, to=10000, orient=HORIZONTAL, length=580,resolution=12.5,digits=5)
		self.extSlider.place(relx=0.218,rely=0.46,anchor=tk.CENTER)

		#Micrometer label
		self.mLabel2 = tk.Label(self,text = "\u03BCm")
		self.ScanningMenuMenuFont = ("jua",9)
		self.mLabel2.config(font=self.ScanningMenuMenuFont)
		self.mLabel2.place(relx=0.420,rely=0.47,anchor=tk.CENTER)

		#Title label for integration time option
		self.intTimeLabel = tk.Label(self,text = "Integration Time:")
		self.ScanningMenuMenuFont = ("jua",20,"bold")
		self.intTimeLabel.config(font=self.ScanningMenuMenuFont)
		self.intTimeLabel.place(relx=0.113,rely=0.52,anchor=tk.CENTER)

		#Integration time slider
		self.intSlider = tk.Scale(self, from_=1, to=200, orient=HORIZONTAL, length=580,resolution=1)
		self.intSlider.place(relx=0.218,rely=0.57,anchor=tk.CENTER)

		#Seconds label
		self.sLabel = tk.Label(self,text = "ms")
		self.ScanningMenuMenuFont = ("jua",9)
		self.sLabel.config(font=self.ScanningMenuMenuFont)
		self.sLabel.place(relx=0.420,rely=0.58,anchor=tk.CENTER)

		#Title label Time Increment Option and a side note marked by an asterisk
		self.timeIncLabel = tk.Label(self,text = "Time Increment:")
		self.ScanningMenuMenuFont = ("jua",20,"bold")
		self.timeIncLabel.config(font=self.ScanningMenuMenuFont)
		self.timeIncLabel.place(relx=0.108,rely=0.63,anchor=tk.CENTER)

		self.asteriskNote = tk.Label(self, text = "*")
		self.asteriskFont = ("jua",15,"normal")
		self.asteriskNote.config(font = self.asteriskFont)
		self.asteriskNote.place(relx=0.01,rely=0.63,anchor=tk.CENTER)

		self.sideNote = tk.Label(self, text = "*If Time Increment is zero, then the Integration Time becomes the effective Time Increment.")
		self.sideFont = ("jua",8,"normal")
		self.sideNote.config(font = self.sideFont)
		self.sideNote.place(relx=0.76,rely=0.98,anchor=tk.CENTER)

		#Time Increment Slider
		self.timeIncSlider = tk.Scale(self, from_=1, to=1000, orient=HORIZONTAL, length=580,resolution=10,digits=11)
		self.timeIncSlider.place(relx=0.218,rely=0.68,anchor=tk.CENTER)

		#Milleseconds label
		self.sLabel2 = tk.Label(self,text = "ms")
		self.ScanningMenuMenuFont = ("jua",9)
		self.sLabel2.config(font=self.ScanningMenuMenuFont)
		self.sLabel2.place(relx=0.420,rely=0.69,anchor=tk.CENTER)

		#Title label total Time Base Scan time Option
		self.totalTimeLabel = tk.Label(self,text = "Total Scan Time:")
		self.ScanningMenuMenuFont = ("jua",20,"bold")
		self.totalTimeLabel.config(font=self.ScanningMenuMenuFont)
		self.totalTimeLabel.place(relx=0.108,rely=0.74,anchor=tk.CENTER)

		#Total Time Slider
		self.totalTimeSlider = tk.Scale(self, from_=1, to=200000, orient=HORIZONTAL, length=580,resolution=100,digits=11)
		self.totalTimeSlider.place(relx=0.218,rely=0.79,anchor=tk.CENTER)

		#Milleseconds label
		self.sLabel3 = tk.Label(self,text = "ms")
		self.ScanningMenuMenuFont = ("jua",9)
		self.sLabel3.config(font=self.ScanningMenuMenuFont)
		self.sLabel3.place(relx=0.420,rely=0.80,anchor=tk.CENTER)



#########Drop down menus
		#Title label for grating option
		self.gratingLabel = tk.Label(self,text = "Grating:")
		self.ScanningMenuMenuFont = ("jua",20,"bold")
		self.gratingLabel.config(font=self.ScanningMenuMenuFont)
		self.gratingLabel.place(relx=0.065,rely=0.84,anchor=tk.CENTER)

		#Drop-down menu for grating options (Note: gratingDefault is the actual menu, I originally thought this was just a way to set the default)
		self.gratingDefault = StringVar(self)
		self.gratingDefault.set('1800 l/mm (Vis)') #This sets the default
		self.gratingBox = OptionMenu(self,self.gratingDefault,'1800 l/mm (Vis)','600 l/mm (IR)')
		self.gratingBox.place(relx=0.065,rely=0.89,anchor=tk.CENTER)

		#Title label for detector option
		self.detectorLabel = tk.Label(self,text = "Detector:")
		self.ScanningMenuMenuFont = ("jua",20,"bold")
		self.detectorLabel.config(font=self.ScanningMenuMenuFont)
		self.detectorLabel.place(relx=0.23,rely=0.84,anchor=tk.CENTER)

		#Drop-down menu for detector options (Note: detectorDefault is the actual menu, I originally thought this was just a way to set the default)
		self.detectorDefault = StringVar(self)
		self.detectorDefault.set('Side')
		self.detectorBox = OptionMenu(self,self.detectorDefault,'Side','Front')
		self.detectorBox.place(relx=0.23,rely=0.89,anchor=tk.CENTER)

		#Title label for the gain option
		self.gainLabel = tk.Label(self,text = "Gain:")
		self.ScanningMenuMenuFont = ("jua",20,"bold")
		self.gainLabel.config(font=self.ScanningMenuMenuFont)
		self.gainLabel.place(relx=0.39,rely=0.84,anchor=tk.CENTER)

		#Drop-down menu for gain options (Note: gainDefault is the actual menu, I originally thought this was just a way to set the default)
		self.gainDefault = StringVar(self)
		self.gainDefault.set('AUTO')
		self.gainBox = OptionMenu(self,self.gainDefault,'AUTO','1x','10x','100x','1000x')
		self.gainBox.place(relx=0.39,rely=0.89,anchor=tk.CENTER)

		#Title label for the "Wavelength Scanning" Menu or "Time Base Scanning" menu option
		self.modeMenuLabel = tk.Label(self,text = "Scanning Menus:")
		self.ScanningMenuFont = ("jua",10,"bold")
		self.modeMenuLabel.config(font=self.ScanningMenuFont)
		self.modeMenuLabel.place(relx=0.078,rely=0.13,anchor=tk.CENTER)

		#Drop-down menu for the "Wavelength Scanning" Menu or "Time Base Scanning" menu option
		self.scanOptionDefault = StringVar(self)
		self.scanOptionDefault.set('Time Base Scanning') #This sets the default
		self.scanOptionBox = OptionMenu(self,self.scanOptionDefault,'Wavelength Scanning', command = self.scanningDropOption)
		self.scanOptionBox.place(relx=0.078,rely=0.17,anchor=tk.CENTER)


#########Buttons	   
		#Button for returning to main menu
		self.mainMenuFrame = ttk.Label(self)
		self.mainMenuFrame.place(relx=0.062,rely=0.07,anchor=tk.CENTER)
		self.menuButton = tk.Button(self.mainMenuFrame, text="Main Menu",command=self.menuButton)
		self.buttonFont = ("jua",10,'bold')
		self.menuButton.config(font=self.buttonFont)
		self.menuButton.grid(column=0,row=1)
		self.menuButton.config(height=2,width=10)

		#Button to apply settings
		self.applyButtonFrame = ttk.Label(self)
		self.applyButtonFrame.place(relx=0.10,rely=0.96,anchor=tk.CENTER)
		self.applyButton = tk.Button(self.applyButtonFrame, text="Apply Settings",command=self.applySettingsButton)
		self.buttonFont = ("jua",14,'bold')
		self.applyButton.config(font=self.buttonFont)
		self.applyButton.grid(column=0,row=1)
		self.applyButton.config(height=2,width=15)
  
		#Button to start scan
		self.startButtonFrame = ttk.Label(self)
		self.startButtonFrame.place(relx=0.32,rely=0.96,anchor=tk.CENTER)
		self.startButton = tk.Button(self.startButtonFrame, text="Start Scan",command=self.startScan_threading)
		self.buttonFont = ("jua",14,'bold')
		self.startButton.config(font=self.buttonFont)
		self.startButton.grid(column=0,row=1)
		self.startButton.config(height=2,width=15)
		self.startButton.config(state=DISABLED)

		#Button to end current scan
		self.endScanButtonFrame = ttk.Label(self)
		self.endScanButtonFrame.place(relx=0.47,rely=0.96,anchor=tk.CENTER)
		self.endButton = tk.Button(self.endScanButtonFrame, text="End Scan",command=self.endScanButton)
		self.buttonFont = ("jua",14,'bold')
		self.endButton.config(font=self.buttonFont)
		self.endButton.grid(column=0,row=1)
		self.endButton.config(height=2,width=15)
		self.endButton.config(state=DISABLED)
		self.endScanFlag = False #flag for determining whether endScan button has been pressed

		#Button for starting realtime data collection
		self.debugButtonFrame = ttk.Label(self)
		self.debugButtonFrame.place(relx=0.4,rely=0.07,anchor=tk.CENTER)
		self.debugButton = tk.Button(self.debugButtonFrame, text="get realtime \n data",command=self.getRealButton)
		self.buttonFont = ("jua",8,'bold')
		self.debugButton.config(font=self.buttonFont)
		self.debugButton.grid(column=0,row=1)
		self.debugButton.config(height=2,width=10)

		#Button for debugging (commented out if no longer needed)
		self.debugButtonFrame2 = ttk.Label(self)
		self.debugButtonFrame2.place(relx=0.30,rely=0.07,anchor=tk.CENTER)
		self.debugButton2 = tk.Button(self.debugButtonFrame2, text="DEBUG:\n scan status",command=self.debugButton2)
		self.buttonFont = ("jua",8,'bold')
		self.debugButton2.config(font=self.buttonFont)
		self.debugButton2.grid(column=0,row=1)
		self.debugButton2.config(height=2,width=10)
		
		

#########Read out window
		#Create canvas for the plot and add it to the window
		"""
		#plot the real time data with bar graph
		self.fBar = Figure(figsize=(7,5.4),dpi=100)
		self.ax = self.fBar.add_subplot(111)
		self.ax.set(xlim=(0, 5), ylim=(0, 40))
		self.dataBar = [20]
		self.index = np.arange(1)
		self.width = 0.5
		self.rect = self.ax.bar(self.index, self.dataBar, self.width)
		
		
		#create a canvas for the plot
		self.pltcanvas = FigureCanvasTkAgg(self.fig,self)
		self.pltcanvas.show()
		self.pltcanvas.get_tk_widget().place(relx=0.72,rely=0.5,anchor=tk.CENTER)
		"""
########Error Label Definitions:
		#wavelength value is nan
		self.errorLabelWavelength = tk.Label(self,text = "Error: Wavelength value entered is not a number! Please enter again!")
		self.errorFont = ("jua",12,"bold")
		self.errorLabelWavelength.config(font=self.errorFont,foreground='red')

		#Range out of bounds (visible)
		self.outOfRange1800 = tk.Label(self,text = "Error: Range must be between 300nm and 869.5875069567nm \n for 1800 grating!")
		self.outOfRange1800.config(font=self.errorFont,foreground='red')

		#Range out of bounds (IR)
		self.outOfRange600 = tk.Label(self,text = "Error: Range must be between 300nm and 1000nm \n for 600 grating!")
		self.outOfRange600.config(font=self.errorFont,foreground='red')

#########

#########Buttons/Functionality
	#function to lock access to all button features
	def lockFeatures(self):
		#Lock all scan features
		self.menuButton.configure(state=DISABLED)
		self.startButton.configure(state=DISABLED)
		self.endButton.config(state=DISABLED)
		self.applyButton.config(state=DISABLED)
		self.gainBox.config(state=DISABLED)
		self.detectorBox.config(state=DISABLED)
		self.gratingBox.config(state=DISABLED)
		self.intSlider.config(state=DISABLED)
		self.extSlider.config(state=DISABLED)
		self.entSlider.config(state=DISABLED)
		self.wavelengthEntry.config(state=DISABLED)
	
	#button to unlock access to all button features 
	def unlockFeatures(self):
		#Lock all scan features
		self.menuButton.configure(state=NORMAL)
		self.startButton.configure(state=NORMAL)
		self.endButton.config(state=NORMAL)
		self.applyButton.config(state=NORMAL)
		self.gainBox.config(state=NORMAL)
		self.detectorBox.config(state=NORMAL)
		self.gratingBox.config(state=NORMAL)
		self.intSlider.config(state=NORMAL)
		self.extSlider.config(state=NORMAL)
		self.entSlider.config(state=NORMAL)
		self.wavelengthEntry.config(state=NORMAL)


	#Function to handle main menu button push
	def menuButton(self):
		window.geometry('900x507')
		self.controller.show_frame(MainMenu)

	def scanningDropOption(self, scanMode):
		#Make the window bigger for the time base scanning menu so the user can see the plot well enough
		window.geometry('1500x900')
		self.controller.show_frame(Scanning)

	#Function used to check if input from user is a number (Used in scanning menu; plot options menu)
	def is_number(self,a):
		try:
			float(a)
			return True
		except ValueError:
			pass

		return False

	def applySettingsButton(self):
		self.update()
		#Collect all the user input
		wavelength = self.wavelengthEntry.get()
		gain = self.gainDefault.get()
		grating = self.gratingDefault.get()
		detector = self.detectorDefault.get()
		entSize = self.entSlider.get()
		extSize = self.extSlider.get()
		intTime = self.intSlider.get()
		incTime = self.timeIncSlider.get()
		totalTime = self.totalTimeSlider.get()

	####Error handling
		#Check if wavelength value is a number:
		if self.is_number(wavelength)==False:

			#If it isn't throw an error at user:
			self.errorLabelWavelength.place(relx=0.76,rely=0.94,anchor=tk.CENTER)
			return
		
		#If the low value IS a number, clear the error
		self.errorLabelWavelength.place_forget()

		#Check if out of range for 1800 grating
		if grating=='1800 l/mm (Vis)' and (float(wavelength)>869.5875069567 or float(wavelength)<300):
			#If out of range, throw error
			self.outOfRange1800.place(relx=0.76,rely=0.94,anchor=tk.CENTER)
			return
		
		#Clear the error if the wavelength is in correct range
		self.outOfRange1800.place_forget()

		#Check if out of range for 600 grating
		if grating=='600 l/mm (IR)' and (float(wavelength)>1000 or float(wavelength)<300):

			#If out of range, throw error
			self.outOfRange600.place(relx=0.76,rely=0.94,anchor=tk.CENTER)
			return

		#Clear the error if the wavelength is in correct range
		self.outOfRange600.place_forget()
	####

	####Functionality and communication to Spectrometer.py
	
		#Prepare Gain setting:
		if gain=='AUTO':
			gain=4

		if gain=='1x':
			gain=0

		if gain=='10x':
			gain=1
	 
		if gain=='100x':
			gain=2

		if gain=='1000x':
			gain=3

		#Prepare mirror setting:
		if detector=='Side':
			detector = 's'

		if detector=='Front':
			detector = 'f'

		#Find the desired grating position based on given wavelength input
		if grating=='1800 l/mm (Vis)':
			#Compute the grating step position to park the monochromator
			gratingPos = int(float(wavelength)/0.0041666667)
		elif grating=='600 l/mm (IR)':
			gratingPos = int(float(wavelength)/0.0125)

		#Prepare grating setting:
		if grating=='1800 l/mm (Vis)':
			grating = 'vis'

		if grating=='600 l/mm (IR)':
			grating = 'ir'

		if grating=='1800 l/mm (Vis)':
			#Compute the grating step position to park the monochromator
			gratingPos = int(float(wavelength)/0.0041666667)
		elif grating=='600 l/mm (IR)':
			gratingPos = int(float(wavelength)/0.0125)

		print('Mono is getting prepared for scanning, please wait')
		response = a.setScanGUI('0','0','0',str(intTime),str(int(entSize/12.5)),str(int(extSize/12.5)),str(gain),grating,detector,'3',str(gratingPos),str(incTime),str(totalTime))
		print("Apply Settings Response: ", response)
		if response == 0:
		   self.startButton.configure(state=NORMAL)
		   

	def startScanButton(self):
		#start Scan
		self.lockFeatures()
		self.endButton.config(state=NORMAL)
		self.isScanning = True
		response_start = a.startScan(self.totalTimeSlider.get())

		self.scanning = False

		if response_start == 0:
			#Get and print the data
			self.steps,self.intensities = a.getDataScan(1, True)

			self.unlockFeatures()
			print(self.intensities)
			print(len(self.intensities))

			self.endButton.config(state=DISABLED)
			return

		self.unlockFeatures()
		self.endButton.config(state=DISABLED)


	def startScan_threading(self):
		scanThread = threading.Thread(target=self.startScanButton)
		scanThread.start()

	def endScanButton(self):
		#Used to stop the current time base scan
		endFlag = True
		totalTime = 0
		while endFlag:
			try:
				response_end = a.scanStop()
				endFlag = False
			except serial.serialutil.SerialException:
				   time.sleep(0.001)
		self.unlockFeatures()


#	def endScanButton(self):
#		#Used to stop the current time base scan
#		endFlag = True
#		totalTime = 0
#		while endFlag:
#			try:
#				#response_end = a.scanStop()
#				#print("Total Time: ", totalTime)
#				status = self.reportStatus()
#				if status == 0:
#				   endFlag = False
#				elif status == 3:
#				   #self.lastIntensity = a.getDataScan()[1][-1]
#				   self.intensities = a.getDataScan()[1][0:]
#				#print(self.lastIntensity)
#				print(self.intensities)
#			except serial.serialutil.SerialException:
#				   time.sleep(0.001)
#				   totalTime += 0.001
#		self.unlockFeatures()

	def reportStatus(self):
		status = a.getScanStatus()
		print(status)
		return status

	"""
	def getRealAnimation(self, i):
		xs = []
		ys = []
		print('should be called if animating!!!')
		with open('realTimeData.csv', mode = 'r+') as liveDataFile:
			self.dataRead = liveDataFile.read()
			liveDataFile.close()

		dataLine = self.dataRead.split('\n')
		
		for line in dataLine:
			if len(line) > 1:
				pos, intensity = line.split(',')

				
				positions.append(pos)
				intensityF = float(intensity)
				intensities.append(intensityF)

				#noise filter
				intensities = noiseFilter.movingAverage(intensities, MA_Size = 6, lowerLim = 2050, upperLim = 2200)
	"""

	def startAnimation(self):
		anim = plotbuilder.animatedPlot()
		anim.runAnimate(animTime = self.totalTimeSlider.get()/1000) 
	
	def getReals(self):
		a.getDataFromPos(0, truncateFile = True, live = True)#clear the file for next use
		endFlag = True
		while endFlag:
			lastDataPos = a.getLastDataPos()
			intensity = a.getDataFromPos(lastDataPos, live = True)
			print('intensity:', intensity)

			if a.getScanStatus() == 0:
				endFlag = False
	def getRealButton(self):
		self.getRealData_thread()
		self.startAnimation()	
		

	def getRealData_thread(self):
		getReal = threading.Thread(target=self.getReals)
		getReal.start()
		

	def debugButton2(self):
		a.getScanStatus()
		self.startButton.config(state=NORMAL)

def mainloop_thread():
	app = HR460App()
	app.mainloop()


def main():
	#thread_mainloop = threading.Thread(target = mainloop_thread)
	#thread_mainloop.start()
	print('running2')
	app = HR460App()
	app.mainloop()

	
if __name__ == '__main__':
	print('running')
	main()
