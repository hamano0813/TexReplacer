from PySide6.QtWidgets import QFrame, QLayoutItem, QSpacerItem, QVBoxLayout, QWidget
from qfluentwidgets import (
    ComboBoxSettingCard,
    CustomColorSettingCard,
    MessageBox,
    OptionsSettingCard,
    ScrollArea,
    SettingCardGroup,
    setFont,
    setTheme,
    setThemeColor,
)

import config
from core import utils
from ui.custom import CustomIcon


class OptionInterface(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName(self.__class__.__name__)

        self.sub_frame = QFrame()

        self.theme = OptionsSettingCard(
            config.option.themeMode, CustomIcon.THEME, "主题模式", "更改界面显示颜色", texts=["浅色", "深色", "跟随系统设置"]
        )
        self.color = CustomColorSettingCard(config.option.themeColor, CustomIcon.PALETTE, "主题颜色", "更改界面显示的主题颜色")
        self.dpi = ComboBoxSettingCard(
            config.option.dpi,
            CustomIcon.ZOOM,
            "界面缩放",
            "更改界面显示的缩放比例",
            ["100%", "125%", "150%", "175%", "200%"],
        )
        self.ui_group = self.create_group("界面设置", [self.theme, self.color, self.dpi])

        sub_layout = QVBoxLayout()
        sub_layout.addWidget(self.ui_group)
        sub_layout.addStretch()

        self.sub_frame.setLayout(sub_layout)
        self.scroll_area = ScrollArea(self)
        self.scroll_area.setWidget(self.sub_frame)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.enableTransparentBackground()

        layout = QVBoxLayout(self)
        layout.addWidget(self.scroll_area)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)

        config.option.themeChanged.connect(setTheme)
        config.option.themeColorChanged.connect(setThemeColor)
        config.option.dpi.valueChanged.connect(self.dpi_changed)

    def create_group(self, title: str, widgets: list[QWidget] = list()):
        group = SettingCardGroup(title, self)
        setFont(group.titleLabel, 14)
        group.titleLabel.setIndent(6)
        spacer: QSpacerItem | QLayoutItem = group.vBoxLayout.itemAt(1)
        if isinstance(spacer, QSpacerItem):
            spacer.changeSize(0, 5)
        if widgets:
            for widget in widgets:
                group.addSettingCard(widget)
        return group

    def dpi_changed(self, dpi: float):
        config.qconfig.save()
        scale = int(dpi * 100)
        w = MessageBox(f"界面缩放比例调整为{scale}%", "缩放将在重新启动界面后生效", self.window())
        w.yesButton.setText("现在重启")
        w.cancelButton.setText("暂不重启")
        if w.exec():
            utils.restart()
