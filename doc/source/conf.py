# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Tissue-Simulation-Toolkit'
copyright = '2024, Roeland Mekrs'
author = 'Roeland Mekrs'
release = '2.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["breathe", 'sphinx.ext.autodoc']

source_suffix = ['.rst', '.md']

# source_suffix = {
#     '.rst': 'restructuredtext',
#     '.txt': 'markdown',
#     '.md': 'markdown',
# }


templates_path = ['_templates']
exclude_patterns = []

breathe_projects = {
    "Tissue-Simulation-Toolkit": "../build/xml/",
}
breathe_default_project = "Tissue-Simulation-Toolkit"


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
