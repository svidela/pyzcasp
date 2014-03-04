import os
from pyzcasp import potassco, asp, examples
from zope import interface, component

## Interfaces (usually in interfaces.py)
class IBird(interface.Interface):
    name = interface.Attribute("bird name")
    penguin = interface.Attribute("True if is a penguin, False otherwise")

class IBirdList(interface.Interface):
    pass

## Implementations (usually in impl.py)
class Bird(object):
    interface.implements(IBird)
    
    def __init__(self, name, penguin=False):
        self.name = name
        self.penguin = penguin
        
class BirdList(list):
    interface.implements(IBirdList)
    
    def __init__(self, iterable):
        super(BirdList, self).__init__(iterable)
    
## Adapters (usually in adapters.py)
class BirdList2TermSet(asp.TermSetAdapter):
    component.adapts(IBirdList)
    interface.implements(asp.ITermSet)
    
    def __init__(self, birds):
        super(BirdList2TermSet, self).__init__()
        for bird in birds:
            self._termset.add(asp.Term('bird', [bird.name]))
            if bird.penguin:
                self._termset.add(asp.Term('penguin', [bird.name]))

class AnswerSet2BirdList(object):
    component.adapts(asp.IAnswerSet)
    interface.implements(IBirdList)
    
    def __init__(self, answer):
        super(AnswerSet2BirdList, self).__init__()

        parser = asp.Grammar()
        parser.function.setParseAction(lambda t: Bird(t['args'][0]))
        self.birds = BirdList([parser.parse(atom) for atom in answer.atoms])
        
    def __iter__(self):
        return iter(self.birds)

## Registry (usually in __init__.py)
gsm = component.getGlobalSiteManager()
path = os.path.dirname(examples.__file__)

gsm.registerAdapter(BirdList2TermSet)
gsm.registerAdapter(AnswerSet2BirdList)
gsm.registerUtility(asp.EncodingRegistry(), asp.IEncodingRegistry, 'example')

reg = component.getUtility(asp.IEncodingRegistry, 'example')
reg.register('flies', os.path.join(path, 'encodings/flies.lp'), potassco.IGringo4)


## Showtime
@asp.cleanrun #Use cleanrun decorator to avoid temp files leftovers
def runner(birds):
    clingo = component.getUtility(potassco.IClingo) # get clingo utility
    encodings = component.getUtility(asp.IEncodingRegistry).encodings(clingo.grounder) # get encodings for its grounder
    instance = asp.ITermSet(birds) # adapt the list of birds to a TermSet object
    #run clingo with an instance and encoding. Resulting answer sets are adapted to a list of birds
    answers = clingo.run(grounder_args=[instance.to_file(), encodings('flies')], adapter=IBirdList)
    if clingo.sat:
        # return the first list of birds
        return answers[0]
    else:
        raise "Something went very wrong..."
    
if __name__ == '__main__':
    # first thing you would do is to register clingo utility
    potassco.configure(clingo="clingo")
    
    # tweety and sam are birds, sam is a penguin
    tweety = Bird('tweety')
    sam = Bird('sam', True)
    birds = BirdList([tweety, sam])

    flying_birds = runner(birds)
    for bird in flying_birds:
        print bird.name # prints only tweety

    print '---'
    birds[1].penguin = False # fly sam, fly!!!
    flying_birds = runner(birds)
    for bird in flying_birds:
        print bird.name # prints tweety and sam
