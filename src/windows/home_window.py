import sys
from datetime import date
from decimal import Decimal
from functools import partial

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QStringListModel, QLocale, QModelIndex
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QMessageBox, QDialog, QApplication
from sqlalchemy import exc

from database import data
from dialogs.select_product_dialog import SelectProductDialog
from pyqt.reference_classes.home_window import Ui_HomeWindow
from utils.delegate import QTableWidgetDisabledItem, QTableWidgetEnabledItem

TWOPLACES = Decimal('.01')


class HomeWindow(QWidget, Ui_HomeWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.selected_customer = None

        self.model = QStringListModel()
        self.display_customers_list()
        self.listView.setModel(self.model)
        self.sti = QStandardItemModel()
        self.tableView.setModel(self.sti)
        self.dateEdit.setDate(date.today())
        self.listView.selectionModel().selectionChanged.connect(self._load_customer_template)
        self._select_index(0)
        self._build_table()

    def _build_table(self):
        # Setting the columns' widths
        self.sti.setHorizontalHeaderLabels([
            "Nazwa", "Symbol", "j.m.", "Cena\nnetto [zł]", "Ilość", "Wartość\nnetto [zł]", "Stawka\nVAT [%]",
            "Wartość\nVAT [%]", "Wartość\nbrutto [zł]"
        ])
        header = self.tableView.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.tableView.setItemDelegateForColumn(0, QTableWidgetDisabledItem(self.tableView))
        column_widths = (75, 50, 95, 50, 100, 90, 90, 105)
        for i, w in enumerate(column_widths):
            self.tableView.setColumnWidth(i + 1, w)
            header.setSectionResizeMode(i + 1, QtWidgets.QHeaderView.Fixed)
            # set custom item delegate with disabled editing mode for every column
            # except 4th one (i != 3 because we're iterating from the second column)
            # the first one is set above
            self.tableView.setItemDelegateForColumn(
                i + 1,
                QTableWidgetDisabledItem(self.tableView) if i != 3 else QTableWidgetEnabledItem(self.tableView)
            )

        self.tableView.itemDelegateForColumn(4).closeEditor.connect(self._update_template_quantity)

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
                self._add_new_row(temp)

    def _add_new_row(self, template):
        self.sti.appendRow([
            QStandardItem(template.product.product_name),
            QStandardItem(template.product.symbol),
            QStandardItem(template.product.unit),
            QStandardItem(QLocale().toString(
                float(template.product.unit_net_price)
            )),
            QStandardItem(str(int(template.quantity))),
            QStandardItem(QLocale().toString(
                float(template.net_val)
            )),
            QStandardItem(str(int(template.product.vat_rate * 100))),
            QStandardItem(QLocale().toString(
                float(template.tax_val.quantize(TWOPLACES))
            )),
            QStandardItem(QLocale().toString(
                float(template.gross_val.quantize(TWOPLACES))
            ))
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
            self.selected_customer = session.query(data.Customer).filter(data.Customer.alias == selected_alias).one()
            self._fill_template_data(self.selected_customer.template)
            self.customer_label.setText(self.selected_customer.alias)
            self._build_table()
        except exc.IntegrityError as errmsg:
            self._display_critical_window(errmsg, session)
        finally:
            session.close()

    @QtCore.pyqtSlot()
    def _add_product(self):
        session = data.Session()
        try:
            select_product = SelectProductDialog(session, self.selected_customer)
            if select_product.exec_() == QDialog.Accepted:
                QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
                self._add_new_row(self.selected_customer.template[-1])
                self._build_table()
                QApplication.restoreOverrideCursor()
        except exc.IntegrityError as errmsg:
            self._display_critical_window(errmsg, session)
        finally:
            session.close()

    def _update_template_quantity(self, editor, hint):
        row = self.tableView.selectionModel().selectedRows()[0].row()
        selected_template = self.selected_customer.template[row]
        if editor.text():
            selected_template.quantity = Decimal(editor.text())
        else:
            selected_template.quantity = Decimal(0)
            self.sti.setData(self.sti.index(row, 4), "0")

        # calculate net value
        self.sti.setData(self.sti.index(row, 5), QLocale().toString(
                float(selected_template.net_val)
            )
        )

        # calculate tax value
        self.sti.setData(self.sti.index(row, 7), QLocale().toString(
                float(selected_template.tax_val.quantize(TWOPLACES)
                      )
            )
        )

        # calculate gross value
        self.sti.setData(self.sti.index(row, 8), QLocale().toString(
                float(selected_template.gross_val.quantize(TWOPLACES)
                      )
            )
        )

    @QtCore.pyqtSlot()
    def _save_template(self):
        session = data.Session()
        try:
            QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
            session.add_all(self.selected_customer.template)
            session.commit()
            QMessageBox.information(
                self, 'Informacja',
                'Wzorzec zapisany'
            )
            QApplication.restoreOverrideCursor()
        except exc.IntegrityError as errmsg:
            self._display_critical_window(errmsg, session)
        finally:
            session.close()