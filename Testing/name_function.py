def get_formatted_name(first, middle, last=''):
    """Строит отформатированное полное имя."""
    if last:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + middle
    return full_name.title()
