Run doctests using:

    $ nosetests --with-doctest --doctest-extension=rst --doctest-fixtures=_fixt --doctest-options='+NORMALIZE_WHITESPACE,+ELLIPSIS' --with-coverage --cover-package pyzcasp.asp --cover-package pyzcasp.potassco
    ..............
    Name                          Stmts   Miss  Cover   Missing
    -----------------------------------------------------------
    pyzcasp.asp                      12      0   100%
    pyzcasp.asp.adapters             58      0   100%
    pyzcasp.asp.impl                 91      1    99%   150
    pyzcasp.asp.interfaces           62      0   100%
    pyzcasp.asp.utilities            74     19    74%   36-59, 65
    pyzcasp.potassco                 30      0   100%
    pyzcasp.potassco.adapters        42      0   100%
    pyzcasp.potassco.impl             0      0   100%
    pyzcasp.potassco.interfaces      24      0   100%
    pyzcasp.potassco.utilities      117     12    90%   45-57, 188, 194
    -----------------------------------------------------------
    TOTAL                           510     32    94%
    ----------------------------------------------------------------------
    Ran 14 tests in 0.342s
        
    OK

Check out some [examples](pyzcasp/examples) use cases.
