# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import gettext
import os
import sys

PY3 = sys.version_info > (3,)

LOCALES_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    'locales'
)


class Translator(object):

    def configure(self, locale):
        if not os.path.exists(os.path.join(LOCALES_DIR, locale)):
            locale = 'en'

        self.lang = gettext.translation(
            'messages', localedir=LOCALES_DIR, languages=[locale])
        self.lang.install()

    def translate(self, string):
        if PY3:
            return self.lang.gettext(string)
        else:
            return self.lang.ugettext(string)


class __proxy__(object):

    def __init__(self, string, translator):
        self.translator = translator
        self.string = string

    def __repr__(self):
        return self.translator.translate(self.string)

    def __str__(self):
        return self.translator.translate(self.string)


class LazyTranslator(object):

    def __init__(self):
        self.translator = Translator()

    def __call__(self, string):
        self.proxy = __proxy__(string, self.translator)

        return self.proxy


translate_lazy = LazyTranslator()
