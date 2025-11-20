import os
from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))

setup(
    name="AICHATBOT",
    version="1.0.0",
    author="Ashutosh Shekhar",
    author_email="ashutoshshekhar37@gmail.com",
    description="A short description of AICHATBOT",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[],
    python_requires=">=3.8",
)
