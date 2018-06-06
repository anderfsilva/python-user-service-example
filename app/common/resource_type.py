from validate_email import validate_email


def email(email_str):
    """
    Return email_str if valid, raise an exception in other case.
    """

    if validate_email(email_str):
        return email_str
    else:
        raise ValueError('The given email [{}] is not valid.'.format(email_str))
