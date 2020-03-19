from PyQt5.QtCore import QLocale
from PyQt5.QtWidgets import QMessageBox
from decimal import Decimal

from dialogs.product_dialog import ProductDialog


class EditProductDialog(ProductDialog):
    def __init__(self, session, product):
        super().__init__(session)
        self.product = product
        self._fill_data()

    def _fill_data(self):
        self.name_line_edit.setText(self.product.product_name)
        self.symbol_line_edit.setText(self.product.symbol)
        self.unit_line_edit.setText(self.product.unit)
        self.unit_net_price_line_edit.setText(
            QLocale().toString(float(self.product.unit_net_price))
        )
        self.vat_line_edit.setText(str(int(self.product.vat_rate)))
        self.yes_radio_btn.setChecked(self.product.per_month)

    def _commit_to_database(self):
        self.product.product_name = self.name_line_edit.text()
        self.product.symbol = self.symbol_line_edit.text()
        self.product.unit = self.unit_line_edit.text()
        self.product.unit_net_price = QLocale().toDouble(
            self.unit_net_price_line_edit.text())[0]
        self.product.vat_rate = self.vat_line_edit.text()
        self.product.per_month = self.yes_radio_btn.isChecked()

        self.session.commit()
        QMessageBox.information(
            self, 'Informacja',
            'Produkt zaktualizowany pomyślnie'
        )