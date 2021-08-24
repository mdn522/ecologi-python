"""The python wrapper for Ecologi API package setup."""
from setuptools import (setup, find_packages)

setup(
    name="ecologi",
    version="0.0.1",
    packages=find_packages(),
    install_requires=["requests"],
    include_package_data=True,
    description="Ecologi.com API for Python",
    long_description="Ecologi.com API for Python",
    url="https://github.com/mdn522/ecologi-python",
    author="Abdullah Mallik",
    author_email="mdn522@gmail.com",
    zip_safe=False
)
