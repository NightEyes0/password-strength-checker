# Password Strength Checker

A Python-based password strength checker that analyses password complexity, checks whether a password has appeared in known data breaches, provides improvement recommendations, and can generate secure random passwords.

# Features

- Checks password length
- Detects uppercase letters
- Detects lowercase letters
- Detects numbers
- Detects special characters
- Calculates a password strength score from 0–100
- Rates passwords from Very Weak to Very Strong
- Checks passwords against the Have I Been Pwned API
- Warns when a password has appeared in known breaches
- Provides recommendations for improving passwords
- Generates secure random passwords 
- Includes automated unit tests
- Handles invalid input and API errors

# Technologies

- Python
- Pytest
- Have I Been Pwned API
- `hashlib`
- `urllib`
- `secrets`

## How It Works

The password is analysed for:

1. Length
2. Uppercase characters
3. Lowercase characters
4. Numbers
5. Special characters

These characteristics are used to calculate a score out of 100.
The password is also checked against the Have I Been Pwned API. Only the first five characters are sent to the API rather than the password itself.

# Strength Ratings

0–29 VERY WEAK 
30–49 WEAK 
50–69 MODERATE 
70–89 STRONG 
90–100 VERY STRONG 

If a password is found in a known breach, it is marked as COMPROMISED

## Running the Program

Run the password checker with:
python password_checker.py
Run the tests with
python -m pytest

