# Lektor Creative Commons

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
