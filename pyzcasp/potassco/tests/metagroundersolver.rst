Required imports::

    >>> from zope import component
    >>> from pyzcasp import potassco

Multi-adapt a grounder and solver object::

    >>> grover = component.getMultiAdapter((fake_gringo, fake_clasp), potassco.IMetaGrounderSolver, 'metasp')
    
Next, use run with optional stdin and filter to be applied over each answer set::

    >>> solutions = grover.run(termset_filter=lambda t: t.arg(0) < 5)
    >>> [t for t in sorted(solutions[0], key=lambda t:t.arg(0))]
    [Term('a',[1]), Term('a',[2]), Term('a',[3]), Term('a',[4])]
    
You can also provide an interface in order to adapt each answer set::
    
    >>> solutions = grover.run(adapter=INumbers)
    >>> solutions[0]
    [1, 2, 3, 4, 5]