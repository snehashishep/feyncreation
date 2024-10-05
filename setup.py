# setup.py
from setuptools import setup, find_packages

setup(
    name='feyncreation',
    version='0.3',
    description='A package for drawing Feynman diagrams',
    author='Snehashis Parashar',
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
