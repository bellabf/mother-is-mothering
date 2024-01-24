from setuptools import setup, find_packages
import os

current_dir = os.path.abspath(os.path.dirname(__file__))

name = 'mother-is-mothering'
description = 'Words of wisdom from Taylor Swift'
version = '2024.1003-alpha'
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
    install_requires=["numpy>=1.26.3"],
    package_data={
        'mother-is-mothering': ['src/ts-lyrics.pkl'],
    },
    extras_require={},
    python_requires='>=3.7',
    zip_safe=False,
)
