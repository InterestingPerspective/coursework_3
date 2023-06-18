def get_last_5_operations(sorted_operations):
    """
    Получает последние 5 выполненных операций
    """
    last_5 = []
    for operation in sorted_operations:
        if operation["state"] == "EXECUTED" and len(last_5) <= 4:
            last_5.append(operation)
        elif len(last_5) == 5:
            break

    return last_5
