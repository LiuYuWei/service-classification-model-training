"""Define fastapi input variable type."""
# import relation package.
from pydantic import BaseModel

# import project package.


class SvmClassificationBaseModel(BaseModel):
    """The input of change direction"""
    support_vectors: list
    n_support: list
    timestamp: str
    number_data: int
    model_path: str

class MessageBaseModel(BaseModel):
    message: str
    status_code: int