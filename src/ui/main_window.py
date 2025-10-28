
from PySide6.QtCore import QEventLoop, QSize, QTimer
from PySide6.QtWidgets import QApplication
from qfluentwidgets import FluentWindow, NavigationItemPosition as NIP, SplashScreen

from ui import AboutInterface, HelperInterface, OptionInterface

from .custom import CustomIcon


class MainWindow(FluentWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowIcon(CustomIcon.LOGO.icon())

        self.splash = SplashScreen(CustomIcon.LOGO.icon(), self)
        self.splash.setIconSize(QSize(500, 500))

        self.helper_interface = HelperInterface(self)
        self.option_interface = OptionInterface(self)
        self.about_interface = AboutInterface(self)

        self.show()
        self.init_ui()
        self.splash.finish()

    def init_ui(self):
        loop = QEventLoop(self)
        QTimer.singleShot(1000, loop.quit)

        self.resize(1080, 720)
        self.setWindowTitle("TexPeplacer V0.1")

        desktop = QApplication.primaryScreen().size()
        w, h = desktop.width(), desktop.height()
        self.move(w // 2 - self.width() // 2, h // 2 - self.height() // 2)

        self.navigationInterface.setExpandWidth(150)

        self.addSubInterface(self.option_interface, CustomIcon.OPTION, "设置", NIP.BOTTOM)
        self.addSubInterface(self.helper_interface, CustomIcon.HELP, "帮助", NIP.BOTTOM)
        self.addSubInterface(self.about_interface, CustomIcon.ABOUT, "关于", NIP.BOTTOM)

        loop.exec()
