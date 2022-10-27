#!/usr/bin/python3
"""docs are to up
"""


class Archive:
    """docs are to up"""
    def __init__(self, stored_data, type_of_data="basic"):
        """..."""
        self._data = stored_data
        self._container = type_of_data

    @property
    def data(self):
        """..."""
        return self._data

    @property
    def container(self):
        """..."""
        return self._container

    def __call__(self, *kwargs):
        print("work in progess...")
