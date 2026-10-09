def send_email(subject, body, to, cc=None,):
    if cc:
        print(f" Sending email to {to} with cc: {cc}")
    else:
        print(f" Sending email to {to} without cc")

send_email("Meeting Reminder", "Don't forget the meeting at 10 AM. Please be on time.", "colleague@example.com", "boss@example.com")

