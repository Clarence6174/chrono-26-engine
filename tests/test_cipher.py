import sys
import os

# Add the root directory to path so we can import 'app'
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.core.engine import Chrono26Engine


def test_chrono_cycle():
    engine = Chrono26Engine()
    test_message = "BackendDev123"
    shift_key = 12

    print(f"Testing Message: {test_message}")

    # Encrypt
    encrypted = engine.encrypt(test_message, shift_key)
    print(f"Encrypted Binary: {encrypted[:50]}...")

    # Decrypt
    decrypted_data = engine.decrypt(encrypted, shift_key)

    assert decrypted_data["message"] == test_message
    print(f"Test Passed! Decrypted: {decrypted_data['message']} (Timestamp: {decrypted_data['timestamp']})")


if __name__ == "__main__":
    test_chrono_cycle()
