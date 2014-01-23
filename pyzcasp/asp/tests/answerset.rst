Required import::

    >>> from pyzcasp.asp import AnswerSet
    
An instance of AnswerSet is simply a list of atoms an a score

    >>> ans = AnswerSet(['a','b'], 10)
    >>> ans.atoms
    ['a', 'b']
    >>> ans.score
    10

Both arguments are actually optional::

    >>> empty = AnswerSet()
    >>> empty.atoms
    []
    >>> empty.score
    
