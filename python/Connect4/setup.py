

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Connect4 in Python',
    'author': 'Max Resnick',
    'url': 'URL to get it at.',
    'download_url': '',
    'author_email': 'max_resnick@fastmail.fm',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['connect4'],
    'scripts': [],
    'name': 'Connect4'
}

setup(**config)