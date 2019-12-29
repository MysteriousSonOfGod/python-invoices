import sys

from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QWidget, QMessageBox
from sqlalchemy import exc

from database import data
from pyqt.reference_classes.home_window import Ui_HomeWindow

class HomeWindow(QWidget, Ui_HomeWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Setting the columns' widths
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        column_widths = (75, 50, 95, 50, 100, 90, 90, 105)
        for i, w in enumerate(column_widths):
            self.tableWidget.setColumnWidth(i + 1, w)
            header.setSectionResizeMode(i + 1, QtWidgets.QHeaderView.Fixed)

    def display_data(self):
        session = data.Session()
        try:
            pass
        except exc.IntegrityError as errmsg:
            print(errmsg)
            session.rollback()
            session.close()
            msg = QMessageBox(icon=QMessageBox.Critical, text="Błąd krytyczny bazy danych",
                              title="Błąd krytyczny", buttons=QMessageBox.Ok)
            msg.setDetailedText(errmsg)
            msg.buttonClicked.connect(sys.exit)