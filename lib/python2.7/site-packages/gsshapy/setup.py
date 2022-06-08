import setuptools
from distutils.core import setup

setup(name='gsshapy', version='2.3.5', packages=['gsshapy'])

#with open("README.md", "r") as fh:
#    long_description = fh.read()

setuptools.setup(
    name="gsshapy", # Replace with your own username
    version="2.3.5",
    author="",
    author_email="",
    description="gssha preprocessing",
    #long_description=description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: BSD",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.7',
)
