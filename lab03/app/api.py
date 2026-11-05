"""Готовый внешний контракт. Не изменять."""
from app.services.assembly import build_service
from app.services import notification_service as implementation


def create():
    return build_service()


def send(service, channel, recipient, message):
    return implementation.send_message(service, channel, recipient, message)


def sent(service):
    return implementation.sent_messages(service)
