from setuptools import setup, find_packages
from typing import  List

def get_requirements(file_path:str)-> List:[str]:
    requirements =[]
    with open('requirements.txt') as file_obj:
    requirements = file_obj.readlines()





setup(
name='mlproject',
version='0.0.1',
author='ketaki',
packages=  find_packages(),
install_requires=get_requirements('requirements.txt')
)