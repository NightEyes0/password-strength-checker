# Import libraries for hashing and API requests
import hashlib
import urllib.request

# Get the password from the user
password = input("Enter a password: ")

# Check the password length
length = len(password)

# Check for different character types
has_uppercase = any(char.isupper() for char in password)
has_lowercase = any(char.islower() for char in password)
has_number = any(char.isdigit() for char in password)

# Check for special characters
special_characters = "!@#$%^&*()-_=+[]{};:'\",.<>?/\\|`~"
has_special = any(char in special_characters for char in password)

# Start the score at zero
score = 0

# Award points based on password length
if length >= 8:
    score += 20

if length >= 12:
    score += 20

# Award points for character types
if has_uppercase:
    score += 15

if has_lowercase:
    score += 15

if has_number:
    score += 15

if has_special:
    score += 15

# Hash the password using SHA-1
password_hash = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()

# Split the hash into a 5-character prefix and the remaining suffix
hash_prefix = password_hash[:5]
hash_suffix = password_hash[5:]

# Check the password against the Have I Been Pwned API
url = f"https://api.pwnedpasswords.com/range/{hash_prefix}"
request = urllib.request.Request(
    url,
    headers={"User-Agent": "Password-Strength-Checker"}
)

response = urllib.request.urlopen(request)
data = response.read().decode("utf-8")

# Check whether the full hash appears in the API response
times_pwned = 0

for line in data.splitlines():
    returned_suffix, count = line.split(":")
    if returned_suffix == hash_suffix:
        times_pwned = int(count)
        break

# Determine the password strength
if score < 30:
    strength = "VERY WEAK"
elif score < 50:
    strength = "WEAK"
elif score < 70:
    strength = "MODERATE"
elif score < 90:
    strength = "STRONG"
else:
    strength = "VERY STRONG"

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
print("Times found in breaches:", times_pwned)