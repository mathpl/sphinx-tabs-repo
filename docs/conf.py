project = 'Sphinx pydata tabs test'
copyright = 'mathpl'
author = 'mathpl'

# -- General configuration ---------------------------------------------------
version = "v1.0"

extensions = [
    'sphinx.ext.extlinks',
    'sphinx_tabs.tabs',
    'myst_parser',
]

html_theme_options = {
  "check_switcher": False,
  "switcher": {
      "json_url": "http://localhost:8000/_static/switcher.json",
      "version_match": version,
  },
  "navbar_start": ["navbar-logo", "version-switcher"],
}

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']
