# -*- coding: utf-8 -*-

import os

from setuptools import setup
from setuptools import find_packages


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()


setup(
    name='racka',
    version='0.1.dev0',
    description='racka',
    long_description=read('README.rst') +
                     read('HISTORY.rst'),
    classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
    ],
    keywords='web wsgi pylons pyramid',
    author='mr test',
    author_email='br@example.com',
    url='',
    license='BSD',
    packages=find_packages(),
    install_requires=[
        'setuptools',
        'pyramid',
        'pyramid_tm',
        'raven',
        'alembic',
        'zope.sqlalchemy',
        'pyramid_jinja2',
        'mock',
#        'pyramid_webassets',
#        'pyramid_marrowmailer',
    ],
    extras_require={
        'test': [
            'nose',
            'nose-selecttests',
            'coverage',
            'unittest2',
            'flake8',
            'webtest',
        ],
        'development': [
            'zest.releaser',
            'Sphinx',
            'pyramid_debugtoolbar',
            'waitress',
        ],
        'production': [
            'psycopg2',
            'gunicorn',
            'supervisor',
        ],
    },
    entry_points="""
    [paste.app_factory]
    main = racka:main

    [console_scripts]
    """,
    paster_plugins=['pyramid'],
    include_package_data=True,
    zip_safe=False,
)
