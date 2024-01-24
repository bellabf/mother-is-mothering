from setuptools import setup, find_packages
import os

current_dir = os.path.abspath(os.path.dirname(__file__))

name = 'mother-is-mothering'
version = '2024.1004-alpha'
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
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'mother-is-mothering': ['src/ts-lyrics.pkl'],
    },
    extras_require={},
    zip_safe=False,
)
