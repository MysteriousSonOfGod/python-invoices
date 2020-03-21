import sys

from PyQt5 import uic, QtWidgets, QtCore
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QFont
from PyQt5.QtWidgets import QWidget, QDialog, QMessageBox, QApplication
from sqlalchemy import exc

from database import data
from dialogs.edit_customer_dialog import EditCustomerDialog
from dialogs.new_customer_dialog import NewCustomerDialog
from pyqt.reference_classes.customers_window import Ui_CustomersWindow


class CustomersWindow(QWidget, Ui_CustomersWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.sti = QStandardItemModel()
        self.fill_table()
        self.customersTableView.setModel(self.sti)

        # https://stackoverflow.com/questions/26681578/qtableview-column-width
        self.build_table()

    def build_table(self):
        # Setting the columns' widths
        self.sti.setHorizontalHeaderLabels([
            "Alias", "Imię", "Nazwisko", "PESEL/NIP", "Nazwa\nfirmy", "Adres", "Kod\npocztowy", "Miasto", "Płatność"
        ])
        header = self.customersTableView.horizontalHeader()
        column_widths = (180, 100, 200, 180, 150, 200, 100, 150, 90)
        for i, w in enumerate(column_widths):
            self.customersTableView.setColumnWidth(i, w)
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.Fixed)

    def fill_table(self):
        self.sti.clear()
        session = data.Session()
        for cust in session.query(data.Customer):
            self.add_new_row(cust)
        session.close()

    def add_new_row(self, customer):
        self.sti.appendRow([
            QStandardItem(customer.alias),
            QStandardItem(customer.first_name),
            QStandardItem(customer.last_name),
            QStandardItem(customer.tax_id),
            QStandardItem(customer.firm_name),
            QStandardItem(customer.address),
            QStandardItem(customer.postal_code),
            QStandardItem(customer.city),
            QStandardItem("Gotówka" if customer.payment else "Przelew")
        ])

    def _refresh_table(self):
        QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        self.fill_table()
        self.build_table()
        QApplication.restoreOverrideCursor()

    def _assert_any_checked(self):
        selected_item = self.customersTableView.selectedIndexes()
        if not selected_item:
            QMessageBox.warning(
                self, "Informacja",
                "Nie wybrano żadnego kontrahenta do edycji")
            return False
        return True

    @QtCore.pyqtSlot()
    def add_customer(self):
        session = data.Session()
        try:
            customers_dialog = NewCustomerDialog(session)
            if customers_dialog.exec_() == QDialog.Accepted:
                self._refresh_table()
        except exc.IntegrityError as errmsg:
            print(errmsg)
            session.rollback()
            msg = QMessageBox()
            msg.setText("Krytyczny błąd bazy danych")
            msg.setWindowTitle("Błąd krytyczny")
            msg.setDetailedText(errmsg)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.buttonClicked.connect(sys.exit)
        finally:
            session.close()

    @QtCore.pyqtSlot()
    def edit_customer(self):
        if self._assert_any_checked():
            session = data.Session()
            try:
                selected_item = self.customersTableView.selectedIndexes()
                customer_query_obj = session.query(data.Customer).filter(
                    data.Customer.alias == selected_item[0].data()).one()
                edit_employee_window = EditCustomerDialog(session, customer_query_obj)
                if edit_employee_window.exec_() == QDialog.Accepted:
                    self._refresh_table()
            except exc.IntegrityError as errmsg:
                print(errmsg)
                self.session.rollback()
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Krytyczny błąd bazy danych")
                msg.setWindowTitle("Błąd krytyczny")
                msg.setDetailedText(errmsg)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.buttonClicked.connect(sys.exit)
            finally:
                session.close()

    @QtCore.pyqtSlot()
    def delete_customer(self):
        if self._assert_any_checked():
            msg_box = QMessageBox(self)
            msg_box.setIcon(QMessageBox.Question)
            msg_box.setWindowTitle('Informacja')
            msg_box.setText('Na pewno usunąć kontrahenta?')
            msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            buttonY = msg_box.button(QMessageBox.Yes)
            buttonY.setText('Tak')
            buttonN = msg_box.button(QMessageBox.No)
            buttonN.setText('Nie')
            msg_box.exec_()

            if msg_box.clickedButton() == buttonY:
                session = data.Session()
                element = self.customersTableView.selectionModel().selectedIndexes()
                try:
                    c = session.query(data.Customer).filter(data.Customer.alias == element[0].data()).one()
                    session.delete(c)
                    session.commit()
                    QMessageBox.information(
                        self, 'Informacja',
                        'Kontrahent usunięty'
                    )
                    self._refresh_table()
                except Exception:
                    QMessageBox.warning(
                        self, 'Błąd',
                        'Nieznany błąd'
                    )
                finally:
                    session.close()