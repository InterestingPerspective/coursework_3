import datetime


def convert_date(operation):
    """
    Конвертирует дату в формат ДД.ММ.ГГГГ
    """
    return datetime.datetime.strptime(operation["date"], '%Y-%m-%dT%H:%M:%S.%f').strftime('%d.%m.%Y')
