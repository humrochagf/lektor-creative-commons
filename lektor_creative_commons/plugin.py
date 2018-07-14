# -*- coding: utf-8 -*-

from __future__ import unicode_literals

try:
    # python 3
    from urllib.error import URLError
except ImportError:
    # legacy python
    URLError = IOError

import os

from lektor.context import get_ctx
from lektor.pluginsystem import Plugin
from markupsafe import Markup

from .translation import translate_lazy as _

TEMPLATES = {
    'full': (
        '<a rel="license" target="_blank" href="https://creativecommons.org/'
        'licenses/{type}/{version}/deed.{locale}">'
        '<img alt="{license}" style="border-width:0" src="{icon_path}" />'
        '</a><br />{message} '
        '<a rel="license" target="_blank" href="https://creativecommons.org/'
        'licenses/{type}/{version}/deed.{locale}">{license}</a>.'
    ),
    'image-only': (
        '<a rel="license" target="_blank" href="https://creativecommons.org/'
        'licenses/{type}/{version}/deed.{locale}">'
        '<img alt="{license}" style="border-width:0" src="{icon_path}" /></a>'
    ),
    'text-only': (
        '{message} '
        '<a rel="license" target="_blank" href="https://creativecommons.org/'
        'licenses/{type}/{version}/deed.{locale}">{license}</a>.'
    ),
}

LICENSES = {
    'by': {
        'type': 'by',
        'version': '4.0',
        'license_type': _('Attribution'),
    },
    'by-nc': {
        'type': 'by-nc',
        'version': '4.0',
        'license_type': _('Attribution - NonCommercial'),
    },
    'by-sa': {
        'type': 'by-sa',
        'version': '4.0',
        'license_type': _('Attribution - ShareAlike'),
    },
    'by-nc-sa': {
        'type': 'by-nc-sa',
        'version': '4.0',
        'license_type': _('Attribution - NonCommercial - ShareAlike'),
    },
    'by-nd': {
        'type': 'by-nd',
        'version': '4.0',
        'license_type': _('Attribution - NoDerivatives'),
    },
    'by-nc-nd': {
        'type': 'by-nc-nd',
        'version': '4.0',
        'license_type': _('Attribution - NonCommercial - NoDerivatives'),
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

    def render_cc_license(self, type, size='normal', template='full',
                          caller=None):
        license = LICENSES[type].copy()
        license['size'] = LICENSE_SIZES[size]
        license['locale'] = self.locale
        license['message'] = _('This work is licensed under a')
        license['license'] = _(
            'Creative Commons %(license_type)s 4.0 International License',
            license
        )
        license['license_url'] = (
            'https://creativecommons.org/'
            'licenses/{type}/{version}/deed.{locale}'
        ).format(**license)
        license['icon_path'] = self.icon_path(license)

        if callable(caller):
            if caller.catch_kwargs:
                return Markup(caller(**license))
            else:
                license_subset = dict(
                    (argument_name, license[argument_name])
                    for argument_name in caller.arguments
                )

                return Markup(caller(**license_subset))

        return Markup(TEMPLATES[template].format(**license))

    def icon_path(self, license):
        icon_target_path = (
            '/static/lektor-creative-commons/{type}/{version}/{size}.png'
        ).format(**license)
        icon_source_path = os.path.join(
            os.path.dirname(__file__), 'assets', license['type'],
            license['version'], license['size'] + '.png'
        )
        ctx = get_ctx()

        @ctx.sub_artifact(
            icon_target_path,
            sources=[ctx.source.source_filename],
            source_obj=icon_source_path
        )
        def copy_icon(artifact):
            artifact.replace_with_file(artifact.source_obj, copy=True)

        return icon_target_path

    def on_setup_env(self, **extra):
        self.env.jinja_env.globals.update(
            render_cc_license=self.render_cc_license
        )
