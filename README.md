# About

This is the source for [my blog](https://www.rausch-dupont.de). It is build using [Sphinx](https://www.sphinx-doc.org/), [sphinx-book-theme](https://sphinx-book-theme.readthedocs.io/) and [ablog](https://ablog.readthedocs.io/)
for the blogging side of things.

Most of the custom design is inspired by [Chris Holgraf's website](https://predictablynoisy.com/).

## Getting started
If you wish to create a similar blog follow these steps:
- Clone this repoe
- Make sure poetry is installed and run `poetry install`
- The name, author etc. can be changed in `conf.py`, for the non-sphinx options have a look at the documentation of `ablog` and the `sphinx-book-theme`.
- The displayed image can be changed in the `_static/` folder
- To build and view the website run the following command:
    `poetry run ablog build && poetry run serve`
