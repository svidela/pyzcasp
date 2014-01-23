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
from zope import component, interface
from pyzcasp import asp
from interfaces import *
from impl import *


class MetaAnswerSet2TermSet(asp.TermSetAdapter):
    component.adapts(IMetaAnswerSet, asp.ITermSetParser)
    
    def __init__(self, answer, parser):
        super(MetaAnswerSet2TermSet, self).__init__()
        
        for atom in answer.atoms:
            meta = parser.parse(atom)
            self._termset.add(meta.arg(0).arg(0))
        
        self._termset.score = answer.score

class MetaGrounderSolver(asp.GrounderSolverAdapter):
    component.adapts(IGringoGrounder, IClaspDSolver)
    interface.implements(IMetaGrounderSolver)
    
    
    def __init__(self, grounder, solver):
        super(MetaGrounderSolver, self).__init__(grounder, solver)
        self.optimize = asp.TermSet()
        
    def run(self, lp="", grounder_args=[], solver_args=[]):
        if '--reify' not in grounder_args:
            grounder_args.append('--reify')
            
        grounding = self.grounder.execute("", *grounder_args)
                
        reg = component.getUtility(asp.IEncodingRegistry, 'potassco')
        meta = reg.get_encoding('meta')
        metaD = reg.get_encoding('metaD')
        metaO = reg.get_encoding('metaO')
        
        super(MetaGrounderSolver, self).run(grounding + lp, grounder_args=[meta, metaD, metaO, self.optimize.to_file()], solver_args=solver_args)

    def __iter__(self):
        with asp.Lexer() as lexer:
            with asp.ITermSetParser(lexer) as parser:
                for answer in self.solver.answers():
                    interface.directlyProvides(answer, IMetaAnswerSet)
                    yield component.getMultiAdapter((answer, parser), asp.ITermSet)