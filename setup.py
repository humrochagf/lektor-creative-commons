from setuptools import setup

setup(
    name='lektor-creative-commons',
    version='0.1',
    author=u'Humberto Rocha',
    author_email='humrochagf@gmail.com',
    license='MIT',
    py_modules=['lektor_creative_commons'],
    entry_points={
        'lektor.plugins': [
            'creative-commons = lektor_creative_commons:CreativeCommonsPlugin',
        ]
    }
)
