from utils.sort_operations import sort_operations


def test_sort_operations(some_operations):
    assert [x["date"] for x in sort_operations(some_operations)] == ["2019-12-03T04:27:03.427014", "2019-08-19T16:30:41.967497", "2018-11-23T23:52:36.999661", "2018-06-20T03:59:34.851630", "2018-03-02T02:03:11.563721", "2018-02-03T07:16:28.366141", "2018-01-21T01:10:28.317704"]
