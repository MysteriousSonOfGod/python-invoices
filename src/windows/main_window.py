from PyQt5.QtWidgets import QMainWindow

from database import data
from pyqt.reference_classes.main_window import Ui_MainWindow
from PyQt5 import QtCore

from windows.customers_window import CustomersWindow
from windows.home_window import HomeWindow
from windows.products_window import ProductsWindow
from windows.settings_window import SettingsWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.switch_to_homepage()
        self.show()

    @QtCore.pyqtSlot()
    def switch_to_homepage(self):
        home_win = HomeWindow()
        self.setCentralWidget(home_win)

    @QtCore.pyqtSlot()
    def switch_to_customers(self):
        session = data.Session()
        customers_win = CustomersWindow(session)
        self.setCentralWidget(customers_win)

    @QtCore.pyqtSlot()
    def switch_to_products(self):
        products_win = ProductsWindow()
        self.setCentralWidget(products_win)

    @QtCore.pyqtSlot()
    def switch_do_settings(self):
        settings_win = SettingsWindow()
        self.setCentralWidget(settings_win)