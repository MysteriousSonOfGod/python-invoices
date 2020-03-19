from abc import abstractmethod

from PyQt5 import QtCore
from PyQt5.QtCore import QRegularExpression
from PyQt5.QtGui import QRegularExpressionValidator
from PyQt5.QtWidgets import QDialog, QMessageBox

from database import data
from pyqt.reference_classes.product_dialog import Ui_ProductDialog


class ProductDialog(QDialog, Ui_ProductDialog):
    def __init__(self, session):
        super().__init__()
        self.setupUi(self)
        self.session = session
        self._init_line_edits()

    def _init_line_edits(self):
        validator = QRegularExpressionValidator(QRegularExpression("[^ ]+"))

        self.name_line_edit.setValidator(validator)
        self.symbol_line_edit.setValidator(validator)
        self.unit_line_edit.setValidator(validator)
        self.unit_net_price_line_edit.setValidator(QRegularExpressionValidator(QRegularExpression(
            "\d+(,\d{2})?")
        ))
        self.vat_line_edit.setValidator(QRegularExpressionValidator(QRegularExpression(
            "\d{1,2}")
        ))

    @QtCore.pyqtSlot()
    def _validate_input(self):
        if not self.name_line_edit.text() \
                or not self.unit_net_price_line_edit.text() \
                or not self.vat_line_edit.text():
            QMessageBox.warning(
                self, "Wymagane pola są puste",
                ("Jedno z wymaganych pól jest puste:\n\n"
                 "Nazwa\nCena jednostkowa netto\nStawka VAT")
            )
            return

        self._commit_to_database()

    @abstractmethod
    def _commit_to_database(self):
        ...