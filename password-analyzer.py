import string

def check_password_strength(password):
    weaknesses = []

    if len(password) < 8:
        weaknesses.append("Password must be at least 8 characters long.")

    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)

    if not has_upper:
        weaknesses.append("Password should contain at least one uppercase letter.")
    if not has_lower:
        weaknesses.append("Password should contain at least one lowercase letter.")
    if not has_digit:
        weaknesses.append("Password should contain at least one digit.")
    if not has_special:
        weaknesses.append("Password should contain at least one special character.")

    
    if not weaknesses:
        print(" Password strength: Strong!")
    else:
        print(" Password strength: Weak. Please address the following issues:")
        for weakness in weaknesses:
            print(f"- {weakness}")
    
    return weaknesses

user_password = input("Enter a password to check its strength: ")
check_password_strength(user_password)