"""Confusion matrix calculation service."""
# coding=utf-8
# import relation package.
import datetime
from sklearn.svm import SVC

# import project package.
from config.config_setting import ConfigSetting


class SvmClassificationService:
    """Confusion matrix calculation service."""

    def __init__(self):
        """Initial variable and module"""
        config_setting = ConfigSetting()
        self.log = config_setting.set_logger(
            "[svm_classification_service]")
        self.config = config_setting.yaml_parser()

    def svm_training(self, x_value, y_value, kernel="linear"):
        clf = SVC(kernel = kernel)
        clf.fit(x_value, y_value)
        payload = {}
        payload["support_vectors"] = clf.support_vectors_.tolist()
        payload["n_support"] = clf.n_support_.tolist()
        payload["timestamp"] = datetime.datetime.now().isoformat()
        payload["number_data"] = len(x_value)
        return payload