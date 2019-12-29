# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'products_window.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ProductsWindow(object):
    def setupUi(self, ProductsWindow):
        ProductsWindow.setObjectName("ProductsWindow")
        ProductsWindow.resize(1366, 697)
        self.gridLayout = QtWidgets.QGridLayout(ProductsWindow)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtWidgets.QTableWidget(ProductsWindow)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 6)
        self.pushButton = QtWidgets.QPushButton(ProductsWindow)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/nowyPrzedrostek/images/icons8-dodaj-produkt-30.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(30, 30))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(ProductsWindow)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_2.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/nowyPrzedrostek/images/icons8-edytuj-produkt-30.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(ProductsWindow)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_3.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/nowyPrzedrostek/images/icons8-usuń-produkt-30.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 0, 2, 1, 1)

        self.retranslateUi(ProductsWindow)
        QtCore.QMetaObject.connectSlotsByName(ProductsWindow)

    def retranslateUi(self, ProductsWindow):
        _translate = QtCore.QCoreApplication.translate
        ProductsWindow.setWindowTitle(_translate("ProductsWindow", "Form"))
        self.pushButton.setText(_translate("ProductsWindow", "Dodaj"))
        self.pushButton_2.setText(_translate("ProductsWindow", "Edytuj"))
        self.pushButton_3.setText(_translate("ProductsWindow", "Usuń"))

import resources_rc
