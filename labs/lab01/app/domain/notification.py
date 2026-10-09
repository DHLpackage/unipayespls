from dataclasses import dataclass

from app.support.errors import DomainError
from app.support.types import Recipient


@dataclass(frozen=True)
class Notification:

    recipient: Recipient
    message: str

    def __post_init__(self) -> None:
        if not isinstance(self.message, str) or not self.message.strip():
            raise DomainError("EMPTY_MESSAGE")
        object.__setattr__(self, "message", self.message.strip())

    def describe(self) -> str:
        return f"message={self.message}"