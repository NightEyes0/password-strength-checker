# Import functions from the password checker
from password_checker import check_password, calculate_score, get_strength


# Test password character checks
def test_check_password():
    result = check_password("Hello123!")

    assert result == (9, True, True, True, True)


# Test password scoring
def test_calculate_score():
    score = calculate_score(12, True, True, True, True)

    assert score == 100


# Test weak password rating
def test_weak_password():
    strength = get_strength(20, 0, True)

    assert strength == "VERY WEAK"


# Test strong password rating
def test_strong_password():
    strength = get_strength(85, 0, True)

    assert strength == "STRONG"


# Test compromised password rating
def test_compromised_password():
    strength = get_strength(100, 1000, True)

    assert strength == "COMPROMISED"