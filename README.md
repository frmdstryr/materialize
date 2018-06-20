# Materialize

Materialize web components for enaml web.

### Installing

Install with pip

`pip install semantic-ui`

### Usage

Simply have your page/templates extend the base `MaterializePage` as follows.


```python
from web.components.api import *
from web.core.api import Block
from materialize.page import MaterializePage


enamldef Page(MaterializePage):
    stylesheets = [
        '/static/custom.css',
    ]
    scripts = [
        '/static/custom.js'
    ]
    
    Block:
        block = parent.header
        H2:
            text = "Page header"
    Block:
        block = parent.content
        P:
            text = "Content..."
    Block:
        block = parent.footer
        Div:
            text = "Page footer"

```

See [enaml-web](https://github.com/codelv/enaml-web) for more info.
