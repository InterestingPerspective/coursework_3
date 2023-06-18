from utils.date_converter import convert_date


def test_convert_date(some_operations):
    assert convert_date(some_operations[0]) == "02.03.2018"
    assert convert_date(some_operations[1]) == "21.01.2018"
    assert convert_date(some_operations[2]) == "03.12.2019"
    assert convert_date(some_operations[3]) == "03.02.2018"
    assert convert_date(some_operations[4]) == "19.08.2019"
    assert convert_date(some_operations[5]) == "20.06.2018"
    assert convert_date(some_operations[6]) == "23.11.2018"
    