import sys

from PyQt5.QtWidgets import QApplication
from PyQt5 import uic

app = QApplication(sys.argv)
main_window = uic.loadUi("/home/kuba/PycharmProjects/python-invoices/resources/pyqt/main_window.ui")
home_window = uic.loadUi("/home/kuba/PycharmProjects/python-invoices/resources/pyqt/home_window.ui")
main_window.setCentralWidget(home_window)
main_window.show()
sys.exit(app.exec())