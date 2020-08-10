"""This file creates the fastapi service."""
# coding=utf-8
# import relation package.
from fastapi import APIRouter
from fastapi.responses import HTMLResponse

# import project package.
from config.config_setting import ConfigSetting
from src.app.svm_classification_app import SvmClassificationApp
from src.util.svm_router_base_model import SvmClassificationBaseModel, MessageBaseModel

def create_svm_router():
    """The function to creates the fastapi api router service."""
    config_setting = ConfigSetting()
    log = config_setting.set_logger("[create_confusion_matrix_router]")
    config = config_setting.yaml_parser()

    user_router = APIRouter()
    svm_classification_app = SvmClassificationApp()

    @user_router.post("/json/svm_classification_training", response_model=SvmClassificationBaseModel)
    def calculate_confusion_matrix(x_value: list, y_value:list):
        payload = svm_classification_app.svm_classification(x_value, y_value)
        return payload

    @user_router.delete("/action/remove_svm_model", response_model=MessageBaseModel)
    def remove_svm_model(model_path: str):
        payload = svm_classification_app.delete_svm_model(model_path)
        return payload
    
    log.info("Successfully setting the svm router.")
    return user_router