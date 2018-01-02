from codecs import open
from os import path
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

def read(*parts):
    # intentionally *not* adding an encoding option to open
    # see here: https://github.com/pypa/virtualenv/issues/201#issuecomment-3145690
    return open(path.join(here, *parts), 'r').read()

setup(
    name='quickemailverification',
    version='1.0.1',
    description='Official QuickEmailVerification API library client for python',
    long_description=long_description,
    author='QuickEmailVerification',
    author_email='support@quickemailverification.com',
    url='https://github.com/quickemailverification/quickemailverification-python',
    license='MIT',
    install_requires=[
        'requests >= 2.1.0',
        'six >= 1.9.0'
    ],
    packages=[
        'quickemailverification',
        'quickemailverification.api',
        'quickemailverification.error',
        'quickemailverification.http_client'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
