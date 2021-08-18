from setuptools import setup, find_packages
from sphinx.setup_command import BuildDoc

name = "aardvark"
version = "0.1.0"

setup(
    name=name,
    version=version,

    cmdclass={'build_sphinx': BuildDoc},
    command_options={
        'build_sphinx': {
            'project': ('setup.py', name),
            'version': ('setup.py', version),
            'source_dir': ('setup.py', 'docs/source')
        }
    },

    packages=find_packages(),
    package_data={"pyaardvark": ["lib/linux/aardvark.so", "lib/win/aardvark.dll"]},
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
