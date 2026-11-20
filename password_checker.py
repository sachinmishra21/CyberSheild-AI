import re

def check_password(password):

    score = 0
    remarks = []

    if len(password) >= 8:
        score += 20
    else:
        remarks.append("Password should contain at least 8 characters.")

    if re.search(r"[A-Z]", password):
        score += 20
    else:
        remarks.append("Add at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        score += 20
    else:
        remarks.append("Add at least one lowercase letter.")

    if re.search(r"\d", password):
        score += 20
    else:
        remarks.append("Add at least one number.")

    if re.search(r"[!@#$%^&*()_+=\-{}\[\]:;\"'<>,.?/]", password):
        score += 20
    else:
        remarks.append("Add at least one special character.")

    if score >= 80:
        strength = "Strong"
    elif score >= 50:
        strength = "Medium"
    else:
        strength = "Weak"

    return {
        "strength": strength,
        "score": score,
        "remarks": remarks
    }