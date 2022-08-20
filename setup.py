from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in nextweb/__init__.py
from nextweb import __version__ as version

setup(
	name="nextweb",
	version=version,
	description="nextwebsite",
	author="nextwebsite",
	author_email="nextweb@deciss.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
