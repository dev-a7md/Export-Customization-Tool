from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in export_customizations_tool/__init__.py
from export_customizations_tool import __version__ as version

setup(
	name="export_customizations_tool",
	version=version,
	description="Export Customizations Tool",
	author="DV",
	author_email="erp@ex.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
