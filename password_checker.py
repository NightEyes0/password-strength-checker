password = input("Enter a password: ")

length = len(password)
has_uppercase = any(char.isupper() for char in password)
has_lowercase = any(char.islower() for char in password)
has_number = any(char.isdigit() for char in password)

special_characters = "!@#$%^&*()-_=+[]{};:'\",.<>?/\\|`~"
has_special = any(char in special_characters for char in password)

score = 0

if length >= 8:
    score += 20

if length >= 12:
    score += 20

if has_uppercase:
    score += 15

print("\nPassword Analysis")
print("-----------------")
print("Length:", length)
print("Uppercase:", has_uppercase)
print("Lowercase:", has_lowercase)
print("Number:", has_number)
print("Special character:", has_special)
print("Score:", score)