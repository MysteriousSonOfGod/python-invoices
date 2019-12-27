from PyQt5 import uic
from PyQt5.QtWidgets import QWidget

from pyqt.reference_classes.home_window import Ui_HomeWindow


class HomeWindow(QWidget, Ui_HomeWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        uic.loadUi("/home/kuba/PycharmProjects/python-invoices/resources/pyqt/home_window.ui")