Required imports::

    >>> from zope import component
    >>> from pyzcasp import asp

Multi-adapt a grounder and solver object::

    >>> grover = component.getMultiAdapter((fake_grounder, fake_solver), asp.IGrounderSolver)
    
Next, use run with optional stdin and filter to be applied over each answer set::

    >>> solutions = grover.run("d.", termset_filter=lambda t: len(t.args) == 0)
    >>> [t for t in sorted(solutions[0], key=lambda t:t.pred)]
    [Term('a'), Term('b')]
    >>> solutions[0].score
    10
    
    >>> [t for t in sorted(solutions[1], key=lambda t:t.pred)]
    [Term('a'), Term('c')]
    >>> solutions[1].score
    12

You can also provide an interface in order to adapt each answer set::
    
    >>> solutions = grover.run(adapter=IScore)
    >>> sorted(solutions, key=lambda o: o.score)
    [10, 12]
    
An adapter from ``asp.IAnswerSet`` to ``IScore`` must be registered beforehand (see groundersolver_fixt.py).

    >>> solutions = grover.run(adapter=INoAdapter)
    Traceback (most recent call last):
    ...
    TypeError: ('Could not adapt', <pyzcasp.asp.impl.AnswerSet object at ...>, <InterfaceClass groundersolver_fixt.INoAdapter>)
