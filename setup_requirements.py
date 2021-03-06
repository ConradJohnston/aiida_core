# -*- coding: utf-8 -*-
###########################################################################
# Copyright (c), The AiiDA team. All rights reserved.                     #
# This file is part of the AiiDA code.                                    #
#                                                                         #
# The code is hosted on GitHub at https://github.com/aiidateam/aiida_core #
# For further information on the license, see the LICENSE.txt file        #
# For further information please visit http://www.aiida.net               #
###########################################################################

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import
install_requires = [
    'reentry==1.2.1',
    'python-dateutil==2.7.2',
    'python-mimeparse==1.6.0',
    'django==1.8.19',
    'django-extensions==1.5.0',
    'tzlocal==1.5.1',
    'pytz==2018.4',
    'PyYAML==3.12',
    'six==1.11.0',
    'anyjson==0.3.3',
    'psutil==5.4.5',
    'meld3==1.0.2',
    'mock==2.0.0',
    'numpy==1.14.3',
    'SQLAlchemy==1.2.12',
    'SQLAlchemy-Utils==0.33.0',
    'alembic==0.9.9',
    'ujson==1.35',
    'aldjemy==0.8.0',
    'passlib==1.7.1',
    'validate-email==1.3',
    'click==6.7',
    'click-completion==0.3.1',
    'click-plugins==1.0.3',
    'click-spinner==0.1.7',
    'tabulate==0.8.2',
    'ete3==3.1.1',
    'uritools==2.1.0',
    'psycopg2-binary==2.7.4',
    'paramiko==2.4.2',
    'ecdsa==0.13',
    'ipython>=4.0,<6.0',  # Version of ipython non enforced, because some still prefer version 4 rather than the latest
    'plumpy==0.11.4',
    'circus==0.14.0',
    'tornado==4.5.3',  # As of 2018/03/06 Tornado released v5.0 which breaks circus 0.14.0
    'pyblake2==1.1.2; python_version<"3.6"',
    'chainmap; python_version<"3.5"',
    'pathlib2; python_version<"3.5"',
    'singledispatch>=3.4.0.3; python_version<"3.5"',
    'enum34==1.1.6; python_version<"3.5"',
    'simplejson==3.16.0'
]

extras_require = {
    # Requirements for ssh transport with authentification through Kerberos token
    # N. B.: you need to install first libffi and MIT kerberos GSSAPI including header files.
    # E.g. for Ubuntu 14.04: sudo apt-get install libffi-dev libkrb5-dev
    'ssh_kerberos': [
        'pyasn1==0.4.2',
        'python-gssapi==0.6.4',
    ],
    # Requirements for RESTful API
    'rest': [
        'Flask==1.0.2',
        'Flask-RESTful==0.3.6',
        'Flask-Cors==3.0.4',
        'pyparsing==2.2.0',
        'Flask-SQLAlchemy==2.3.2',
        'sqlalchemy-migrate==0.11.0',
        'marshmallow-sqlalchemy==0.13.2',
        'flask-marshmallow==0.9.0',
        'itsdangerous==0.24',
        'Flask-HTTPAuth==3.2.3',
        'Flask-Cache==0.13.1',
        'python-memcached==1.59',
    ],
    # Requirements to building documentation
    'docs': [
        'Sphinx==1.7.7',
        'Pygments==2.2.0',
        'docutils==0.14',
        'Jinja2==2.10',
        'MarkupSafe==1.0',
        'sphinx-rtd-theme==0.3.1',  # Required by readthedocs
    ],
    # Requirements for non-core functionalities that rely on external atomic manipulation/processing software
    'atomic_tools': [
        'spglib==1.10.3.65',
        'pymatgen==2018.4.20',
        'ase==3.12.0',  # Updating breaks tests
        'PyMySQL==0.8.0',  # Required by ICSD tools
        "PyCifRW==4.2.1; python_version < '3'",  # Does not support python3
        "PyCifRW==4.4; python_version >= '3'",  # Does not support python2
        'seekpath==1.8.1',
        'qe-tools==1.1.0',
    ],
    # Requirements for jupyter notebook
    'notebook': [
        'jupyter==1.0.0',
    ],
    # Requirements for testing
    'testing': [
        'unittest2==1.1.0; python_version<"3.5"',
        'pgtest==1.1.0',
        'sqlalchemy-diff==0.1.3',
        'coverage==4.5.1',
        'codecov==2.0.15',
        'futures; python_version=="2.7"',
    ],
    'dev_precommit': [
        'pre-commit==1.8.2',
        'yapf==0.23.0',
        'prospector==0.12.11',
        'pylint==1.8.4',
        'pylint-django==0.11.1',
        'pep8-naming==0.3.3',
        'toml==0.9.4'
    ],
    'dev_sphinxext': [
        'pytest==3.6.3',
        'pytest-cov==2.5.1',
    ],
    'bpython': [
        'bpython==0.17.1',
    ]
}

extras_require['dev_sphinxext'] += extras_require['docs']
extras_require['testing'] += extras_require['rest'] + extras_require['atomic_tools'] + extras_require['dev_sphinxext']
extras_require['all'] = [item for sublist in extras_require.values() for item in sublist if item != 'bpython']
