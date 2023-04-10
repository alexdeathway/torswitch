import os
import codecs
from setuptools import setup, find_packages

current_dir = os.path.abspath(os.path.dirname(__file__))
with codecs.open(os.path.join(current_dir, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

def read_requirements():
    with open('requirements.txt') as req:
        content=req.read()
        requirements=content.split('\n')

    return requirements   

def get_version():
    with open("version.txt") as ver:
        Version=ver.read()
    return Version    

DESCRIPTION = 'Python package for an easy-to-use interaction with the Tor proxy and controlling IP address rotations.'

# Setting up
setup(
    name="torswitch",
    version=get_version(),
    author="Alex Deathway",
    author_email="<alexdeathway@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=read_requirements(),
    keywords=['python', 'tor', 'pythontor', 'onion','ipaddress'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
    #    "Operating System :: Unix",
    #    "Operating System :: MacOS :: MacOS X",
    #    "Operating System :: Microsoft :: Windows",
    ]
)