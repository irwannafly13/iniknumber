from setuptools import setup, find_packages

setup(
    name="iniknumber",   
    version="0.1.0",  
    description="A Python package for parsing and validating NIK numbers.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="irwannafly13",
    author_email="anggadventurez@gmail.com",
    url="https://github.com/irwannafly13/iniknumber",  
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "pandas",
    ],
    package_data={
        "iniknumber": ["data/*.csv"],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
