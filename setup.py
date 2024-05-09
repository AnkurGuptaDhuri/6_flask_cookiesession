from setuptools import find_packages
from setuptools import setup

setup(
    name='flasksessionpackage',
    version='1.0',
    long_description=__doc__,
    packages= find_packages(), #['main.py'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask', 'setuptools', 'flask_session']
)