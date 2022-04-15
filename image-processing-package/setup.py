from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image-processing-testing",
    version="0.0.1",
    author="Guilherme de Oliveira",
    author_email="guilhermeoliveira.94@hotamil.com",
    description="Passo a passo passado por Karina Kato.",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/guilhermeoliveira94",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)