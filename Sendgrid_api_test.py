import requests

def send_via_sendgrid(api_key, from_email, to_email, subject, content):
    url = "https://api.sendgrid.com/v3/mail/send"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "personalizations": [{"to": [{"email": to_email}]}],
        "from": {"email": from_email},
        "subject": subject,
        "content": [{"type": "text/plain", "value": content}]
    }
    response = requests.post(url, json=data, headers=headers)
    print(" Status Code:", response.status_code)
    print("Response:", response.text)
