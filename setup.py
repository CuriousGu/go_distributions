from setuptools import setup
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\\n" + fh.read()

setup(
    name="go_dists",
    version='{{VERSION_PLACEHOLDER}}',
    author="Gustavo M. Ortega",
    author_email="gustavo_ortega@usp.br",
    description="Easier way to calculate probability distributions",
    url = "https://github.com/CuriousGu/go_distributions",
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=["app"],
    install_requires=[''],
    keywords=['probability', 'probabilidade', 'distributions', 'distribuições'],

)