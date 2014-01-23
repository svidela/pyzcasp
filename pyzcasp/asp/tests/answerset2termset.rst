Required imports::

    >>> from zope import component
    >>> from zope.interface import providedBy
    >>> from pyzcasp.asp import Term, NativeAtom, Lexer, AnswerSet, ITermSetParser, ITermSet

Let's create a simple ``AnswerSet`` instance and together with a parser, (multi-)adapt them to ``ITermSet``::

    >>> answer = AnswerSet(['predicate(6,"string",1,atom,nested(1,2))',  'predicate(6,1)'], 10)
    >>> with Lexer() as lexer:
    ...     with ITermSetParser(lexer) as parser:
    ...         termset = component.getMultiAdapter((answer, parser), ITermSet)
    ...
    >>> len(termset)
    2
    >>> Term('predicate',[6,'string',1,NativeAtom('atom'),Term('nested',[1,2])]) in termset
    True
    >>> Term('predicate',[6,1]) in termset
    True
