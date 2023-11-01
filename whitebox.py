def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

import pytest

def test_divide_positive_numbers():
    result = divide(10, 2)
    assert result == 5

def test_divide_by_zero_raises_exception():
    with pytest.raises(ValueError):
        divide(10, 0)

if __name__ == '_main_':
    pytest.main()