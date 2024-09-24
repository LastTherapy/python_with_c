from setuptools import setup, Extension
from Cython.Build import cythonize

# Определение C модуля
moduler = Extension('calculator', sources=['calculator.c'])

# Определение Cython модуля
matrix = Extension('matrix', sources=['multiply.pyx'])

setup(
    name='calculator_and_matrix',  # Имя пакета
    version='0.1',  # Версия пакета
    ext_modules=cythonize([moduler, matrix]),  # Компиляция C и Cython модулей
    packages=['matrix'],  # Определение пакета matrix
    zip_safe=False,  # Параметр безопасности
)
