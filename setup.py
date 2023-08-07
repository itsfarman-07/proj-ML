from setuptools import find_packages,setup
from typing import List

FLAG='-end- .'
def get_requirements(file_path:str)->List[str]:
    '''
    return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if FLAG in requirements:
            requirements.remove(FLAG)
    
    return requirements

setup(
name='ML',
version='0.0.1',
author='Farman',
author_email='skmdfarman49@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt'))