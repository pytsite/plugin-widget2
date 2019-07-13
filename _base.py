"""Base Widget
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

import htmler
from typing import List, Type
from json import dumps as json_dumps
from pytsite import util


def _json_serializer(obj):
    if isinstance(obj, Base):
        return {
            'cid': obj.cid,
            'weight': obj.weight,
            'props': obj.props,
            'children': obj.children,
        }

    raise TypeError()


class Base:
    @property
    def cid(self) -> str:
        """Get class ID
        """
        return self._cid

    @property
    def props(self) -> dict:
        """Get properties
        """
        return self._props

    @property
    def children(self):
        """Get children

        :rtype: List[Base]
        """
        return self._children

    @property
    def weight(self) -> int:
        """Get weight
        """
        return self._weight

    def __init__(self, uid: str = None, **kwargs):
        """Init
        """
        self._cid = (self.__class__.__module__ + '.' + self.__class__.__name__).lower().replace('._', '.')
        self._uid = uid or util.random_str()
        self._weight = kwargs.get('weight', 0)
        self._children = []  # type: List[Base]
        self._em_type = kwargs.get('em_type', htmler.Div)  # type: Type[htmler.Element]
        self._em_css = kwargs.get('em_css', 'pytsite-widget2')

        self._props = {
            'className': kwargs.get('css'),
            'id': kwargs.get('id'),
        }

    def append_child(self, child):
        """Append a child widget
        """
        self._children.append(child)
        self._children.sort(key=lambda x: x.weight)

        return self

    def render(self) -> htmler.Element:
        """Render a widget
        """

        return self._em_type(css=self._em_css,
                             data_cid=self._cid,
                             data_uid=self._uid,
                             data_weight=self._weight,
                             data_props=json_dumps(util.cleanup_dict(self._props)),
                             data_children=json_dumps(self._children, default=_json_serializer))

    def __str__(self) -> str:
        """__str___()
        """
        return str(self.render())
