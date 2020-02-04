# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainMenu_Design.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainMenu(object):
    def setupUi(self, MainMenu):
        MainMenu.setObjectName("MainMenu")
        MainMenu.resize(830, 663)
        MainMenu.setMinimumSize(QtCore.QSize(830, 0))
        MainMenu.setMaximumSize(QtCore.QSize(1000, 901))
        MainMenu.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.gridLayout_3 = QtWidgets.QGridLayout(MainMenu)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.spectroPicA = QtWidgets.QLabel(MainMenu)
        self.spectroPicA.setText("")
        self.spectroPicA.setPixmap(QtGui.QPixmap("MainMenu_pic2.png"))
        self.spectroPicA.setObjectName("spectroPicA")
        self.verticalLayout.addWidget(self.spectroPicA)
        self.SpectroPicB = QtWidgets.QLabel(MainMenu)
        self.SpectroPicB.setText("")
        self.SpectroPicB.setPixmap(QtGui.QPixmap("MainMenu_pic1.png"))
        self.SpectroPicB.setObjectName("SpectroPicB")
        self.verticalLayout.addWidget(self.SpectroPicB)
        self.gridLayout_3.addLayout(self.verticalLayout, 0, 1, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.fillerLabel2 = QtWidgets.QLabel(MainMenu)
        self.fillerLabel2.setStyleSheet("\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.18408 rgba(0, 0, 0, 97), stop:1 rgba(255, 255, 255, 255));")
        self.fillerLabel2.setText("")
        self.fillerLabel2.setObjectName("fillerLabel2")
        self.gridLayout_2.addWidget(self.fillerLabel2, 3, 2, 1, 1)
        self.ToolControlMenu_Button = QtWidgets.QPushButton(MainMenu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ToolControlMenu_Button.sizePolicy().hasHeightForWidth())
        self.ToolControlMenu_Button.setSizePolicy(sizePolicy)
        self.ToolControlMenu_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ToolControlMenu_Button.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 240, 114), stop:1 rgba(255, 255, 255, 255));")
        self.ToolControlMenu_Button.setObjectName("ToolControlMenu_Button")
        self.gridLayout_2.addWidget(self.ToolControlMenu_Button, 4, 2, 1, 1)
        self.InformationMenu_Button = QtWidgets.QPushButton(MainMenu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.InformationMenu_Button.sizePolicy().hasHeightForWidth())
        self.InformationMenu_Button.setSizePolicy(sizePolicy)
        self.InformationMenu_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.InformationMenu_Button.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(240, 0, 0, 114), stop:1 rgba(255, 255, 255, 255));\n"
"")
        self.InformationMenu_Button.setObjectName("InformationMenu_Button")
        self.gridLayout_2.addWidget(self.InformationMenu_Button, 0, 2, 1, 1)
        self.ScanningMenu_Button = QtWidgets.QPushButton(MainMenu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ScanningMenu_Button.sizePolicy().hasHeightForWidth())
        self.ScanningMenu_Button.setSizePolicy(sizePolicy)
        self.ScanningMenu_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ScanningMenu_Button.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 240, 0, 114), stop:1 rgba(255, 255, 255, 255));")
        self.ScanningMenu_Button.setObjectName("ScanningMenu_Button")
        self.gridLayout_2.addWidget(self.ScanningMenu_Button, 2, 2, 1, 1)
        self.fillerLabel1 = QtWidgets.QLabel(MainMenu)
        self.fillerLabel1.setStyleSheet("\n"
"\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.18408 rgba(0, 0, 0, 97), stop:1 rgba(255, 255, 255, 255));")
        self.fillerLabel1.setText("")
        self.fillerLabel1.setObjectName("fillerLabel1")
        self.gridLayout_2.addWidget(self.fillerLabel1, 1, 2, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.retranslateUi(MainMenu)
        QtCore.QMetaObject.connectSlotsByName(MainMenu)

    def retranslateUi(self, MainMenu):
        _translate = QtCore.QCoreApplication.translate
        MainMenu.setWindowTitle(_translate("MainMenu", "Form"))
        self.ToolControlMenu_Button.setText(_translate("MainMenu", "Tool Control"))
        self.InformationMenu_Button.setText(_translate("MainMenu", "Information"))
        self.ScanningMenu_Button.setText(_translate("MainMenu", "Scanning"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainMenu = QtWidgets.QWidget()
    ui = Ui_MainMenu()
    ui.setupUi(MainMenu)
    MainMenu.show()
    sys.exit(app.exec_())
