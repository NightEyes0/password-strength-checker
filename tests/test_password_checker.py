# Import functions from the password checker
from password_checker import (
    check_password,
    calculate_score,
    check_pwned_password,
    get_strength
)

from unittest.mock import patch


# Test that all character types are detected
def test_check_password():
    result = check_password("Hello123!")

    assert result == (9, True, True, True, True)


# Test a password with only lowercase letters
def test_lowercase_password():
    result = check_password("hello")

    assert result == (5, False, True, False, False)


# Test a password with only numbers
def test_number_password():
    result = check_password("123456")

    assert result == (6, False, False, True, False)


# Test a password with a special character
def test_special_character():
    result = check_password("hello!")

    assert result == (6, False, True, False, True)


# Test the maximum password score
def test_maximum_score():
    score = calculate_score(12, True, True, True, True)

    assert score == 100


# Test a password with no requirements met
def test_zero_score():
    score = calculate_score(5, False, False, False, False)

    assert score == 0


# Test weak password rating
def test_weak_password():
    strength = get_strength(20, 0, True)

    assert strength == "VERY WEAK"


# Test moderate password rating
def test_moderate_password():
    strength = get_strength(60, 0, True)

    assert strength == "MODERATE"


# Test strong password rating
def test_strong_password():
    strength = get_strength(85, 0, True)

    assert strength == "STRONG"


# Test compromised password rating
def test_compromised_password():
    strength = get_strength(100, 1000, True)

    assert strength == "COMPROMISED"


# Test the HIBP function with a mocked API response
@patch("password_checker.urllib.request.urlopen")
def test_pwned_password(mock_urlopen):
    class FakeResponse:
        def read(self):
            return b"CBFDA5E9E5A8C1B2D3E4F5A6B7C8D9E0:12345\n"

    mock_urlopen.return_value = FakeResponse()

    result = check_pwned_password("password")

    assert result[1] is True