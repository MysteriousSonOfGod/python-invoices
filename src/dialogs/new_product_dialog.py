from PyQt5 import QtCore
from PyQt5.QtCore import QLocale
from PyQt5.QtWidgets import QMessageBox, QApplication

from database import data
from dialogs.product_dialog import ProductDialog


class NewProductDialog(ProductDialog):
    def __init__(self, session):
        super().__init__(session)

    def _commit_to_database(self):
        # product existence check
        stmt = self.session.query(data.Product).filter(data.Product.product_name == self.name_line_edit.text())
        # https://stackoverflow.com/questions/7646173/sqlalchemy-exists-for-query
        if self.session.query(stmt.exists()).scalar():
            QMessageBox.warning(
                self, "Duplikat",
                "Produkt o takiej nazwie już istnieje!"
            )
            return

        QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        product = data.Product(
            product_name=self.name_line_edit.text(),
            symbol=self.symbol_line_edit.text(),
            unit=self.unit_line_edit.text(),
            unit_net_price=QLocale().toDouble(
                self.unit_net_price_line_edit.text())[0],
            vat_rate=self.vat_line_edit.text(),
            per_month=self.yes_radio_btn.isChecked()
        )

        self.session.add(product)
        self.session.commit()
        QMessageBox.information(
            self, 'Informacja',
            'Produkt dodany pomyślnie'
        )
        QApplication.restoreOverrideCursor()