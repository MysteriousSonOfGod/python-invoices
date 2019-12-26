from PyQt5 import uic
from PyQt5.QtWidgets import QWidget

from resources.pyqt.reference_classes.customers_window import Ui_CustomersWindow


class CustomersWindow(QWidget, Ui_CustomersWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        uic.loadUi("/home/kuba/PycharmProjects/python-invoices/resources/pyqt/customers_window.ui")