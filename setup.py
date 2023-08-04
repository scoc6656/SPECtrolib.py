from setuptools import setup, find_packages
VERSION = '0.1.3' 
URL = 'https://github.com/scoc6656/SPECtro.py'
PACKAGE_NAME = 'spectrolib' 
AUTHORS= 'Sigrid Oñate Campos, Ursula Sáez Parra, Irma Pizarro Sáez, Angel Paisano Martinez'
INSTALL_REQUIRES = ['numpy', 'matplotlib','astropy']
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
