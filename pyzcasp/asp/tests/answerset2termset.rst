Required imports::

    >>> from zope import component
    >>> from zope.interface import providedBy
    >>> from pyzcasp.asp import Term, AnswerSet, ITermSet

Let's create a simple ``AnswerSet`` instance and adapt it to ``ITermSet``::

    >>> answer = AnswerSet(['predicate(6,"string",1,term,nested(1,2))',  'predicate(6,1)'], 10)
    >>> termset = ITermSet(answer)
    >>> len(termset)
    2
    >>> Term('predicate',[6,'string',1,Term('term'),Term('nested',[1,2])]) in termset
    True
    >>> Term('predicate',[6,1]) in termset
    True
