from calculator import add


def test_zero_for_empty_strings():
    """If function is calle with an empty string, the returned value should be zero."""
    assert add("") == 0
