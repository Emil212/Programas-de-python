#En este programa se creara un paquete distribuible para que se pueda ocupar desde cualquier lado
from setuptools import setup

setup(

    name="PaqueteCalculos", 
    version=1.0,
    description="Paquete de redondeo y potencia",
    author="Emiliano Ceron",
    author_email="mattbfmv@outlook.com",
    packages=["Calculos","Calculos.Redondeo_Potencia"]

    )