# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ScanningMenu_Design.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ScanningMenu(object):
    def setupUi(self, ScanningMenu):
        ScanningMenu.setObjectName("ScanningMenu")
        ScanningMenu.resize(1073, 730)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ScanningMenu.sizePolicy().hasHeightForWidth())
        ScanningMenu.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(ScanningMenu)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName("gridLayout_5")
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
        self.gridLayout_5.addLayout(self.horizontalLayout_6, 3, 2, 1, 1)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.sub_mdiArea = QtWidgets.QMdiArea(self.centralwidget)
        self.sub_mdiArea.setMaximumSize(QtCore.QSize(1100, 900))
        self.sub_mdiArea.setObjectName("sub_mdiArea")
        self.plot_subwindowA = QtWidgets.QWidget()
        self.plot_subwindowA.setObjectName("plot_subwindowA")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.plot_subwindowA)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.subLayoutA = QtWidgets.QGridLayout()
        self.subLayoutA.setObjectName("subLayoutA")
        self.gridLayout_8.addLayout(self.subLayoutA, 0, 0, 1, 1)
        self.plot_subwindowB = QtWidgets.QWidget()
        self.plot_subwindowB.setObjectName("plot_subwindowB")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.plot_subwindowB)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.subLayoutB = QtWidgets.QGridLayout()
        self.subLayoutB.setObjectName("subLayoutB")
        self.gridLayout_10.addLayout(self.subLayoutB, 0, 0, 1, 1)
        self.plot_subwindowC = QtWidgets.QWidget()
        self.plot_subwindowC.setObjectName("plot_subwindowC")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.plot_subwindowC)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.subLayoutC = QtWidgets.QGridLayout()
        self.subLayoutC.setObjectName("subLayoutC")
        self.gridLayout_12.addLayout(self.subLayoutC, 0, 0, 1, 1)
        self.plot_subwindowD = QtWidgets.QWidget()
        self.plot_subwindowD.setObjectName("plot_subwindowD")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.plot_subwindowD)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.subLayoutD = QtWidgets.QGridLayout()
        self.subLayoutD.setObjectName("subLayoutD")
        self.gridLayout_14.addLayout(self.subLayoutD, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.sub_mdiArea, 0, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.progressBar.setFont(font)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_7.addWidget(self.progressBar, 1, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_7, 2, 2, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.StepSize_Label = QtWidgets.QLabel(self.centralwidget)
        self.StepSize_Label.setMaximumSize(QtCore.QSize(16777215, 30))
        self.StepSize_Label.setObjectName("StepSize_Label")
        self.gridLayout_4.addWidget(self.StepSize_Label, 18, 2, 1, 1)
        self.ExitSlitSlider = QtWidgets.QSlider(self.centralwidget)
        self.ExitSlitSlider.setCursor(QtGui.QCursor(QtCore.Qt.SizeHorCursor))
        self.ExitSlitSlider.setOrientation(QtCore.Qt.Horizontal)
        self.ExitSlitSlider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.ExitSlitSlider.setObjectName("ExitSlitSlider")
        self.gridLayout_4.addWidget(self.ExitSlitSlider, 9, 2, 1, 1)
        self.ExitSlit_Label = QtWidgets.QLabel(self.centralwidget)
        self.ExitSlit_Label.setMaximumSize(QtCore.QSize(16777215, 30))
        self.ExitSlit_Label.setObjectName("ExitSlit_Label")
        self.gridLayout_4.addWidget(self.ExitSlit_Label, 5, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 22, 3, 1, 1)
        self.EntranceSlitSlider = QtWidgets.QSlider(self.centralwidget)
        self.EntranceSlitSlider.setCursor(QtGui.QCursor(QtCore.Qt.SizeHorCursor))
        self.EntranceSlitSlider.setOrientation(QtCore.Qt.Horizontal)
        self.EntranceSlitSlider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.EntranceSlitSlider.setObjectName("EntranceSlitSlider")
        self.gridLayout_4.addWidget(self.EntranceSlitSlider, 2, 2, 1, 1)
        self.IntTime_Label = QtWidgets.QLabel(self.centralwidget)
        self.IntTime_Label.setMaximumSize(QtCore.QSize(16777215, 30))
        self.IntTime_Label.setObjectName("IntTime_Label")
        self.gridLayout_4.addWidget(self.IntTime_Label, 14, 2, 1, 1)
        self.StepSizeSlider = QtWidgets.QSlider(self.centralwidget)
        self.StepSizeSlider.setCursor(QtGui.QCursor(QtCore.Qt.SizeHorCursor))
        self.StepSizeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.StepSizeSlider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.StepSizeSlider.setObjectName("StepSizeSlider")
        self.gridLayout_4.addWidget(self.StepSizeSlider, 19, 2, 1, 1)
        self.IntegrationTimeSlider = QtWidgets.QSlider(self.centralwidget)
        self.IntegrationTimeSlider.setCursor(QtGui.QCursor(QtCore.Qt.SizeHorCursor))
        self.IntegrationTimeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.IntegrationTimeSlider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.IntegrationTimeSlider.setObjectName("IntegrationTimeSlider")
        self.gridLayout_4.addWidget(self.IntegrationTimeSlider, 15, 2, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lcdNum_ExitSlider = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNum_ExitSlider.setMinimumSize(QtCore.QSize(300, 0))
        self.lcdNum_ExitSlider.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lcdNum_ExitSlider.setDigitCount(10)
        self.lcdNum_ExitSlider.setObjectName("lcdNum_ExitSlider")
        self.gridLayout.addWidget(self.lcdNum_ExitSlider, 0, 0, 1, 1)
        self.micrometer_label2 = QtWidgets.QLabel(self.centralwidget)
        self.micrometer_label2.setObjectName("micrometer_label2")
        self.gridLayout.addWidget(self.micrometer_label2, 0, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout, 10, 2, 1, 1)
        self.EntanceSlit_Label = QtWidgets.QLabel(self.centralwidget)
        self.EntanceSlit_Label.setMaximumSize(QtCore.QSize(16777215, 30))
        self.EntanceSlit_Label.setObjectName("EntanceSlit_Label")
        self.gridLayout_4.addWidget(self.EntanceSlit_Label, 0, 2, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lcdNum_EntranceSlider = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNum_EntranceSlider.setMinimumSize(QtCore.QSize(300, 0))
        self.lcdNum_EntranceSlider.setMaximumSize(QtCore.QSize(280, 16777215))
        self.lcdNum_EntranceSlider.setDigitCount(10)
        self.lcdNum_EntranceSlider.setObjectName("lcdNum_EntranceSlider")
        self.horizontalLayout_3.addWidget(self.lcdNum_EntranceSlider)
        self.micrometer_label1 = QtWidgets.QLabel(self.centralwidget)
        self.micrometer_label1.setObjectName("micrometer_label1")
        self.horizontalLayout_3.addWidget(self.micrometer_label1)
        self.gridLayout_4.addLayout(self.horizontalLayout_3, 4, 2, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lcdNum_IntTimeSlider = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNum_IntTimeSlider.setMinimumSize(QtCore.QSize(300, 0))
        self.lcdNum_IntTimeSlider.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lcdNum_IntTimeSlider.setDigitCount(10)
        self.lcdNum_IntTimeSlider.setObjectName("lcdNum_IntTimeSlider")
        self.gridLayout_2.addWidget(self.lcdNum_IntTimeSlider, 0, 0, 1, 1)
        self.millisec_label1 = QtWidgets.QLabel(self.centralwidget)
        self.millisec_label1.setObjectName("millisec_label1")
        self.gridLayout_2.addWidget(self.millisec_label1, 0, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_2, 16, 2, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lcdNum_StepSizeSlider = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNum_StepSizeSlider.setMinimumSize(QtCore.QSize(300, 0))
        self.lcdNum_StepSizeSlider.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lcdNum_StepSizeSlider.setSmallDecimalPoint(False)
        self.lcdNum_StepSizeSlider.setDigitCount(10)
        self.lcdNum_StepSizeSlider.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNum_StepSizeSlider.setProperty("value", 0.0)
        self.lcdNum_StepSizeSlider.setProperty("intValue", 0)
        self.lcdNum_StepSizeSlider.setObjectName("lcdNum_StepSizeSlider")
        self.gridLayout_3.addWidget(self.lcdNum_StepSizeSlider, 0, 0, 1, 1)
        self.nanometer_label3 = QtWidgets.QLabel(self.centralwidget)
        self.nanometer_label3.setObjectName("nanometer_label3")
        self.gridLayout_3.addWidget(self.nanometer_label3, 0, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 20, 2, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_4, 2, 0, 1, 1)
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.to_label = QtWidgets.QLabel(self.centralwidget)
        self.to_label.setObjectName("to_label")
        self.gridLayout_9.addWidget(self.to_label, 1, 3, 1, 1)
        self.fro_label = QtWidgets.QLabel(self.centralwidget)
        self.fro_label.setObjectName("fro_label")
        self.gridLayout_9.addWidget(self.fro_label, 1, 0, 1, 1)
        self.lowerWavelength_input = QtWidgets.QLineEdit(self.centralwidget)
        self.lowerWavelength_input.setText("")
        self.lowerWavelength_input.setObjectName("lowerWavelength_input")
        self.gridLayout_9.addWidget(self.lowerWavelength_input, 1, 1, 1, 1)
        self.nanometer_label1 = QtWidgets.QLabel(self.centralwidget)
        self.nanometer_label1.setObjectName("nanometer_label1")
        self.gridLayout_9.addWidget(self.nanometer_label1, 1, 2, 1, 1)
        self.upperWavelength_input = QtWidgets.QLineEdit(self.centralwidget)
        self.upperWavelength_input.setText("")
        self.upperWavelength_input.setObjectName("upperWavelength_input")
        self.gridLayout_9.addWidget(self.upperWavelength_input, 1, 4, 1, 1)
        self.nanometer_label2 = QtWidgets.QLabel(self.centralwidget)
        self.nanometer_label2.setObjectName("nanometer_label2")
        self.gridLayout_9.addWidget(self.nanometer_label2, 1, 5, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_9, 1, 0, 1, 1)
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
        self.EndScan_Button = QtWidgets.QPushButton(self.centralwidget)
        self.EndScan_Button.setMinimumSize(QtCore.QSize(0, 50))
        self.EndScan_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.EndScan_Button.setObjectName("EndScan_Button")
        self.horizontalLayout_5.addWidget(self.EndScan_Button)
        self.gridLayout_5.addLayout(self.horizontalLayout_5, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout_5.addWidget(self.label, 0, 0, 1, 1)
        self.MenuLabel = QtWidgets.QLabel(self.centralwidget)
        self.MenuLabel.setMaximumSize(QtCore.QSize(1500, 900))
        font = QtGui.QFont()
        font.setFamily("Lucida Bright")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.MenuLabel.setFont(font)
        self.MenuLabel.setObjectName("MenuLabel")
        self.gridLayout_5.addWidget(self.MenuLabel, 1, 2, 1, 1)
        ScanningMenu.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ScanningMenu)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1073, 26))
        self.menubar.setObjectName("menubar")
        self.menuScan = QtWidgets.QMenu(self.menubar)
        self.menuScan.setObjectName("menuScan")
        self.menuMain = QtWidgets.QMenu(self.menubar)
        self.menuMain.setObjectName("menuMain")
        self.menuDetector = QtWidgets.QMenu(self.menubar)
        self.menuDetector.setObjectName("menuDetector")
        self.menuGain = QtWidgets.QMenu(self.menubar)
        self.menuGain.setObjectName("menuGain")
        self.menuGrating = QtWidgets.QMenu(self.menubar)
        self.menuGrating.setObjectName("menuGrating")
        self.menu_SubwindowPlots = QtWidgets.QMenu(self.menubar)
        self.menu_SubwindowPlots.setObjectName("menu_SubwindowPlots")
        ScanningMenu.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ScanningMenu)
        self.statusbar.setObjectName("statusbar")
        ScanningMenu.setStatusBar(self.statusbar)
        self.actionTimeMenu = QtWidgets.QAction(ScanningMenu)
        self.actionTimeMenu.setEnabled(True)
        self.actionTimeMenu.setObjectName("actionTimeMenu")
        self.actionWavelengthMenu = QtWidgets.QAction(ScanningMenu)
        self.actionWavelengthMenu.setCheckable(True)
        self.actionWavelengthMenu.setChecked(True)
        self.actionWavelengthMenu.setEnabled(False)
        self.actionWavelengthMenu.setObjectName("actionWavelengthMenu")
        self.actionMainMenu = QtWidgets.QAction(ScanningMenu)
        self.actionMainMenu.setObjectName("actionMainMenu")
        self.actionSide = QtWidgets.QAction(ScanningMenu)
        self.actionSide.setCheckable(True)
        self.actionSide.setChecked(True)
        self.actionSide.setObjectName("actionSide")
        self.actionFront = QtWidgets.QAction(ScanningMenu)
        self.actionFront.setCheckable(True)
        self.actionFront.setObjectName("actionFront")
        self.actionAuto = QtWidgets.QAction(ScanningMenu)
        self.actionAuto.setCheckable(True)
        self.actionAuto.setChecked(True)
        self.actionAuto.setObjectName("actionAuto")
        self.action1X = QtWidgets.QAction(ScanningMenu)
        self.action1X.setCheckable(True)
        self.action1X.setObjectName("action1X")
        self.action10X = QtWidgets.QAction(ScanningMenu)
        self.action10X.setCheckable(True)
        self.action10X.setObjectName("action10X")
        self.action100X = QtWidgets.QAction(ScanningMenu)
        self.action100X.setCheckable(True)
        self.action100X.setObjectName("action100X")
        self.action1000X = QtWidgets.QAction(ScanningMenu)
        self.action1000X.setCheckable(True)
        self.action1000X.setObjectName("action1000X")
        self.action1800Grating = QtWidgets.QAction(ScanningMenu)
        self.action1800Grating.setCheckable(True)
        self.action1800Grating.setChecked(True)
        self.action1800Grating.setObjectName("action1800Grating")
        self.action600Grating = QtWidgets.QAction(ScanningMenu)
        self.action600Grating.setCheckable(True)
        self.action600Grating.setObjectName("action600Grating")
        self.actionTiled = QtWidgets.QAction(ScanningMenu)
        self.actionTiled.setObjectName("actionTiled")
        self.actionCascade = QtWidgets.QAction(ScanningMenu)
        self.actionCascade.setObjectName("actionCascade")
        self.actionPlotA = QtWidgets.QAction(ScanningMenu)
        self.actionPlotA.setCheckable(True)
        self.actionPlotA.setChecked(True)
        self.actionPlotA.setObjectName("actionPlotA")
        self.actionPlotB = QtWidgets.QAction(ScanningMenu)
        self.actionPlotB.setCheckable(True)
        self.actionPlotB.setObjectName("actionPlotB")
        self.actionPlotC = QtWidgets.QAction(ScanningMenu)
        self.actionPlotC.setCheckable(True)
        self.actionPlotC.setObjectName("actionPlotC")
        self.actionPlotD = QtWidgets.QAction(ScanningMenu)
        self.actionPlotD.setCheckable(True)
        self.actionPlotD.setObjectName("actionPlotD")
        self.menuScan.addAction(self.actionTimeMenu)
        self.menuScan.addAction(self.actionWavelengthMenu)
        self.menuMain.addAction(self.actionMainMenu)
        self.menuDetector.addAction(self.actionSide)
        self.menuDetector.addAction(self.actionFront)
        self.menuGain.addAction(self.actionAuto)
        self.menuGain.addAction(self.action1X)
        self.menuGain.addAction(self.action10X)
        self.menuGain.addAction(self.action100X)
        self.menuGain.addAction(self.action1000X)
        self.menuGrating.addAction(self.action1800Grating)
        self.menuGrating.addAction(self.action600Grating)
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

        self.retranslateUi(ScanningMenu)
        QtCore.QMetaObject.connectSlotsByName(ScanningMenu)

    def retranslateUi(self, ScanningMenu):
        _translate = QtCore.QCoreApplication.translate
        ScanningMenu.setWindowTitle(_translate("ScanningMenu", "Scanning Menu"))
        self.ExportPNG_Button.setText(_translate("ScanningMenu", "Export Plot: PNG"))
        self.ExportJPG_Button.setText(_translate("ScanningMenu", "Export Plot: JPG"))
        self.ExportCSV_Button.setText(_translate("ScanningMenu", "Export Data: CSV"))
        self.PlotOptions_Button.setText(_translate("ScanningMenu", "Plot Options"))
        self.plot_subwindowA.setWindowTitle(_translate("ScanningMenu", "Subwindow"))
        self.plot_subwindowB.setWindowTitle(_translate("ScanningMenu", "Subwindow"))
        self.plot_subwindowC.setWindowTitle(_translate("ScanningMenu", "Subwindow"))
        self.plot_subwindowD.setWindowTitle(_translate("ScanningMenu", "Subwindow"))
        self.progressBar.setFormat(_translate("ScanningMenu", "Busy"))
        self.StepSize_Label.setText(_translate("ScanningMenu", "Step Size"))
        self.ExitSlit_Label.setText(_translate("ScanningMenu", "Exit Slit Width"))
        self.IntTime_Label.setText(_translate("ScanningMenu", "Integration Time"))
        self.micrometer_label2.setText(_translate("ScanningMenu", "μm"))
        self.EntanceSlit_Label.setText(_translate("ScanningMenu", "Entrance Slit Width"))
        self.micrometer_label1.setText(_translate("ScanningMenu", "μm"))
        self.millisec_label1.setText(_translate("ScanningMenu", "ms"))
        self.nanometer_label3.setText(_translate("ScanningMenu", "nm"))
        self.to_label.setText(_translate("ScanningMenu", "To:"))
        self.fro_label.setText(_translate("ScanningMenu", "From:"))
        self.lowerWavelength_input.setPlaceholderText(_translate("ScanningMenu", "300"))
        self.nanometer_label1.setText(_translate("ScanningMenu", "nm"))
        self.upperWavelength_input.setPlaceholderText(_translate("ScanningMenu", "870"))
        self.nanometer_label2.setText(_translate("ScanningMenu", "nm"))
        self.ApplySettings_Button.setText(_translate("ScanningMenu", "Apply Settings"))
        self.StartScan_Button.setText(_translate("ScanningMenu", "Start Scan"))
        self.EndScan_Button.setText(_translate("ScanningMenu", "End Scan"))
        self.label.setText(_translate("ScanningMenu", "Wavelength Range:"))
        self.MenuLabel.setText(_translate("ScanningMenu", "Wavelength Scanning"))
        self.menuScan.setTitle(_translate("ScanningMenu", "Scanning Menus"))
        self.menuMain.setTitle(_translate("ScanningMenu", "Main Menu"))
        self.menuDetector.setTitle(_translate("ScanningMenu", "Detector"))
        self.menuGain.setTitle(_translate("ScanningMenu", "Gain"))
        self.menuGrating.setTitle(_translate("ScanningMenu", "Grating"))
        self.menu_SubwindowPlots.setTitle(_translate("ScanningMenu", "Subwindow Plots"))
        self.actionTimeMenu.setText(_translate("ScanningMenu", "Time Base Scanning"))
        self.actionWavelengthMenu.setText(_translate("ScanningMenu", "Wavelength Scanning"))
        self.actionMainMenu.setText(_translate("ScanningMenu", "Main Menu"))
        self.actionSide.setText(_translate("ScanningMenu", "Side"))
        self.actionFront.setText(_translate("ScanningMenu", "Front"))
        self.actionAuto.setText(_translate("ScanningMenu", "AUTO"))
        self.action1X.setText(_translate("ScanningMenu", "1X"))
        self.action10X.setText(_translate("ScanningMenu", "10X"))
        self.action100X.setText(_translate("ScanningMenu", "100X"))
        self.action1000X.setText(_translate("ScanningMenu", "1000X"))
        self.action1800Grating.setText(_translate("ScanningMenu", "1800 l/mm (Vis)"))
        self.action600Grating.setText(_translate("ScanningMenu", "600 l/mm (IR)"))
        self.actionTiled.setText(_translate("ScanningMenu", "tiled"))
        self.actionCascade.setText(_translate("ScanningMenu", "cascade"))
        self.actionPlotA.setText(_translate("ScanningMenu", "add/view/set plotA"))
        self.actionPlotB.setText(_translate("ScanningMenu", "add/view/set plotB"))
        self.actionPlotC.setText(_translate("ScanningMenu", "add/view/set plotC"))
        self.actionPlotD.setText(_translate("ScanningMenu", "add/view/set plotB"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ScanningMenu = QtWidgets.QMainWindow()
    ui = Ui_ScanningMenu()
    ui.setupUi(ScanningMenu)
    ScanningMenu.show()
    sys.exit(app.exec_())
