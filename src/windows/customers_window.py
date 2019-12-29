from PyQt5 import uic
from PyQt5.QtWidgets import QWidget

from pyqt.reference_classes.customers_window import Ui_CustomersWindow


class CustomersWindow(QWidget, Ui_CustomersWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        uic.loadUi("pyqt/customers_window.ui")