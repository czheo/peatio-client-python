from setuptools import setup

def readme():
    with open("README.md") as f:
        return f.read()

setup(
    name = "peatio_client",
    version = "0.0.2",
    description = "a client library to the bitcoin exchange Peatio",
    long_description = readme(),
    author = "czheo",
    license = "LGPL",
    keywords = "bitcoin peatio yunbi.com",
    test_suite = "tests",
    packages = [
        "peatio_client"
    ],
    install_requires = [
        "requests"
    ],
    zip_safe = False
)
