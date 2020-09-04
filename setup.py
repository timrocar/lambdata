""" lambdata - a collection of Data Science functions
"""

import setuptools

REQUIRED = [
    "numpy",
    "pandas" 
]

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

setuptools.setup(
    name="lambdata-timrocar",
    version='0.0.98',
    author='timrocar',
    description='A collection of Data Science functions',
    long_description=LONG_DESCRIPTION,
    long_description_content="text/markdown",
    url="https://github.com/timrocar/lambdata",
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    install_requires=REQUIRED,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
    