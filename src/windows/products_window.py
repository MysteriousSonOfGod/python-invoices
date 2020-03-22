import sys

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QLocale
from PyQt5.QtGui import QStandardItemModel, QFont, QStandardItem
from PyQt5.QtWidgets import QWidget, QApplication, QDialog, QMessageBox
from sqlalchemy import exc

from database import data
from dialogs.edit_product_dialog import EditProductDialog
from dialogs.new_product_dialog import NewProductDialog
from pyqt.reference_classes.products_window import Ui_ProductsWindow


class ProductsWindow(QWidget, Ui_ProductsWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.sti = QStandardItemModel()
        self.fill_table()
        self.products_table_view.setModel(self.sti)

        # https://stackoverflow.com/questions/26681578/qtableview-column-width
        self.build_table()

    def build_table(self):
        # Setting the columns' widths
        self.sti.setHorizontalHeaderLabels([
            "Nazwa", "Symbol", "Jednostka", "Cena jednostkowa\nnetto [zł]", "Stawka\nVAT [%]", "Comiesięczny"
        ])
        header = self.products_table_view.horizontalHeader()
        column_widths = (730, 75, 100, 180, 100, 150)
        for i, w in enumerate(column_widths):
            self.products_table_view.setColumnWidth(i, w)
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.Fixed)

    def fill_table(self):
        self.sti.clear()
        session = data.Session()
        for prod in session.query(data.Product):
            self.add_new_row(prod)
        session.close()

    def add_new_row(self, product):
        self.sti.appendRow([
            QStandardItem(product.product_name),
            QStandardItem(product.symbol),
            QStandardItem(product.unit),
            QStandardItem(QLocale().toString(
                float(product.unit_net_price)
            )),
            QStandardItem(str(int(product.vat_rate * 100))),
            QStandardItem("Tak" if product.per_month else "Nie")
        ])

    def _refresh_table(self):
        QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        self.fill_table()
        self.build_table()
        QApplication.restoreOverrideCursor()

    def _assert_any_checked(self):
        selected_item = self.products_table_view.selectedIndexes()
        if not selected_item:
            QMessageBox.warning(
                self, "Informacja",
                "Nie wybrano żadnego produktu do edycji")
            return False
        return True

    @QtCore.pyqtSlot()
    def add_product(self):
        session = data.Session()
        try:
            products_dialog = NewProductDialog(session)
            if products_dialog.exec_() == QDialog.Accepted:
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
    def edit_product(self):
        if self._assert_any_checked():
            session = data.Session()
            try:
                selected_item = self.products_table_view.selectedIndexes()
                product_query_obj = session.query(data.Product).filter(
                    data.Product.product_name == selected_item[0].data()).one()
                edit_employee_window = EditProductDialog(session, product_query_obj)
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
    def delete_product(self):
        if self._assert_any_checked():
            msg_box = QMessageBox(self)
            msg_box.setIcon(QMessageBox.Question)
            msg_box.setWindowTitle('Informacja')
            msg_box.setText('Na pewno usunąć produkt?')
            msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            buttonY = msg_box.button(QMessageBox.Yes)
            buttonY.setText('Tak')
            buttonN = msg_box.button(QMessageBox.No)
            buttonN.setText('Nie')
            msg_box.exec_()

            if msg_box.clickedButton() == buttonY:
                session = data.Session()
                element = self.products_table_view.selectionModel().selectedIndexes()
                try:
                    c = session.query(data.Product).filter(data.Product.product_name == element[0].data()).one()
                    session.delete(c)
                    session.commit()
                    QMessageBox.information(
                        self, 'Informacja',
                        'Produkt usunięty'
                    )
                    self._refresh_table()
                except Exception:
                    QMessageBox.warning(
                        self, 'Błąd',
                        'Nieznany błąd'
                    )
                finally:
                    session.close()