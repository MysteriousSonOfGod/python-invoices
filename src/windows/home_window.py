import sys

from PyQt5 import uic, QtWidgets, QtCore
from PyQt5.QtCore import QStringListModel
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QMessageBox
from sqlalchemy import exc
from datetime import date

from database import data
from pyqt.reference_classes.home_window import Ui_HomeWindow

class HomeWindow(QWidget, Ui_HomeWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.model = QStringListModel()
        self.display_customers_list()
        self.listView.setModel(self.model)
        self.sti = QStandardItemModel()
        self.tableView.setModel(self.sti)
        self._build_table()
        self.dateEdit.setDate(date.today())
        self.listView.selectionModel().selectionChanged.connect(self._load_customer_template)
        self._select_index(0)

    def _build_table(self):
        # Setting the columns' widths
        self.sti.setHorizontalHeaderLabels([
            "Nazwa", "Symbol", "j.m.", "Cena\nnetto [zł]", "Ilość", "Wartość\nnetto [zł]", "Stawka\nVAT [%]",
            "Wartość\nVAT [%]", "Wartość\nbrutto [zł]"
        ])
        header = self.tableView.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        column_widths = (75, 50, 95, 50, 100, 90, 90, 105)
        for i, w in enumerate(column_widths):
            self.tableView.setColumnWidth(i + 1, w)
            header.setSectionResizeMode(i + 1, QtWidgets.QHeaderView.Fixed)
            

    def _display_critical_window(self, errmsg, session):
        print(errmsg)
        session.rollback()
        msg = QMessageBox(icon=QMessageBox.Critical, text="Błąd krytyczny bazy danych",
                          title="Błąd krytyczny", buttons=QMessageBox.Ok)
        msg.setDetailedText(errmsg)
        msg.buttonClicked.connect(sys.exit)

    def display_customers_list(self):
        session = data.Session()
        try:
            self.model.setStringList([alias for alias, in session.query(data.Customer.alias)])
        except exc.IntegrityError as errmsg:
            self._display_critical_window(errmsg, session)
        finally:
            session.close()

    def _fill_template_data(self, templates_list):
        self.sti.clear()
        if len(templates_list) > 0:
            for temp in templates_list:
                self.add_new_row(temp)

    def add_new_row(self, template):
        self.sti.appendRow([
            QStandardItem(template.product.product_name)
        ])

    def _select_index(self, row):
        if self.model.rowCount() > 0:
            self.listView.setCurrentIndex(self.model.index(row))

    @QtCore.pyqtSlot()
    def _select_first(self):
        self._select_index(0)

    @QtCore.pyqtSlot()
    def _select_next(self):
        next_idx = self.listView.selectedIndexes()[0].row() + 1
        if next_idx < self.model.rowCount():
            self._select_index(next_idx)

    @QtCore.pyqtSlot()
    def _select_last(self):
        self._select_index(self.model.rowCount() - 1)

    @QtCore.pyqtSlot()
    def _select_prev(self):
        next_idx = self.listView.selectedIndexes()[0].row() - 1
        if next_idx >= 0:
            self._select_index(next_idx)

    @QtCore.pyqtSlot()
    def _load_customer_template(self):
        selected_alias = self.listView.selectionModel().selectedIndexes()[0].data()
        session = data.Session()
        try:
            customer = session.query(data.Customer).filter(data.Customer.alias == selected_alias).one()
            self._fill_template_data(customer.template)
            self.customer_label.setText(customer.alias)
        except exc.IntegrityError as errmsg:
            self._display_critical_window(errmsg, session)
        finally:
            session.close()