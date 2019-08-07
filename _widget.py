"""Base Widget
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

import htmler
from typing import Any
from json import dumps as json_dumps
from pytsite.util import cleanup_dict, random_password as random_str


def _json_serialize(obj):
    if isinstance(obj, Widget):
        return obj.as_jsonable()

    raise TypeError()


class Widget:
    @property
    def cid(self) -> str:
        """Get class ID
        """
        return self._cid

    @property
    def css(self) -> str:
        """Get CSS
        """
        return self._props['className']

    @css.setter
    def css(self, css: str):
        """Set CSS
        """
        self._props['className'] = css

    @property
    def props(self) -> dict:
        """Get properties
        """
        return self._props

    @property
    def uid(self) -> str:
        """Get UID
        """
        return self._props['id']

    @uid.setter
    def uid(self, uid: str):
        """Set UID
        """
        self._props['id'] = uid

    @property
    def value(self) -> Any:
        """Get value
        """
        return self._props['value']

    @value.setter
    def value(self, value: Any):
        """Set value
        """
        self._props['value'] = value

    def __init__(self, uid: str = None, **kwargs):
        """Init
        """
        self._cid = (self.__class__.__module__ + '.' + self.__class__.__name__).lower().replace('._', '.')
        self._props = {
            'className': kwargs.get('css', 'pytsite-widget2'),
            'id': uid or random_str(alphanum_only=True),
            'value': kwargs.get('value'),
        }

    def as_jsonable(self):
        """Hook
        """
        return {
            'cid': self.cid,
            'props': cleanup_dict(self._props),
        }

    def render(self) -> htmler.Element:
        """Render the widget
        """
        return htmler.Div(
            css='pytsite-widget2-container',
            data_cid=self.cid,
            data_props=json_dumps(cleanup_dict(self._props), default=_json_serialize),
        )

    def __str__(self) -> str:
        """__str___()
        """
        return str(self.render())
