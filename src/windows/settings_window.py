from PyQt5 import uic
from PyQt5.QtWidgets import QWidget

from pyqt.reference_classes.settings_window import Ui_SettingsWindow


class SettingsWindow(QWidget, Ui_SettingsWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        uic.loadUi("/home/kuba/PycharmProjects/python-invoices/resources/pyqt/settings_window.ui")