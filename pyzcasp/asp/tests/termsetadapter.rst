Required imports::

    >>> import os
    >>> from pyzcasp.asp import TermSetAdapter, TermSet, Term, ITermSet
    >>> from zope import component, interface
    
Suppose we have an interface IObject and a class implementing such interface::

    >>> class IObject(interface.Interface):
    ...     values = interface.Attribute("Some values")
    ...
    
    >>> class Object(object):
    ...     interface.implements(IObject)
    ...
    ...     def __init__(self, values):
    ...         self.values = values
    ...
    
Now, let's define an adapter from IMyObject to ITermSet using TermSetAdapter base class::

    >>> class Object2TermSet(TermSetAdapter):
    ...     component.adapts(IObject)
    ...     
    ...     def __init__(self, obj):
    ...         super(Object2TermSet, self).__init__()
    ...         for value in obj.values:
    ...             self._termset.add(Term('value', [value]))
    ...
    >>> component.globalSiteManager.registerAdapter(Object2TermSet)
    
Next, we can create an instance of Object class and adapt it to ITermSet interface::

    >>> obj = Object([1,2,3])
    >>> termset = ITermSet(obj)
    
Let's check that the 3 value where added as Term instances::
    
    >>> len(termset)
    3
    >>> for i in [1,2,3]:
    ...     assert(Term('value',[i]) in termset)
    ...
    
Then, we can add more terms or union another term set::

    >>> termset.add(Term('some',['pred']))
    >>> termset = termset.union(TermSet([Term('atom')]))
    
and of course, dump everything to a file::

    >>> tmp = termset.to_file()
    >>> fd = open(tmp, 'r')
    >>> lines = fd.read().split()
    >>> for i in [1,2,3]:
    ...     assert('value(%s).' % i in lines)
    ...
    >>> 'some("pred").' in lines and 'atom.' in lines
    True
    >>> os.unlink(tmp)
