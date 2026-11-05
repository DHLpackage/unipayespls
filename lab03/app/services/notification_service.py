from app.domain.senders import EmailSender, SmsSender, NotificationSender
from app.support.types import DeliveryReceipt, validate_receipt, Outbox
from app.support.errors import DomainError


class NotificationService:
    def __init__(self):
        self._outbox = Outbox()
        self._senders: dict[str, NotificationSender] = {
            "EMAIL": EmailSender(),
            "SMS": SmsSender(),
        }

    def send(self, channel: str, notification) -> DeliveryReceipt:
        if channel not in self._senders:
            raise DomainError("UNSUPPORTED_CHANNEL")
        sender = self._senders[channel]
        receipt = sender.send(notification)
        validate_receipt(receipt, channel)
        self._outbox.add(receipt)
        return receipt

    def sent(self) -> tuple[DeliveryReceipt, ...]:
        return self._outbox.all()


def new_service():
    return NotificationService()


def send_message(service, channel, recipient, message):
    from app.domain.notification import Notification
    return service.send(channel, Notification(recipient, message))


def sent_messages(service):
    return service.sent()