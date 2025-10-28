from enum import Enum

from qfluentwidgets import FluentIconBase, Theme, getIconColor

import res


class CustomIcon(FluentIconBase, Enum):
    LOGO = "logo/logo"

    HELP = "icon/help"
    OPTION = "icon/option"
    ABOUT = "icon/about"

    PARAMETER = "icon/parameter"

    THEME = "icon/theme"
    PALETTE = "icon/palette"
    ZOOM = "icon/zoom"

    def path(self, theme=Theme.AUTO):
        return f":/{self.value}_{getIconColor(theme)}.svg"
