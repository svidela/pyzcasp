Run doctests using:

    $ nosetests --with-doctest --doctest-extension=rst --doctest-fixtures=_fixt --with-coverage --cover-package pyzcasp
    .......
    Name                          Stmts   Miss  Cover   Missing
    -----------------------------------------------------------
    pyzcasp                           0      0   100%
    pyzcasp.asp                      11      0   100%
    pyzcasp.asp.adapters             92      6    93%   98, 143, 148, 151, 154, 162
    pyzcasp.asp.impl                123      0   100%
    pyzcasp.asp.interfaces           60      0   100%
    pyzcasp.asp.utilities            61     21    66%   31-32, 35-50, 56, 59, 62, 65, 78, 83, 89
    pyzcasp.potassco                 13      0   100%
    pyzcasp.potassco.adapters        35     19    46%   28-34, 42, 44, 48-57, 61-65
    pyzcasp.potassco.impl             0      0   100%
    pyzcasp.potassco.interfaces      10      0   100%
    pyzcasp.potassco.utilities       66     34    48%   35, 38-42, 45-51, 54, 57, 59-66, 70, 74, 86, 89, 92-99, 102-103, 106, 112, 118
    -----------------------------------------------------------
    TOTAL                           471     80    83%
    ----------------------------------------------------------------------
    Ran 7 tests in 0.190s
    
    OK

Check out some [examples](pyzcasp/examples) use cases.
