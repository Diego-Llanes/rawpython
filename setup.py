from setuptools import setup
from pathlib import Path

readme = Path(__file__).parent / 'README.md'

with open(readme, "r") as f:
    long_description = f.read()

setup(
    name='rawpython',
    version='{{VERSION_PLACEHOLDER}}',
    description="a library for people who hate libraries",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Diego-Llanes/rawpython",
    author='Diego Llanes',
    author_email='rawpython@diegollanes.com',
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
