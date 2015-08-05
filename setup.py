import sys
IS_PYTHON3 = sys.version_info[0] == 3
if not IS_PYTHON3:
    print("Error: CompDB requires python version >= 3.x.")
    sys.exit(1)

from setuptools import setup, find_packages

setup(
    name = 'compdb',
    version = '0.1.5dev1',
    package_dir = {'': 'src'},
    packages = find_packages('src'),

    author = 'Carl Simon Adorf',
    author_email = 'csadorf@umich.edu',
    description = "Computational Database.",
    keywords = 'simulation tools mc md monte-carlo mongodb jobmanagement materials database',

    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Topic :: Scientific/Engineering :: Physics",
        ],

    install_requires=['pymongo>=2.8', 'jsonpickle','networkx'],

    extras_require = {
        'mpi': ['mpi4py'],
        },
    entry_points = {
        'console_scripts': [
            'compdb = compdb.contrib.script:main',
            'compdb_init = compdb.contrib.init_project:main',
            'compdb_configure = compdb.contrib.configure:main',
            'compdb_admin = compdb.admin.manage:main',
            'compdb_server = compdb.contrib.server:main',
            'compdb_user = compdb.contrib.admin:main',
            'compdb_admin_project = compdb.admin.manage_project:main',
        ],
    },
)
