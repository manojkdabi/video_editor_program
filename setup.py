#!/usr/bin/env python3
"""
Setup script for Video Editor Program.
"""

from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="video-editor-insoil",
    version="1.0.0",
    author="InSoil",
    author_email="tech@insoil.com",
    description="A video editing tool for InSoil's agricultural and educational content",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/manojkdabi/video_editor_program",
    py_modules=["video_editor", "cli", "examples"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Multimedia :: Video",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "insoil-video-editor=cli:main",
        ],
    },
)
