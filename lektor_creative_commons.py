# -*- coding: utf-8 -*-

import os
from gettext import translation

from lektor.pluginsystem import Plugin
from markupsafe import Markup


LOCALES_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    'locales'
)


class Translator(object):

    def configure(self, locale):
        self.lang = translation(
            'messages', localedir=LOCALES_DIR, languages=[locale])
        self.lang.install()

    def translate(self, string):
        return self.lang.gettext(string)


class __proxy__(object):

    def __init__(self, string, translator):
        self.translator = translator
        self.string = string

    def __repr__(self):
        return self.translator.translate(self.string)

    def __str__(self):
        return self.translator.translate(self.string)


class translate_lazy(object):

    def __init__(self):
        self.translator = Translator()

    def __call__(self, string):
        self.proxy = __proxy__(string, self.translator)

        return self.proxy


_ = translate_lazy()


TEMPLATE = (
    '<a rel="license" target="_blank" href="http://creativecommons.org/'
    'licenses/{type}/{version}/deed.{locale}">'
    '<img alt="Creative Commons {type}" style="border-width:0" '
    'src="https://i.creativecommons.org/l/{type}/{version}/{size}.png" />'
    '</a><br />{message} '
    '<a rel="license" target="_blank" href="http://creativecommons.org/'
    'licenses/{type}/{version}/deed.{locale}">{license}</a>.'
)

LICENSES = {
    'by': {
        'type': 'by',
        'version': '4.0',
        'license': _(
            'Creative Commons Attribution 4.0 International License'
        ),
    },
    'by-nc': {
        'type': 'by-nc',
        'version': '4.0',
        'license': _(
            'Creative Commons Attribution-NonCommercial '
            '4.0 International License'
        ),
    },
    'by-sa': {
        'type': 'by-sa',
        'version': '4.0',
        'license': _(
            'Creative Commons Attribution-ShareAlike 4.0 '
            'International License'
        ),
    },
    'by-nc-sa': {
        'type': 'by-nc-sa',
        'version': '4.0',
        'license': _(
            'Creative Commons Attribution-NonCommercial-ShareAlike '
            '4.0 International License'
        ),
    },
    'by-nd': {
        'type': 'by-nd',
        'version': '4.0',
        'license': _(
            'Creative Commons Attribution-NoDerivatives 4.0 '
            'International License'
        ),
    },
    'by-nc-nd': {
        'type': 'by-nc-nd',
        'version': '4.0',
        'license': _(
            'Creative Commons Attribution-NonCommercial-NoDerivatives '
            '4.0 International License'
        ),
    },
}

LICENSE_SIZES = {
    'normal': '88x31',
    'compact': '80x15',
}


class CreativeCommonsPlugin(Plugin):

    name = 'Creative Commons'
    description = 'Add Creative Commons license to your pages.'

    def __init__(self, env, id):
        self.locale = env.load_config().site_locale or 'en'
        _.translator.configure(self.locale)

        super(CreativeCommonsPlugin, self).__init__(env, id)

    def render_cc_license(self, type, size='normal'):
        license = LICENSES[type].copy()
        license['size'] = LICENSE_SIZES[size]
        license['locale'] = self.locale
        license['message'] = _('This work is licensed under a')

        return Markup(TEMPLATE.format(**license))

    def on_setup_env(self, **extra):
        self.env.jinja_env.globals.update(
            render_cc_license=self.render_cc_license
        )
