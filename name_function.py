import re
def get_formatted_name(first, last, middle=''):
    """Generate a neatly formatted full name."""
    full_name=first + ' ' + middle+' ' + last
    full_name=re.sub(' +',' ', full_name)
    return full_name.title()
    