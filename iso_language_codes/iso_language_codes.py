# -*- coding: utf-8 -*-
import shelve


def language(code):
    assert (len(code) == 2)  # Please provide a two-letter code
    code.lower()
    with shelve.open('language_codes.db', flag='r') as s:
        return s[f'{code}']


def language_name(code):
    assert (len(code) == 2)  # Please provide a two-letter code
    code.lower()
    with shelve.open('language_codes.db', flag='r') as s:
        return s[f'{code}']['Name']


def language_autonym(code):
    assert (len(code) == 2)  # Please provide a two-letter code
    code.lower()
    with shelve.open('language_codes.db', flag='r') as s:
        return s[f'{code}']['Autonym']


def language_dictionary():
    with shelve.open('language_codes.db', flag='r') as s:
        return dict(s)
