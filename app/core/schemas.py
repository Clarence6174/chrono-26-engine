from pydantic import BaseModel

class EncryptRequest(BaseModel):
    text: str
    shift: int

class DecryptRequest(BaseModel):
    binary_data: str
    shift: int

class DecryptResponseData(BaseModel):
    message: str
    timestamp: str
