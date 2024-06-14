"""setup.py"""

from pathlib import Path

import setuptools

README = Path() / "README.md"
if not README.exists():
    raise RuntimeError(f"{README.name} does not exist")

REQUIREMENTS = Path() / "requirements.txt"
if not REQUIREMENTS.exists():
    raise RuntimeError(f"{REQUIREMENTS.name} does not exist")


def get_version():
    """Retrieve package version."""
    version_path = Path() / "taegis_sdk_python" / "_version.py"
    if not version_path.exists():
        raise RuntimeError(f"{version_path.name} does not exist")

    for line in version_path.read_text(encoding="utf-8").splitlines():
        if line.startswith("__version__"):
            quote = '"' if '"' in line else "'"
            version = line.split()[2]
            return version.replace(quote, "")
    raise RuntimeError("Unable to read version.")


setuptools.setup(
    name="taegis-sdk-python",
    version=get_version(),
    author="Secureworks",
    author_email="sdks@secureworks.com",
    description="Taegis Python SDK",
    long_description=README.read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",
    url="https://github.com/secureworks/taegis-sdk-python",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        package.replace("==", ">=")
        for package in REQUIREMENTS.read_text(encoding="utf-8").splitlines()
    ],
    python_requires=">=3.8",
)
