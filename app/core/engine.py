import datetime


class Chrono26Engine:
    def __init__(self):
        # The specific 26-letter shuffle sequence derived from your instructions
        self.STD_U = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.STD_L = self.STD_U.lower()
        self.CUS_U = "VWXQRSJKLEFGAZTUNOPBCDYHIM"
        self.CUS_L = self.CUS_U.lower()

        # Supporting digits and symbols for the timestamp logic
        chars = self.CUS_U + self.CUS_L + "0123456789:|"
        self.BIN_MAP = {c: format(ord(c), '08b') for c in chars}
        self.REV_BIN = {v: k for k, v in self.BIN_MAP.items()}

    def encrypt(self, text: str, shift: int) -> str:
        timestamp = datetime.datetime.now().strftime("%H:%M")
        payload = f"{text}|{timestamp}"

        shifted_custom = ""
        for char in payload:
            if char in self.STD_U:
                idx = (self.STD_U.find(char) + shift) % 26
                shifted_custom += self.CUS_U[idx]
            elif char in self.STD_L:
                idx = (self.STD_L.find(char) + shift) % 26
                shifted_custom += self.CUS_L[idx]
            else:
                shifted_custom += char

        # Join into space-delimited 8-bit blocks
        return " ".join(self.BIN_MAP[c] for c in shifted_custom if c in self.BIN_MAP)

    def decrypt(self, binary_string: str, shift: int) -> dict:
        try:
            parts = binary_string.split(" ")
            custom_chars = "".join(self.REV_BIN[p] for p in parts if p in self.REV_BIN)

            decoded = ""
            for char in custom_chars:
                if char in self.CUS_U:
                    idx = (self.CUS_U.find(char) - shift) % 26
                    decoded += self.STD_U[idx]
                elif char in self.CUS_L:
                    idx = (self.CUS_L.find(char) - shift) % 26
                    decoded += self.STD_L[idx]
                else:
                    decoded += char

            msg, ts = decoded.split("|")
            return {"message": msg, "timestamp": ts}
        except Exception:
            raise ValueError("Decryption failed. Ensure the binary string and shift key are correct.")
