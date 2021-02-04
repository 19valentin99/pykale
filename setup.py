#!/usr/bin/env python3
import re
from io import open
from os import path

from setuptools import find_packages, setup

# Core kale API dependencies. If updating this, you may need to update docs/requirements.txt too.
# Not all have a min-version specified, which is not uncommon. Specify when known or necessary (e.g. errors).
# Install PyTorch from the official website to match the hardware.
# To work on graphs, install torch-geometric following the official instructions (e.g. below):
# python -m pip install torch-cluster torch-scatter torch-sparse torch-spline
requirements = [
    'numpy>=1.18.0',
    'pytorch-lightning',
    'scikit-image',
    'scikit-learn',
    'tensorly',
    'torch>=1.7.0',
    'torchvision',  # >=0.8.1
]

# Additional dependencies for examples/tutorials and development
extra_requirements = [
    'black',
    'flake8',
    'flake8-print',
    'ipykernel',
    'ipython',
    'isort',
    'm2r',
    'matplotlib',
    'mypy',
    'nbsphinx',
    'nbval',
    'pre-commit',
    'pytest',
    'sphinx',
    'sphinx_rtd_theme',
    'torchsummary>=1.5.0',
    'yacs>=0.1.7',
]


# Get version
def read(*names, **kwargs):
    with open(path.join(path.dirname(__file__), *names), encoding=kwargs.get("encoding", "utf8")) as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


readme = open("README.md").read()
version = find_version("kale", "__init__.py")


# Run the setup
setup(
    name="pykale",
    version=version,
    description="Knowledge-aware machine learning from multiple sources in Python",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="The PyKale team",
    url="https://github.com/pykale/pykale",
    author_email="pykale-group@sheffield.ac.uk",
    project_urls={
        "Bug Tracker": "https://github.com/pykale/pykale/issues",
        "Documentation": "https://pykale.readthedocs.io",
        "Source": "https://github.com/pykale/pykale",
    },
    packages=find_packages(exclude=("docs", "examples", "tests")),
    python_requires=">=3.6",
    install_requires=requirements,
    extras_require={'extras': extra_requirements},
    setup_requires=['setuptools>=38.6.0'],
    license="MIT",
    keywords="machine learning, pytorch, deep learning, multimodal learning, transfer learning",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Healthcare Industry",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
        "Topic :: Software Development :: Libraries",
        "Natural Language :: English",
    ],
)
