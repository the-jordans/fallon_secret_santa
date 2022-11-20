# Fallon Secret Santa

Note: make sure you're using Python 3, consider adding `alias python=python3` to your `~/.zshrc` or `~/.bash_profile`

### Generate and Send Emails
1. `cd back_end`
1. `echo "export SENDGRID_API_KEY='{{insert API key here}}'" > sendgrid.env`
1. `source ./sendgrid.env`
1. `python email_sender.py`
