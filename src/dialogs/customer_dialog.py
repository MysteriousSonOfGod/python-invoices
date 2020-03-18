from abc import abstractmethod

from PyQt5 import QtCore
from PyQt5.QtCore import QRegularExpression
from PyQt5.QtGui import QRegularExpressionValidator
from PyQt5.QtWidgets import QDialog

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
    @abstractmethod
    def _validate_input(self):
        ...
