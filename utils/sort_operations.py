def sort_operations(operations):
    """
    Сортирует все операции по дате, начиная с последней, и убирает пустые словари
    """
    sorted_operations = sorted(
        filter(None, operations),
        key=lambda x: x['date'],
        reverse=True
    )
    return sorted_operations
