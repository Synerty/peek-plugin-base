import os
import shutil
from distutils.core import setup

from setuptools import find_packages

package_name = "peek-plugin-base"
package_version = '0.0.19'

egg_info = "%s.egg-info" % package_name
if os.path.isdir(egg_info):
    shutil.rmtree(egg_info)

if os.path.isfile('MANIFEST'):
    os.remove('MANIFEST')

requirements = [
    "SQLAlchemy >= 1.0.14",  # Database abstraction layer
    "SQLAlchemy-Utils >= 0.32.9",
    "alembic >= 0.8.7",  # Database migration utility

    # Celery packages
    "celery",

    # The package for RW support
    "json-cfg-rw"

]

# Packages that are presently installed from a git repo
dependency_links= [
]

setup(
    name=package_name,
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    install_requires=requirements,
    dependency_links=dependency_links,
    version=package_version,
    description='Peek Plugin Base',
    author='Synerty',
    author_email='contact@synerty.com',
    url='https://github.com/Synerty/%s' % package_version,
    download_url='https://github.com/Synerty/%s/tarball/%s' % (
        package_name, package_version),
    keywords=['Peek', 'Python', 'Platform', 'synerty'],
    classifiers=[
        "Programming Language :: Python :: 3.5",
    ],
)
