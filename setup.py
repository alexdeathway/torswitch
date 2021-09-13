from setuptools import setup, find_packages

def read_requirements():
    with open('requirements.txt') as req:
        content=req.read()
        requirements=content.split('\n')

    return requirements   

def get_version():
    with open("version.txt") as ver:
        Version=ver.read()
    return Version    

DESCRIPTION = 'A basic package to control tor with python.'

# Setting up
setup(
    name="torswitch",
    version=get_version(),
    author="Alex Deathway",
    author_email="<alexdeathway@gmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=read_requirements(),
    keywords=['python', 'tor', 'pythontor', 'iproatation','ipaddress'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)