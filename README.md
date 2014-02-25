Run doctests using:

    $ nosetests --with-doctest --doctest-extension=rst --doctest-fixtures=_fixt --doctest-options='+NORMALIZE_WHITESPACE' --with-coverage --cover-package pyzcasp
    ..........
    Name                          Stmts   Miss  Cover   Missing
    -----------------------------------------------------------
    pyzcasp                           0      0   100%
    pyzcasp.asp                      12      0   100%
    pyzcasp.asp.adapters             97      1    99%   76
    pyzcasp.asp.impl                110      8    93%   146, 149-150, 169-172, 175
    pyzcasp.asp.interfaces           61      0   100%
    pyzcasp.asp.utilities            80     22    73%   36-59, 65, 68, 71, 74
    pyzcasp.potassco                 13      0   100%
    pyzcasp.potassco.adapters        42     29    31%   28-34, 42-44, 47-58, 62-76
    pyzcasp.potassco.impl             0      0   100%
    pyzcasp.potassco.interfaces      16      0   100%
    pyzcasp.potassco.utilities      120     76    37%   37-42, 45-57, 60-72, 76, 80, 84, 88, 91, 98, 101-104, 107, 110-117, 120-121, 127, 133, 140, 144, 147-150, 153, 156-159, 162-163, 169-176, 179-198
    -----------------------------------------------------------
    TOTAL                           551    136    75%
    ----------------------------------------------------------------------
    Ran 9 tests in 0.172s
    
    OK

Check out some [examples](pyzcasp/examples) use cases.
