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

    def translate(self, string, arguments=None):
        if PY3:
            gettext = self.lang.gettext
        else:
            gettext = self.lang.ugettext

        translated = gettext(string)
        if arguments is not None:
            translated = translated % arguments

        return translated


class __proxy__(object):

    def __init__(self, string, translator, arguments):
        self.translator = translator
        self.string = string
        self.arguments = arguments

    def __repr__(self):
        return self.translator.translate(self.string, self.arguments)

    __str__ = __repr__


class LazyTranslator(object):

    def __init__(self):
        self.translator = Translator()

    def __call__(self, string, arguments=None):
        self.proxy = __proxy__(string, self.translator, arguments)

        return self.proxy


translate_lazy = LazyTranslator()
