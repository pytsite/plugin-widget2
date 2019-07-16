"""PytSite Widget2 Plugin, Static Widgets
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from htmler import Element
from ._widget import Widget


class HTML(Widget):
    """Static HTML Widget
    """

    def __init__(self, em: Element, **kwargs):
        """Init
        """
        super().__init__(**kwargs)

        self._props.update({
            'html': str(em)
        })
