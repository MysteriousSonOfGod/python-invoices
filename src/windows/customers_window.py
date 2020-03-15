from PyQt5 import uic, QtWidgets, QtCore
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QFont
from PyQt5.QtWidgets import QWidget

from database import data
from pyqt.reference_classes.customers_window import Ui_CustomersWindow


class CustomersWindow(QWidget, Ui_CustomersWindow):
    def __init__(self, session):
        super().__init__()
        self.session = session
        self.setupUi(self)
        uic.loadUi("pyqt/customers_window.ui")
        self.sti = QStandardItemModel()
        self.fill_table()
        self.customersTableView.setModel(self.sti)

        # https://stackoverflow.com/questions/26681578/qtableview-column-width
        self.build_table()

    def build_table(self):
        # Setting the columns' widths
        self.sti.setHorizontalHeaderLabels([
            "Alias", "Imię", "Nazwisko", "PESEL/NIP", "Nazwa\nfirmy", "Adres", "Kod\npocztowy", "Miasto", "Płatność"
        ])
        header = self.customersTableView.horizontalHeader()
        # https://doc.qt.io/qt-5/qfont.html#Weight-enum
        header.setFont(QFont("Sans Serif", pointSize=15, weight=75, italic=False))
        header.setFixedHeight(40)
        column_widths = (180, 100, 200, 180, 150, 200, 100, 150, 90)
        for i, w in enumerate(column_widths):
            self.customersTableView.setColumnWidth(i, w)
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.Fixed)

    def fill_table(self):
        self.sti.clear()
        for cust in self.session.query(data.Customer):
            self.add_new_row(cust)

    def add_new_row(self, customer):
        self.sti.appendRow([
            QStandardItem(customer.alias),
            QStandardItem(customer.first_name),
            QStandardItem(customer.last_name),
            QStandardItem(customer.tax_id),
            QStandardItem(customer.firm_name),
            QStandardItem(customer.address),
            QStandardItem(customer.postal_code),
            QStandardItem(customer.city),
            QStandardItem(customer.payment)
        ])

    @QtCore.pyqtSlot()
    def add_customer(self):
        pass

    @QtCore.pyqtSlot()
    def edit_customer(self):
        pass

    @QtCore.pyqtSlot()
    def delete_customer(self):
        pass