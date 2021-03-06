import platform
from setuptools import setup, find_packages

from sqlcomplete import __version__

description = "SQL Completion Engine"

install_requirements = [
    "click >= 4.1",
    "Pygments >= 2.0",  # Pygments has to be Capitalcased. WTF?
    "prompt_toolkit>=2.0.6,<3.0.0",
    "sqlparse >=0.3.0,<0.4",
    "configobj >= 5.0.6",
    "humanize >= 0.5.1",
    "cli_helpers[styles] >= 1.2.0",
]


# setproctitle is used to mask the password when running `ps` in command line.
# But this is not necessary in Windows since the password is never shown in the
# task manager. Also setproctitle is a hard dependency to install in Windows,
# so we'll only install it if we're not in Windows.
if platform.system() != "Windows" and not platform.system().startswith("CYGWIN"):
    install_requirements.append("setproctitle >= 1.1.9")

setup(
    name="sqlcomplete",
    author="DBCLI Core Team",
    author_email="pgcli-dev@googlegroups.com",
    version=__version__,
    license="BSD",
    url="http://dbcli.com",
    packages=find_packages(),
    package_data={"sqlcomplete": ["sql_literals/sql_literals.json"]},
    description=description,
    long_description=open("README.md").read(),
    install_requires=install_requirements,
    extras_require={"keyring": ["keyring >= 12.2.0"]},
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: Unix",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: SQL",
        "Topic :: Database",
        "Topic :: Database :: Front-Ends",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
