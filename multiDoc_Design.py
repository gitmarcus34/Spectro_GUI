# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'multiDocUIDesign.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CoreWindow(object):
	def setupUi(self, CoreWindow):
		CoreWindow.setObjectName("CoreWindow")
		CoreWindow.resize(1273, 881)
		self.centralwidget = QtWidgets.QWidget(CoreWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
		self.gridLayout_2.setObjectName("gridLayout_2")
		self.gridLayout = QtWidgets.QGridLayout()
		self.gridLayout.setObjectName("gridLayout")
		self.mdiArea = QtWidgets.QMdiArea(self.centralwidget)
		self.mdiArea.setObjectName("mdiArea")
		self.gridLayout.addWidget(self.mdiArea, 0, 0, 1, 1)
		self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
		CoreWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(CoreWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 1273, 26))
		self.menubar.setObjectName("menubar")
		self.menufiles = QtWidgets.QMenu(self.menubar)
		self.menufiles.setObjectName("menufiles")
		CoreWindow.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(CoreWindow)
		self.statusbar.setObjectName("statusbar")
		CoreWindow.setStatusBar(self.statusbar)
		self.actionstart = QtWidgets.QAction(CoreWindow)
		self.actionstart.setObjectName("actionstart")
		self.actioncascade = QtWidgets.QAction(CoreWindow)
		self.actioncascade.setObjectName("actioncascade")
		self.actiontiled = QtWidgets.QAction(CoreWindow)
		self.actiontiled.setObjectName("actiontiled")
		self.menufiles.addAction(self.actionstart)
		self.menufiles.addAction(self.actioncascade)
		self.menufiles.addAction(self.actiontiled)
		self.menubar.addAction(self.menufiles.menuAction())

		self.retranslateUi(CoreWindow)
		QtCore.QMetaObject.connectSlotsByName(CoreWindow)

	def retranslateUi(self, CoreWindow):
		_translate = QtCore.QCoreApplication.translate
		CoreWindow.setWindowTitle(_translate("CoreWindow", "CoreWindow"))
		self.menufiles.setTitle(_translate("CoreWindow", "files"))
		self.actionstart.setText(_translate("CoreWindow", "Start "))
		self.actioncascade.setText(_translate("CoreWindow", "cascade"))
		self.actiontiled.setText(_translate("CoreWindow", "tiled"))


if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	CoreWindow = QtWidgets.QMainWindow()
	ui = Ui_CoreWindow()
	ui.setupUi(CoreWindow)
	CoreWindow.show()
	sys.exit(app.exec_())
