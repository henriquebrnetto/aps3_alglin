from setuptools import setup, find_packages
import os


def find_subdir(start_dir):
    # Get the list of all subdirectories starting at the given path
    subdirectories = [x[0] for x in os.walk(start_dir)]
    subdirectories = [x.split('/',1)[-1]+'/*' for x in subdirectories]
    return subdirectories

# Lendo o conteúdo do README.md para usar como descrição longa
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

MODULE_STUB = "aps3_alglin_hbucci"

setup(
    name=MODULE_STUB,  # Substitua pelo nome do seu pacote
    version="0.1.0",
    author="Henrique Bucci",
    author_email="henriquebrn@al.insper.edu.br",
    description="A simple hello world module",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/henriquebrnetto/aps3_alglin_hbucci",  # URL do repositório do seu projeto (se houver)
    packages=find_packages(),  # Encontra automaticamente todos os pacotes no diretório
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.11',
    entry_points={
        'console_scripts': [
            f'aps3_alglin_hbucci-cli={MODULE_STUB}.main:app',
        ],
    },
    install_requires=[  # Instala as dependências especificadas no requirements.txt
        line.strip() for line in open("requirements.txt").readlines()
    ],
)
