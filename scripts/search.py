import functools
from utils import check_range
import logging
from datetime import datetime


@functools.lru_cache(maxsize=200)
def search_mail(account, *args, **kwargs) -> dict:
    """
    Searches for mail for the current date and for a particular recipient
        :param account: user's account object
        :params *args: List of the search recipients
        :params **kwargs: Search Date
        :return: Boolean - If mail found marks status of the mail as True else marks False
        :rtype: dict
        :Example:
        >>> search_mail(account, 'dimple.mathew@cerner.com')
        {'email':True,...}

    """
    status = {}
    for recipient in args:

        for item in account.inbox.filter(sender=recipient).values('datetime_received'):
            received_date = str(item['datetime_received']).split(" ")[0]
            if received_date == kwargs['sender_date']:
                status[recipient] = True
                break
            elif not check_range(kwargs['sender_date'], received_date):
                status[recipient] = False
                break
    logging.info('Search result for {} is -->{}'.format(datetime, status))
    return status
