import os
import sys

sys.path.append(os.path.dirname(__file__))

import ctypes

from PySide6.QtWidgets import QApplication
from qfluentwidgets import FluentTranslator

import config
from ui.main_window import MainWindow

try:
    ctypes.windll.shcore.SetProcessDpiAwareness(0)
except Exception:
    pass


def scale_dpi():
    os.environ["QT_ENABLE_HIGHDPI_SCALING"] = "0"
    os.environ["QT_SCALE_FACTOR"] = str(config.option.get(config.option.dpi))


def main():
    scale_dpi()

    app = QApplication(sys.argv)
    translator = FluentTranslator()
    app.installTranslator(translator)
    MainWindow()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
