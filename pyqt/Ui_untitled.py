# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\项目文件\电赛\2022_dians_E\pyqt\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
# import sys 
# sys.path.append("..") 
# import test
# from GCC_Method import test
print(__name__)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 600)
        MainWindow.setMinimumSize(QtCore.QSize(1024, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(580, 130, 121, 51))
        self.pushButton.setObjectName("pushButton")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(580, 10, 131, 71))
        font = QtGui.QFont()
        font.setFamily("Adobe Heiti Std")
        font.setPointSize(24)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.graphicsView = PlotWidget(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(10, 10, 521, 231))
        self.graphicsView.setObjectName("graphicsView")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(740, 130, 131, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.graphicsView_2 = PlotWidget(self.centralwidget)
        self.graphicsView_2.setGeometry(QtCore.QRect(10, 250, 521, 251))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.graphicsView_3 = PlotWidget(self.centralwidget)
        self.graphicsView_3.setGeometry(QtCore.QRect(540, 200, 471, 301))
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(760, 10, 141, 71))
        font = QtGui.QFont()
        font.setFamily("Adobe Heiti Std")
        font.setPointSize(24)
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.setObjectName("textBrowser_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "启动"))
        self.pushButton_2.setText(_translate("MainWindow", "停止"))
from pyqtgraph import PlotWidget
