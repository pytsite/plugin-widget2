"""PytSite Widget2 Plugin Input Widgets
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

import htmler
from ._widget import Widget


class Input(Widget):
    """Base Input
    """

    def __init__(self, uid: str = None, **kwargs):
        super().__init__(uid, **kwargs)

        self._type = kwargs.get('type', 'hidden')

    def render(self) -> htmler.Element:
        self._props.update({
            'type': self._type,
        })

        return super().render()


class Hidden(Input):
    """Hidden Input
    """

    def __init__(self, uid: str = None, **kwargs):
        super().__init__(uid, type='hidden', **kwargs)


class Text(Input):
    """Text Input
    """

    def __init__(self, uid: str = None, **kwargs):
        """Init.
        """
        super().__init__(uid, type='text', **kwargs)

        self._props.update({
            'autoComplete': kwargs.get('autocomplete', 'on'),
            'minLength': kwargs.get('min_length'),
            'maxLength': kwargs.get('max_length'),
            'prepend': kwargs.get('prepend'),
            'append': kwargs.get('append'),
            'inputmask': kwargs.get('inputmask'),
        })
