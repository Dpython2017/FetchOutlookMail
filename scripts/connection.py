from exchangelib import Credentials, Configuration, Account, DELEGATE


def connect(server, email, username, password):
    """
    Get Exchange account connection with server
    """
    creds = Credentials(username=username, password=password)
    config = Configuration(server=server, credentials=creds)
    return Account(primary_smtp_address=email, autodiscover=False,
                   config = config, access_type=DELEGATE)
