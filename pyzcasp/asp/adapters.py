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
        self._termset = TermSet()

    @property
    def score(self):
        return self._termset.score
        
    def add(self, term):
        self._termset.add(term)
    
    def union(self, other):
        return self._termset.union(other)
                
    def to_file(self, filename=None):
        return self._termset.to_file(filename)
            
    def __iter__(self):
        return iter(self._termset)
        
    def __len__(self):
        return len(self._termset)
        
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
            if re.match(self.lex.t_NUM, t[1]):
                t[0] = int(t[1])
            elif re.match(self.lex.t_STRING, t[1]):
                t[0] = t[1][1:-1]
            else:
                t[0] = NativeAtom(t[1])
        else:
            t[0] = Term(t[1], t[3])

class AnswerSet2TermSet(TermSetAdapter):
    component.adapts(IAnswerSet, ITermSetParser)
    
    def __init__(self, answer, parser):
        super(AnswerSet2TermSet, self).__init__()
        
        for atom in answer.atoms:
            self._termset.add(parser.parse(atom))
        
        self._termset.score = answer.score

class GrounderSolver(object):
    interface.implements(IGrounderSolver)
    component.adapts(IGrounder, ISolver)

    def __init__(self, grounder, solver):
        super(GrounderSolver, self).__init__()
        self.grounder = grounder
        self.solver = solver
        
    def run(self, lp="", grounder_args=[], solver_args=[], lazy=True):
        if lp and '-' not in grounder_args:
            grounder_args.append('-')
            
        grounding, code = self.grounder.execute(lp, *grounder_args)
        self.solver.execute(grounding, *solver_args)
        
        if not lazy:
            return list(iter(self))
        
    def __iter__(self):
        with Lexer() as lexer:
            with ITermSetParser(lexer) as parser:        
                for answer in self.solver.answers():
                    yield component.getMultiAdapter((answer, parser), ITermSet)
                    