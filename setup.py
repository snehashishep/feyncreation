# setup.py
from setuptools import setup, find_packages

setup(
    name='feyncreation',
    version='0.1',
    description='A package for drawing Feynman diagrams',
    author='Your Name',
    packages=find_packages(),
    install_requires=[
        'matplotlib',
        'feynman'
    ],
    entry_points={
        'console_scripts': [
            'feyncreation=feyncreation.feyncreation:get_user_input',  # Simplified command
        ],
    }
)