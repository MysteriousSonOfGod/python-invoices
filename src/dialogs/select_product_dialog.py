from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QLocale
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QDialog

from database import data
from pyqt.reference_classes.select_product_dialog import Ui_SelectProductDialog


class SelectProductDialog(QDialog, Ui_SelectProductDialog):
    def __init__(self, session, customer):
        super().__init__()
        self.customer = customer
        self.session = session
        super().setupUi(self)
        self.sti = QStandardItemModel()
        self._fill_table()
        self.tableView.setModel(self.sti)
        self._build_table()
        self.tableView.setCurrentIndex(self.sti.index(0, 0))

    def _build_table(self):
        # Setting the columns' widths
        self.sti.setHorizontalHeaderLabels([
            "Nazwa", "Symbol", "Jednostka", "Cena\nnetto [zł]", "Stawka\nVAT [%]", "Comiesięczny"
        ])
        header = self.tableView.horizontalHeader()
        column_widths = (223, 75, 100, 120, 100, 150)
        for i, w in enumerate(column_widths):
            self.tableView.setColumnWidth(i, w)
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.Fixed)

    def _fill_table(self):
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
            QStandardItem(str(int(product.vat_rate))),
            QStandardItem("Tak" if product.per_month else "Nie")
        ])

    @QtCore.pyqtSlot()
    def add_product_template(self):
        selected_item = self.tableView.selectedIndexes()
        product_query_obj = self.session.query(data.Product).filter(
            data.Product.product_name == selected_item[0].data()).one()
        template = data.Template(self.customer.id)
        template.product = product_query_obj
        self.customer.template.append(template)
        self.session.add(template)
        self.session.commit()