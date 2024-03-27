import pytest
from data_structures.hashtable import Hashtable


def test_exists():
    assert Hashtable


#@pytest.mark.skip("TODO")
def test_get_apple():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    actual = hashtable.get("apple")
    expected = "Used for apple sauce"
    assert actual == expected


#@pytest.mark.skip("TODO")
def test_internals():
    hashtable = Hashtable(1024)
    hashtable.set("ahmad", 30)
    hashtable.set("silent", True)
    hashtable.set("listen", "to me")

    actual = []

    # Iterate over each bucket in the hashtable
    for bucket in hashtable._buckets:
        if bucket:  # Check if the bucket is not empty
            for key, value in bucket:
                actual.append((key, value))

    # Now 'actual' will contain all key-value pairs in the hashtable
