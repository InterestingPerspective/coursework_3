def mask_numbers(operation):
    """
    Скрывает цифры карт и счетов
    """
    if "from" in operation:
        if "Счет" in operation["from"]:
            masked_from = f"Счет **{operation['from'][-4:]}"
        else:
            masked_from = f"{operation['from'][:-16]}{operation['from'][-16:-12]} {operation['from'][-12:-10]}** **** \
{operation['from'][-4:]}"

    if "Счет" in operation["to"]:
        masked_to = f"Счет **{operation['to'][-4:]}"
    else:
        masked_to = f"{operation['to'][:-16]}{operation['to'][-16:-12]} {operation['to'][-12:-10]}** **** \
{operation['to'][-4:]}"

    if "from" in operation:
        return f"{masked_from} -> {masked_to}"
    else:
        return masked_to
