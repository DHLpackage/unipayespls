import pytest
from app import api
from app.support.errors import DomainError


def assert_code(code, operation):
    with pytest.raises(DomainError) as error:
        operation()
    assert error.value.code == code

from app.support.types import Recipient, DeliveryReceipt


def recipient():
    return Recipient(email="alice@example.test", phone="+000001", push_token="device-1")


@pytest.mark.parametrize("channel,destination", [
    ("EMAIL", "alice@example.test"), ("SMS", "+000001"),
])
def test_existing_channels(channel, destination):
    service = api.create()
    result = api.send(service, channel, recipient(), "Покупка 4.50 EUR")
    assert result == DeliveryReceipt(channel, destination, "Покупка 4.50 EUR")
    assert api.sent(service) == (result,)


def test_two_messages_keep_their_own_text():
    service = api.create()
    first = api.send(service, "EMAIL", recipient(), "Первое")
    second = api.send(service, "SMS", recipient(), "Второе")
    assert first.text == "Первое"
    assert second.text == "Второе"
    assert api.sent(service) == (first, second)


def test_repeat_is_two_explicit_deliveries():
    service = api.create()
    api.send(service, "EMAIL", recipient(), "Повтор")
    api.send(service, "EMAIL", recipient(), "Повтор")
    assert len(api.sent(service)) == 2


def test_unknown_channel_does_not_append():
    service = api.create()
    before = api.sent(service)
    assert_code("UNSUPPORTED_CHANNEL", lambda: api.send(service, "UNKNOWN", recipient(), "OK"))
    assert api.sent(service) == before


def test_delivery_is_returned_not_printed(capsys):
    receipt = api.send(api.create(), "SMS", recipient(), "OK")
    assert isinstance(receipt, DeliveryReceipt)
    assert capsys.readouterr().out == ""


def test_snapshot_and_receipt_are_read_only():
    service = api.create()
    receipt = api.send(service, "EMAIL", recipient(), "OK")
    snapshot = api.sent(service)
    with pytest.raises((AttributeError, TypeError)):
        receipt.text = "Изменено"
    api.send(service, "EMAIL", recipient(), "Позже")
    assert snapshot == (receipt,)
    assert len(api.sent(service)) == 2
