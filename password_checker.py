# Get password from user / input
password = input("Enter a password: ")

# Check password length
length = len(password)

# Check for different character types
has_uppercase = any(char.isupper() for char in password)
has_lowercase = any(char.islower() for char in password)
has_number = any(char.isdigit() for char in password)

# Check for special characters
special_characters = "!@#$%^&*()-_=+[]{};:'\",.<>?/\\|`~"
has_special = any(char in special_characters for char in password)

# Start score at zero
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

# Display the password analysis/ Output
print("\nPassword Analysis")
print("-----------------")
print("Length:", length)
print("Uppercase:", has_uppercase)
print("Lowercase:", has_lowercase)
print("Number:", has_number)
print("Special character:", has_special)
print("Score:", score)