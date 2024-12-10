"""
This is a setup configuration file for the CNN Classifier package.
It handles package metadata and dependencies for a chest cancer prediction project.

Project Details:
    - Package Name: cnnClassifier
    - Version: 0.0.0
    - Description: A small python package for CNN app
    - Repository: https://github.com/spandan114/chest-cancer-prediction
    - Author: spandan114 (spandanj685@gmail.com)

The setup uses README.md for long description and configures the package source
directory under 'src/'.
"""

import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "chest-cancer-prediction"
AUTHOR_USER_NAME = "spandan114"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "spandanj685@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)