#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `iso_language_codes` package."""


import unittest

from iso_language_codes import iso_language_codes


class TestIso_language_codes(unittest.TestCase):
    """Tests for `iso_language_codes` package."""

    def test_000_language(self):
        value = iso_language_codes.language('ru')
        self.assertEqual(value, {'Name': 'Russian', 'Autonym': 'Русский'})

    def test_001_language_name(self):
        value = iso_language_codes.language_name('ru')
        self.assertEqual(value, 'Russian')

    def test_002_language_autonym(self):
        value = iso_language_codes.language_autonym('ru')
        self.assertEqual(value, 'Русский')
