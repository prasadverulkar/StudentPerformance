from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''

    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

setup(
    name='Student Performance',
    version='0.0.1',
    author='PrasadVerulkar',
    author_email='prasadvverulkar@gmail.com',
    packages=find_packages(), # To find all the necessary packages, create a src folder and __init__.py file because when this line runs, it looks for that file
    install_requires=get_requirements('requirements.txt')

)

"""
Setup script for the 'Student Performance' project.

This script uses `setuptools` to package and distribute the project, ensuring 
necessary dependencies are installed for smooth execution.

Functions:
----------
- get_requirements(file_path: str) -> List[str]: 
    Reads a requirements file and returns a list of dependencies to install.

Key Components:
----------------
- name: The name of the project ("Student Performance").
- version: Current version of the project (0.0.1).
- author: Project author's name.
- author_email: Author's contact email.
- packages: Uses `find_packages()` to automatically discover and include project packages.
- install_requires: Populates with package dependencies listed in `requirements.txt`.

Notes:
------
- The function `get_requirements()` removes any `-e .` entry from the requirements list. This is mentioned because
it triggers setup.py file whenever requirements.txt file is run.
- Ensure that sub-packages contain an `__init__.py` file for proper package discovery when 
this line runs - packages=find_packages().
  
Usage:
------
To install the project locally:
    $ python setup.py install
"""

