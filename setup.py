from setuptools import setup

def readme():
    with open("README.md") as f:
        return f.read()

setup(
    name = "peatio_client",
    version = "0.1.1",
    description = "a client library for the bitcoin exchange Peatio",
    url = 'https://github.com/czheo/peatio-client-python',
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
