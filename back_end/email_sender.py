import json
import os
import random
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, TemplateId
from secret_santa_hub import return_matches_for_everyone, pull_to_email


def generate_message(to_email, gift_receiver):
    message = Mail(
        from_email='secret.santa@jordanfallon.com',
        to_emails=to_email
    )

    message.template_id = TemplateId('d-6717fc23c4af49e3aa57f5efd94a97fa')
    message.dynamic_template_data = {
        'giftReceiver': gift_receiver,
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


def email_pipeline(match):
    to_email = pull_to_email(match['giver'])
    gift_receiver = match['receiver']
    msg = generate_message(to_email, gift_receiver)
    send_message(msg)


def record(matches):
    for_hagan = [x for x in matches if x['receiver'] == 'Jordan Fallon']
    for_fallon = [x for x in matches if x not in for_hagan]
    random.shuffle(for_fallon)
    rando = for_fallon.pop()
    for_hagan.append(rando)

    f = open("secret_santas_for_fallon.json", "w")
    f.write(json.dumps(for_fallon, indent=4))
    f.close()

    f = open("secret_santas_for_hagan.json", "w")
    f.write(json.dumps(for_hagan, indent=4))
    f.close()


if __name__ == '__main__':
    matches = return_matches_for_everyone()
    record(matches)
    # for match in matches:
    #     email_pipeline(match)
