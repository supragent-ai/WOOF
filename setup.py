#!/usr/bin/env python3
"""
Setup script for WOOF Format
"""

from setuptools import setup, find_packages
import os

# Read the README file
def read_readme():
    with open("README.md", "r", encoding="utf-8") as fh:
        return fh.read()

# Read requirements
def read_requirements():
    with open("requirements.txt", "r", encoding="utf-8") as fh:
        return [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="woof-format",
    version="1.0.0",
    author="WOOF Team",
    author_email="woof@example.com",
    description="The most Paw-some Image File Format for your AI workflows",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/woof",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Multimedia :: Graphics",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.6",
    install_requires=read_requirements(),
    entry_points={
        "console_scripts": [
            "woof=woof_format:main",
            "woof-gui=woof_gui:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["*.txt", "*.md", "*.png", "*.ico"],
    },
    keywords="image format steganography ai metadata png",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/woof/issues",
        "Source": "https://github.com/yourusername/woof",
        "Documentation": "https://github.com/yourusername/woof#readme",
    },
) 