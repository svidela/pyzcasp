    >>> import os
    >>> from zope import component
    >>> from pyzcasp import asp

First we get the registry utility using::
    
    >>> reg = component.getUtility(asp.IEncodingRegistry)
    
Next, we will register the this file::

    >>> root = __file__.rsplit('/', 1)[0]
    >>> path = os.path.join(root, 'encodingregistry.rst')
    >>> reg.register('package.enco', path , asp.IGrounder)

Now, let's suppose we have a grounder object::

    >>> grounder = asp.Grounder(None)
    
we get the encodings for the grounder at hand using::
    
    >>> encodings = reg.encodings(grounder)
    
and we ask for a specific encoding by it's name::

    >>> encodings('package.enco') == path
    True
    
Non existing file will fail when trying to register them::

    >>> reg.register('package.error', 'non-existing-filepath' , asp.IGrounder)
    Traceback (most recent call last):
    ...
    IOError: File not found: non-existing-filepath
