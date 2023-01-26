from setuptools import setup, find_packages

setup(
    name='climodoro',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'typer[all]'
    ],
    entry_points={
        'console_scripts': [
            'climodoro = climodoro.__main__:app',
        ],
    },
)