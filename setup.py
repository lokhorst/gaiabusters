from setuptools import setup, find_packages

# Load the __version__ variable without importing the package already
exec(open("gaiabusters/version.py").read())

setup(
    name = "gaiabusters",
    version = __version__,
    packages=find_packages()
)