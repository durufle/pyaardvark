from setuptools import setup, find_packages
from sphinx.setup_command import BuildDoc

name = "pyaardvark"
version = "0.0.0"

setup(
    name=name,
    version=version,
    packages=find_packages(),
    package_data={'': ['aardvark.dll']},
    classifiers=[
        'License :: OSI Approved ::  Massachusetts Institute of Technology (MIT)',
        'Operating System :: Microsoft :: Windows :: Windows 10',
        'Programming Language:: Python:: 3',
        'Topic :: Device driver',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users',
    ],

    keywords='aardvark',

    url="https://git.ul-ts.com/ims-se/hardware-team/pybench/pyaardvark",

    license="MIT",
    author="Laurent Bonnet",
    author_email="laurent.bonnet@ul.com",
    python_requires='>=3.8'
)
