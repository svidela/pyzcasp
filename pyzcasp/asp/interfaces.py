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
# along with caspo.  If not, see <http://www.gnu.org/licenses/>.import random
# -*- coding: utf-8 -*-

from zope import interface

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
    
    termset = interface.Attribute("Set of ITerms")
    score = interface.Attribute("Score(s)")
    
    def to_file(self, filename=None):
        """
        Write terms to filename or temp file.
        Returns a file descriptor object.
        """
        
    def union(self, other):
        """"""
        
    def __iter__(self):
        """
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
    def clean(self):
        """
        Remove default parsing aux files
        """
    
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
    
    def __getstats__(self):
        """"""
        
    def __getatoms__(self, answer):
        """"""
        
    def __getscore__(self, answer):
        """"""
        
    def __filteratoms__(self, atoms):
        """"""
        

    
class IAnswerSet(interface.Interface):
    """
    An plain answer set
    """
    
    atoms = interface.Attribute("Set of atoms as strings")
    
class IGrounderSolver(interface.Interface):
    """
    Abstract ground and solve
    """

    def run(self, lp="", grounder_args=[], solver_args=[]):
        """"""

    def __iter__(self):
        """
        """
        
class IDefaultGrounderSolver(IGrounderSolver):
    """
    Ground, solve and parse to TermSet
    """
    
class IEncodingRegistry(interface.Interface):
    """
    """
    
    def register_encoding(self, path, name):
        """"""
        
    def get_encoding(self, name):
        """"""
    