import argparse

from zope import component

from pyzcasp import asp, potassco

def main(args):
    gringo = component.getUtility(potassco.IGringoGrounder)
    clasp = component.getUtility(potassco.IClaspSolver)
    clingo = component.getMultiAdapter((gringo, clasp), asp.IGrounderSolver)
    myprog = """
    a :- not b.
    b :- not a.
    c(k).
    """
    
    solutions = clingo.run(myprog, grounder_args=["-c k=2"], solver_args=["0"])
    for termset in solutions:
        print [term for term in termset]

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
                        
    parser.add_argument("--clasp", dest="clasp", default="clasp",
                        help="clasp solver binary (Default to 'clasp')", metavar="C")
                        
    parser.add_argument("--gringo", dest="gringo", default="gringo",
                        help="gringo grounder binary (Default to 'gringo')", metavar="G")
                        
    parser.add_argument("--gringo-series", dest="gringo_series", type=int, default=3, choices=[3,4],
                        help="gringo grounder binary (Default to 'gringo')", metavar="G")
                        
    args = parser.parse_args()
    
    gsm = component.getGlobalSiteManager()

    if args.gringo_series == 3:
        grounder = potassco.Gringo3(args.gringo)
        gsm.registerUtility(grounder, potassco.IGringo3)
    else:
        grounder = potassco.Gringo4(args.gringo)
        gsm.registerUtility(grounder, potassco.IGringo4)
    
    solver = potassco.ClaspSolver(args.clasp)
    gsm.registerUtility(solver, potassco.IClaspSolver)
    
    main(args)
