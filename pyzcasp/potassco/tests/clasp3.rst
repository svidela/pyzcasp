Minimalistic sanity check for Clasp3 solver. We start with the first fake execution (results are fixed by test fixtures)::

    >>> ret, code = clasp3.execute(1)
    >>> clasp3.complete
    True
    >>> clasp3.unknown
    False
    >>> clasp3.sat
    False
    >>> clasp3.unsat
    False
    >>> clasp3.optimum
    True
    >>> clasp3.calls
    2
    >>> ans = list(clasp3.answers())
    >>> [(a.atoms, a.score) for a in ans]
    [([u'a(1)', u'a(2)'], [3]), ([u'a(1)', u'a(2)'], [3])]

Second fake execution simulate quiet solving::

    >>> ret, code = clasp3.execute(2)
    >>> clasp3.sat
    True
    >>> ans = list(clasp3.answers())
    >>> [(a.atoms, a.score) for a in ans]
    []
