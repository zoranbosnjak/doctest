# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

def readFile(filename):
    with open(filename) as f:
        return f.read()

def readFirstLine(filename):
    return readFile(filename).splitlines()[0].strip()

project = 'test'
copyright = '2023, test'
author = 'test'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

master_doc = 'index'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

# -- Options for Latex output

latex_engine = 'xelatex'

latex_documents = [
  (master_doc, 'test.tex', project,
   'author', 'manual', False),
]

#latex_logo = 'logo.png'

latex_toplevel_sectioning = None

latex_appendices = []

latex_domain_indices = True

latex_show_pagerefs = True

latex_show_urls = 'footnote'

latex_use_latex_multicolumn = False #

latex_use_xindy = True

latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '11pt',
    'fontpkg': readFile('fontpkg.tex'),
    'preamble': readFile('preamble.tex'),
    #'maketitle': readFile('title.tex'),
    #'hyperref': readFile('hyperref.tex'),
    #'babel': readFile('babel.tex'),
    #'geometry': readFile('geometry.tex'),
    'sphinxsetup': 'VerbatimColor={rgb}{0.93, 1.00, 0.80}',
    # TODO: other latex config, see LaTeX customization in sphinx-doc
}

latex_additional_files = []

# latex_theme =

# latex_theme_options =

# latex_theme_path =

