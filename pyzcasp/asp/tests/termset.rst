Required imports::

    >>> import os
    >>> from pyzcasp.asp import TermSet, Term, cleanrun

We create TermSet instances from a list of Term instances and using the `union` method::

    >>> t1 = Term('term1', [1, 'string'])
    >>> t2 = Term('term2', [3, 4])
    >>> ts = TermSet([t1]).union(TermSet([t2]))
    >>> len(ts)
    2
    >>> t1 in ts
    True
    >>> t2 in ts
    True
    
We can also add new terms::

    >>> t3 = Term('term3')
    >>> ts.add(t3)
    >>> len(ts)
    3

TermSet implements `__iter__` to iterate over its terms::

    >>> l = list(iter(ts))
    >>> len(l)
    3
    >>> t1 in l
    True
    >>> t2 in l
    True
    >>> t3 in l
    True

We can dump the TermSet instance to a temporary file::

    >>> tmp = ts.to_file()
    >>> fd = open(tmp, 'r')
    >>> lines = fd.read().split()
    >>> len(lines)
    3
    >>> 'term1(1,"string").' in lines
    True
    >>> 'term2(3,4).' in lines
    True
    >>> 'term3.' in lines
    True

Note that the temporary file is still there (must remain accesible for the grounder afterwards)::

    >>> os.path.isfile(tmp)
    True
    >>> os.unlink(tmp)
    
Hence, we can use a decorator to have automated cleaning of temporary files. First let's define a function
that will dump the TermSet to a temporary file and simply returns its name.

    >>> @cleanrun
    ... def somefunc():
    ...     tmp = ts.to_file()
    ...     #call grounder and solver
    ...     return tmp

Now, we can call this function and check that the file was removed::

    >>> tmp = somefunc()
    >>> os.path.isfile(tmp)
    False

It is also possible to provide a specific filename if you want to make sure that the file is not removed by someone else::

    >>> ts.to_file('my-name.lp')
    'my-name.lp'
    >>> fd = open('my-name.lp', 'r')
    >>> lines = fd.read().split()
    >>> len(lines)
    3
    >>> 'term1(1,"string").' in lines
    True
    >>> 'term2(3,4).' in lines
    True
    >>> 'term3.' in lines
    True
    >>> tmp = somefunc()
    >>> os.path.isfile(tmp)
    False
    >>> os.path.isfile('my-name.lp')
    True
    >>> os.unlink('my-name.lp')
