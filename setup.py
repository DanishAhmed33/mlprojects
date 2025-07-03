from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT='-e .'
def get_requires(file_path:str)-> List[str]:

    """Load requirements from a file."""

    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements


setup(
    name='mlprojects',
    version='0.1.0',
    author='Danish Ahmed',
    author_email='danahm149@gmail.com',
    packages=find_packages(),
    install_requires=get_requires('requirements.txt'),

)