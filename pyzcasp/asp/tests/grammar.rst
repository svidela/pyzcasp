Required import::

    >>> from pyzcasp import asp
    
First we get the grammar for parsing atoms::
    
    >>> parser = asp.Grammar()

Next, we can parse a string as returned by ASP solvers::
    
    >>> atom1 = parser.parse('predicate(6,"string",1,term,nested(1,2))')[0]

By default, the parser will return a ``Term`` object::

    >>> atom1.pred
    'predicate'
    >>> len(atom1.args)
    5
    >>> atom1
    Term('predicate',[6,'"string"',1,Term('term'),Term('nested',[1,2])])
    
But also, we can add custom parse actions (see pyparsing docs). To do it, we can access to ``function`` or ``integer`` token objects::

    >>> f = []
    >>> r = parser.function.addParseAction(lambda t: f.append(t[0].pred))
    >>> atom2 = parser.parse('predicate(6,"string",1,term,nested(1,2))')[0]
    >>> f
    ['term', 'nested', 'predicate']
    
Since we used ``addParseAction``, we still get the ``Term`` object::

    >>> atom1 == atom2
    True

Instead, if we use ``setParseAction`` we can access directly to ParseResult objects::

    >>> f = []
    >>> r = parser.function.setParseAction(lambda t: f.append(t[0]))
    >>> atom3 = parser.parse('predicate(6,"string",1,term,nested(1,2))')
    >>> f
    ['term', 'nested', 'predicate']
    
But the final result is no longer a ``Term`` object::
    
    >>> atom3[0]
    'predicate'
    >>> atom3[1].asList()
    [6, 'string', 1, 'term', [], 'nested', [1, 2]]

Next, with the token object for numbers::

    >>> n = []
    >>> r = parser.integer.addParseAction(lambda t: n.append(t[0] + 10))
    >>> atom4 = parser.parse('predicate(6,"string",1,term,nested(1,2))')
    >>> n
    [16, 11, 11, 12]
