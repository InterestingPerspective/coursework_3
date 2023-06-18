import json


def load_operations(filename):
    """
    Заносит все операции из файла в переменную
    """
    with open(filename, encoding="utf-8") as file:
        data = json.load(file)
    return data
