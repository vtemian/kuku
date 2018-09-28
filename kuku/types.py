from typing import Dict, Any, Callable, List
from collections import ChainMap


# Context is used to pass variables
class Context(ChainMap):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._missing_keys = []

    def __getitem__(self, key):
        """ Return empty string if the key to retrieve is missing """

        try:
            return super().__getitem__(key)
        except KeyError:
            self._missing_keys.append(key)

        return ''

    @property
    def is_complete(self):
        return len(self._missing_keys) == 0

    @property
    def missing_keys(self):
        return set(self._missing_keys)


# template file path -> template function
Templates = Dict[str, Callable]

# template file path -> List of K8S objects
Rendering = Dict[str, List[Any]]


class IgnoredListItem:
    """Placeholder list item to be ignored for deep merges of lists"""

    ...
