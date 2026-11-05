import pytest
from datetime import date, datetime, timezone
from decimal import Decimal
from app import api
from app.support.errors import DomainError


def code(expected, operation):
    with pytest.raises(DomainError) as caught:
        operation()
    assert caught.value.code == expected

from app.domain.notification import Notification
from app.domain.senders import EmailSender, SmsSender
from app.support.types import Recipient, DeliveryReceipt

@pytest.mark.parametrize("sender,good,bad", [
 (EmailSender, Recipient(email="a@test"), Recipient(phone="123")),
 (SmsSender, Recipient(phone="123"), Recipient(email="a@test"))])
def test_progression_sender_success_error_success(sender, good, bad):
    sender = sender()
    first = sender.send(Notification(good, "FIRST"))
    code("MISSING_CONTACT", lambda: sender.send(Notification(bad, "FAILED")))
    third = sender.send(Notification(good, "THIRD"))
    assert isinstance(first, DeliveryReceipt) and isinstance(third, DeliveryReceipt)
    assert (first.text, third.text) == ("FIRST", "THIRD")

def test_progression_failed_send_is_not_recorded():
    service = api.create()
    first = api.send(service, "EMAIL", Recipient(email="a@test"), "FIRST")
    before = api.sent(service)
    code("MISSING_CONTACT", lambda: api.send(service, "EMAIL", Recipient(phone="1"), "FAILED"))
    assert api.sent(service) == before
    third = api.send(service, "EMAIL", Recipient(email="c@test"), "THIRD")
    assert api.sent(service) == (first, third)
    assert first.destination == "a@test" and third.destination == "c@test"
