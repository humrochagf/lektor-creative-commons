#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import subprocess

from setuptools import find_packages, setup

try:
    import pypandoc
    README = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
    README = ''


def create_mo_files():
    data_files = []
    localedir = 'lektor_creative_commons/locales'
    po_dirs = [
        localedir + '/' + l + '/LC_MESSAGES/'
        for l in next(os.walk(localedir))[1]
    ]

    for d in po_dirs:
        mo_files = []
        po_files = [
            f for f in next(os.walk(d))[2] if os.path.splitext(f)[1] == '.po'
        ]

        for po_file in po_files:
            filename, extension = os.path.splitext(po_file)
            mo_file = filename + '.mo'
            msgfmt_cmd = 'msgfmt {} -o {}'.format(d + po_file, d + mo_file)
            subprocess.call(msgfmt_cmd, shell=True)
            mo_files.append(d + mo_file)

        data_files.append((d, mo_files))

    return data_files


setup(
    name='lektor-creative-commons',
    description='Lektor plugin to add Creative Commons license to your pages',
    long_description=README,
    version='0.3',
    url='https://github.com/humrochagf/lektor-creative-commons',
    author='Humberto Rocha',
    author_email='humrochagf@gmail.com',
    license='MIT',
    py_modules=['lektor_creative_commons'],
    entry_points={
        'lektor.plugins': [
            'creative-commons=lektor_creative_commons:CreativeCommonsPlugin',
        ]
    },
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    data_files=create_mo_files(),
)
