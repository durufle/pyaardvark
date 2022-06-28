# AARDVARK python package

This is based on the following TotalPhase distribution:

    - Aardvark Software API v5.50 (Windows x86 64-bit)
    - Aardvark Software API v5.50 (Linux x86 64-bit)

What is the differences with the original distribution 

    - Can be installed as any type of python package using pip.
    - Can be installed and used on Windows and Linux platforms.
    - Include a sphinx documentation of the API.
    
To install this package in your environment

```bash
pip install pyaardvark
```

To develop:

Install the necessary packages for development for example in a virtual environment:

```bash
# Create virtual environment
python -m venv venv

# Activate your environment
# On Windows
venv\Scripts\activate.bat
# On linux or MacOS
source venv/bin/activate

# install packages in our virtual environment

(venv) pip install -r requirements.txt
```

