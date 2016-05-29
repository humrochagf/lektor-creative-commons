# -*- coding: utf-8 -*-

import os

from markupsafe import Markup

from lektor.pluginsystem import Plugin

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


    def __init__(self, *args, **kwargs):
        super(CreativeCommonsPlugin, self).__init__(*args, **kwargs)

        # append plugin templates to the template path
        self.env.jinja_env.loader.searchpath.append(
            os.path.join(self.path, 'templates'))

    def render_cc_license(self, type, size='normal'):
        license = LICENSES[type].copy()
        license['size'] = LICENSE_SIZES[size]

        return Markup(self.env.jinja_env.get_template(
            'creative-commons.html').render(license=license))

    def on_setup_env(self, **extra):
        self.env.jinja_env.globals.update(
            render_cc_license=self.render_cc_license
        )
