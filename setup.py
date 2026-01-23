## we'll write the code that packaging the entire content

'''
The setup.py file is an essential part of packaging and distributing python projects.It is used by Setuptools(or distutils in order python versions) to define the configuration of the project,such as its metadata,dependencies.

'''
import sys
from setuptools import find_packages,setup

def get_requirements()->List[str]:
    """
    this function will return al the requirements"""
    requirement_lst:List[str]=[]
    try:
        with open("requirement.txt",'r') as file:
            #read lines from the file
            lines=file.readlines()
            for line in lines:
                #process each line
                requirement=line.strip()
                ##ignore empty lines and -e.
                if requirement and requirement!='-e.':
                    requirement_lst.append(requirement)

    except FileNotFoundError:
        print("The requuirement.txt file not found")

    return requirement_lst


setup(
    name="NetworkSecurityProject",
    version="0.0.1",
    author="sireesha",
    author_email="smilychinnu2006@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)
