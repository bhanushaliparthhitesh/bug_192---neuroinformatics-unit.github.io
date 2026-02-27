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
import os


# -- Project information -----------------------------------------------------

project = "neuroinformatics-unit homepage"
copyright = "2022–2026, Neuroinformatics Unit"
author = "Neuroinformatics Unit"

# The full version, including alpha/beta/rc tags
release = "0.0.1"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.githubpages",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "sphinx_design",
    "sphinx_sitemap",
    "sphinx_reredirects",
    "myst_parser",
    "numpydoc",
    "nbsphinx",
    "ablog",
]

# Configure the myst parser to enable cool markdown features
myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]
# Automatically add anchors to markdown headings
myst_heading_anchors = 3

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# Ignore links that do not work with github actions link checking
# https://github.com/neuroinformatics-unit/actions/pull/24#issue-1978966182
linkcheck_anchors_ignore_for_url = [
    "https://neuroinformatics.zulipchat.com/",
    "https://cocodataset.org/",
]
linkcheck_ignore = [
    "https://opensource.org",
    "https://www.incf.org/recommendations-gsoc-contributors",
    "https://www.incf.org/sites/default/files/files/INCF_GSoC_2022_Application_template.pdf",
    "https://neuroinformatics.dev/slides-templates-atlases/#/on-templates-and-atlases",
    "https://errantscience.com/",
    "https://in2scienceuk.org/our-programmes/in2research/",
    "https://www.biorxiv.org/content/10.1101/2025.03.30.645770v1",
    "https://chatgpt.com/",
    r"https://www\.cell\.com/.*",  # Use regex pattern to match all cell.com URLs
    r"https?://(?:dx\.)?doi\.org/.*",  # Use regex pattern to match all DOI URLs
    "https://besjournals.onlinelibrary.wiley.com/doi/10.1111/2041-210X.14460",
    "https://onlinelibrary.wiley.com/doi/full/10.1111/eth.12739",  # trajR
    "https://github.com/SuperElastix/elastix/releases/download/5.2.0/elastix-5.2.0-manual.pdf",
]
linkcheck_request_headers = {
    "https://github.com": {
        "Authorization": f"Bearer {os.environ.get('GITHUB_TOKEN', '')}",
    },
}
# Suppress strikethrough warnings - strikethrough is only supported in HTML
suppress_warnings = ['myst.strikethrough']


# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    "**.ipynb_checkpoints",
    # to ensure that include files (partial pages) aren't built, exclude them
    # https://github.com/sphinx-doc/sphinx/issues/1965#issuecomment-124732907
    "**/includes/**",
]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "pydata_sphinx_theme"
html_title = "NIU"

# Redirect the webpage to another URL
# Sphinx will create the appropriate CNAME file in the build directory
# https://www.sphinx-doc.org/en/master/usage/extensions/githubpages.html
html_baseurl = "https://neuroinformatics.dev/"
sitemap_url_scheme = "{link}"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

html_css_files = [
    "css/custom.css",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css"
]

html_favicon = "_static/logo_light.png"

# Customize the theme
html_theme_options = {
    "icon_links": [
        {
            # Label for this link
            "name": "GitHub",
            # URL where the link will redirect
            "url": "https://github.com/neuroinformatics-unit/",  # required
            # Icon class (if "type": "fontawesome"), or path to local image (if "type": "local")
            "icon": "fa-brands fa-github",
            # The type of image to be used (see below for details)
            "type": "fontawesome",
        },
        {
            "name": "LinkedIn",
            "url": "https://www.linkedin.com/company/neuroinformatics-unit",
            "icon": "fa-brands fa-linkedin",
        },
        {
            "name": "Mastodon",
            "url": "https://mastodon.online/@neuroinformatics",
            "icon": "fa-brands fa-mastodon",
        },
        {
            "name": "Bluesky",
            "url": "https://bsky.app/profile/neuroinformatics.dev",
            "icon": "fa-brands fa-bluesky",
        },
        {
            # Label for this link
            "name": "Zulip (chat)",
            # URL where the link will redirect
            "url": "https://neuroinformatics.zulipchat.com/",  # required
            # Icon class (if "type": "fontawesome"), or path to local image (if "type": "local")
            "icon": "fa-solid fa-comments",
            # The type of image to be used (see below for details)
            "type": "fontawesome",
        },
    ],
    "logo": {
        "text": "NIU",
        "image_light": "logo_light.png",
        "image_dark": "logo_dark.png",
    },
    "footer_start": ["footer_start"],
    "footer_end": ["footer_end"],
    "analytics": {
        "google_analytics_id": "G-6260TGM7TY",
    },
     "announcement": "Would you like a paid internship with the NIU this summer? We're taking part in <a href='https://neuroinformatics.dev/get-involved/gsoc/index.html'>Google Summer of Code</a>!",
}

html_sidebars = {
    "blog/index": [
        # Ablog sidebars (https://ablog.readthedocs.io/en/stable/manual/ablog-configuration-options.html#sidebars)
        "ablog/recentposts.html"
    ],  # 'ablog/archives.html << we may want to use archives when we have more posts.
    "**": [],
}


