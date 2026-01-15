import pytest
from game_logic import check_name

def test_correct_name():
    assert check_name("Tushar") is True

def test_wrong_name():
    assert check_name("Rahul") is False

def test_empty_name():
    with pytest.raises(ValueError):
        check_name("")
