import os

from qfluentwidgets import (
    ConfigItem,
    FolderValidator,
    OptionsConfigItem,
    OptionsValidator,
    QConfig,
    RangeConfigItem,
    RangeValidator,
    qconfig,
)

current_path = os.path.dirname(os.path.dirname(__file__)).replace("\\", "/")
config_path = os.path.join(current_path, "config.json")


class Option(QConfig):
    dpi = OptionsConfigItem("QFluentWidgets", "DPI", 1, OptionsValidator([1, 1.25, 1.5, 1.75, 2]), restart=True)

    view_pixel = RangeConfigItem("View", "Pixel", 12, RangeValidator(12, 144))

    folder_dumps = ConfigItem("Folder", "dumps", "", FolderValidator())
    folder_backup = ConfigItem("Folder", "backup", "", FolderValidator())
    folder_export = ConfigItem("Folder", "export", "", FolderValidator())

    font_loader = OptionsConfigItem(
        "Font",
        "Loader",
        [
            [32, 32, 0, 0, 18, 18],
        ],
    )


option = Option()
qconfig.load(config_path, option)
