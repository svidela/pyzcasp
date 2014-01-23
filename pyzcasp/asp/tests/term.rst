Required imports::

    >>> from pyzcasp.asp import NativeAtom, Term

We start creating a Term instance with some arguments::

    >>> term1 = Term('predicate', [1,u'unicode', 'string', NativeAtom('native')])

We can get the predicate name and its arguments by using::

    >>> term1.pred
    'predicate'
    >>> term1.args
    [1, u'"unicode"', '"string"', 'native']
    >>> term1.arg(0), term1.arg(1), term1.arg(2), str(term1.arg(3))
    (1, u'unicode', 'string', 'native')

Term instances implement `__str__`::

    >>> str(term1)
    'predicate(1,"unicode","string",native)'

We can also create a Term without arguments::

    >>> noargs = Term('noargs')
    >>> str(noargs)
    'noargs'
    >>> noargs.args
    []
    >>> noargs.arg(0)
    Traceback (most recent call last):
    ...
    IndexError: list index out of range

Instances of Term are comparable and hashable::

    >>> term1 == noargs
    False
    >>> term1 != noargs
    True
    >>> term2 = Term('predicate', [1,u'unicode', 'string', NativeAtom('native')])
    >>> term1 == term2
    True
    >>> hash(term1) == hash(term2) 
    True


Term instances implement `__repr__`::

    >>> term1
    Term('predicate',[1,u'"unicode"','"string"','native'])
    >>> noargs
    Term('noargs')


Term predicate name must be a non-empty string::

    >>> noargs = Term(2)
    Traceback (most recent call last):
    ...
    TypeError: Predicate name must be string. 2 <type 'int'>

    >>> noargs = Term('')
    Traceback (most recent call last):
    ...
    ValueError: Predicate name must be a non-empty string.

Term arguments cannot be neither float nor complex numbers::

    >>> novalid = Term('novalid', [1.2, complex(1,3)])
    Traceback (most recent call last):
    ...
    TypeError: Number arguments must be integers. The following arguments are forbidden: [1.2, (1+3j)]
