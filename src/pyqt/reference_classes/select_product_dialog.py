# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'select_product_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SelectProductDialog(object):
    def setupUi(self, SelectProductDialog):
        SelectProductDialog.setObjectName("SelectProductDialog")
        SelectProductDialog.resize(800, 400)
        self.verticalLayout = QtWidgets.QVBoxLayout(SelectProductDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableView = QtWidgets.QTableView(SelectProductDialog)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.tableView.setFont(font)
        self.tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableView.setAlternatingRowColors(True)
        self.tableView.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableView.setSortingEnabled(True)
        self.tableView.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableView)
        self.buttonBox = QtWidgets.QDialogButtonBox(SelectProductDialog)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(SelectProductDialog)
        self.buttonBox.accepted.connect(SelectProductDialog.accept)
        self.buttonBox.rejected.connect(SelectProductDialog.reject)
        self.buttonBox.accepted.connect(SelectProductDialog.add_product_template)
        QtCore.QMetaObject.connectSlotsByName(SelectProductDialog)

    def retranslateUi(self, SelectProductDialog):
        _translate = QtCore.QCoreApplication.translate
        SelectProductDialog.setWindowTitle(_translate("SelectProductDialog", "Dialog"))

