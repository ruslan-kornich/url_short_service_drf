import validators


def is_valid_url(val):
    valid = validators.url(val)
    if valid:
        return True
    else:
        return False
