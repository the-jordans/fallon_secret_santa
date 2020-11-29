import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, TemplateId, Substitution
from secret_santa_hub import return_matches_for_everyone, pull_to_email


def generate_message(to_email, gift_reciever):
    message = Mail(
        from_email='secret.santa@jordanfallon.com',
        to_emails=to_email
        )

    message.template_id = TemplateId('d-b1b2395dc84146e4b7cd441de7f01dd2')
    message.dynamic_template_data = {
            'giftReceiver': gift_reciever,
        }
    return message


def send_message(message):
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)


if __name__ == '__main__':
    to_email = pull_to_email('Jordan Hagan')
    gift_receiver = 'Test'
    msg = generate_message(to_email, gift_receiver)
    send_message(msg)



