# This file will contain all the logic code for local package installation which are present in requirements.txt:

import setuptools

# First import the README file: Can be used when the publishing of the project is required
with open("README.md","r",encoding = "utf-8") as f:
    long_description = f.read()

#Specifying the version of your software:
__version__ = "0.0.0"

#Specifying the details of the repository and author:
REPO_NAME = "Text_Summarizer_Project"
AUTHOR_USER_NAME = "Shivv3"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "shivam2048sinha@gmail.com"

#Final Code for the local package setup from the requirements.txt:
setuptools.setup(
    name = SRC_REPO,
    version = __version__,
    author = AUTHOR_USER_NAME,
    author_email = AUTHOR_EMAIL,
    description = "A small Python package for NLP - Text_Summarizer App",
    long_description = "text/markdown",
    url = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir = {"":"src"},
    packages = setuptools.find_packages(where="src")
)
