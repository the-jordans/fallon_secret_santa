import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, TemplateId, Substitution
from secret_santa_hub import return_matches_for_everyone

message = Mail(
    from_email='secret.santa@jordanfallon.com',
    to_emails='jordan.hagan@gmail.com'
    )

message.template_id = TemplateId('d-b1b2395dc84146e4b7cd441de7f01dd2')
message.dynamic_template_data = {
        'giftReceiver': 'Jordan-Test',
    }

try:
    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)