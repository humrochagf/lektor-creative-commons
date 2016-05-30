# Lektor Creative Commons

[![License: MIT](https://img.shields.io/pypi/l/lektor-creative-commons.svg)](https://github.com/humrochagf/lektor-creative-commons/blob/master/LICENSE)
[![Current version at PyPI](https://img.shields.io/pypi/v/lektor-creative-commons.svg)](https://pypi.python.org/pypi/lektor-creative-commons)
[![Downloads per month on PyPI](https://img.shields.io/pypi/dm/lektor-creative-commons.svg)](https://pypi.python.org/pypi/lektor-creative-commons)

Lektor plugin to add Creative Commons license to your pages


## Usage

On your templates use:

```
<div class="license">{{ render_cc_license(type, size) }}</div>
```

- `type` is a `string` with the license type (e.g.: `'by'`, `'by-sa'`, `'by-nc-sa'`).
- `size` is an opitional parameter with the size `'normal'` or `'compact'`. Default is `'normal'`

## Example

```
<div class="license">{{ render_cc_license('by-sa') }}</div>
```
