from setuptools import setup

setup(
    name='pytzconvert',
    version='0.2',
    packages=['pytzconvert',],
    description= "Convert non-pytz timezones to pytz timezones.",
    long_description=open('README.md').read(),
    url="https://github.com/rchrd2/pytzconvert",
    author="Richard Caceres",
    author_email="me@rchrd.net",
    install_requires=['pytz']
)
