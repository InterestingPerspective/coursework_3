import pytest


@pytest.fixture
def some_operations():
    return [
        {
            "id": 361044570,
            "state": "EXECUTED",
            "date": "2018-03-02T02:03:11.563721",
            "operationAmount": {
                "amount": "7484.91",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 96008924215040031147",
            "to": "Счет 30377212495530283001"
        },
        {
            "id": 634356296,
            "state": "EXECUTED",
            "date": "2018-01-21T01:10:28.317704",
            "operationAmount": {
                "amount": "96900.90",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 33407225454123927865",
            "to": "Счет 79619011266276091215"
        },
        {
            "id": 560813069,
            "state": "CANCELED",
            "date": "2019-12-03T04:27:03.427014",
            "operationAmount": {
                "amount": "17628.50",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "MasterCard 1796816785869527",
            "to": "Visa Classic 7699855375169288"
        },
        {
            "id": 893507143,
            "state": "EXECUTED",
            "date": "2018-02-03T07:16:28.366141",
            "operationAmount": {
                "amount": "90297.21",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 37653295304860108767"
        },
        {
            "id": 619287771,
            "state": "EXECUTED",
            "date": "2019-08-19T16:30:41.967497",
            "operationAmount": {
                "amount": "81150.87",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 17691325653939384901",
            "to": "Счет 49304996510329747621"
        },
        {
            "id": 580054042,
            "state": "EXECUTED",
            "date": "2018-06-20T03:59:34.851630",
            "operationAmount": {
                "amount": "96350.51",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на счет",
            "from": "МИР 3766446452238784",
            "to": "Счет 86655182730188443980"
        },
        {
            "id": 34148726,
            "state": "EXECUTED",
            "date": "2018-11-23T23:52:36.999661",
            "operationAmount": {
                "amount": "79428.73",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Platinum 5355133159258236",
            "to": "Maestro 8045769817179061"
        }
    ]
