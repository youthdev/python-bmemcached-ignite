import six

__all__ = ('long', 'unicode')

if six.PY3:
    long = int
    unicode = str
else:
    long = long
    unicode = unicode
