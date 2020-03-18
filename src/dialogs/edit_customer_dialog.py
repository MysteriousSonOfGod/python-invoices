from PyQt5.QtWidgets import QMessageBox

from dialogs.customer_dialog import CustomersDialog


class EditCustomerDialog(CustomersDialog):
    def __init__(self, session, customer):
        super().__init__(session)
        self.customer = customer
        self._fill_data()

    def _fill_data(self):
        self.alias_line_edit.setText(self.customer.alias)
        self.firm_line_edit.setText(self.customer.firm_name)
        self.name_line_edit.setText(self.customer.first_name)
        self.lastname_line_edit.setText(self.customer.last_name)
        self.taxid_line_edit.setText(self.customer.tax_id)
        self.address_line_edit.setText(self.customer.address)
        self.postalcode_line_edit.setText(self.customer.postal_code)
        self.city_line_edit.setText(self.customer.city)
        self.cash_radio_btn.setChecked(self.customer.payment)

    def _commit_to_database(self):
        self.customer.alias = self.alias_line_edit.text()
        self.customer.firm_name = self.firm_line_edit.text()
        self.customer.last_name = self.lastname_line_edit.text()
        self.customer.first_name = self.name_line_edit.text()
        self.customer.tax_id = self.taxid_line_edit.text()
        self.customer.address = self.address_line_edit.text()
        self.customer.postal_code = self.postalcode_line_edit.text()
        self.customer.city = self.city_line_edit.text()
        self.customer.payment = self.cash_radio_btn.isChecked()

        self.session.commit()
        QMessageBox.information(
            self, 'Informacja',
            'Kontrahent zaktualizowany pomyślnie'
        )