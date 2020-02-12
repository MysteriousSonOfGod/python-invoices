from PyQt5 import uic
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget

from pyqt.reference_classes.customers_window import Ui_CustomersWindow


class CustomersWindow(QWidget, Ui_CustomersWindow):
    def __init__(self, session, customers):
        super().__init__()
        self.customers = customers
        self.session = session
        self.setupUi(self)
        uic.loadUi("pyqt/customers_window.ui")
        self.sti = QStandardItemModel()
        self.fill_table()

    def fill_table(self):
        self.sti.setHorizontalHeaderLabels([
            "Alias", "Imię", "Nazwisko", "PESEL/NIP", "Nazwa firmy", "Adres", "Kod pocztowy", "Miasto", "Płatność"
        ])
        for cust in self.customers:
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