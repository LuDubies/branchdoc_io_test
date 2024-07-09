# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Branchdoc'
copyright = '2024, Luca Dubies'
author = 'Luca Dubies'
release = '1.0.0'
conf_py_path = "/doc/" # with leading and trailing slashes

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinxcontrib.mermaid','myst_parser', "sphinx_rtd_dark_mode"]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# HTML theme and static files
html_theme = "sphinx_rtd_theme"
html_static_path = ['_static']
html_css_files = ['css/svg.css']

# HTML theme options
default_dark_mode = True

# Mermaid configuration
mermaid_output_format = 'svg'
mermaid_cmd = 'mmdc'
mermaid_params = ['--theme', 'dark', '--backgroundColor', 'transparent']