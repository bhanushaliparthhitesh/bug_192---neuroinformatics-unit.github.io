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
# Custom next / previous page navigation
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
# Example – remove the "Next" button entirely on a page:
#
#   ---
#   next_page: ""
#   ---
#
# Notes:
#   • Docnames must NOT include the file extension (use 'about', not 'about.md').
#   • Paths are relative to the docs/source root
#     (e.g., 'get-involved/index', 'blog/index').
#   • To remove the Next or Previous button entirely, set the value to an
#     empty string: ``next_page: ""``
#
# ---------------------------------------------------------------------------
# Worked example – tracing the full flow end-to-end
# ---------------------------------------------------------------------------
#
# The site's toctree order is:
#
#   index  →  about  →  people  →  projects  →  publications  →  …
#
# By default Sphinx gives "index" a "Next ▶ About us" button.
#
# Goal: make the "index" page jump straight to "projects" for Next, and
#       make the "projects" page return straight to "index" for Previous.
#       (The "about" and "people" pages keep their default buttons.)
#
# Step 1 – add front-matter to docs/source/index.md:
#
#   ---
#   next_page: projects
#   next_page_title: "Projects"
#   ---
#
# Step 2 – add front-matter to docs/source/projects.md:
#
#   ---
#   prev_page: index
#   prev_page_title: "Home"
#   ---
#
# Step 3 – Sphinx reads both files and stores their metadata:
#
#   env.metadata["index"]    == {"next_page": "projects",
#                                "next_page_title": "Projects"}
#   env.metadata["projects"] == {"prev_page": "index",
#                                "prev_page_title": "Home"}
#
# Step 4 – when Sphinx renders "index", it fires html-page-context and
#           calls _override_next_prev_page(app, "index", ..., context, ...):
#
#   metadata = env.metadata.get("index", {})
#   # metadata == {"next_page": "projects", "next_page_title": "Projects"}
#
#   if "next_page" in metadata:          # True – key is present
#       next_docname = "projects"
#
#       if next_docname == "":           # False – not suppressing
#           ...
#       else:
#           next_title = "Projects"      # from next_page_title
#
#           context["next"] = {
#               "link": "projects/",     # relative URL to projects page
#               "title": "Projects",
#               "subtitle": "",
#           }
#
#   if "prev_page" in metadata:          # False – key absent; Sphinx default
#       ...                              # (index has no Previous button anyway)
#
# Step 5 – when Sphinx renders "projects", the same callback fires:
#
#   metadata = env.metadata.get("projects", {})
#   # metadata == {"prev_page": "index", "prev_page_title": "Home"}
#
#   if "next_page" in metadata:          # False – no override; default kept
#       ...
#
#   if "prev_page" in metadata:          # True
#       prev_docname = "index"
#       prev_title   = "Home"
#
#       context["prev"] = {
#           "link": "../",               # relative URL back to index
#           "title": "Home",
#           "subtitle": "",
#       }
#
# Step 6 – the Jinja2 template reads the context and renders:
#
#   On index:    <a href="projects/">Next ▶ Projects</a>
#   On projects: <a href="../">◀ Previous Home</a>
#
# The "about" and "people" pages are untouched and use Sphinx defaults.
#
# ---------------------------------------------------------------------------
# How to change the navigation flow – step-by-step guide
# ---------------------------------------------------------------------------
#
# The navigation flow is the sequence in which "Next ▶" and "◀ Previous"
# buttons take the reader from page to page.  There are three ways to change
# it, ranging from simplest to most powerful:
#
# ── Option A: Override links on individual pages (no Python changes needed) ──
#
#   This is the recommended approach for one-off adjustments.  Open the
#   Markdown source of any page and add (or edit) its YAML front-matter block.
#
#   Step 1.  Identify the *docname* of the page you want to link to.
#            A docname is the path from docs/source/ to the file, without its
#            extension.  For example:
#              docs/source/about.md          → docname: "about"
#              docs/source/get-involved/index.md → docname: "get-involved/index"
#
#   Step 2.  Open the Markdown file whose buttons you want to change.
#
#   Step 3.  Add or edit the front-matter at the very top of the file:
#
#              ---
#              next_page: <target-docname>        # required
#              next_page_title: "Custom label"    # optional
#              prev_page: <target-docname>        # required
#              prev_page_title: "Custom label"    # optional
#              ---
#
#            Omit a key to leave the corresponding button unchanged.
#            Set a key to "" (empty string) to hide the button entirely.
#
#   Step 4.  Rebuild the docs:  make -C docs html
#            The buttons on that page will now point to your chosen targets.
#
# ── Option B: Change the default toctree order (affects ALL pages) ──
#
#   If you want to change the default sequence for a whole section, edit the
#   toctree directives in the relevant index.rst / index.md files.  Sphinx
#   will automatically derive next/prev from the new order.  Pages that carry
#   explicit front-matter overrides (Option A) still take precedence.
#
# ── Option C: Modify this Python callback (advanced) ──
#
#   You can change the Python code in _override_next_prev_page() itself to
#   implement custom logic that front-matter alone cannot express.  Common
#   extension points:
#
#   • Add new front-matter keys  – mirror the existing "next_page" / "prev_page"
#     pattern: read a new key from `metadata`, compute the desired value, and
#     write it into `context`.
#
#   • Apply site-wide rules  – move logic outside the per-page `if` guards to
#     apply transformations to every page unconditionally.
#
#   • Derive targets programmatically  – instead of reading a static docname
#     from metadata, call any Python code (look up a database, parse a config
#     file, inspect env.toctree_includes, …) and write the result into context.
#
#   After any Python change, rebuild the docs to see the effect.
#
# ---------------------------------------------------------------------------
# Worked example – tracing a real bidirectional flow change
# ---------------------------------------------------------------------------
#
# This section traces exactly what happens when the two overrides currently
# present in about.md and projects.md are processed by the build.
#
# ── The default toctree chain (no front-matter) ──────────────────────────────
#
#   about  →  people  →  projects  →  publications  →  …
#
#   Sphinx derives this order from the toctree in index.md.  Every page's
#   "Next ▶" button leads to the page listed immediately after it in that
#   toctree, and every "◀ Previous" button leads to the page listed before it.
#
# ── What the overrides do ─────────────────────────────────────────────────────
#
#   about.md front-matter:
#     next_page: projects
#     next_page_title: "Projects"
#
#   projects.md front-matter:
#     prev_page: about
#     prev_page_title: "About us"
#
#   Resulting navigation:
#
#     ◀  About  ──Next──▶  Projects  ──Next──▶  Publications  …
#                           ◀──Prev──  About
#
#   The "people" page is now bypassed in both directions: the reader can
#   still reach it via the sidebar, but the Next/Prev buttons skip it.
#
# ── Step-by-step trace through the Python code ───────────────────────────────
#
#   When Sphinx renders about.html it fires the html-page-context event.
#   _override_next_prev_page is called with pagename="about".
#
#   1.  env.metadata.get("about", {})
#         → {"next_page": "projects", "next_page_title": "Projects"}
#
#   2.  "next_page" is found in metadata  →  enter the if-block.
#
#   3.  next_docname = "projects"  (not empty, so the else-branch runs)
#
#   4.  next_title = metadata.get("next_page_title", "")
#         → "Projects"  (author supplied an explicit label)
#
#   5.  context["next"] = {
#           "link":     get_relative_uri("about", "projects")
#                         → a relative URL such as "projects/" or "projects.html"
#                           (exact format depends on the builder configuration),
#           "title":    "Projects",
#           "subtitle": "",
#       }
#       The template now renders: Next ▶ Projects
#
#   The "prev_page" key is absent from about.md, so context["prev"] is
#   left as the toctree default (nothing before "about").
#
#   ---
#
#   When Sphinx renders projects.html (pagename="projects"):
#
#   1.  env.metadata.get("projects", {})
#         → {"prev_page": "about", "prev_page_title": "About us"}
#
#   2.  "prev_page" is found  →  enter the if-block.
#
#   3.  prev_docname = "about"  (not empty)
#
#   4.  prev_title = "About us"  (explicit label)
#
#   5.  context["prev"] = {
#           "link":     get_relative_uri("projects", "about")
#                         → a relative URL such as "../about/" or "../about.html"
#                           (exact format depends on the builder configuration),
#           "title":    "About us",
#           "subtitle": "",
#       }
#       The template now renders: ◀ About us
#
#   context["next"] is left at the toctree default
#   (publications, the page after projects).
#
# ── How to reproduce / adapt this for your own pages ─────────────────────────
#
#   1.  Decide the new chain, e.g.  about → projects → people → publications
#
#   2.  In about.md add:
#         next_page: projects
#
#   3.  In projects.md add:
#         next_page: people
#         prev_page: about
#
#   4.  In people.md add:
#         next_page: publications
#         prev_page: projects
#
#   5.  Run:  make -C docs html
#       The buttons reflect the new chain immediately.
#
# ---------------------------------------------------------------------------

