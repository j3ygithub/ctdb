from datetime import timedelta

from django.utils import timezone


def now():
    """
    Return a datetime.datetime object of now with timezone.localtime computed.
    """
    return timezone.localtime(timezone.now())


def today():
    """
    Return a datetime.date object of today with timezone.localtime computed.
    """
    return timezone.localtime(timezone.now()).date()


def tomorrow():
    """
    Return a datetime.date object of tomorrow with timezone.localtime computed.
    """
    return timezone.localtime(timezone.now() + timedelta(days=1)).date()


def date_range(start_date, end_date):
    """
    Given two datetime.date or datetime.datetime, retrun a date range.
    """
    days = (end_date - start_date).days
    date_range = [start_date + timedelta(n) for n in range(days)]
    return date_range


def remove_unnecessary_seperator(s, seperator):
    """
    Remove the trailing seperator if there is one.
    """
    if s[-1:] == seperator:
        return s[:-1]
    return s


def get_permission_codename(model_meta, action):
    """
    Return the codename of the permission for the specified action.
    """
    app_label, model_name = model_meta.app_label, model_meta.model_name
    codename = f'{app_label}.{action}_{model_name}'
    return codename


def has_add_permission(model_meta, user):
    """
    Return True if the given user has permission to add an object.
    """
    codename = get_permission_codename(model_meta, 'add')
    return user.has_perm(codename)
