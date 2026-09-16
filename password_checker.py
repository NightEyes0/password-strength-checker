# Import libraries for hashing, API requests, and password generation
import hashlib
import urllib.request
import secrets
import string

# Check the password for different character types
def check_password(password):
    length = len(password)
    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_number = any(char.isdigit() for char in password)

    special_characters = "!@#$%^&*()-_=+[]{};:'\",.<>?/\\|`~"
    has_special = any(char in special_characters for char in password)

    return length, has_uppercase, has_lowercase, has_number, has_special

# Generate a secure random password
def generate_password(length=16):
    if length < 4:
        raise ValueError("Password length must be at least 4.")

    special_characters = "!@#$%^&*()-_=+[]{};:'\",.<>?/\\|`~"
    password_characters = [
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.digits),
        secrets.choice(special_characters)
    ]

    all_characters = string.ascii_letters + string.digits + special_characters

    while len(password_characters) < length:
        password_characters.append(secrets.choice(all_characters))

    secrets.SystemRandom().shuffle(password_characters)

    return "".join(password_characters)

# Calculate the password score
def calculate_score(length, has_uppercase, has_lowercase, has_number, has_special):
    score = 0

    if length >= 8:
        score += 20
    if length >= 12:
        score += 20
    if has_uppercase:
        score += 15
    if has_lowercase:
        score += 15
    if has_number:
        score += 15
    if has_special:
        score += 15

    # Short passwords cannot receive a high score
    if length < 8:
        score = min(score, 20)

    return score

# Generate recommendations for improving the password
def get_recommendations(length, has_uppercase, has_lowercase, has_number, has_special):
    recommendations = []

    if length < 8:
        recommendations.append("Use at least 8 characters.")
    if length < 12:
        recommendations.append("Consider using at least 12 characters.")
    if not has_uppercase:
        recommendations.append("Add an uppercase letter.")
    if not has_lowercase:
        recommendations.append("Add a lowercase letter.")
    if not has_number:
        recommendations.append("Add a number.")
    if not has_special:
        recommendations.append("Add a special character.")

    if not recommendations:
        recommendations.append("Your password meets all basic requirements.")

    return recommendations

# Check the password against the Have I Been Pwned API
def check_pwned_password(password):
    password_hash = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    hash_prefix = password_hash[:5]
    hash_suffix = password_hash[5:]

    try:
        url = f"https://api.pwnedpasswords.com/range/{hash_prefix}"
        request = urllib.request.Request(
            url,
            headers={"User-Agent": "Password-Strength-Checker"}
        )

        response = urllib.request.urlopen(request)
        data = response.read().decode("utf-8")

        for line in data.splitlines():
            returned_suffix, count = line.split(":")

            if returned_suffix == hash_suffix:
                return int(count), True

        return 0, True

    except urllib.error.URLError:
        return 0, False

# Determine the password strength
def get_strength(score, times_pwned, breach_check_available):
    if breach_check_available and times_pwned > 0:
        return "COMPROMISED"

    if score < 30:
        return "VERY WEAK"
    elif score < 50:
        return "WEAK"
    elif score < 70:
        return "MODERATE"
    elif score < 90:
        return "STRONG"
    else:
        return "VERY STRONG"

# Run the password checker
def main():
    # Get the password from the user
    password = input("Enter a password: ")

    # Analyse the password
    length, has_uppercase, has_lowercase, has_number, has_special = check_password(password)

    # Calculate the password score
    score = calculate_score(
        length,
        has_uppercase,
        has_lowercase,
        has_number,
        has_special
    )

    # Check whether the password has appeared in breaches
    times_pwned, breach_check_available = check_pwned_password(password)

    # Determine the password strength
    strength = get_strength(score, times_pwned, breach_check_available)

    # Generate recommendations
    recommendations = get_recommendations(
        length,
        has_uppercase,
        has_lowercase,
        has_number,
        has_special
    )

    # Display the password analysis
    print("\nPassword Analysis")
    print("-----------------")
    print("Length:", length)
    print("Uppercase:", has_uppercase)
    print("Lowercase:", has_lowercase)
    print("Number:", has_number)
    print("Special character:", has_special)
    print("Score:", score)
    print("Strength:", strength)

    if breach_check_available:
        print("Times found in breaches:", times_pwned)
    else:
        print("Breach check: Unavailable")

    # Display recommendations
    print("\nRecommendations")
    print("----------------")

    for recommendation in recommendations:
        print("-", recommendation)

# Only run the program when this file is executed directly
if __name__ == "__main__":
    main()