"""Confusion matrix calculation service."""
# coding=utf-8
# import relation package.
import os
import pickle
import datetime
from sklearn.svm import SVC

# import project package.
from config.config_setting import ConfigSetting
from src.dao.model_information_dao import ModelInformationDao


class SvmClassificationService:
    """Confusion matrix calculation service."""

    def __init__(self):
        """Initial variable and module"""
        config_setting = ConfigSetting()
        self.log = config_setting.set_logger(
            "[svm_classification_service]")
        self.config = config_setting.yaml_parser()
        self.model_name = "svm_model"
        self.model_information_dao = ModelInformationDao()
        self.model_information_dao.setting_model_database(self.model_name)

    def svm_training(self, x_value, y_value, kernel="linear"):
        clf = SVC(kernel = kernel)
        clf.fit(x_value, y_value)
        payload = {}
        now_time = datetime.datetime.now()
        payload["timestamp"] = now_time.isoformat()
        payload["number_data"] = len(x_value)
        payload["model_path"] = 'data/model/svm/svm_model_{}.pickle'.format(now_time.strftime("%Y%m%d_%H%M%S"))
        self.model_information_dao.save_data(payload, self.model_name)
        with open(payload["model_path"], 'wb') as file:
            pickle.dump(clf, file)
        payload["support_vectors"] = clf.support_vectors_.tolist()
        payload["n_support"] = clf.n_support_.tolist()
        return payload
    
    def remove_svm_model(self, model_path):
        payload = {"message":"Unsuccessfully remove the model", "status_code": 601}
        if os.path.exists(model_path):
            os.remove(model_path)
            payload = {"message": "Successfully remove the model", "status_code": 200}
        return payload
