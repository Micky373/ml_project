# Importing libraries for geting packages
from setuptools import find_packages, setup

# Creating a function to get the packages that we need to install
def get_requirements(file_path):

    requirements = []
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.replace('\n','') for req in requirements]    
        
        if "-e ." in requirements:
            requirements.remove("-e .")

    return requirements

# Creating a setup file for the project
setup(
    name="ml project",
    version="0.01",
    author="Michael Tamirie",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)