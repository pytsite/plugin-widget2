"""PytSite Widget2 Plugin
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from typing import List
from ._widget import Widget


class Container(Widget):
    @property
    def children(self):
        """Get children

        :rtype: Iterator[Widget]
        """
        return (w for w in self._children)

    def __init__(self, uid: str = None, **kwargs):
        super().__init__(uid, **kwargs)

        self._props['children'] = []  # type: List[Widget]

    def append_child(self, child):
        """Append a child widget

        :type child: Widget
        :rtype: Widget
        """
        if not isinstance(child, Widget):
            raise TypeError(f'Instance of {type(Widget)} expected, not {type(child)}')

        self._props['children'].append(child)

        return self

    def __len__(self) -> int:
        """__len__()
        """
        return len(self._children)
