from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."
def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''

    req = []
    with open(file_path) as file_obj:
        req = file_obj.readlines()
        req = [reqs.replace("\n", "") for reqs in req]

        if HYPEN_E_DOT in req:
            req.remove(HYPEN_E_DOT)


setup(
    name="MLProject",
    version="0.0.1",
    author="ishu",
    author_email="arnavsingla99@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)