from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str) -> List[str]:

    requirements = []

    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.replace("\n", " ") for req in requirements]

        if '-e .' in requirements:
            requirements.remove('-e .')
    
    return requirements

setup(
    name='ml_project',
    version='1.0.0',
    author='Darpan',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt') 
)
