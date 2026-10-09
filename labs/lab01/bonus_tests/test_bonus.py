import pytest
from app import api
from app.support.errors import DomainError


def assert_code(code, operation):
    with pytest.raises(DomainError) as error:
        operation()
    assert error.value.code == code

from app.support.types import Recipient, DeliveryReceipt

def test_description_has_no_contacts():
    from app.domain import notification as module
    assert hasattr(module, "Notification"), "Сначала выполните обязательную ЛР1"
    message = module.Notification(Recipient(email="private@example.test"), "Покупка 4.50 EUR")
    assert message.describe() == "message=Покупка 4.50 EUR"
