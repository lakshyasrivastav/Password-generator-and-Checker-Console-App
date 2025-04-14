import re
import random
import string

def load_common_passwords(filepath="common_passwords.txt"):
    try:
        with open(filepath, "r") as file:
            return set(p.strip() for p in file.readlines())
    except FileNotFoundError:
        return set()

def check_strength(password, common_passwords):
    score = 0
    suggestions = []

    length = len(password)
    if length >= 8:
        score += 25
    else:
        suggestions.append("Use at least 8 characters.")

    if re.search(r"[A-Z]", password):
        score += 15
    else:
        suggestions.append("Add uppercase letters.")

    if re.search(r"[a-z]", password):
        score += 15
    else:
        suggestions.append("Add lowercase letters.")

    if re.search(r"[0-9]", password):
        score += 15
    else:
        suggestions.append("Add numbers.")

    if re.search(r"[^A-Za-z0-9]", password):
        score += 15
    else:
        suggestions.append("Add special characters (!, @, #, etc.)")

    if password.lower() not in common_passwords:
        score += 15
    else:
        suggestions.append("Avoid common passwords.")

    return score, suggestions

def generate_strong_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))
