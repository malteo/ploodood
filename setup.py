from setuptools import setup

setup(
    name='ploodood',
    version='0.1',
    description='Generates words that "sound like real words"',
    author = 'Matteo Giordano',
    author_email = 'ilmalteo@gmail.com',
    url = 'https://github.com/malteo/ploodood',
    download_url = 'https://github.com/malteo/ploodood/tarball/0.1',
    keywords = ['password', 'generator', 'cli', 'command line'],
    packages=['ploodood'],
    py_modules=['ploodood'],
    classifiers = [],
    install_requires=[
        'Click',
        'Requests',
        'untangle'
    ],
    entry_points='''
        [console_scripts]
        ploodood=ploodood:ploodood
    ''',
)
