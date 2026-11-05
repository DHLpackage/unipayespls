import pytest
from app import api
from app.support.errors import DomainError


def assert_code(code, operation):
    with pytest.raises(DomainError) as error:
        operation()
    assert error.value.code == code

from app.support.types import Recipient, DeliveryReceipt

def test_email_prefix_is_optional():
    from app.domain.notification import Notification
    from app.domain.senders import EmailSender
    notification = Notification(Recipient(email="a@example.test"), "OK")
    assert EmailSender().send(notification).text == "OK"
    assert EmailSender(prefix="[TEST] ").send(notification).text == "[TEST] OK"
