from abc import ABC, abstractmethod

from app.support.types import DeliveryReceipt, contact
from app.support.errors import DomainError


class NotificationSender(ABC):
    """Абстрактный отправитель уведомлений (ЛР3: общий контракт)."""

    @abstractmethod
    def send(self, notification) -> DeliveryReceipt:
        """Отправить уведомление и вернуть квитанцию."""
        ...


class EmailSender(NotificationSender):
    def __init__(self, prefix: str = ""):
        self._prefix = prefix

    def send(self, notification) -> DeliveryReceipt:
        r = notification.recipient
        addr = contact(r.email)
        text = self._prefix + notification.message
        return DeliveryReceipt(channel="EMAIL", destination=addr, text=text)


class SmsSender(NotificationSender):
    def send(self, notification) -> DeliveryReceipt:
        r = notification.recipient
        addr = contact(r.phone)
        return DeliveryReceipt(channel="SMS", destination=addr, text=notification.message)