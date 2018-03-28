from setuptools import setup

with open('README.md') as readme_file:
    README = readme_file.read()

setup(
    name='lektor-creative-commons',
    description='Lektor plugin to add Creative Commons license to your pages',
    long_description=README,
    long_description_content_type='text/markdown',
    version='0.1.3',
    url='https://github.com/humrochagf/lektor-creative-commons',
    author='Humberto Rocha',
    author_email='humrochagf@gmail.com',
    license='MIT',
    py_modules=['lektor_creative_commons'],
    entry_points={
        'lektor.plugins': [
            'creative-commons = lektor_creative_commons:CreativeCommonsPlugin',
        ]
    }
)
