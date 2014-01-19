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

from zope import component
from ply import yacc

import re, os

from interfaces import *
from impl import *

class TermSetAdapter(object):
    interface.implements(ITermSet)
    
    def __init__(self):
        super(TermSetAdapter, self).__init__()
        self.termset = TermSet()

    @property
    def score(self):
        return self.termset.score

    def union(self, other):
        return self.termset.union(other)
        
    def to_file(self, filename=None):
        return self.termset.to_file(filename)
            
    def __iter__(self):
        return self.termset.__iter__()
        
class ParserAdapter(object):
    interface.implements(IParser)
    
    def __init__(self, lexer):
        super(ParserAdapter, self).__init__()
        
        self.lex = lexer
        self.parser = yacc.yacc(module=self, debug=0, optimize=1)
        
    def parse(self, exp):
        return self.parser.parse(exp, lexer=self.lex.lexer)
        
    def __enter__(self):
        return self
        
    def __exit__(self, type, value, traceback):
        if os.path.isfile("parser.out"):
            os.remove("parser.out")
        
        if os.path.isfile("parsetab.py"): 
            os.remove("parsetab.py")
            
        if os.path.isfile("parsetab.pyc"): 
            os.remove("parsetab.pyc")
                    
    def p_error(self, t):
        raise SyntaxError(str(t))


class Lexer2TermSetParser(ParserAdapter):
    component.adapts(ILexer)
    interface.implements(ITermSetParser)
    
    def __init__(self, lexer):
        self.tokens = (lexer.STRING, lexer.IDENT, lexer.MIDENT, lexer.NUM, lexer.LP, lexer.RP, lexer.COMMA)
        self.start = 'atom'
        super(Lexer2TermSetParser, self).__init__(lexer)        
        
    def __dir__(self):
        return ['p_atom', 'p_error', 'p_term', 'p_terms', 'start', 'tokens']
                
    def p_atom(self, t):
        """atom : IDENT LP terms RP
                | IDENT
                | MIDENT LP terms RP
                | MIDENT
        """
        if len(t) == 2:
            t[0] = Term(t[1])
        elif len(t) == 5:
            t[0] = Term(t[1], t[3])

    def p_terms(self, t):
        """terms : term COMMA terms
                 | term
        """
        if len(t) == 2:
            t[0] = [t[1]]
        else:
            t[0] = [t[1]] + t[3]

    def p_term(self, t):
        """term : IDENT LP terms RP
                | STRING
                | IDENT
                | NUM
        """
        if len(t) == 2:
            if re.match(r'-?[0-9]+', t[1]) != None:
                t[0] = int(t[1])
            else:
                t[0] = t[1]
        else:
            t[0] = Term(t[1], t[3])

class AnswerSet2TermSet(TermSetAdapter):
    component.adapts(IAnswerSet, ITermSetParser)
    
    def __init__(self, answer, parser):
        super(AnswerSet2TermSet, self).__init__()
        self.answer = answer
        self.parser = parser
        
        for atom in self.answer.atoms:
            self.termset.add(self.parser.parse(atom))
        
        self.termset.score = answer.score

class GrounderSolverAdapter(object):
    interface.implements(IGrounderSolver)

    def __init__(self, grounder, solver):
        super(GrounderSolverAdapter, self).__init__()
        self.grounder = grounder
        self.solver = solver
        
    def run(self, lp="", grounder_args=[], solver_args=[]):
        if lp and '-' not in grounder_args:
            grounder_args.append('-')
            
        grounding = self.grounder.execute(lp, *grounder_args)
        self.solver.execute(grounding, *solver_args)
        
    def __iter__(self):
        raise NotImplementedError("This is an abstract grounder and solver")

class DefaultGrounderSolver(GrounderSolverAdapter):
    component.adapts(IGrounder, ISolver)
    interface.implements(IDefaultGrounderSolver)

    def __iter__(self):
        with Lexer() as lexer:
            with ITermSetParser(lexer) as parser:        
                for answer in self.solver.answers():
                    yield component.getMultiAdapter((answer, parser), ITermSet)
