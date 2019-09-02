=====
Usage
=====

Import this package in your script:
> `from iso_language_codes import *`

Get info about a language via Two-letter ISO code:
> `language('ru')`
> _{'Name': 'Russian', 'Autonym': 'Русский'}_

Or get name and autonym directly with:
> `language_name('ru')`
> _'Russian'_
> `language_autonym('ru')`
> _'Русский'_

You can also get entire dictionary of languages:
> `languages = language_dictionary()`
> `languages.keys()`
> _dict_keys(['', 'aa', 'bn', 'ab', ...])_