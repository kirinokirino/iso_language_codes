==================
ISO Language Codes
==================


.. image:: https://img.shields.io/pypi/v/iso_language_codes.svg
        :target: https://pypi.python.org/pypi/iso_language_codes

.. image:: https://img.shields.io/travis/kirinokirino/iso_language_codes.svg
        :target: https://travis-ci.org/kirinokirino/iso_language_codes

.. image:: https://readthedocs.org/projects/iso-language-codes/badge/?version=latest
        :target: https://iso-language-codes.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




Get ISO code for a given language


* Free software: MIT license
* Documentation: https://iso-language-codes.readthedocs.io.


Usage
--------

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

Credits
-------
This package uses edited iso639-autonyms database from `bbqsrc/iso639-autonyms`
.. _`bbqsrc/iso639-autonyms`: https://github.com/bbqsrc/iso639-autonyms
This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