redirects = {
    'open-software-week/index.html': '/open-software-summer-school/index.html',
}

# Define footer links and partner information in html_context
# This makes the footer maintainable via conf.py instead of hardcoding in templates
html_context = {
    "footer_partners": [
        {
            "name": "Sainsbury Wellcome Centre",
            "url": "https://www.sainsburywellcome.org/web/",
            "logo_light": "_static/light-logo-swc.png",
            "logo_dark": "_static/dark-logo-swc.png",
        },
        {
            "name": "Gatsby Computational Neuroscience Unit",
            "url": "https://www.ucl.ac.uk/gatsby/gatsby-computational-neuroscience-unit",
            "logo_light": "_static/light-logo-gatsby.png",
            "logo_dark": "_static/dark-logo-gatsby.png",
        },
        {
            "name": "University College London",
            "url": "https://www.ucl.ac.uk/",
            "logo_light": "_static/light-logo-ucl.png",
            "logo_dark": "_static/dark-logo-ucl.png",
        },
    ],
    "footer_connect_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/neuroinformatics-unit/",
            "icon": "fa-brands fa-github",
            "type": "text_with_icon",  # Shows icon + text
        },
        {
            "name": "Zulip Chat",
            "url": "https://neuroinformatics.zulipchat.com/",
            "icon": "fa-solid fa-comments",
            "type": "text_with_icon",  # Shows icon + text
        },
        {
            "name": "Mastodon",
            "url": "https://mastodon.online/@neuroinformatics",
            "icon": "fa-brands fa-mastodon",
            "type": "icon_only",  # Shows only icon in circular button
        },
        {
            "name": "Bluesky",
            "url": "https://bsky.app/profile/neuroinformatics.dev",
            "icon": "fa-brands fa-bluesky",
            "type": "icon_only",  # Shows only icon in circular button
        },
    ],
}


# ---------------------------------------------------------------------------
# Custom page navigation override
# ---------------------------------------------------------------------------
# By default, Sphinx automatically determines the "Next" and "Previous" page
# buttons based on the order pages appear in each toctree.  This behaviour can
# be overridden on a per-page basis by adding YAML front-matter metadata to
# any Markdown (.md) file.
#
# Supported front-matter keys:
#   next_page       – docname of the page to use as "Next"
#                     (path relative to docs/source/, WITHOUT file extension)
#   prev_page       – docname of the page to use as "Previous"
#   next_page_title – optional: title to display in the "Next" button
#                     (defaults to the target page's own heading)
#   prev_page_title – optional: title to display in the "Previous" button
#
# Example – make the "About" page link to "projects" instead of "people":
#
#   ---
#   next_page: projects
#   ---
#
# Example – full override with custom titles:
#
#   ---
#   next_page: get-involved/index
#   next_page_title: "Get Involved"
#   prev_page: about
#   prev_page_title: "About us"
#   ---
#
# Notes:
#   • Docnames must NOT include the file extension (use 'about', not 'about.md').
#   • Paths are relative to the docs/source root
#     (e.g., 'get-involved/index', 'blog/index').
#   • To remove the Next or Previous button entirely, set the value to an
#     empty string: ``next_page: ""``
# ---------------------------------------------------------------------------

def _override_next_prev_page(app, pagename, templatename, context, doctree):
    """Override auto-generated next/prev nav links using per-page front-matter.

    Reads ``next_page`` and ``prev_page`` (and their optional ``_title``
    variants) from the page's YAML front-matter metadata and, when present,
    replaces the navigation context that Sphinx passes to the HTML template.
    """
    env = app.builder.env
    metadata = env.metadata.get(pagename, {})

    # Override the "next" navigation link if 'next_page' metadata is set.
    if "next_page" in metadata:
        next_docname = metadata["next_page"]
        if next_docname == "":
            # An empty string means "remove the Next button".
            context["next"] = None
        else:
            next_title = metadata.get("next_page_title", "")
            if not next_title and next_docname in env.titles:
                next_title = env.titles[next_docname].astext()
            context["next"] = {
                "link": app.builder.get_relative_uri(pagename, next_docname),
                "title": next_title,
                "subtitle": "",
            }

    # Override the "prev" navigation link if 'prev_page' metadata is set.
    if "prev_page" in metadata:
        prev_docname = metadata["prev_page"]
        if prev_docname == "":
            # An empty string means "remove the Previous button".
            context["prev"] = None
        else:
            prev_title = metadata.get("prev_page_title", "")
            if not prev_title and prev_docname in env.titles:
                prev_title = env.titles[prev_docname].astext()
            context["prev"] = {
                "link": app.builder.get_relative_uri(pagename, prev_docname),
                "title": prev_title,
                "subtitle": "",
            }


def setup(app):
    """Register the custom next/prev navigation override with Sphinx."""
    # Connect to the 'html-page-context' event so we can inspect and replace
    # the next/prev navigation links just before each page is rendered.
    app.connect("html-page-context", _override_next_prev_page)
