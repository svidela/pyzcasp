Required imports::

    >>> import os
    >>> from pyzcasp.asp import Lexer, ITermSetParser, TermSet

First, we simply test that we can adapt a Lexer instance to a TermSetParser::

    >>> lexer = Lexer()
    >>> parser = ITermSetParser(lexer)

Now, let's see that the parser is able to parse an atom (string) as given by ASP solvers, to an instance of Term class::

    >>> atom = 'predicate(6,"string",1,atom,nested(1,2))'
    >>> term = parser.parse(atom)
    >>> term
    Term('predicate',[6,'"string"',1,'atom',Term('nested',[1,2])])
    >>> term.arg(0), term.arg(1), term.arg(2), term.arg(3), term.arg(4)
    (6, 'string', 1, 'atom', Term('nested',[1,2]))
    
The issue with the code above is that lex and yacc generate some auxiliary files::

    >>> aux = ('parsetab.py', 'lextab.py')
    >>> for f in aux:
    ...     assert(os.path.isfile(f))
    ...
    
Thus, to remove this file automatically, our Lexer and TermSetParser should be used with the `with` statement::

    >>> with Lexer() as lexer:
    ...     with ITermSetParser(lexer) as parser:
    ...         term = parser.parse(atom)
    ...
    >>> term
    Term('predicate',[6,'"string"',1,'atom',Term('nested',[1,2])])
    >>> for f in aux:
    ...     assert(not os.path.isfile(f))
    ...
