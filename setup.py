from setuptools import setup, find_packages
from typing import List

PROJECT_NAME = "Machine Learning Pipeline"
VERSION = "0.0.1"
DESCRIPTION = "This is our ML project in modular coding"
AUTHOR = "Aashish Chapain"
AUTHOR_EMAIL = "aashishchapain@gmail.com"
# URL = ""

REQUIREMENTS_FILE_NAME = "requirements.txt"

HYPHEN_E_DOT = "-e ."

def get_requirements_list() -> List[str]:
    with open(REQUIREMENTS_FILE_NAME, "r") as f:
        requirement_list = f.readlines()
        requirement_list = [requirement_name.replace("\n", "") for requirement_name in requirement_list]

    if HYPHEN_E_DOT in requirement_list:
        requirement_list.remove(HYPHEN_E_DOT)


setup(
    name=PROJECT_NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    # url="",
    packages=find_packages(),
    install_requires="",
)