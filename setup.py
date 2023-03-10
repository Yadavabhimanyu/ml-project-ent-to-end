from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'

def get_reuirements(file_path:str)->List[str]:
    '''
    This function will return the lists of requirements
    '''
    requirements=[]
    with open(file_path) as f:
        requirements=f.readlines()
        requirements=[x.replace("\n","") for x in requirements]
    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)
    
    return requirements
setup(
    name="mlproject",
    version="0.0.1",
    author="Albert",
    author_email="abhiyad111@gmail.com",
    packages=find_packages(),
    install_requires=get_reuirements("requirements.txt")
)