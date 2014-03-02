Required imports::

    >>> from zope import interface
    >>> from pyzcasp.asp import AnswerSet, ITermSet
    >>> from pyzcasp.potassco import IMetaAnswerSet

Let's define a toy answer set as returned by metasp encodings::
    
    >>> atoms = ["hold(atom(a(5)))", "hold(atom(a(4)))", "hold(atom(a(3)))", "hold(atom(a(2)))", "hold(atom(a(1)))"]
    >>> answer = AnswerSet(atoms, [42])
    >>> interface.directlyProvides(answer, IMetaAnswerSet)

Now, we can adapt this answer set to a ``TermSet`` as follows::
    
    >>> ts = ITermSet(answer)
    >>> s = sorted(ts, key=lambda t: t.arg(0))
    >>> s
    [Term('a',[1]), Term('a',[2]), Term('a',[3]), Term('a',[4]), Term('a',[5])]
    >>> ts.score
    [42]
    