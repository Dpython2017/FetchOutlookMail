def get_recent_emails(account, folder_name, count):
    """
    Retrieve reverse ranked date received emails for a given folder
    """
    # Get the folder object
    folder = account.root / 'Top of Information Store' / folder_name
    # Get emails
    return folder.all().order_by('-datetime_received')[:count]