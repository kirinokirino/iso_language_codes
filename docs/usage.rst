=====
Usage
=====

Import this package in your script:

    >>> from iso_language_codes import *

Get info about a language via Two-letter ISO code:

    >>> language('ru')
{'Name': 'Russian', 'Autonym': 'Русский'}

Or get name and autonym directly with:

    >>> language_name('ru')
'Russian'

    >>> language_autonym('ru')
'Русский'

You can also get entire dictionary of languages:

    >>>languages = language_dictionary()
    >>>languages.keys()
dict_keys(['', 'aa', 'bn', 'ab', ...])