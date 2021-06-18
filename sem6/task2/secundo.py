# Разработать программу, позволяющую генерировать уникальные
# идентификаторы: UUID (universally unique identifier). Структура UUID — на
# усмотрение студента.
import secrets
import binascii


class Uuid4:
    ENC = "ascii"

    def __init__(self):
        uuid = secrets.token_bytes(16)  # 32 + 4
        uuid = bytearray(uuid)

        uuid[6] = uuid[6] & 0x0F | 0x4F
        uuid[8] = uuid[8] & 0x3F | 0x80

        self._hex = binascii.hexlify(uuid)  # uuid

    def __str__(self):
        uuid = f"{self._slice_hex(0, 8)}-"
        uuid += f"{self._slice_hex(8, 12)}-"
        uuid += f"{self._slice_hex(12, 16)}-"
        uuid += f"{self._slice_hex(16, 20)}-"
        uuid += f"{self._slice_hex(20, 32)}"

        return uuid

    def _slice_hex(self, start: int = 0, end: int = 32) -> str:
        return self._hex[start:end].decode(self.ENC)
