from utils.load_operations import load_operations


def test_load_operations():
    assert isinstance(load_operations("operations.json"), list)
