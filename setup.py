"""
OpenOpenMMReporters
A short description of the project.
"""
import sys
from setuptools import setup, find_packages
import versioneer

short_description = __doc__.split("\n")

# from https://github.com/pytest-dev/pytest-runner#conditional-requirement
needs_pytest = {'pytest', 'test', 'ptr'}.intersection(sys.argv)
pytest_runner = ['pytest-runner'] if needs_pytest else []

try:
    with open("README.md", "r") as handle:
        long_description = handle.read()
except:
    long_description = "\n".join(short_description[2:])

setup(
    # Self-descriptive entries which should always be present
    name='OpenOpenMMReporters',
    author='UIBCDF Lab',
    author_email='uibcdf@gmail.com',
    description=short_description[0],
    long_description=long_description,
    long_description_content_type="text/markdown",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    license='MIT',

    # Which Python importable modules should be included when your package is installed
    # Handled automatically by setuptools. Use 'exclude' to prevent some specific
    # subpackage(s) from being added, if needed
    package_dir={'openopenmmreporters': 'openopenmmreporters'},
    packages=find_packages(),
    package_data={'openopenmmreporters': []},

    # Optional include package data to ship with your package
    # Customize MANIFEST.in if the general case does not suit your needs
    # Comment out this line to prevent the files from being packaged with your software
    include_package_data=True,

    # Allows `setup.py test` to work correctly with pytest
    setup_requires=[] + pytest_runner,

    # Additional entries
    url='http://uibcdf.org',
    download_url ='https://github.com/uibcdf/OpenOpenMMReporters',

    # Manual control if final package is compressible or not, set False to prevent the .egg from being made
    # zip_safe=False,
)

