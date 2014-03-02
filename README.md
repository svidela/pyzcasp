Run doctests using:

    $ nosetests --with-doctest --doctest-extension=rst --doctest-fixtures=_fixt --doctest-options='+NORMALIZE_WHITESPACE,+ELLIPSIS' --with-coverage --cover-package pyzcasp.asp --cover-package pyzcasp.potassco
    ...........
    Name                          Stmts   Miss  Cover   Missing
    -----------------------------------------------------------
    pyzcasp.asp                      12      0   100%
    pyzcasp.asp.adapters             58      0   100%
    pyzcasp.asp.impl                 91      1    99%   150
    pyzcasp.asp.interfaces           64      0   100%
    pyzcasp.asp.utilities            80     22    73%   36-59, 65, 68, 71, 74
    pyzcasp.potassco                 14      0   100%
    pyzcasp.potassco.adapters        42      0   100%
    pyzcasp.potassco.impl             0      0   100%
    pyzcasp.potassco.interfaces      18      0   100%
    pyzcasp.potassco.utilities      123     71    42%   38, 45-57, 60-72, 76, 80, 84, 88, 91, 98, 101-104, 107, 110-117, 120-121, 127, 133, 139-141, 143-145, 148-150, 154, 158, 162-164, 167, 170, 173-176, 179-180, 186-193, 196-202
    -----------------------------------------------------------
    TOTAL                           502     94    81%
    ----------------------------------------------------------------------
    Ran 11 tests in 0.330s
        
    OK

Check out some [examples](pyzcasp/examples) use cases.
