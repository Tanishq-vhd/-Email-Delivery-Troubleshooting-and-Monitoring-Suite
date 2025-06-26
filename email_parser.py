from email import message_from_string

def parse_headers(raw_email):
    msg = message_from_string(raw_email)
    headers = ['From', 'To', 'Subject', 'Received', 'Authentication-Results']
    parsed = {}
    for header in headers:
        parsed[header] = msg.get(header)
        print(f"{header}: {parsed[header]}")
    return parsed
