"""PytSite Widget2 Plugin Input Widgets
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

import htmler
from . import _base


class Input(_base.Base):
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

    def __init__(self, uid: str, **kwargs):
        """Init.
        """
        super().__init__(uid, type='text', **kwargs)

        self._props.update({
            'autocomplete': kwargs.get('autocomplete', 'on'),
            'min_length': kwargs.get('min_length'),
            'max_length': kwargs.get('max_length'),
            'prepend': kwargs.get('prepend'),
            'append': kwargs.get('append'),
            'inputmask': kwargs.get('inputmask'),
        })
