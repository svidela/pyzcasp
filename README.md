Run doctests using:

    $ nosetests --with-doctest --doctest-extension=rst --doctest-fixtures=_fixt --doctest-options='+NORMALIZE_WHITESPACE' --with-coverage --cover-package pyzcasp
    ..........
    Name                          Stmts   Miss  Cover   Missing
    -----------------------------------------------------------
    pyzcasp                           0      0   100%
    pyzcasp.asp                      12      0   100%
    pyzcasp.asp.adapters             97      1    99%   76
    pyzcasp.asp.impl                124      8    94%   167, 170-171, 190-193, 196
    pyzcasp.asp.interfaces           64      0   100%
    pyzcasp.asp.utilities            80     22    73%   36-59, 65, 68, 71, 74
    pyzcasp.potassco                 13      0   100%
    pyzcasp.potassco.adapters        42     29    31%   28-34, 42-44, 47-58, 62-76
    pyzcasp.potassco.impl             0      0   100%
    pyzcasp.potassco.interfaces      16      0   100%
    pyzcasp.potassco.utilities      120     76    37%   37-42, 45-57, 60-72, 76, 80, 84, 88, 91, 98, 101-104, 107, 110-117, 120-121, 127, 133, 140, 144, 147-150, 153, 156-159, 162-163, 169-176, 179-198
    -----------------------------------------------------------
    TOTAL                           568    136    76%
    ----------------------------------------------------------------------
    Ran 10 tests in 0.180s
    
    OK

Check out some [examples](pyzcasp/examples) use cases.
