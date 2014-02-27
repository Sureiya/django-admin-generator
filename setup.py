import os
import sys
import django_admin_generator as metadata
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

if os.path.isfile('README.rst'):
    long_description = open('README.rst').read()
else:
    long_description = 'See http://pypi.python.org/pypi/formatter/'


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)

setup(
    name=metadata.__package_name__,
    version=metadata.__version__,
    author=metadata.__author__,
    author_email=metadata.__author_email__,
    description=metadata.__description__,
    url=metadata.__url__,
    license='BSD',
    packages=find_packages(),
    long_description=long_description,
    tests_require=['pytest'],
    cmdclass={'test': PyTest},
    py_modules=['django_admin_generator'],
    classifiers=['License :: OSI Approved :: BSD License'],
)
