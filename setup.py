from setuptools import setup, find_packages
VERSION = '0.1.0' 
URL = 'https://github.com/scoc6656/SPECtro.py'
PACKAGE_NAME = 'SPECtro' 
AUTHORS= 'Sigrid Oñate Campos, Ursula Saez Parra, Irma Pizarro Saez, Angel Paisano Martinez'
INSTALL_REQUIRES = ['numpy, matplotlib, astropy, pandas']
DESCRIPTION = '''SPECtro es un paquete que te permite trabajar con mayor facilidad los datos 
de espectros estelares que vienen en formato fits, para ello tienen las funciones labels y normalized_data'''

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    url=URL,
    description=DESCRIPTION,
    author=AUTHORS,
    install_requires=INSTALL_REQUIRES,
    packages=find_packages(),
    include_package_data=True
)
