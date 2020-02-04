# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StartUpMenu_Design.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_StartUp_Menu(object):
    def setupUi(self, StartUp_Menu):
        StartUp_Menu.setObjectName("StartUp_Menu")
        StartUp_Menu.resize(903, 550)
        StartUp_Menu.setMinimumSize(QtCore.QSize(903, 550))
        StartUp_Menu.setMaximumSize(QtCore.QSize(900, 550))
        self.centralwidget = QtWidgets.QWidget(StartUp_Menu)
        self.centralwidget.setObjectName("centralwidget")
        self.MainMenu_Button = QtWidgets.QPushButton(self.centralwidget)
        self.MainMenu_Button.setGeometry(QtCore.QRect(370, 220, 171, 51))
        self.MainMenu_Button.setObjectName("MainMenu_Button")
        self.Initialize_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Initialize_Button.setGeometry(QtCore.QRect(370, 140, 171, 51))
        self.Initialize_Button.setObjectName("Initialize_Button")
        self.slide1_background = QtWidgets.QLabel(self.centralwidget)
        self.slide1_background.setGeometry(QtCore.QRect(-10, -50, 911, 561))
        self.slide1_background.setAutoFillBackground(False)
        self.slide1_background.setText("")
        self.slide1_background.setPixmap(QtGui.QPixmap("StartUpMenu_background.jpeg"))
        self.slide1_background.setScaledContents(False)
        self.slide1_background.setObjectName("slide1_background")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(300, 450, 371, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.slide1_background.raise_()
        self.MainMenu_Button.raise_()
        self.Initialize_Button.raise_()
        self.progressBar.raise_()
        StartUp_Menu.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(StartUp_Menu)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 903, 26))
        self.menubar.setObjectName("menubar")
        self.menustartUp = QtWidgets.QMenu(self.menubar)
        self.menustartUp.setObjectName("menustartUp")
        StartUp_Menu.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(StartUp_Menu)
        self.statusbar.setObjectName("statusbar")
        StartUp_Menu.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(StartUp_Menu)
        self.toolBar.setObjectName("toolBar")
        StartUp_Menu.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionMainMenu = QtWidgets.QAction(StartUp_Menu)
        self.actionMainMenu.setObjectName("actionMainMenu")
        self.actionInformation = QtWidgets.QAction(StartUp_Menu)
        self.actionInformation.setObjectName("actionInformation")
        self.menustartUp.addAction(self.actionMainMenu)
        self.menustartUp.addAction(self.actionInformation)
        self.menubar.addAction(self.menustartUp.menuAction())

        self.retranslateUi(StartUp_Menu)
        QtCore.QMetaObject.connectSlotsByName(StartUp_Menu)

    def retranslateUi(self, StartUp_Menu):
        _translate = QtCore.QCoreApplication.translate
        StartUp_Menu.setWindowTitle(_translate("StartUp_Menu", "MainWindow"))
        self.MainMenu_Button.setText(_translate("StartUp_Menu", "Main Menu"))
        self.Initialize_Button.setText(_translate("StartUp_Menu", "Initialize"))
        self.menustartUp.setTitle(_translate("StartUp_Menu", "startUp"))
        self.toolBar.setWindowTitle(_translate("StartUp_Menu", "toolBar"))
        self.actionMainMenu.setText(_translate("StartUp_Menu", "MainMenu"))
        self.actionInformation.setText(_translate("StartUp_Menu", "Information"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StartUp_Menu = QtWidgets.QMainWindow()
    ui = Ui_StartUp_Menu()
    ui.setupUi(StartUp_Menu)
    StartUp_Menu.show()
    sys.exit(app.exec_())
