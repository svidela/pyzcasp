# Copyright (c) 2014, Santiago Videla
#
# This file is part of caspo.
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

class INativeAtom(interface.Interface):
    """
    """
    name = interface.Attribute("Atom name")
    
    def __str__(self):
        """"""
        
    def __repr__(self):
        """"""
        
    def __eq__(self):
        """"""
    
    def __ne__(self):
        """"""
        
    def __hash__(self):
        """"""

class ITerm(interface.Interface):
    """
    Term pyasp object
    """
    
    pred = interface.Attribute("Term predicate name")
    args = interface.Attribute("Term arguments list")
            
    def __str__(self):
        """"""
        
    def __repr__(self):
        """"""
        
    def __eq__(self):
        """"""
        
    def __hash__(self):
        """"""
    
class ITermSet(interface.Interface):
    """
    TermSet pyasp object
    """
    
    score = interface.Attribute("Score(s)")
    
    def to_file(self, filename=None):
        """
        Write terms to filename or temp file.
        Returns a file descriptor object.
        """
    
    def add(self, term):
        """
        Adds a term to the TermSet
        """
        
    def union(self, other):
        """
        Return the union of self and other TermSet
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
    System calls
    """
    
    def execute(self):
        """
        """

class IGrounder(IProcess):
    """
    ASP grounder
    """
    
class ISolver(IProcess):
    """
    ASP Solver
    """
    
    complete = interface.Attribute("")
    unknown = interface.Attribute("")
    unsat = interface.Attribute("")
    sat = interface.Attribute("")
    optimum = interface.Attribute("")
    
    def __getstats__(self):
        """"""
        
    def __getatoms__(self, answer):
        """"""
        
    def __getscore__(self, answer):
        """"""
        
    def __filteratoms__(self, atoms):
        """"""
        
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

    def run(self, lp="", grounder_args=[], solver_args=[], lazy=True):
        """"""

    def __iter__(self):
        """
        """
    
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
