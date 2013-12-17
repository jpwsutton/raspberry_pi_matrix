try:
    from setuptools import setup
except:
    from distutils.core import setup

config = {
    'description': 'Raspberry Pi Matrix',
    'author': 'James sutton',
    'url': 'https://github.com/jpwsutton/raspberry_pi_-matrix',
    'download_url': 'https://github.com/jpwsutton/raspberry_pi_matrix',
    'author_email': 'code@jsutton.co.uk',
    'version': '0.1',
    'install_requires': [],
    'packages': ['raspberry_pi_matrix'],
    'scripts': [],
    'name': 'raspberry_pi_matrix'
}

setup(**config)
