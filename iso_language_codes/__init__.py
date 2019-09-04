# -*- coding: utf-8 -*-

import shelve
from pathlib import Path

db = str(Path(__file__).resolve().parent.joinpath('language_codes.db'))


def language(code):
    """Get name and autonym for a given two-letter language code.

    :param code: two-letter ISO language code
    :type code: str
    :return: {'Name': String with english name,
              'Autonym': String with native name}
    :rtype: dict
    :raises KeyError: raises key exception
    :raises TypeError: raises type exception
    :raises AssertionError: raises assert exception

    """
    assert (len(code) == 2)  # Please provide a two-letter code
    with shelve.open(db, flag='r') as s:
        return s[code.lower()]


def language_name(code):
    """Get name for a given two-letter language code.

    :param code: two-letter ISO language code
    :type code: str

    """
    assert (len(code) == 2)  # Please provide a two-letter code
    with shelve.open(db, flag='r') as s:
        return s[code.lower()]['Name']


def language_autonym(code):
    """Get autonym for a given two-letter ISO language code.

    :param code: two-letter ISO language code
    :type code: str

    """
    assert (len(code) == 2)  # Please provide a two-letter code
    with shelve.open(db, flag='r') as s:
        return s[code.lower()]['Autonym']


def language_dictionary():
    """Get entire dictionary. Two-letter code as keys."""
    with shelve.open(db, flag='r') as s:
        return dict(s)


__author__ = """Andrei Ruzin"""
__email__ = 'kirinokirino2501@gmail.com'
__version__ = '1.0.6'
