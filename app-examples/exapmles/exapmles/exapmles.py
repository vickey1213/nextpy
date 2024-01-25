# This file has been modified by the Nextpy Team in 2023 using AI tools and automation scripts.
# We have rigorously tested these modifications to ensure reliability and performance. Based on successful test results, we are confident in the quality and stability of these changes.

import nextpy as xt

# Construct the filename to display
from xtconfig import config

filename = f"{config.app_name}/{config.app_name}.py"


# define index page. Frontend Pages are just functions that return a frontend components
def index() -> xt.Component:
    return xt.fragment(
        xt.button("click me"),
        xt.checkbox(),
        xt.color_mode_switch(),
        xt.DatePicker(),
        xt.editable("ni"),
        xt.password(),
    )


app = xt.App()
app.add_page(index)
