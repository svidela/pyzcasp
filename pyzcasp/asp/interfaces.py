# Copyright (c) 2014, Santiago Videla
#
# This file is part of pyzcasp.
#
# caspo is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# caspo is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with caspo.  If not, see <http://www.gnu.org/licenses/>.
# -*- coding: utf-8 -*-

from zope import interface

class INativeTerm(interface.Interface):
    """
    Represents a function symbol name without arguments
    """
    name = interface.Attribute("Term name")
    
    def __init__(self, name):
        """
        Constructor
        
        :param str name: term name
        """
        
    def __str__(self):
        """
        Returns name
        """
        
    def __repr__(self):
        """
        Returns name
        """
        
    def __eq__(self, other):
        """
        Compare by name
        """
    
    def __ne__(self, other):
        """
        Compare by name
        """
        
    def __hash__(self):
        """
        Hash by name
        """

class ITerm(interface.Interface):
    """
    Represents a term as a function symbol followed by a list of arguments.
    String arguments are automatically escaped, e.g. 'a' becomes '"a"' in order
    to avoid conlfict with uppercase strings. To avoid this, use an instance
    of NativeTerm. Number arguments must be integers.
    """
    
    pred = interface.Attribute("Term predicate name")
    args = interface.Attribute("Term arguments list")
    
    def __init__(self, predicate, arguments=[]):
        """
        Constructor
        
        :param str predicate: term name
        :param list arguments: list of arguments
        """
            
    def __str__(self):
        """
        Term as string
        """
        
    def __repr__(self):
        """
        Term object representation
        """
        
    def __eq__(self, other):
        """
        Compare by pred and args
        """

    def __ne__(self, other):
        """
        Compare by pred and args
        """
        
    def __hash__(self):
        """
        Hash by ([pred] + args)
        """
    
class ITermSet(interface.Interface):
    """
    Represents a set of terms objects. Typically used to describe an input instance
    and resulting answer sets.
    """
    
    score = interface.Attribute("List of score(s) if any")
    
    def __init__(self, terms=[], score=None):
        """
        Constructor
        
        :param list terms: list of terms objects
        :param list score: list of score(s)
        """
    
    def to_file(self, filename=None):
        """
        Write terms to filename or temp file. If filename==None, the filename is collected
        in the ICleaner utility for a proper cleaning using @cleanrun decorator.
        
        :param str filename: an optional filename
        :returns: a file descriptor object.
        """
    
    def add(self, term):
        """
        Adds a term to the TermSet
        
        :param Term term: a Term object
        """
        
    def union(self, other):
        """
        Returns the union of self and other TermSet
        
        :param TermSet other: other TermSet object
        """
        
    def __iter__(self):
        """
        Return an iterator over terms
        """
        
    def __len__(self):
        """
        Return number of terms in the TermSet
        """
        
class ILexer(interface.Interface):
    """
    Lexer object
    """
    
    lexer = interface.Attribute("PLY Lexer object")
    
class IParser(interface.Interface):
    """
    Parser object
    """
    
    parser = interface.Attribute("PLY Parser object")
    
class ITermSetParser(IParser):
    """
    Paser of TermSet objects
    """

class IProcess(interface.Interface):
    """
    Represents a program to be executed using system calls
    """

    def __init__(self, prg, allowed_returncodes = [0], strict_args=None):
        """
        Constructor
        
        :param str prg: excutable command
        :param list allowed_returncodes: list of allowed code by `prg`
        :param dict strict_args: mapping of fixed arguments
        """
        
    def execute(self, stdin, *args):
        """
        Execute the program via a system call.
        An Exception is raised if the `prg` is not found. A ProcessError exception is raised
        if the returned code is not in the allowed_returncodes.
        
        :param str stdin: a valid input for `prg`
        :param list *args: any accepted argument by `prg`
        
        :returns: tuple with standard output from `prg` and its returned code
        """

class IGrounder(IProcess):
    """
    Represents an ASP grounder program
    """
    
class ISolver(IProcess):
    """
    Represents an ASP solver program
    """
    
    complete = interface.Attribute("True if the solving was completed, False otherwise")
    unknown = interface.Attribute("True if SAT is unknown, False otherwise")
    unsat = interface.Attribute("True if the solving was UNSAT, False otherwise")
    sat = interface.Attribute("True if the solving was SAT, False otherwise")
    optimum = interface.Attribute("True if the solving found an optimum, False otherwise")
    
    def __getstats__(self):
        """
        """
        
    def __getatoms__(self, answer):
        """
        """
        
    def __getscore__(self, answer):
        """
        """
        
    def __filteratoms__(self, atoms):
        """
        """
        
class ISubsetMinimalSolver(interface.Interface):
    """
    Marker interface for subset minimal solver
    """
    
class IAnswerSet(interface.Interface):
    """
    An plain answer set
    """
    
    atoms = interface.Attribute("Set of atoms as strings")
    
class IGrounderSolver(interface.Interface):
    """
    Ground, solve and parse to TermSet
    """
    
    grounder = interface.Attribute("Grounder")
    solver = interface.Attribute("Solver")

    def run(self, lp="", grounder_args=[], solver_args=[], adapter=None, termset_filter=None):
        """"""
        
    def processing(self, answers, adapter=None, termset_filter=None):
        """"""
    
class IEncodingRegistry(interface.Interface):
    """
    """
    
    def register(self, name, path, igrounder):
        """"""
        
    def encodings(self, igrounder):
        """"""

class IEncoding(interface.Interface):
    """
    """
    

class IArgumentRegistry(interface.Interface):
    """
    """
    
    def register(self, name, args, iprocess):
        """"""
        
    def encodings(self, iprocess):
        """"""

class IArgument(interface.Interface):
    """
    """
    
class ICleaner(interface.Interface):
    """
    """
    
    def collect_file(self, filename):
        """"""
        
    def clean_files(self):
        """"""
        
class IProcessError(interface.Interface):
    """
    """
    prg = interface.Attribute("")
    code = interface.Attribute("")
    stdout = interface.Attribute("")
    stderr = interface.Attribute("")
