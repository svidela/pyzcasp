Minimalistic sanity check for Clasp2 solver. We start with the first fake execution (results are fixed by test fixtures)::

    >>> ret, code = clasp2.execute(1)
    >>> clasp2.complete
    True
    >>> clasp2.unknown
    False
    >>> clasp2.sat
    False
    >>> clasp2.unsat
    False
    >>> clasp2.optimum
    True
    >>> ans = list(clasp2.answers())
    >>> [(a.atoms, a.score) for a in ans]
    [([u'a(2)', u'a(3)'], [5]), ([u'a(1)', u'a(3)'], [4]), ([u'a(1)', u'a(2)'], [3]), ([u'a(1)', u'a(2)', u'a(3)'], [6])]

Second fake execution simulate brave consequences::

    >>> ret, code = clasp2.execute(2)
    >>> clasp2.optimum
    False
    >>> ans = list(clasp2.answers())
    >>> [a.atoms for a in ans]
    [[u'a(1)', u'a(2)', u'a(3)']]
    
Third fake execution simulate cautious consequences::

    >>> ret, code = clasp2.execute(3)
    >>> clasp2.optimum
    False
    >>> ans = list(clasp2.answers())
    >>> [a.atoms for a in ans]
    [[]]
    
Fourth fake execution simulate quiet solving::

    >>> ret, code = clasp2.execute(4)
    >>> clasp2.sat
    True
    >>> ans = list(clasp2.answers())
    >>> [a.atoms for a in ans]
    []