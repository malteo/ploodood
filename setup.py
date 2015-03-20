from setuptools import setup

setup(
    name='ploodood',
    version='0.1',
    py_modules=['ploodood'],
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
