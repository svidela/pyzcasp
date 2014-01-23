Required import::

    >>> from zope.interface import providedBy
    >>> from pyzcasp.asp import AnswerSet, IAnswerSet
    
An instance of AnswerSet provides IAnswerSet and is simply a list of atoms an a score::

    >>> ans = AnswerSet(['a','b'], 10)
    >>> IAnswerSet in providedBy(ans)
    True
    >>> ans.atoms
    ['a', 'b']
    >>> ans.score
    10

Both arguments are actually optional::

    >>> empty = AnswerSet()
    >>> empty.atoms
    []
    >>> empty.score
    
