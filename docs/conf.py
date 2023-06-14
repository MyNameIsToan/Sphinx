# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Lesson01'
copyright = '2023, La Quoc Toan'
author = 'La Quoc Toan'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    sphinx_needs
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

needs_types = [
               dict(directive="stkh_req", title="Stakeholder Requirement", prefix="STAKEHOLDER_REQ", color="#ac6dd1", style="artifact"),
               dict(directive="sys_req", title="System Requirement", prefix="SYSTEM_REQ_", color="#ac6dd1", style="artifact"),
               dict(directive="sw_req", title="Software Requirement", prefix="SOFTWARE_REQ_", color="#ac6dd1", style="artifact"),
               dict(directive="interface_req", title="Interface Requirement", prefix="INTERFACE_REQ_", color="#ac6dd1", style="artifact"),
               dict(directive="req_desc", title="Requirement Description", prefix="REQ_DESC_", color="#ac6dd1", style="artifact"),
               dict(directive="verify", title="Verification Criteria", prefix="VC_", color="#fedcd2", style="artifact"),
               dict(directive="design", title="Design", prefix="DESIGN_", color="ffcc00", style="artifact"),
               dict(directive="design_decision", title="Design Decision", prefix="DESIGN_DECISION_", color="ffcc00", style="artifact"),
               dict(directive="test_set", title="Test Set", prefix="TS_", color="#FEDCD2", style="artifact"),
               dict(directive="test_case", title="Test Case", prefix="TC_", color="#bbff00", style="artifact"),
               dict(directive="test_step", title="Test Step", prefix="TS_", color="#bbff00", style="artifact"),
               dict(directive="test_run", title="Test Run", prefix="TR_", color="#cccccc", style="artifact"),
               dict(directive="test_exe", title="Test Execution", prefix="TEX_", color="#bbff00", style="artifact"),
               dict(directive="sw_comp", title="Software Component", prefix="SW_COMP_", color="#bbff00", style="artifact")
               ]
