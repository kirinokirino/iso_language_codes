=====
Usage
=====

Import this package in your script:
.. code:: python

    from iso_language_codes import *

Get info about a language via Two-letter ISO code:
.. code:: python

    language('ru')

{'Name': 'Russian', 'Autonym': 'Русский'}

Or get name and autonym directly with:
.. code:: python

    language_name('ru')

'Russian'
.. code:: python

    language_autonym('ru')

'Русский'

You can also get entire dictionary of languages:
.. code:: python

    languages = language_dictionary()
    languages.keys()

dict_keys(['', 'aa', 'bn', 'ab', ...])