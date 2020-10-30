from datetime import datetime
import logging
import re


def check_range(date1, date2) -> bool:
    return __check_date_range(date1, date2)


def __check_date_range(date1, date2):
    """
    Implementation detail that checks if the date of emails in the list is lesser than the search date
    in that case returns True to the parent method else returns False

    :param date1: search date
    :param date2: date of mails from inbox
    :rtype: bool

    """
    recipient_date = datetime.strptime(date1, '%Y-%m-%d')
    mail_date = datetime.strptime(date2, '%Y-%m-%d')

    if mail_date < recipient_date:
        return False
    return True


def to_email(assoc_id) -> str:
    """ Returns associate email """
    return assoc_id + '@cerner.net'


def validate(username, email):
    user = __validate_username(username)
    mail = __validate_email(email)
    if user and mail:
        return True
    return False


def __validate_username(username) -> bool:
    """
    Validating the username input from user
    :param username: str
    :rtype: bool
    """
    if 8 < len(username) < 8:
        logging.critical("Incorrect username entered, username entered is -->{}"
                         .format(username))
        raise ValueError('Please enter Associate ID of eight characters')
    return True


def __validate_email(email):
    """
    Validating email input from user
    :param email: str
    :rtype: bool
    """
    pattern = r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?"
    pattern = re.compile(pattern)
    if not re.match(pattern, email):
        logging.critical("Incorrect email entered, email entered is -->{}"
                         .format(email))
        raise ValueError("You failed to match %s" % email)
    return True
