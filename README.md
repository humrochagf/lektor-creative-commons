# Lektor Creative Commons

[![License: MIT](https://img.shields.io/pypi/l/lektor-creative-commons.svg)](https://github.com/humrochagf/lektor-creative-commons/blob/master/LICENSE)
[![Current version at PyPI](https://img.shields.io/pypi/v/lektor-creative-commons.svg)](https://pypi.python.org/pypi/lektor-creative-commons)
[![Downloads per month on PyPI](https://img.shields.io/pypi/dm/lektor-creative-commons.svg)](https://pypi.python.org/pypi/lektor-creative-commons)

Lektor plugin to add Creative Commons license to your pages


## Usage

On your templates use:

```
<div class="license">{{ render_cc_license(type, size, template, caller) }}</div>
```

- `type` is a `string` with the license type (e.g.: `'by'`, `'by-sa'`, `'by-nc-sa'`).
- `size` is an optional parameter with the size `'normal'` or `'compact'`. It defaults to `'normal'`.
- `template` is an optional parameter with the template `'full'`, `'image-only'` or `'text-only'`. It defaults to `'full'`.
- `locale` is an optional parameter that overrides the locale at function calling time.
- `caller` is an optional parameter that you can pass an callable to mount your own template. This argument is usually omitted. See the example of how to use it with the [Jinja call feature](http://jinja.pocoo.org/docs/2.10/templates/#call).

## Examples

Simply rendering the license of your choice:

```
<div class="license">{{ render_cc_license('by-sa') }}</div>
```

Using Jinja2 [call](http://jinja.pocoo.org/docs/2.10/templates/#call) block to inject your own template:

```
{% call(license, license_url, icon_path) render_cc_license('by-sa', size='normal') %}
  <a class="nav-item" rel="license" target="_blank" href="{{ license_url }}">
    <img alt="{{ license }}" style="border-width:0" src="{{ icon_path }}" />
  </a>
{% endcall %} 
```

There are more variables, you can check which with

```
{% call() render_cc_license('by-sa', size='normal') %}
  {{ kwargs }}
{% endcall %} 
```

Notice that using the call block it injects its content as `caller` parameter to the `render_cc_license` function that skips the need of choosing a template and renders your own.

## Internationalization support

This plugin has support to internationalization, and changes it language based on `.lektorproject` file.
The Current supported locales are:

- en
- pt_BR
- de

Any other locale will default to `en` (English).
