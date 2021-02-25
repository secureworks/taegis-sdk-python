import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="taegis-sdk-python",
    version="1.1.0",
    author="Max Terekhov, Dani Vainstein, David Addai, Marco Sanabria, Jose Lopez",
    author_email="",
    description="Taegis XDR Python SDK",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/secureworks/tdr-sdk-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "gql==3.0.0a4",
        "graphql-core",
        "python-dateutil",
        "oauthlib",
        "requests",
        "requests-oauthlib",
        "stringcase"
    ],
    python_requires='>=3.8',
)
