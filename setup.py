try:
    from setuptools import setup
except:
    from distutils.core import setup

config = {
    'description': 'Raspberry Pi Matrix',
    'author': 'James sutton',
    'url': 'https://github.com/jpwsutton/raspberry-pi-matrix',
    'download_url': 'https://github.com/jpwsutton/raspberry-pi-matrix',
    'author_email': 'code@jsutton.co.uk',
    'version': '0.1',
    'install_requires': [],
    'packages': ['matrix'],
    'scripts': [],
    'name': 'raspberry-pi-matrix'
}

setup(**config)
