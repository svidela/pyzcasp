Required imports::

    >>> from zope import component
    >>> from pyzcasp import potassco
    
Call to configure helper::

    >>> potassco.configure(gringo3="fake", gringo4="fake", clasp2="fake", clasp3="fake", hclasp="fake", claspD="fake", clingo="fake")
    
Let's get the utilities now.
- Gringo3::

    >>> component.getUtility(potassco.IGringo3)
    <pyzcasp.potassco.utilities.Gringo3 object at ...>

- Gringo4::

    >>> component.getUtility(potassco.IGringo4)
    <pyzcasp.potassco.utilities.Gringo4 object at ...>
    
- Clasp2::

    >>> component.getUtility(potassco.IClasp2)
    <pyzcasp.potassco.utilities.Clasp2 object at ...>
    
- Clasp3::

    >>> component.getUtility(potassco.IClasp3)
    <pyzcasp.potassco.utilities.Clasp3 object at ...>
    
- HClasp::
    
    >>> component.getUtility(potassco.IHClasp)
    <pyzcasp.potassco.utilities.HClasp object at ...>
    
- ClaspD::

    >>> component.getUtility(potassco.IClaspD)
    <pyzcasp.potassco.utilities.ClaspD object at ...>
    
- Clingo::

    >>> component.getUtility(potassco.IClingo)
    <pyzcasp.potassco.utilities.Clingo object at ...>
