# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here.
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Dmitry\'s Handbook'
copyright = '2025, Dmitry Kuznetsov'
author = 'Dmitry Kuznetsov'
# release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.githubpages',
    'sphinx.ext.intersphinx',
    'ablog',
    'myst_parser',
    'sphinx_design',
]

templates_path = ['_templates']
exclude_patterns = []

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

# -- MyST configuration -------------------------------------------------------
# https://myst-parser.readthedocs.io/en/latest/configuration.html

myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "dollarmath",
    "html_image",
]

myst_heading_anchors = 2

myst_highlight_code_blocks = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'
# html_theme = 'sphinx_rtd_theme'
html_theme = 'pydata_sphinx_theme'
# html_theme = 'sphinx_book_theme'

html_theme_options = {
    # Samall search button
    "navbar_persistent": ["search-button"],
    # Number of links before dropdown
    "header_links_before_dropdown": 3,
    "header_dropdown_text": "Other",
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/kuzned",
            "icon": "fa-brands fa-square-github",
            "type": "fontawesome",
        },
        {
            "name": "Twitter",
            "url": "https://twitter.com/kuzned",
            "icon": "fa-brands fa-square-twitter",
            # The default for `type` is `fontawesome`, so it is not required in the above examples
        },
    ],
}

# Sphinx Book Theme
# html_theme_options = {
#     "repository_url": "https://github.com/kuzned/lumache-stuff",
#     "use_repository_button": True,
#     "article_header_end": ["article-header-buttons", "switcher.html"],
# }

# File system and favicon:
html_static_path = ["_static"]
templates_path = ["_templates"]
html_css_files = ["css/custom.css"]
html_js_files = ["js/custom.js"]
# html_favicon = "_static/images/logo.ico"

html_sidebars = {
    # "index": ["home.html"],
    # "index": ["search-button-field"],
    "about": ["home.html"],
    # handbook": ["home.html"],
    # "projects": ["home.html"],
    # Primary sidebar for posts list
    "blog": ["ablog/categories.html", "ablog/tagcloud.html", "ablog/archives.html"],
    # Primary sidebar for individual post
    "blog/**": ["ablog/postcard.html", "ablog/recentposts.html", "ablog/archives.html"],
}

# Works for Book theme
# html_sidebars = {
#     "**": [
#         "navbar-logo.html",
#         "search-button-field.html",
#         "sbt-sidebar-nav.html",
#         # "switcher.html",
#         # "ablog/postcard.html",
#     ]
# }

# Works for Alabaster theme
# html_sidebars = {
#     '**': [
#         'about.html',
#         'navigation.html',
#         'switcher.html'
#     ]
# }

# ABlog sidebars
# html_sidebars = {
#    "**": [
#       # Comes from Alabaster theme
#       # "about.html",
#       # "searchfield.html",
#       # Ablog sidebars
#       "ablog/postcard.html",
#       "ablog/recentposts.html",
#       "ablog/tagcloud.html",
#       "ablog/categories.html",
#       "ablog/archives.html",
#       "ablog/authors.html",
#       "ablog/languages.html",
#       # "ablog/locations.html",
#    ]
# }

html_static_path = ['_static']

html_title = 'Electronics & Progs'

# EPUB options
epub_show_urls = 'footnote'

# -- Options for localization -----------------------------
# https://sphinx-intl.readthedocs.io/en/master/quickstart.html

# locale_dirs = ['locale/']
# gettext_compact = False