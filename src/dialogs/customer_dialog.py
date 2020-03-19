from abc import abstractmethod

from PyQt5 import QtCore
from PyQt5.QtCore import QRegularExpression
from PyQt5.QtGui import QRegularExpressionValidator
from PyQt5.QtWidgets import QDialog, QMessageBox

from database import data
from pyqt.reference_classes.customer_dialog import Ui_CustomerDialog


class CustomersDialog(QDialog, Ui_CustomerDialog):
    def __init__(self, session):
        super().__init__()
        self.setupUi(self)
        self.session = session
        self._init_line_edits()

    def _init_line_edits(self):
        self.name_line_edit.setValidator(QRegularExpressionValidator(QRegularExpression(
            "[a-zA-ZĄąĆćĘęŁłŃńÓóŚśŻżŹź\\s]+"
        )))
        self.lastname_line_edit.setValidator(QRegularExpressionValidator(QRegularExpression(
            "[a-zA-ZĄąĆćĘęŁłŃńÓóŚśŻżŹź\\s\\-]+"
        )))
        self.taxid_line_edit.setValidator(QRegularExpressionValidator(QRegularExpression(
            "[\\d\\-?]+"
        )))
        self.postalcode_line_edit.setValidator(QRegularExpressionValidator(QRegularExpression(
            "\\d{2}\\-\\d{3}"
        )))
        self.city_line_edit.setValidator(QRegularExpressionValidator(QRegularExpression(
            "[a-zA-ZĄąĆćĘęŁłŃńÓóŚśŻżŹź\\s\\-]+"
        )))

    @QtCore.pyqtSlot()
    def _validate_input(self):
        if not self.address_line_edit.text() \
                or not self.alias_line_edit.text() \
                or not self.taxid_line_edit.text():
            QMessageBox.warning(
                self, "Wymagane pola są puste",
                ("Jedno z wymaganych pól jest puste:\n\n"
                 "Nazwa\nAdres\nNIP/PESEL")
            )
            return

        self._commit_to_database()

    @abstractmethod
    def _commit_to_database(self):
        ...