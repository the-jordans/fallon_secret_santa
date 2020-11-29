import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from secret_santa_hub import return_matches_for_everyone

message = Mail(
    from_email='secret.santa@jordanfallon.com',
    to_emails='jordan.hagan@gmail.com',
    subject='Test Email',
    html_content='<strong>and easy to do anywhere, even with Python</strong>')

try:
    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)