import argparse

from zope import component

from pyzcasp import asp, potassco

def main(args):
    gringo = component.getUtility(potassco.IGringoGrounder)
    clasp = component.getUtility(potassco.IClaspSolver)
    clingo = component.getMultiAdapter((gringo, clasp), asp.IGrounderSolver)
    
    encodings = component.getUtility(asp.IEncodingRegistry).encodings(gringo)
    
    models = clingo.run(grounder_args=["-c k=2", encodings('enco-1')], solver_args=["0"], lazy=False)
    print [term for term in models[0]]
    print [term for term in models[1]]

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
                        
    parser.add_argument("--clasp", dest="clasp", default="clasp",
                        help="clasp solver binary (Default to 'clasp')", metavar="C")
                        
    parser.add_argument("--gringo", dest="gringo", default="gringo",
                        help="gringo grounder binary (Default to 'gringo')", metavar="G")
                        
    args = parser.parse_args()
    
    gsm = component.getGlobalSiteManager()

    grounder = potassco.GringoGrounder(args.gringo)
    gsm.registerUtility(grounder, potassco.IGringoGrounder)
    
    solver = potassco.ClaspSolver(args.clasp)
    gsm.registerUtility(solver, potassco.IClaspSolver)
    
    gsm.registerUtility(asp.EncodingRegistry(), asp.IEncodingRegistry, 'example')

    root = __file__.rsplit('/', 1)[0]
    reg = component.getUtility(asp.IEncodingRegistry, 'example')
    reg.register('enco-1', root + '/encodings/encoding-1.lp', potassco.IGringoGrounder)
    
    main(args)
