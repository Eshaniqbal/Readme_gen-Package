# setup.py

from setuptools import setup, find_packages

setup(
    name="readme_gen",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[],  # No external dependencies in this example
    author="Eshan Iqbal",
    author_email="mireshan321@gmail.com",
    description="A simple package to generate README files for projects automatically.",
    url="https://github.com/Eshaniqbal/Readme_gen-Package",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
