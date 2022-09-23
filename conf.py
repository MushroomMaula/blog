# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'My blog'
copyright = '2022, Max Rausch-Dupont'
# author = 'Max Rausch-Dupont'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    # "myst_parser",  # included in myst-nb
    "myst_nb",
    "sphinx_design",
    "ablog",
    "sphinx.ext.intersphinx",
    "sphinxcontrib.bibtex"
]

bibtex_bibfiles = ['references.bib']


myst_enable_extensions = [
    "amsmath",
    "dollarmath",
    "colon_fence",  # For admonitions
    "deflist",
    "html_image",
]
myst_update_mathjax = False
myst_dmath_double_inline = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    '_build', 'Thumbs.db', '.DS_Store', '_website',
    "posts/*/.ipynb_checkpoints/*",
    ".github/*",
    ".history",
    "github_submodule/*",
    "LICENSE.md",
    "README.md",
]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_book_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_extra_path = [
    "misc/"  # Includes other static webpages
]
html_template_path = ['_templates']

html_title = "Max Rausch-Dupont"
html_logo = "_static/picture-bw.jpg"
html_sidebars = {
    "index": [
        "info.html", 
        "search-field.html", 
        "recentposts.html", 
        "categories.html"
    ],
    "blog/**": [
        "info.html",
        "search-field.html", 
        "recentposts.html", 
        "categories.html",
        "tagcloud.html",
        "archives.html"
    ],
    "blog": [
        "info.html",
        "search-field.html", 
        "recentposts.html", 
        "categories.html",
        "tagcloud.html",
        "archives.html"
    ],
    "posts/**": [
        "info.html",
        "search-field.html",
        "postcard.html",
        "recentposts.html"
    ],
    "about": [
        "info.html"
    ],
    "climbing": [
        "info.html"
    ],
}


html_theme_options = {
    "use_fullscreen_button": False,
    "use_repository_button": False,
    "use_sidenotes": True,
    "home_page_in_toc": True,
    "github_url": "https://github.com/MushroomMaula/",
    "search_bar_text": "Search posts ...",
    "extra_navbar": "<p>Created using <a href='https://www.sphinx-doc.org/en/master/'>Sphinx</a> and <a href='https://sphinx-book-theme.readthedocs.io/en/stable/'>the sphinx book theme</a>. Design and setup greatly inspired by <a href='https://predictablynoisy.com/'> Chris Holdgraf </a>. </p>",
}


# -- Options for ablog --------------------------------------------------------
blog_post_pattern = "posts/**"
blog_baseurl = "https://www.rausch-dupont.de"
blog_authors = {
    "Max": ("Max Rausch-Dupont", "https://www.rausch-dupont.de")
}
blog_default_author = "Max"

blog_feed_fulltext = True

post_data_format = "%d %B, %Y"
post_auto_image = 1

def setup(app):
    app.add_css_file("custom.css")