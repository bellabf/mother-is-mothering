from setuptools import setup, find_packages
import os

name = 'mother-is-mothering'
version = "2024.1005-alpha"
description = 'Words of wisdom from Taylor Swift'
author = 'Isabella Bicalho Frazeto'
author_email = 'bisnotforbella@gmail.com'
license = 'MIT License'
classifiers = [
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Topic :: Religion",
    "Intended Audience :: Other Audience",
    "Intended Audience :: Education"
]
url = "https://github.com/bellabf/mother-is-mothering"

setup(
    name=name,
    version=version,
    author=author,
    author_email=author_email,
    license=license,
    url=url,
    classifiers=classifiers,
    description=description,
    long_description='Longer package description goes here.',
    packages=find_packages("src"),
    package_dir={"": "src"},
    extras_require={},
    zip_safe=False,
)
