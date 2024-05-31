from setuptools import setup,find_packages
from typing import List






__version__="0.0.4"
REPO_NAME='ineuron_proj'
PKG_NAME="mangodb_connect"
AUTHOR_USER_NAME='Hafsaimranazlan'
AUTHOR_EMAIL='ik9449080@gmail.com'
long_description="xyz"




setup(
    name=PKG_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A python package for connecting with database",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker":f"https://github.com{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"},
    packages=find_packages(where="src")
)