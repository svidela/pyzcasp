This package provides a python framework to build on top of Answer Set Programming tools using the [Zope Component Architecture](http://muthukadan.net/docs/zca.html).

Currently **pyzcasp** supports the usage of most common tools from [Potassco](http://potassco.sourceforge.net/):
- [clingo](https://sourceforge.net/projects/potassco/files/clingo/) (series 4)
- [gringo](https://sourceforge.net/projects/potassco/files/gringo/) (series 3 and 4)
- [clasp](https://sourceforge.net/projects/potassco/files/clasp/) (series 2 and 3)
- [hclasp](https://sourceforge.net/projects/potassco/files/hclasp/)
- [claspD-2](http://www.cs.uni-potsdam.de/claspD/)

The corresponding binaries for each tool must be installed manually. Note that, latest _clingo_, _gringo_ and _clasp_ are available in [Debian](http://www.debian.org), [Ubuntu](http://www.ubuntu.com), [Arch Linux (AUR)](https://aur.archlinux.org/) and [Mac OS X (homebrew)](http://brew.sh/). Moreover, depending on your system, pre-compiled binaries might be available in the links above.


Additional features include:
- Function decorator to avoid tmp files leftovers
- Utility to register and recover encodings by name and specific grounder
- Utility to register and recover arguments by name and specific system (grounder or solver)
- Adapt answer sets by default to a basic python object
- Adapt answer sets to application-specific python objects
- Ready-to-use [metasp](http://www.cs.uni-potsdam.de/wv/metasp/) framework


Run doctests using:
```
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
```

Check out some [examples](pyzcasp/examples) use cases. For a real application using **pyzcasp** take a look to [caspo](https://github.com/bioasp/caspo).

