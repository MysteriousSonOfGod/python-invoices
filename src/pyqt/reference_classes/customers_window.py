# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'customers_window.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CustomersWindow(object):
    def setupUi(self, CustomersWindow):
        CustomersWindow.setObjectName("CustomersWindow")
        CustomersWindow.resize(1366, 697)
        self.gridLayout = QtWidgets.QGridLayout(CustomersWindow)
        self.gridLayout.setObjectName("gridLayout")
        self.tableView = QtWidgets.QTableView(CustomersWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy)
        self.tableView.setObjectName("tableView")
        self.gridLayout.addWidget(self.tableView, 2, 0, 1, 6)
        self.pushButton_3 = QtWidgets.QPushButton(CustomersWindow)
        self.pushButton_3.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_3.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../resources/images/icons8-dodaj-użytkownika-mężczyzna-30.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(CustomersWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../../resources/images/icons8-edycja-użytkownika-mężczyzna-30.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(30, 30))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(CustomersWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_2.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../../resources/images/icons8-usuń-użytkownika-mężczyzna-30.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 2, 1, 1)

        self.retranslateUi(CustomersWindow)
        QtCore.QMetaObject.connectSlotsByName(CustomersWindow)

    def retranslateUi(self, CustomersWindow):
        _translate = QtCore.QCoreApplication.translate
        CustomersWindow.setWindowTitle(_translate("CustomersWindow", "Form"))
        self.pushButton_3.setText(_translate("CustomersWindow", "Dodaj"))
        self.pushButton.setText(_translate("CustomersWindow", "Edytuj"))
        self.pushButton_2.setText(_translate("CustomersWindow", "Usuń"))

