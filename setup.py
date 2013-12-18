from distutils.core import setup
from setuptools import find_packages


setup(
    name='supervisor_filemanager',
    version='0.1',
    packages=find_packages("src"),
    package_dir={"": "src"},
    url='',
    license='',
    author='Jussi Talaskivi',
    author_email='jptalask@gmail.com',
    install_requires = ['supervisor >= 3.0a10'],
    description=''
)
