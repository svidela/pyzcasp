Run doctests using:

    $ nosetests --with-doctest --doctest-extension=rst --doctest-fixtures=_fixt --doctest-options='+NORMALIZE_WHITESPACE,+ELLIPSIS' --with-coverage --cover-package pyzcasp.asp --cover-package pyzcasp.potassco
    ............
    Name                          Stmts   Miss  Cover   Missing
    -----------------------------------------------------------
    pyzcasp.asp                      12      0   100%
    pyzcasp.asp.adapters             58      0   100%
    pyzcasp.asp.impl                 91      1    99%   150
    pyzcasp.asp.interfaces           61      0   100%
    pyzcasp.asp.utilities            74     19    74%   36-59, 65
    pyzcasp.potassco                 30      0   100%
    pyzcasp.potassco.adapters        42      0   100%
    pyzcasp.potassco.impl             0      0   100%
    pyzcasp.potassco.interfaces      24      0   100%
    pyzcasp.potassco.utilities      116     48    59%   45-57, 61, 65, 69, 73, 77, 84, 87-92, 95-99, 102, 105, 108, 111, 114-118, 121, 125, 131, 137, 144, 148, 151, 153-154, 157-158, 162, 171, 187-190
    -----------------------------------------------------------
    TOTAL                           508     68    87%
    ----------------------------------------------------------------------
    Ran 12 tests in 0.335s
        
    OK

Check out some [examples](pyzcasp/examples) use cases.
