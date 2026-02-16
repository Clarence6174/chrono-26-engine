# Chrono-26 Engine — Instructions

This document explains how to run, test, and deploy the Chrono-26 Engine found in this folder.

## What this repo contains
- `app/` — FastAPI application and engine implementation (`app/main.py`, `app/core/engine.py`).
- `requirements.txt` — Python dependencies.
- `Dockerfile`, `docker-compose.yml` — containerized deployment.
- `tests/` — simple unit test: `tests/test_cipher.py`.

## Requirements
- Python 3.8+ (3.11/3.14 tested).
- pip
- (Optional) Docker & Docker Compose for container runs.

## Quick start — Local (recommended)
1. Open PowerShell and change to the project folder:

```powershell
cd C:\Users\HomePC\Documents\root-repo\chrono-26-engine
```

2. Create and activate a virtual environment, upgrade pip, and install dependencies:

```powershell
python -m venv .venv
# Activate venv (PowerShell)
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

3. Run the app with uvicorn (development mode):

```powershell
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

4. Open the interactive docs to exercise the API:

- http://127.0.0.1:8000/docs

## Run the provided unit test (sanity check)

```powershell
# From project root
python -u tests/test_cipher.py
```

Or with pytest (if installed):

```powershell
pip install pytest
pytest -q
```

The included test encrypts and decrypts a short message and asserts the round-trip.

## Example API requests
- Health check:

```powershell
curl "http://127.0.0.1:8000/health"
```

- Encrypt (example):

```powershell
curl -X POST "http://127.0.0.1:8000/encrypt" -H "Content-Type: application/json" -d '{"text":"BackendDev123","shift":12}'
```

- Decrypt (use `binary_payload` returned by /encrypt):

```powershell
curl -X POST "http://127.0.0.1:8000/decrypt" -H "Content-Type: application/json" -d '{"binary_data":"<binary_payload>","shift":12}'
```

## Run with Docker
- With docker-compose (recommended):

```powershell
cd C:\Users\HomePC\Documents\root-repo\chrono-26-engine
docker-compose up --build
```

- Or build and run manually:

```powershell
docker build -t chrono26 .
docker run -p 8000:8000 chrono26
```

After the container is running the API will be available at `http://localhost:8000`.

## Behavior notes and limitations
- The engine appends a timestamp in `HH:MM` to every payload: the payload format is `message|HH:MM` before encryption.
- Supported characters for the binary mapping: the engine maps the custom uppercase letters from `CUS_U`, their lowercase equivalents, digits `0-9`, and the symbols `:` and `|` into 8-bit binary blocks. Characters outside this set will be passed through during the custom-shift step but will not be represented in the binary payload (and therefore will be dropped in the binary output). For reliable round-trip decryption, avoid unsupported symbols or request an update to the character map.

## Troubleshooting
- `uvicorn: command not found` — ensure your virtual environment is activated and `pip install -r requirements.txt` completed successfully.
- Port 8000 in use — change `--port` when running uvicorn or in the Docker port mapping.
- Docker errors — ensure Docker Desktop is running and you have permissions to run Docker commands.
- Decrypt returns a failure — verify you passed the exact `binary_payload` from `/encrypt` and the correct `shift` integer.

## Files to inspect
- `app/main.py` — FastAPI routes
- `app/core/engine.py` — encryption/decryption logic
- `tests/test_cipher.py` — a simple unit test demonstrating usage

## Next steps (optional)
- Add additional characters (space, punctuation) to `BIN_MAP` and `REV_BIN` to support a wider character set.
- Add a small `scripts/run_local.ps1` to automate venv creation + start.
- Add CI workflow to run tests automatically.

---
Generated on: 2026-02-16

