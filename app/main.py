from fastapi import FastAPI, HTTPException
from app.core.engine import Chrono26Engine
from app.core.schemas import EncryptRequest, DecryptRequest

app = FastAPI(
    title="Chrono-26 Engine",
    description="Custom Alphabet & Binary Temporal Encryption API",
    version="1.0.0"
)

# Initialize the backend engine
engine = Chrono26Engine()

@app.post("/encrypt", tags=["Encryption"])
async def encrypt_message(req: EncryptRequest):
    """
    Encrypts standard text to Chrono-26 Binary.
    """
    binary_payload = engine.encrypt(req.text, req.shift)
    return {"status": "success", "binary_payload": binary_payload}

@app.post("/decrypt", tags=["Decryption"])
async def decrypt_message(req: DecryptRequest):
    """
    Decrypts Chrono-26 Binary back to standard text and reveals timestamp.
    """
    try:
        data = engine.decrypt(req.binary_data, req.shift)
        return {"status": "success", "data": data}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/health", tags=["System"])
async def health_check():
    return {"status": "online", "engine": "Chrono-26"}
