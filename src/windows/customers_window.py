import sys

from PyQt5 import uic, QtWidgets, QtCore
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QFont
from PyQt5.QtWidgets import QWidget, QDialog, QMessageBox, QApplication
from sqlalchemy import exc

from database import data
from dialogs.customer_dialog import CustomersDialog
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
        # https://doc.qt.io/qt-5/qfont.html#Weight-enum
        header.setFont(QFont("Sans Serif", pointSize=15, weight=75, italic=False))
        header.setFixedHeight(40)
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
        self.fill_table()
        self.build_table()

    @QtCore.pyqtSlot()
    def add_customer(self):
        session = data.Session()
        try:
            customers_dialog = CustomersDialog(session)
            if customers_dialog.exec_() == QDialog.Accepted:
                QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
                self._refresh_table()
                QApplication.restoreOverrideCursor()
        except exc.IntegrityError as errmsg:
            print(errmsg)
            session.rollback()
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Krytyczny błąd bazy danych")
            msg.setWindowTitle("Błąd krytyczny")
            msg.setDetailedText(errmsg)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.buttonClicked.connect(sys.exit)
        else:
            print('Operacja pomyślna')
        finally:
            session.close()

    @QtCore.pyqtSlot()
    def edit_customer(self):
        pass

    @QtCore.pyqtSlot()
    def delete_customer(self):
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
                c = session.query(data.Customer).filter_by(alias=element[0].data()).one()
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