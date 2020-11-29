# Fallon Secret Santa

### Backend
1. `cd back_end`
1. `pip install -r requirements.txt`
1. To start the app: `python app.py`
1. To run tests: `python test_secret_santa_hub.py`

Note: make sure you're using Python 3, consider adding `alias python=python3` to your `~/.zshrc` or `~/.bash_profile`

### Frontend
1. `cd front_end`
1. `yarn install`
1. `yarn serve`
1. Visit `localhost:8080` in your browser

### Generate and Send Emails
1. `cd back_end`
1. `echo "export SENDGRID_API_KEY='{{insert API key here}}'" > sendgrid.env`
1. `source ./sendgrid.env`
1. `python email_sender.py`
