"""PytSite Widget2 Plugin Input Widgets
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from ._widget import Widget


class Input(Widget):
    """Base Input
    """

    def __init__(self, uid: str = None, **kwargs):
        super().__init__(uid, **kwargs)

        self._props.update({
            'autoComplete': kwargs.get('autocomplete', 'on'),
            'autoFocus': kwargs.get('autofocus', False),
            'disabled': kwargs.get('disabled', False),
            'form': kwargs.get('form'),
            'list': kwargs.get('list'),
            'name': kwargs.get('name', self.uid),
            'readOnly': kwargs.get('readonly', False),
            'required': kwargs.get('required', False),
            'tabIndex': kwargs.get('tabindex'),
            'type': kwargs.get('type', 'hidden'),
        })


class Hidden(Input):
    """Hidden Input
    """

    def __init__(self, uid: str = None, **kwargs):
        super().__init__(uid, type='hidden', **kwargs)


class Text(Input):
    """Text Input
    """

    def __init__(self, uid: str = None, **kwargs):
        """Init
        """
        super().__init__(uid, type='text', **kwargs)

        self._props.update({
            'append': kwargs.get('append'),
            'inputmask': kwargs.get('inputmask'),
            'maxLength': kwargs.get('max_length'),
            'minLength': kwargs.get('min_length'),
            'prepend': kwargs.get('prepend'),
        })


class Submit(Input):
    """Submit Input
    """

    def __init__(self, uid: str = None, **kwargs):
        """Init.
        """
        super().__init__(uid, type='submit', **kwargs)
