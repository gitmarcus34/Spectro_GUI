# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TimeBaseScanningMenu_Design.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TBSMenu(object):
    def setupUi(self, TBSMenu):
        TBSMenu.setObjectName("TBSMenu")
        TBSMenu.resize(1397, 651)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TBSMenu.sizePolicy().hasHeightForWidth())
        TBSMenu.setSizePolicy(sizePolicy)
        TBSMenu.setMaximumSize(QtCore.QSize(10000, 943))
        font = QtGui.QFont()
        font.setItalic(False)
        TBSMenu.setFont(font)
        self.centralwidget = QtWidgets.QWidget(TBSMenu)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lcdNum_EntranceSlider = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNum_EntranceSlider.setMinimumSize(QtCore.QSize(300, 0))
        self.lcdNum_EntranceSlider.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lcdNum_EntranceSlider.setObjectName("lcdNum_EntranceSlider")
        self.horizontalLayout_3.addWidget(self.lcdNum_EntranceSlider)
        self.micrometer_label1 = QtWidgets.QLabel(self.centralwidget)
        self.micrometer_label1.setObjectName("micrometer_label1")
        self.horizontalLayout_3.addWidget(self.micrometer_label1)
        self.gridLayout_4.addLayout(self.horizontalLayout_3, 4, 2, 1, 1)
        self.TimeIncrementSlider = QtWidgets.QSlider(self.centralwidget)
        self.TimeIncrementSlider.setCursor(QtGui.QCursor(QtCore.Qt.SizeHorCursor))
        self.TimeIncrementSlider.setOrientation(QtCore.Qt.Horizontal)
        self.TimeIncrementSlider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.TimeIncrementSlider.setObjectName("TimeIncrementSlider")
        self.gridLayout_4.addWidget(self.TimeIncrementSlider, 19, 2, 1, 1)
        self.gridLayout_12 = QtWidgets.QGridLayout()
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.lcdNum_IntTimeSlider = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNum_IntTimeSlider.setMinimumSize(QtCore.QSize(300, 0))
        self.lcdNum_IntTimeSlider.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lcdNum_IntTimeSlider.setObjectName("lcdNum_IntTimeSlider")
        self.gridLayout_12.addWidget(self.lcdNum_IntTimeSlider, 0, 0, 1, 1)
        self.millisec_label1 = QtWidgets.QLabel(self.centralwidget)
        self.millisec_label1.setObjectName("millisec_label1")
        self.gridLayout_12.addWidget(self.millisec_label1, 0, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_12, 16, 2, 1, 1)
        self.IntegrationTimeSlider = QtWidgets.QSlider(self.centralwidget)
        self.IntegrationTimeSlider.setCursor(QtGui.QCursor(QtCore.Qt.SizeHorCursor))
        self.IntegrationTimeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.IntegrationTimeSlider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.IntegrationTimeSlider.setObjectName("IntegrationTimeSlider")
        self.gridLayout_4.addWidget(self.IntegrationTimeSlider, 15, 2, 1, 1)
        self.ExitSlit_Label = QtWidgets.QLabel(self.centralwidget)
        self.ExitSlit_Label.setMaximumSize(QtCore.QSize(16777215, 30))
        self.ExitSlit_Label.setObjectName("ExitSlit_Label")
        self.gridLayout_4.addWidget(self.ExitSlit_Label, 5, 2, 1, 1)
        self.gridLayout_16 = QtWidgets.QGridLayout()
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.lcdNum_TotalTimeSlider = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNum_TotalTimeSlider.setMinimumSize(QtCore.QSize(300, 0))
        self.lcdNum_TotalTimeSlider.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lcdNum_TotalTimeSlider.setObjectName("lcdNum_TotalTimeSlider")
        self.gridLayout_16.addWidget(self.lcdNum_TotalTimeSlider, 0, 0, 1, 1)
        self.millisec_label3 = QtWidgets.QLabel(self.centralwidget)
        self.millisec_label3.setObjectName("millisec_label3")
        self.gridLayout_16.addWidget(self.millisec_label3, 0, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_16, 25, 2, 1, 1)
        self.TotalTimeSlider = QtWidgets.QSlider(self.centralwidget)
        self.TotalTimeSlider.setCursor(QtGui.QCursor(QtCore.Qt.SizeHorCursor))
        self.TotalTimeSlider.setMinimum(1)
        self.TotalTimeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.TotalTimeSlider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.TotalTimeSlider.setObjectName("TotalTimeSlider")
        self.gridLayout_4.addWidget(self.TotalTimeSlider, 24, 2, 1, 1)
        self.gridLayout_11 = QtWidgets.QGridLayout()
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.micrometer_label2 = QtWidgets.QLabel(self.centralwidget)
        self.micrometer_label2.setObjectName("micrometer_label2")
        self.gridLayout_11.addWidget(self.micrometer_label2, 0, 1, 1, 1)
        self.lcdNum_ExitSlider = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNum_ExitSlider.setMinimumSize(QtCore.QSize(300, 0))
        self.lcdNum_ExitSlider.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lcdNum_ExitSlider.setObjectName("lcdNum_ExitSlider")
        self.gridLayout_11.addWidget(self.lcdNum_ExitSlider, 0, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_11, 10, 2, 1, 1)
        self.EntanceSlit_Label = QtWidgets.QLabel(self.centralwidget)
        self.EntanceSlit_Label.setMaximumSize(QtCore.QSize(16777215, 30))
        self.EntanceSlit_Label.setObjectName("EntanceSlit_Label")
        self.gridLayout_4.addWidget(self.EntanceSlit_Label, 0, 2, 1, 1)
        self.ExitSlitSlider = QtWidgets.QSlider(self.centralwidget)
        self.ExitSlitSlider.setCursor(QtGui.QCursor(QtCore.Qt.SizeHorCursor))
        self.ExitSlitSlider.setOrientation(QtCore.Qt.Horizontal)
        self.ExitSlitSlider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.ExitSlitSlider.setObjectName("ExitSlitSlider")
        self.gridLayout_4.addWidget(self.ExitSlitSlider, 9, 2, 1, 1)
        self.gridLayout_13 = QtWidgets.QGridLayout()
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.lcdNum_TimeIncrementSlider = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNum_TimeIncrementSlider.setMinimumSize(QtCore.QSize(300, 0))
        self.lcdNum_TimeIncrementSlider.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lcdNum_TimeIncrementSlider.setObjectName("lcdNum_TimeIncrementSlider")
        self.gridLayout_13.addWidget(self.lcdNum_TimeIncrementSlider, 0, 0, 1, 1)
        self.millisec_label2 = QtWidgets.QLabel(self.centralwidget)
        self.millisec_label2.setObjectName("millisec_label2")
        self.gridLayout_13.addWidget(self.millisec_label2, 0, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_13, 21, 2, 1, 1)
        self.EntranceSlitSlider = QtWidgets.QSlider(self.centralwidget)
        self.EntranceSlitSlider.setCursor(QtGui.QCursor(QtCore.Qt.SizeHorCursor))
        self.EntranceSlitSlider.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.EntranceSlitSlider.setOrientation(QtCore.Qt.Horizontal)
        self.EntranceSlitSlider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.EntranceSlitSlider.setObjectName("EntranceSlitSlider")
        self.gridLayout_4.addWidget(self.EntranceSlitSlider, 2, 2, 1, 1)
        self.TimeInc_Lavel = QtWidgets.QLabel(self.centralwidget)
        self.TimeInc_Lavel.setMaximumSize(QtCore.QSize(16777215, 30))
        self.TimeInc_Lavel.setObjectName("TimeInc_Lavel")
        self.gridLayout_4.addWidget(self.TimeInc_Lavel, 18, 2, 1, 1)
        self.IntTime_Label = QtWidgets.QLabel(self.centralwidget)
        self.IntTime_Label.setMaximumSize(QtCore.QSize(16777215, 30))
        self.IntTime_Label.setObjectName("IntTime_Label")
        self.gridLayout_4.addWidget(self.IntTime_Label, 14, 2, 1, 1)
        self.TotalTime_Label = QtWidgets.QLabel(self.centralwidget)
        self.TotalTime_Label.setObjectName("TotalTime_Label")
        self.gridLayout_4.addWidget(self.TotalTime_Label, 23, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 26, 3, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_4, 2, 1, 1, 1)
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.wavelength_input = QtWidgets.QLineEdit(self.centralwidget)
        self.wavelength_input.setMaximumSize(QtCore.QSize(70, 16777215))
        self.wavelength_input.setText("")
        self.wavelength_input.setObjectName("wavelength_input")
        self.gridLayout_9.addWidget(self.wavelength_input, 1, 0, 1, 1)
        self.nanometer_label1 = QtWidgets.QLabel(self.centralwidget)
        self.nanometer_label1.setObjectName("nanometer_label1")
        self.gridLayout_9.addWidget(self.nanometer_label1, 1, 1, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_9, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout_5.addWidget(self.label, 0, 1, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.ApplySettings_Button = QtWidgets.QPushButton(self.centralwidget)
        self.ApplySettings_Button.setMinimumSize(QtCore.QSize(0, 50))
        self.ApplySettings_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ApplySettings_Button.setObjectName("ApplySettings_Button")
        self.horizontalLayout_5.addWidget(self.ApplySettings_Button)
        self.StartScan_Button = QtWidgets.QPushButton(self.centralwidget)
        self.StartScan_Button.setMinimumSize(QtCore.QSize(0, 50))
        self.StartScan_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.StartScan_Button.setObjectName("StartScan_Button")
        self.horizontalLayout_5.addWidget(self.StartScan_Button)
        self.StartRealData_Button = QtWidgets.QPushButton(self.centralwidget)
        self.StartRealData_Button.setMinimumSize(QtCore.QSize(0, 50))
        self.StartRealData_Button.setObjectName("StartRealData_Button")
        self.horizontalLayout_5.addWidget(self.StartRealData_Button)
        self.EndScan_Button = QtWidgets.QPushButton(self.centralwidget)
        self.EndScan_Button.setMinimumSize(QtCore.QSize(0, 50))
        self.EndScan_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.EndScan_Button.setObjectName("EndScan_Button")
        self.horizontalLayout_5.addWidget(self.EndScan_Button)
        self.gridLayout_5.addLayout(self.horizontalLayout_5, 3, 1, 1, 1)
        self.MenuLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Lucida Bright")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.MenuLabel.setFont(font)
        self.MenuLabel.setObjectName("MenuLabel")
        self.gridLayout_5.addWidget(self.MenuLabel, 1, 3, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.ExportPNG_Button = QtWidgets.QPushButton(self.centralwidget)
        self.ExportPNG_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ExportPNG_Button.setObjectName("ExportPNG_Button")
        self.horizontalLayout_6.addWidget(self.ExportPNG_Button)
        self.ExportJPG_Button = QtWidgets.QPushButton(self.centralwidget)
        self.ExportJPG_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ExportJPG_Button.setObjectName("ExportJPG_Button")
        self.horizontalLayout_6.addWidget(self.ExportJPG_Button)
        self.ExportCSV_Button = QtWidgets.QPushButton(self.centralwidget)
        self.ExportCSV_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ExportCSV_Button.setObjectName("ExportCSV_Button")
        self.horizontalLayout_6.addWidget(self.ExportCSV_Button)
        self.PlotOptions_Button = QtWidgets.QPushButton(self.centralwidget)
        self.PlotOptions_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PlotOptions_Button.setObjectName("PlotOptions_Button")
        self.horizontalLayout_6.addWidget(self.PlotOptions_Button)
        self.gridLayout_5.addLayout(self.horizontalLayout_6, 3, 3, 1, 1)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.sub_mdiArea = QtWidgets.QMdiArea(self.centralwidget)
        self.sub_mdiArea.setMaximumSize(QtCore.QSize(1500, 900))
        self.sub_mdiArea.setObjectName("sub_mdiArea")
        self.plot_subwindowA = QtWidgets.QWidget()
        self.plot_subwindowA.setObjectName("plot_subwindowA")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.plot_subwindowA)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.subLayoutA = QtWidgets.QGridLayout()
        self.subLayoutA.setObjectName("subLayoutA")
        self.gridLayout_2.addLayout(self.subLayoutA, 0, 0, 1, 1)
        self.plot_subwindowB = QtWidgets.QWidget()
        self.plot_subwindowB.setObjectName("plot_subwindowB")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.plot_subwindowB)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.subLayoutB = QtWidgets.QGridLayout()
        self.subLayoutB.setObjectName("subLayoutB")
        self.gridLayout_10.addLayout(self.subLayoutB, 0, 0, 1, 1)
        self.plot_subwindowC = QtWidgets.QWidget()
        self.plot_subwindowC.setObjectName("plot_subwindowC")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.plot_subwindowC)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.subLayoutC = QtWidgets.QGridLayout()
        self.subLayoutC.setObjectName("subLayoutC")
        self.gridLayout_15.addLayout(self.subLayoutC, 0, 0, 1, 1)
        self.plot_subwindowD = QtWidgets.QWidget()
        self.plot_subwindowD.setObjectName("plot_subwindowD")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.plot_subwindowD)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.subLayoutD = QtWidgets.QGridLayout()
        self.subLayoutD.setObjectName("subLayoutD")
        self.gridLayout_6.addLayout(self.subLayoutD, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.sub_mdiArea, 0, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.progressBar.setFont(font)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_7.addWidget(self.progressBar, 1, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_7, 2, 3, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("tbsDiagram.jpg"))
        self.label_7.setObjectName("label_7")
        self.verticalLayout_4.addWidget(self.label_7)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.gridLayout_5.addLayout(self.verticalLayout_4, 0, 0, 4, 1)
        TBSMenu.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TBSMenu)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1397, 26))
        self.menubar.setObjectName("menubar")
        self.menuScan = QtWidgets.QMenu(self.menubar)
        self.menuScan.setObjectName("menuScan")
        self.menuMain = QtWidgets.QMenu(self.menubar)
        self.menuMain.setObjectName("menuMain")
        self.menuGain = QtWidgets.QMenu(self.menubar)
        self.menuGain.setObjectName("menuGain")
        self.menuGrating = QtWidgets.QMenu(self.menubar)
        self.menuGrating.setObjectName("menuGrating")
        self.menuDetector = QtWidgets.QMenu(self.menubar)
        self.menuDetector.setObjectName("menuDetector")
        self.menu_SubwindowPlots = QtWidgets.QMenu(self.menubar)
        self.menu_SubwindowPlots.setObjectName("menu_SubwindowPlots")
        TBSMenu.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TBSMenu)
        self.statusbar.setObjectName("statusbar")
        TBSMenu.setStatusBar(self.statusbar)
        self.actionTimeMenu = QtWidgets.QAction(TBSMenu)
        self.actionTimeMenu.setCheckable(True)
        self.actionTimeMenu.setChecked(True)
        self.actionTimeMenu.setEnabled(False)
        self.actionTimeMenu.setObjectName("actionTimeMenu")
        self.actionScanningMenu = QtWidgets.QAction(TBSMenu)
        self.actionScanningMenu.setObjectName("actionScanningMenu")
        self.actionMainMenu = QtWidgets.QAction(TBSMenu)
        self.actionMainMenu.setObjectName("actionMainMenu")
        self.actionAuto = QtWidgets.QAction(TBSMenu)
        self.actionAuto.setCheckable(True)
        self.actionAuto.setChecked(True)
        self.actionAuto.setObjectName("actionAuto")
        self.action1X = QtWidgets.QAction(TBSMenu)
        self.action1X.setCheckable(True)
        self.action1X.setObjectName("action1X")
        self.action10X = QtWidgets.QAction(TBSMenu)
        self.action10X.setCheckable(True)
        self.action10X.setObjectName("action10X")
        self.action100X = QtWidgets.QAction(TBSMenu)
        self.action100X.setCheckable(True)
        self.action100X.setObjectName("action100X")
        self.action1000X = QtWidgets.QAction(TBSMenu)
        self.action1000X.setCheckable(True)
        self.action1000X.setObjectName("action1000X")
        self.actionSide = QtWidgets.QAction(TBSMenu)
        self.actionSide.setCheckable(True)
        self.actionSide.setChecked(True)
        self.actionSide.setObjectName("actionSide")
        self.actionFront = QtWidgets.QAction(TBSMenu)
        self.actionFront.setCheckable(True)
        self.actionFront.setObjectName("actionFront")
        self.action1800Grating = QtWidgets.QAction(TBSMenu)
        self.action1800Grating.setCheckable(True)
        self.action1800Grating.setChecked(True)
        self.action1800Grating.setObjectName("action1800Grating")
        self.action600Grating = QtWidgets.QAction(TBSMenu)
        self.action600Grating.setCheckable(True)
        self.action600Grating.setObjectName("action600Grating")
        self.actionTiled = QtWidgets.QAction(TBSMenu)
        self.actionTiled.setObjectName("actionTiled")
        self.actionCascade = QtWidgets.QAction(TBSMenu)
        self.actionCascade.setObjectName("actionCascade")
        self.actionPlotA = QtWidgets.QAction(TBSMenu)
        self.actionPlotA.setCheckable(True)
        self.actionPlotA.setChecked(True)
        self.actionPlotA.setObjectName("actionPlotA")
        self.actionPlotB = QtWidgets.QAction(TBSMenu)
        self.actionPlotB.setCheckable(True)
        self.actionPlotB.setObjectName("actionPlotB")
        self.actionPlotC = QtWidgets.QAction(TBSMenu)
        self.actionPlotC.setCheckable(True)
        self.actionPlotC.setObjectName("actionPlotC")
        self.actionPlotD = QtWidgets.QAction(TBSMenu)
        self.actionPlotD.setCheckable(True)
        self.actionPlotD.setObjectName("actionPlotD")
        self.menuScan.addAction(self.actionTimeMenu)
        self.menuScan.addAction(self.actionScanningMenu)
        self.menuMain.addAction(self.actionMainMenu)
        self.menuGain.addAction(self.actionAuto)
        self.menuGain.addAction(self.action1X)
        self.menuGain.addAction(self.action10X)
        self.menuGain.addAction(self.action100X)
        self.menuGain.addAction(self.action1000X)
        self.menuGrating.addAction(self.action1800Grating)
        self.menuGrating.addAction(self.action600Grating)
        self.menuDetector.addAction(self.actionSide)
        self.menuDetector.addAction(self.actionFront)
        self.menu_SubwindowPlots.addAction(self.actionTiled)
        self.menu_SubwindowPlots.addAction(self.actionCascade)
        self.menu_SubwindowPlots.addAction(self.actionPlotA)
        self.menu_SubwindowPlots.addAction(self.actionPlotB)
        self.menu_SubwindowPlots.addAction(self.actionPlotC)
        self.menu_SubwindowPlots.addAction(self.actionPlotD)
        self.menubar.addAction(self.menuMain.menuAction())
        self.menubar.addAction(self.menuScan.menuAction())
        self.menubar.addAction(self.menuDetector.menuAction())
        self.menubar.addAction(self.menuGain.menuAction())
        self.menubar.addAction(self.menuGrating.menuAction())
        self.menubar.addAction(self.menu_SubwindowPlots.menuAction())

        self.retranslateUi(TBSMenu)
        QtCore.QMetaObject.connectSlotsByName(TBSMenu)

    def retranslateUi(self, TBSMenu):
        _translate = QtCore.QCoreApplication.translate
        TBSMenu.setWindowTitle(_translate("TBSMenu", "Scanning Menu"))
        self.micrometer_label1.setText(_translate("TBSMenu", "μm"))
        self.millisec_label1.setText(_translate("TBSMenu", "ms"))
        self.ExitSlit_Label.setText(_translate("TBSMenu", "Exit Slit Width"))
        self.millisec_label3.setText(_translate("TBSMenu", "seconds"))
        self.micrometer_label2.setText(_translate("TBSMenu", "μm"))
        self.EntanceSlit_Label.setText(_translate("TBSMenu", "Entrance Slit Width"))
        self.millisec_label2.setText(_translate("TBSMenu", "ms"))
        self.TimeInc_Lavel.setText(_translate("TBSMenu", "Time Increment*"))
        self.IntTime_Label.setText(_translate("TBSMenu", "Integration Time"))
        self.TotalTime_Label.setText(_translate("TBSMenu", "Total Time"))
        self.wavelength_input.setPlaceholderText(_translate("TBSMenu", "300 - 870"))
        self.nanometer_label1.setText(_translate("TBSMenu", "nm"))
        self.label.setText(_translate("TBSMenu", "Wavelength:"))
        self.ApplySettings_Button.setText(_translate("TBSMenu", "Apply Settings"))
        self.StartScan_Button.setText(_translate("TBSMenu", "Start Scan"))
        self.StartRealData_Button.setText(_translate("TBSMenu", "Start Live\n"
"Data Collection"))
        self.EndScan_Button.setText(_translate("TBSMenu", "End Scan"))
        self.MenuLabel.setText(_translate("TBSMenu", "Time Base Scanning"))
        self.ExportPNG_Button.setText(_translate("TBSMenu", "Export PNG"))
        self.ExportJPG_Button.setText(_translate("TBSMenu", "Export JPG"))
        self.ExportCSV_Button.setText(_translate("TBSMenu", "Export CSV"))
        self.PlotOptions_Button.setText(_translate("TBSMenu", "Plot Options"))
        self.plot_subwindowA.setWindowTitle(_translate("TBSMenu", "Subwindow"))
        self.plot_subwindowB.setWindowTitle(_translate("TBSMenu", "Subwindow"))
        self.plot_subwindowC.setWindowTitle(_translate("TBSMenu", "Subwindow"))
        self.plot_subwindowD.setWindowTitle(_translate("TBSMenu", "Subwindow"))
        self.progressBar.setFormat(_translate("TBSMenu", "busy"))
        self.label_4.setText(_translate("TBSMenu", "->\'Time Increment\' is the time between\n"
"integration starts.\n"
"\n"
"->\'Total Time\' is the total length of\n"
"time of the scan.\n"
"\n"
"->Note, the max number of data\n"
"points acquirable is 5000 points where\n"
"Total Time/Time Increment = num data pts."))
        self.label_3.setText(_translate("TBSMenu", "*If \'Time Increment\' is zero then then\n"
" the effective \'Time Increment\' will equal\n"
"the \'Integration Time\' value."))
        self.menuScan.setTitle(_translate("TBSMenu", "Scanning Menus"))
        self.menuMain.setTitle(_translate("TBSMenu", "Main Menu"))
        self.menuGain.setTitle(_translate("TBSMenu", "Gain"))
        self.menuGrating.setTitle(_translate("TBSMenu", "Grating"))
        self.menuDetector.setTitle(_translate("TBSMenu", "Detector"))
        self.menu_SubwindowPlots.setTitle(_translate("TBSMenu", "Subwindow Plots"))
        self.actionTimeMenu.setText(_translate("TBSMenu", "Time Base Scanning"))
        self.actionScanningMenu.setText(_translate("TBSMenu", "Wavelength Scanning"))
        self.actionMainMenu.setText(_translate("TBSMenu", "Main Menu"))
        self.actionAuto.setText(_translate("TBSMenu", "AUTO"))
        self.action1X.setText(_translate("TBSMenu", "1X"))
        self.action10X.setText(_translate("TBSMenu", "10X"))
        self.action100X.setText(_translate("TBSMenu", "100X"))
        self.action1000X.setText(_translate("TBSMenu", "1000X"))
        self.actionSide.setText(_translate("TBSMenu", "Side"))
        self.actionFront.setText(_translate("TBSMenu", "Front"))
        self.action1800Grating.setText(_translate("TBSMenu", "1800 l/mm (Vis)"))
        self.action600Grating.setText(_translate("TBSMenu", "600 l/mm (IR)"))
        self.actionTiled.setText(_translate("TBSMenu", "tiled"))
        self.actionCascade.setText(_translate("TBSMenu", "cascade"))
        self.actionPlotA.setText(_translate("TBSMenu", "add/view/set PlotA"))
        self.actionPlotB.setText(_translate("TBSMenu", "add/view/set PlotB"))
        self.actionPlotC.setText(_translate("TBSMenu", "add/view/set PlotC"))
        self.actionPlotD.setText(_translate("TBSMenu", "add/view/set PlotD"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TBSMenu = QtWidgets.QMainWindow()
    ui = Ui_TBSMenu()
    ui.setupUi(TBSMenu)
    TBSMenu.show()
    sys.exit(app.exec_())
