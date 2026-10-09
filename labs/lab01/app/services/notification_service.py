from app.domain.notification import Notification
from app.support.errors import DomainError
from app.support.types import (
    DeliveryReceipt,
    Outbox,
    contact,
    validate_receipt,
)


class NotificationService:
    """Выбирает канал, формирует квитанцию и ведёт журнал отправок."""

    def __init__(self) -> None:
        self._outbox = Outbox()

    def send(self, channel: str, notification: Notification) -> DeliveryReceipt:
        if channel == "EMAIL":
            destination = contact(notification.recipient.email)
        elif channel == "SMS":
            destination = contact(notification.recipient.phone)
        else:
            raise DomainError("UNSUPPORTED_CHANNEL")

        receipt = DeliveryReceipt(channel, destination, notification.message)
        validate_receipt(receipt, channel)
        self._outbox.add(receipt)
        return receipt

    def sent(self) -> tuple[DeliveryReceipt, ...]:
        return self._outbox.all()


# --- Переходные функции: сохраняют прежние имена и сигнатуры ---

def new_service() -> NotificationService:
    return NotificationService()


def send_message(service, channel, recipient, message):
    return service.send(channel, Notification(recipient, message))


def sent_messages(service):
    return service.sent()