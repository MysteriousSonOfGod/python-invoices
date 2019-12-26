import sys

from PyQt5.QtWidgets import QApplication

from resources.windows.main_window import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    sys.exit(app.exec())