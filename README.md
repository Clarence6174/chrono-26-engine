# Chrono-26 Engine 

**Chrono-26** is a dual-layer encryption backend built with FastAPI. It transforms standard text into a custom-shuffled alphabet, applies a time-synced Caesar shift, and outputs a secure 8-bit binary stream.

##  Features
- **Custom Alphabet Mapping:** Uses a non-standard 26-letter sequence (`VWXQRS...`) to bypass standard frequency analysis.
- **Double Encryption:** Layer 1 (Custom Caesar Shift) + Layer 2 (Binary Unicode Mapping).
- **Temporal Verification:** Automatically attaches a `HH:MM` timestamp to every payload.
- **Case Sensitive:** Full support for `A-Z` and `a-z`.
- **Docker Ready:** Includes `Dockerfile` and `docker-compose.yml` for instant deployment.

## 📦 Quick Start (Docker)
1. **Clone the repo:**
   ```bash
   git clone https://github.com/Clarence6174/chrono-26-engine
