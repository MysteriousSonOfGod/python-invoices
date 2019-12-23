import sys

from PyQt5.QtWidgets import QApplication
from PyQt5 import uic

app = QApplication(sys.argv)
main_window = uic.loadUi("/home/kuba/PycharmProjects/python-invoices/src/resources/pyqt/main_window.ui")
main_window.show()
sys.exit(app.exec())