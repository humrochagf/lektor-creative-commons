# -*- coding: utf-8 -*-

import os

from markupsafe import Markup

from lektor.pluginsystem import Plugin

TEMPLATE = (
    '<a rel="license" href="http://creativecommons.org/licenses/' +
    '{type}/{version}/"><img alt="Creative Commons License" ' +
    'style="border-width:0" src="https://i.creativecommons.org/l/' +
    '{type}/{version}/{size}.png" /></a><br />This work is licensed under ' +
    'a <a rel="license" href="http://creativecommons.org/licenses/' +
    '{type}/{version}/">Creative Commons {permissions} {version} ' +
    'International License</a>.'
)

LICENSES = {
    'by': {
        'type': 'by',
        'version': '4.0',
        'permissions': 'Attribution',
    },
    'by-nc': {
        'type': 'by-nc',
        'version': '4.0',
        'permissions': 'Attribution-NonCommercial',
    },
    'by-sa': {
        'type': 'by-sa',
        'version': '4.0',
        'permissions': 'Attribution-ShareAlike',
    },
    'by-nc-sa': {
        'type': 'by-nc-sa',
        'version': '4.0',
        'permissions': 'Attribution-NonCommercial-ShareAlike',
    },
    'by-nd': {
        'type': 'by-nd',
        'version': '4.0',
        'permissions': 'Attribution-NoDerivatives',
    },
    'by-nc-nd': {
        'type': 'by-nc-nd',
        'version': '4.0',
        'permissions': 'Attribution-NonCommercial-NoDerivatives',
    },
}

LICENSE_SIZES = {
    'normal': '88x31',
    'compact': '80x15',
}


class CreativeCommonsPlugin(Plugin):
    name = u'Creative Commons'
    description = u'Add Creative Commons license to your pages.'

    def render_cc_license(self, type, size='normal'):
        license = LICENSES[type].copy()
        license['size'] = LICENSE_SIZES[size]

        return Markup(TEMPLATE.format(**license))

    def on_setup_env(self, **extra):
        self.env.jinja_env.globals.update(
            render_cc_license=self.render_cc_license
        )
