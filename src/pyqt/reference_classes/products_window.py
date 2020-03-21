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
        self.add_product_btn = QtWidgets.QPushButton(ProductsWindow)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.add_product_btn.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/nowyPrzedrostek/images/icons8-dodaj-produkt-30.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_product_btn.setIcon(icon)
        self.add_product_btn.setIconSize(QtCore.QSize(30, 30))
        self.add_product_btn.setObjectName("add_product_btn")
        self.gridLayout.addWidget(self.add_product_btn, 0, 0, 1, 1)
        self.edit_product_btn = QtWidgets.QPushButton(ProductsWindow)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.edit_product_btn.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/nowyPrzedrostek/images/icons8-edytuj-produkt-30.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.edit_product_btn.setIcon(icon1)
        self.edit_product_btn.setIconSize(QtCore.QSize(30, 30))
        self.edit_product_btn.setObjectName("edit_product_btn")
        self.gridLayout.addWidget(self.edit_product_btn, 0, 1, 1, 1)
        self.delete_product_btn = QtWidgets.QPushButton(ProductsWindow)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.delete_product_btn.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/nowyPrzedrostek/images/icons8-usuń-produkt-30.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete_product_btn.setIcon(icon2)
        self.delete_product_btn.setIconSize(QtCore.QSize(30, 30))
        self.delete_product_btn.setObjectName("delete_product_btn")
        self.gridLayout.addWidget(self.delete_product_btn, 0, 2, 1, 1)
        self.products_table_view = QtWidgets.QTableView(ProductsWindow)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.products_table_view.setFont(font)
        self.products_table_view.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.products_table_view.setAlternatingRowColors(True)
        self.products_table_view.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.products_table_view.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.products_table_view.setTextElideMode(QtCore.Qt.ElideLeft)
        self.products_table_view.setSortingEnabled(True)
        self.products_table_view.setObjectName("products_table_view")
        self.gridLayout.addWidget(self.products_table_view, 1, 0, 1, 6)

        self.retranslateUi(ProductsWindow)
        self.add_product_btn.clicked.connect(ProductsWindow.add_product)
        self.edit_product_btn.clicked.connect(ProductsWindow.edit_product)
        self.delete_product_btn.clicked.connect(ProductsWindow.delete_product)
        QtCore.QMetaObject.connectSlotsByName(ProductsWindow)

    def retranslateUi(self, ProductsWindow):
        _translate = QtCore.QCoreApplication.translate
        ProductsWindow.setWindowTitle(_translate("ProductsWindow", "Form"))
        self.add_product_btn.setText(_translate("ProductsWindow", "Dodaj"))
        self.edit_product_btn.setText(_translate("ProductsWindow", "Edytuj"))
        self.delete_product_btn.setText(_translate("ProductsWindow", "Usuń"))

import resources_rc
