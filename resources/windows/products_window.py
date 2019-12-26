from PyQt5 import uic
from PyQt5.QtWidgets import QWidget

from resources.pyqt.reference_classes.products_window import Ui_ProductsWindow


class ProductsWindow(QWidget, Ui_ProductsWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        uic.loadUi("/home/kuba/PycharmProjects/python-invoices/resources/pyqt/products_window.ui")