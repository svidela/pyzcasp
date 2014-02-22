    >>> from zope import component
    >>> from pyzcasp import asp
    
First we get the registry utility using::

    >>> reg = component.getUtility(asp.IArgumentRegistry)
    
Next, we register arguments for generic grounder and solver::

    >>> reg.register('package.fun.args', ["-c k={k}"], asp.IGrounder)
    >>> reg.register('package.fun.args', ["--quiet=1", "--option=some-value"], asp.ISolver)

Now, let's suppose we have a grounder and solver objects::

    >>> grounder = asp.Grounder(None)
    >>> solver = asp.Solver(None)
    
we get the arguments for the grounder and solver at hand using::

    >>> grounder_args = component.getUtility(asp.IArgumentRegistry).arguments(grounder)
    >>> solver_args = component.getUtility(asp.IArgumentRegistry).arguments(solver)
    
and we ask for a specific arguments by their name::    
    
    >>> grounder_args('package.fun.args') == ["-c k={k}"]
    True
    >>> solver_args('package.fun.args') == ["--quiet=1", "--option=some-value"]
    True
