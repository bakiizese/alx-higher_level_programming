#!/usr/bin/python3
"""class MyInt that inherits from int."""


class MyInt(int):
    """Invert operators"""

    def __eq__(self, value):
        """Override behavior"""
        return self.real != value

    def __ne__(self, value):
        """Override behavior"""
        return self.real == value
