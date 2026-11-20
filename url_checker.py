import re
import validators

SUSPICIOUS_WORDS = [
    "login",
    "verify",
    "update",
    "secure",
    "bank",
    "paypal",
    "free",
    "gift",
    "winner",
    "claim",
    "bonus",
    "crypto",
    "wallet"
]


def extract_urls(text):

    pattern = r'https?://[^\s]+|www\.[^\s]+'
    return re.findall(pattern, text)


def check_urls(text):

    urls = extract_urls(text)

    if len(urls) == 0:
        return False, []

    bad = []

    for url in urls:

        if not validators.url(url):
            bad.append(url)
            continue

        lower = url.lower()

        for word in SUSPICIOUS_WORDS:
            if word in lower:
                bad.append(url)
                break

    return len(bad) > 0, bad
import re

from url_checker import check_urls

PHISHING_KEYWORDS = [

    "verify",

    "urgent",

    "bank",

    "password",

    "otp",

    "account",

    "click",

    "winner",

    "gift",

    "free",

    "lottery",

    "claim",

    "bitcoin",

    "wallet",

    "security",

    "limited time",

    "login",

    "confirm"

]


def keyword_score(text):

    score = 0

    found = []

    lower = text.lower()

    for word in PHISHING_KEYWORDS:

        if word in lower:

            score += 6

            found.append(word)

    return score, found


def detect_threat(text):

    risk = 0

    reason = []

    score, words = keyword_score(text)

    risk += score

    if words:

        reason.append("Suspicious Keywords : " + ", ".join(words))

    has_bad_url, urls = check_urls(text)

    if has_bad_url:

        risk += 35

        reason.append("Suspicious URL Detected")

    if re.search(r"\b\d{6}\b", text):

        risk += 10

        reason.append("OTP Mentioned")

    if "http://" in text:

        risk += 10

        reason.append("HTTP (Not Secure)")

    if risk > 100:

        risk = 100

    if risk >= 80:

        threat = "High Risk Phishing"

    elif risk >= 50:

        threat = "Suspicious"

    elif risk >= 25:

        threat = "Needs Review"

    else:

        threat = "Safe"

    return {

        "type": threat,

        "risk": risk,

        "reason": ", ".join(reason)

    }