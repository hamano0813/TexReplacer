from PySide6.QtWidgets import QFrame


class AboutInterface(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName(self.__class__.__name__)
