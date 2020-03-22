from PyQt5.QtWidgets import QItemDelegate, QLineEdit


class QTableWidgetDisabledItem(QItemDelegate):
    """
    Create a readOnly QTableWidgetItem
    """
    def __init__(self, parent):

        QItemDelegate.__init__(self, parent)

    def createEditor(self, parent, option, index):
        return None

class QTableWidgetEnabledItem(QItemDelegate):
    """
        Create a readOnly QTableWidgetItem
        """

    def __init__(self, parent):
        QItemDelegate.__init__(self, parent)

    # def createEditor(self, parent, option, index):
    #     item = QLineEdit(parent)
    #     item.setReadOnly(False)
    #     item.setEnabled(True)
    #     return item

    # def setEditorData(self, editor, index):
    #     editor.blockSignals(True)
    #     editor.setText(index.model().data(index))
    #     editor.blockSignals(False)

    # def setModelData(self, editor, model, index):
    #     model.setData(index, editor.text())