def _override_next_prev_page(app, pagename, templatename, context, doctree):
    """Override auto-generated next/prev nav links using per-page front-matter.

    Sphinx fires the ``html-page-context`` event once for every page it
    renders.  This callback intercepts that event and, when the current page
    carries ``next_page`` or ``prev_page`` keys in its YAML front-matter,
    replaces the auto-generated navigation links that Sphinx would otherwise
    derive from the toctree order.

    Parameters
    ----------
    app : sphinx.application.Sphinx
        The running Sphinx application instance.  Used to access the build
        environment (``app.builder.env``) and to resolve relative URIs
        between pages (``app.builder.get_relative_uri``).
    pagename : str
        The docname of the page currently being rendered (e.g. ``"about"``
        or ``"get-involved/index"``), relative to ``docs/source/`` and
        without a file extension.
    templatename : str
        The Jinja2 template file being used to render this page (e.g.
        ``"page.html"``).  Not used by this function but required by the
        Sphinx event signature.
    context : dict
        The template rendering context that Sphinx will pass to Jinja2.
        This function mutates ``context["next"]`` and/or ``context["prev"]``
        in-place when front-matter overrides are found.  Each value is
        either ``None`` (suppress the button) or a dict with the keys
        ``"link"``, ``"title"``, and ``"subtitle"``.
    doctree : docutils.nodes.document or None
        The parsed doctree for the page.  Not used by this function but
        required by the Sphinx event signature.

    Returns
    -------
    None
        The function modifies *context* in-place; it does not return a value.

    Notes
    -----
    *How it works, step by step:*

    1. ``env.metadata[pagename]`` is consulted for ``next_page`` /
       ``prev_page`` keys written as YAML front-matter in the ``.md`` source.
    2. If a key is absent the corresponding nav link is left unchanged
       (Sphinx's default toctree-derived link is used).
    3. If the key is present but its value is an **empty string** the
       navigation button is suppressed by setting ``context["next"]`` or
       ``context["prev"]`` to ``None``.
    4. Otherwise the docname is resolved to a relative URL with
       ``get_relative_uri``, the title is taken from the optional
       ``next_page_title`` / ``prev_page_title`` front-matter key or, when
       that is absent, looked up from ``env.titles``, and the result is
       written into *context* as a dict that the HTML template understands.

    *Changing the flow – what to modify and where:*

    - **To redirect one page's button**: add ``next_page`` / ``prev_page``
      front-matter to the relevant ``.md`` file and rebuild.  No Python
      change is needed.
    - **To support a new front-matter key**: copy either ``if "next_page"``
      block, rename the key, and write the result into a new ``context``
      entry that your template reads.
    - **To apply a rule to every page**: add unconditional logic before or
      after the existing ``if`` guards; *context* is always available and
      can be read or overwritten freely.
    - **To derive targets programmatically**: replace the
      ``metadata["next_page"]`` lookup with any Python expression
      (e.g., a dict mapping pagenames to targets, a call to
      ``env.toctree_includes``, etc.) and write the result into *context*.
    """
    # ── Shared setup ──────────────────────────────────────────────────────────
    # `env` is the Sphinx build environment; it holds metadata, titles, and
    # the full document graph for every page in the project.
    env = app.builder.env

    # `metadata` is a plain dict populated from the YAML front-matter block
    # (the `--- ... ---` header) of the current Markdown page.  If the page
    # has no front-matter, or the page is not a Markdown file, this is {}.
    metadata = env.metadata.get(pagename, {})

    # ── Next-page override ────────────────────────────────────────────────────
    # Only act when the page author has explicitly set `next_page` in the
    # front-matter.  If the key is absent we leave Sphinx's default alone.
    if "next_page" in metadata:
        # The value is the *docname* of the desired target page, e.g. "about"
        # or "get-involved/index".  An empty string is the author's signal
        # that the Next button should be hidden on this page.
        next_docname = metadata["next_page"]

        if next_docname == "":
            # Setting context["next"] to None tells the HTML template to omit
            # the "Next ▶" button entirely for this page.
            context["next"] = None
        else:
            # ── Resolve the button label ──────────────────────────────────────
            # Prefer an explicit title from the author; fall back to the
            # target page's own H1 heading as recorded in env.titles.
            next_title = metadata.get("next_page_title", "")
            if not next_title and next_docname in env.titles:
                # env.titles[docname] is a docutils Text node; .astext()
                # converts it to a plain Python string.
                next_title = env.titles[next_docname].astext()

            # ── Write the override into the template context ──────────────────
            # get_relative_uri(from, to) computes the relative URL path from
            # the current page to the target page, e.g. "../about/".  This
            # is necessary because HTML pages can live at different directory
            # depths and the template must emit a correct href attribute.
            context["next"] = {
                "link": app.builder.get_relative_uri(pagename, next_docname),
                "title": next_title,
                # "subtitle" is shown below the title in some themes; we
                # leave it empty because front-matter does not supply one.
                "subtitle": "",
            }

    # ── Previous-page override ────────────────────────────────────────────────
    # Identical logic to the next-page block above, applied to the "◀ Prev"
    # button.  See the comments there for a full line-by-line explanation.
    if "prev_page" in metadata:
        prev_docname = metadata["prev_page"]

        if prev_docname == "":
            # Hide the "◀ Previous" button on this page.
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
