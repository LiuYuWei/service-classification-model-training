"""svm classification app."""
# coding=utf-8
# import relation package.

# import project package.
from config.config_setting import ConfigSetting
from src.service.svm_classification_service import SvmClassificationService


class SvmClassificationApp:
    """svm classification app."""

    def __init__(self):
        """Initial variable and module"""
        config_setting = ConfigSetting()
        self.log = config_setting.set_logger(
            "[svm_classification_app]")
        self.config = config_setting.yaml_parser()
        self.svm_classification_service = SvmClassificationService()

    def svm_classification(self, x_value, y_value):
        payload = self.svm_classification_service.svm_training(x_value, y_value, kernel="linear")
        return payload