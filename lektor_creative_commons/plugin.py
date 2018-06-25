# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from lektor.context import get_ctx
from lektor.pluginsystem import Plugin
from markupsafe import Markup

from .translation import translate_lazy as _

TEMPLATES = {
    'full': (
        '<a rel="license" target="_blank" href="https://creativecommons.org/'
        'licenses/{type}/{version}/deed.{locale}">'
        '<img alt="{license}" style="border-width:0" '
        'src="/static/lektor-creative-commons/{type}/{version}/{size}.png" />'
        '</a><br />{message} '
        '<a rel="license" target="_blank" href="https://creativecommons.org/'
        'licenses/{type}/{version}/deed.{locale}">{license}</a>.'
    ),
    'image-only': (
        '<a rel="license" target="_blank" href="https://creativecommons.org/'
        'licenses/{type}/{version}/deed.{locale}">'
        '<img alt="{license}" style="border-width:0" '
        'src="/static/lektor-creative-commons/{type}/{version}/{size}.png" />'
        '</a>'
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
        self._has_copied = False
        
        super(CreativeCommonsPlugin, self).__init__(env, id)

    def render_cc_license(self, type, size='normal', template='full',
                          caller=None):
        self.trigger_icon_copying()
        
        license = LICENSES[type].copy()
        license['size'] = LICENSE_SIZES[size]
        license['locale'] = self.locale
        license['message'] = _('This work is licensed under a')
        license['license'] = _(
            'Creative Commons %(license_type)s 4.0 International License',
            license
        )

        if callable(caller):
            return Markup(caller(**license))

        return Markup(TEMPLATES[template].format(**license))
    
    def trigger_icon_copying(self):
        if self._has_copied:
            return
        
        def download_icon_if_neccessary(artifact):
            with artifact.open('wb') as arifact_file:
                # FIXME needs python2/3 support
                from  urllib.request import urlopen
                response = urlopen(artifact.source_obj)
                arifact_file.write(response.read())
        ctx = get_ctx()
        for license_type, license in LICENSES.items():
            for size_name, size in LICENSE_SIZES.items():
                # url_template = 'https://i.creativecommons.org/l/{type}/{version}/{size}.png'
                url_template = 'https://licensebuttons.net/l/{type}/{version}/{size}.png'
                url = url_template.format(
                    type=license_type, version=license['version'], size=size,
                )
                path = '/static/lektor-creative-commons/{type}/{version}/{size}.png'.format(
                    type=license_type, version=license['version'], size=size,
                )
                # FIXME bug in lektor? should be able to leave out sources argument
                artifact_hook = ctx.sub_artifact(path, source_obj=url, sources=ctx.artifact.sources)
                artifact_hook(download_icon_if_neccessary)
        
        self._has_copied = True
        
    
    def on_setup_env(self, **extra):
        self.env.jinja_env.globals.update(
            render_cc_license=self.render_cc_license
        )
    
