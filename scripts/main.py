import logging
from datetime import datetime
from getpass import getpass
from connection import connect
from search import search_mail
from utils import to_email, validate


def main() -> dict:
    """
    Connection Details

    username: ASSOCIATE_ID@cerner.net
    email: cerner email

    :Example:
       - username: DM050767@cerner.net
       - email: dimple.mathew@cerner.com

    To fetch the mails scripts connects to the office 365 server,
    authentication is done using LDAP creds.

    Once connection is established mail is search for the required
    recipients and for a particular date.

    :rtype: bool

    Methods
    ------
      search_mail(account,recipients, sender_date)
       :args: List of receipents
       :kwargs: sender_date:YYYY-MM-DD

    >>> main()
    {'Achievements@company.com': True, 'Dimple.Mathew@company.com': False}

    """
    logging.basicConfig(filename='app.log', filemode='a+',
                        format='%(name)s - %(levelname)s - %(message)s',
                        level=logging.DEBUG)

    server = 'outlook.office365.com'
    email = input(
        'Please enter your email: '
    )
    username = input(
        'Please enter your username: '
    )
    password = getpass()

    logging.info('Script initiated by {} at {}'.
                 format(username, datetime.now()))

    if validate(username, email):
        logging.info("User validated successfully.")
        username = to_email(username)
        account = connect(server, email, username, password)
        recipients = ['Achievements@company.com',
                      'DimpleMathew@company.com',]

        result = search_mail(account, *recipients,
                             sender_date="2020-09-10")
        return result


if __name__ == "__main__":
    print(main())
