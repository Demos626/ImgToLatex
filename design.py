# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Project\diplom\bin\design.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(658, 656)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(600, 400))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter_2 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.layoutWidget = QtWidgets.QWidget(self.splitter_2)
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.image_path = QtWidgets.QLineEdit(self.layoutWidget)
        self.image_path.setText("")
        self.image_path.setObjectName("image_path")
        self.horizontalLayout.addWidget(self.image_path)
        self.find = QtWidgets.QPushButton(self.layoutWidget)
        self.find.setObjectName("find")
        self.horizontalLayout.addWidget(self.find)
        self.load = QtWidgets.QPushButton(self.splitter_2)
        self.load.setMaximumSize(QtCore.QSize(100, 50))
        self.load.setObjectName("load")
        self.verticalLayout.addWidget(self.splitter_2)
        self.image = PlotWidget(self.centralwidget)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        self.image.setBackgroundBrush(brush)
        self.image.setObjectName("image")
        self.verticalLayout.addWidget(self.image)
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.trash = SpinBox(self.splitter)
        self.trash.setMaximumSize(QtCore.QSize(100, 16777215))
        self.trash.setAlignment(QtCore.Qt.AlignCenter)
        self.trash.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.trash.setMinimum(0)
        self.trash.setMaximum(1)
        self.trash.setProperty("value", 0)
        self.trash.setObjectName("trash")
        self.go = QtWidgets.QPushButton(self.splitter)
        self.go.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.go.setObjectName("go")
        self.verticalLayout.addWidget(self.splitter)
        self.formula = QtWidgets.QLineEdit(self.centralwidget)
        self.formula.setAlignment(QtCore.Qt.AlignCenter)
        self.formula.setReadOnly(True)
        self.formula.setObjectName("formula")
        self.verticalLayout.addWidget(self.formula)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ImgToLatex"))
        self.find.setText(_translate("MainWindow", "Обзор"))
        self.load.setText(_translate("MainWindow", "Загрузить"))
        self.go.setToolTip(_translate("MainWindow", "Перевести формулу"))
        self.go.setText(_translate("MainWindow", "Перевести"))

from pyqtgraph import PlotWidget, SpinBox
