from dataclasses import dataclass
from app.support.errors import DomainError


@dataclass(frozen=True)
class Recipient:
    email: str | None = None
    phone: str | None = None
    push_token: str | None = None


@dataclass(frozen=True)
class DeliveryReceipt:
    channel: str
    destination: str
    text: str


def contact(value: str | None) -> str:
    if not isinstance(value, str) or not value.strip():
        raise DomainError("MISSING_CONTACT")
    return value.strip()


def validate_receipt(receipt: DeliveryReceipt, channel: str) -> None:
    if not isinstance(receipt, DeliveryReceipt) or receipt.channel != channel:
        raise DomainError("INVALID_DELIVERY")
    if not isinstance(receipt.destination, str) or not receipt.destination.strip():
        raise DomainError("INVALID_DELIVERY")
    if not isinstance(receipt.text, str) or not receipt.text.strip():
        raise DomainError("INVALID_DELIVERY")


class Outbox:
    """Готовое хранилище: студент его не переписывает."""

    def __init__(self):
        self._receipts = []

    def add(self, receipt: DeliveryReceipt) -> None:
        self._receipts.append(receipt)

    def all(self) -> tuple[DeliveryReceipt, ...]:
        return tuple(self._receipts)


class LegacyMailbox:
    """Локальная зависимость только для бонуса ЛР5; никакой сети."""

    def __init__(self):
        self.messages = []

    def store(self, destination: str, text: str) -> None:
        self.messages.append((destination, text))
