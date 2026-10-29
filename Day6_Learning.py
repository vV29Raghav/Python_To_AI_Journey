
import unittest
from unittest.mock import Mock, patch
import pytest

#Application code
def add(a, b):
    return a + b

def get_data(api):
    return api.fetch()


#unittest
class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_error(self):
        with self.assertRaises(ValueError):
            raise ValueError("Invalid input")


#Pytest fixture
@pytest.fixture
def api():
    mock_api = Mock()
    mock_api.fetch.return_value = "Success"
    return mock_api


def test_get_data(api):
    assert get_data(api) == "Success"


#Parameterization
@pytest.mark.parametrize(
    "a, b, expected",
    [(1, 2, 3), (3, 4, 7), (5, 5, 10)]
)
def test_add_multiple(a, b, expected):
    assert add(a, b) == expected


#Mocking exceptions
def test_api_error(api):
    api.fetch.side_effect = TimeoutError("API timeout")

    with pytest.raises(TimeoutError):
        get_data(api)


#Patching
def test_patch():
    with patch("test_demo.add", return_value=100):
        assert add(2, 3) == 100


if __name__ == "__main__":
    unittest.main()
