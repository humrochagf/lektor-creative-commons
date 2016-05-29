from setuptools import setup

setup(
    name='lektor-creative-commons',
    description='Lektor plugin to add Creative Commons license to your pages',
    version='0.1.2',
    url='https://github.com/humrochagf/lektor-creative-commons',
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
