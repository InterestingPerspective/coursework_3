from utils.get_last_5_operations import get_last_5_operations


def test_get_last_5_operations(some_operations):
    assert [x["id"] for x in get_last_5_operations(some_operations)] == [361044570, 634356296, 893507143, 619287771, 580054042]
    