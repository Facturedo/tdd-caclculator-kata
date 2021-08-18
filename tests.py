from calculator import add



def test_zero_for_empty_strings():
    """If function is called with an empty string, the returned value should be zero."""
    assert add("") == 0


def test_one_number():
    """If function is called with one number, the number is returned."""
    assert add("1") == 1

def test_two_numbers():
    """If function is called with two numbers, they are added."""
    assert add("1,2") == 3