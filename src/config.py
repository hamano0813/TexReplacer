import os

from qfluentwidgets import OptionsConfigItem, OptionsValidator, QConfig, qconfig

current_path = os.path.dirname(os.path.dirname(__file__)).replace("\\", "/")
config_path = os.path.join(current_path, "config.json")


class Option(QConfig):
    dpi = OptionsConfigItem("QFluentWidgets", "DPI", 1, OptionsValidator([1, 1.25, 1.5, 1.75, 2]), restart=True)


option = Option()
qconfig.load(config_path, option)
