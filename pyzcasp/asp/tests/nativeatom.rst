Required imports::

    >>> from pyzcasp.asp import NativeAtom

We create 3 NativeAtom instances::

    >>> a = NativeAtom('a')
    >>> b = NativeAtom('b')
    >>> c = NativeAtom('a')

We can access to their names using the `name` property::

    >>> a.name
    'a'

or simply by their str representation::

    >>> str(a), str(b), str(c)
    ('a', 'b', 'a')

Instances of NativeAtom are comparable (== , !=) and hashable::

    >>> a != b
    True
    >>> a == b
    False
    >>> a == c
    True
    >>> a != c
    False
    >>> hash(a) == hash(c)
    True
    >>> hash(c) != hash(b)
    True
