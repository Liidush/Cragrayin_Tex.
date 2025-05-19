import re

def is_suspicious_email(text):
    phishing_keywords = ['urgent', 'verify your account', 'click here', 'limited time', 'pay now']
    url_pattern = r'http[s]?://[^\s]+'

    urls = re.findall(url_pattern, text.lower())
    for keyword in phishing_keywords:
        if keyword in text.lower():
            return True, urls
    return False, urls

email_body = """
Hello,

We noticed suspicious activity in your Paylater account.
Please verify your account immediately: http://suspicious-link.com/verify

Thank you!
"""

suspicious, links = is_suspicious_email(email_body)
if suspicious:
    print("Warning: Possible phishing email detected.")
    print("Found links:", links)
else:
    print("No phishing signs found.")

