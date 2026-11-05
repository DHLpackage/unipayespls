# Исходные проверки ЛР3

Успешных проверок: **4**. Ожидаемых падений: **21**.

Не завершены общий интерфейс, алгоритмы исполнителей и основной метод сервиса. Поэтому один незаполненный метод может вызвать несколько падений — это не несколько независимых задач.

Падения ниже связаны с конкретными требованиями [TASK.md](TASK.md). После обязательной части все они должны пройти. Бонус проверяется отдельно и не входит в эти числа.

## Новые последовательности и конфигурации

- `tests.test_progression::test_progression_failed_send_is_not_recorded`
- `tests.test_progression::test_progression_sender_success_error_success[EmailSender-good0-bad0]`
- `tests.test_progression::test_progression_sender_success_error_success[SmsSender-good1-bad1]`

## Предметный контракт и общий интерфейс

- `tests.test_contract::test_abstract_sender_cannot_be_instantiated`
- `tests.test_contract::test_delivery_is_returned_not_printed`
- `tests.test_contract::test_existing_channels[EMAIL-alice@example.test]`
- `tests.test_contract::test_existing_channels[SMS-+000001]`
- `tests.test_contract::test_missing_channel_contact_does_not_append[EMAIL-person0]`
- `tests.test_contract::test_missing_channel_contact_does_not_append[EMAIL-person2]`
- `tests.test_contract::test_missing_channel_contact_does_not_append[SMS-person1]`
- `tests.test_contract::test_phone_only_recipient_can_receive_sms`
- `tests.test_contract::test_repeat_is_two_explicit_deliveries`
- `tests.test_contract::test_sender_alone_checks_its_contact[EmailSender]`
- `tests.test_contract::test_sender_alone_checks_its_contact[SmsSender]`
- `tests.test_contract::test_sender_is_used_in_the_real_path`
- `tests.test_contract::test_senders_share_one_contract[EmailSender-EMAIL-alice@example.test]`
- `tests.test_contract::test_senders_share_one_contract[SmsSender-SMS-+000001]`
- `tests.test_contract::test_snapshot_and_receipt_are_read_only`
- `tests.test_contract::test_text_is_trimmed`
- `tests.test_contract::test_two_messages_keep_their_own_text`
- `tests.test_contract::test_unknown_channel_does_not_append`

## Порядок проверки

Из корня проекта: `python check.py lab03`. Сначала прочитайте первый traceback и ожидаемый результат сценария. Не отключайте тесты, которые пока не проходят.

Ошибка импорта или установки не относится к заданию. Если исходный набор результатов отличается, сохраните вывод и сообщите преподавателю; не удаляйте решения и служебные файлы.
