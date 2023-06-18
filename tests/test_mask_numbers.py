from utils.mask_numbers import mask_numbers


def test_mask_numbers(some_operations):
    assert mask_numbers(some_operations[0]) == "Счет **1147 -> Счет **3001"
    assert mask_numbers(some_operations[1]) == "Счет **7865 -> Счет **1215"
    assert mask_numbers(some_operations[2]) == "MasterCard 1796 81** **** 9527 -> Visa Classic 7699 85** **** 9288"
    assert mask_numbers(some_operations[3]) == "Счет **8767"
    assert mask_numbers(some_operations[4]) == "Счет **4901 -> Счет **7621"
    assert mask_numbers(some_operations[5]) == "МИР 3766 44** **** 8784 -> Счет **3980"
    assert mask_numbers(some_operations[6]) == "Visa Platinum 5355 13** **** 8236 -> Maestro 8045 76** **** 9061"
