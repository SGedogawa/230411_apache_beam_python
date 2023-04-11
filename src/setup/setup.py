from setuptools import setup, find_packages

with open("./requirements.txt") as f:
    requirements = f.readlines()

setup(
    name="Python Apache Beam test",
    version="1.0",
    description="Python Apache Beam pipeline.",
    author="sgedogawa",
    author_email="sgedogawa@gmail.com",
    packages=find_packages(),
    install_requires=requirements,
)