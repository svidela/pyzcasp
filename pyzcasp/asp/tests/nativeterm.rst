Required imports::

    >>> from zope.interface import providedBy
    >>> from pyzcasp.asp import NativeTerm, INativeTerm

We create 3 ``NativeTerm`` instances::

    >>> a = NativeTerm('a')
    >>> b = NativeTerm('b')
    >>> c = NativeTerm('a')
    
Instances of ``NativeTerm`` provide ``INativeTerm``::

    >>> INativeTerm in providedBy(a)
    True
    
We can access to their names using the ``name`` property::

    >>> a.name
    'a'

or simply by their str representation::

    >>> str(a), str(b), str(c)
    ('a', 'b', 'a')

Instances of ``NativeTerm`` are comparable (== , !=) and hashable::

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
