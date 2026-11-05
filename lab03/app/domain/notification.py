from app.support.types import Recipient
from app.support.errors import DomainError


class Notification:
    def __init__(self, recipient: Recipient, message: str):
        if not isinstance(message, str) or not message.strip():
            raise DomainError("INVALID_MESSAGE")
        self._recipient = recipient
        self._message = message.strip()

    @property
    def recipient(self) -> Recipient:
        return self._recipient

    @property
    def message(self) -> str:
        return self._message