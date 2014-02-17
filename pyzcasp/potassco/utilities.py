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

import json, subprocess

from zope import component, interface

from pyzcasp import asp

from interfaces import *
from impl import *

class Gringo3(asp.Process):
    interface.implements(IGringo3)

class Gringo4(asp.Process):
    interface.implements(IGringo4)
    
class ClaspSolver(asp.Process):
    interface.implements(IClaspSolver)
    
    def __init__(self, prg, allowed_returncodes = [10,20,30]):
        super(ClaspSolver, self).__init__(prg, allowed_returncodes)
        
    def execute(self, stdin, *args):
        args = filter(lambda arg: not arg.startswith('--outf'), list(args))
        args.append('--outf=2')
        
        try:
            stdout, code = super(ClaspSolver, self).execute(stdin, *args)
            self.json = json.loads(stdout)
                        
        except asp.ProcessError as e:
            if e.code == 11: # INTERRUPTED
                stdout = e.stdout
                code = e.code
                self.json = json.loads(stdout)
            else:
                raise e
        
        return stdout, code
        
    def answers(self):
        if 'Witnesses' not in self.json:
            return
        
        for answer in self.json['Witnesses']:
            atoms = self.__filteratoms__(self.__getatoms__(answer))
            score = self.__getscore__(answer)
            if score:
                ans = asp.AnswerSet(atoms, score)
            else:
                ans = asp.AnswerSet(atoms)
            
            yield ans     
        
    @property
    def complete(self):
        return self.__getstats__()['Complete'] == "yes"
        
    @property
    def unknown(self):
        return self.json['Result'] == "UNKNOWN"
        
    @property
    def unsat(self):
        return self.json['Result'] == "UNSATISFIABLE"
        
    @property
    def sat(self):
        return self.json['Result'] == "SATISFIABLE"
        
    @property
    def optimum(self):
        return self.json['Result'] == "OPTIMUM FOUND"
                
    def __getstats__(self):
        return self.json['Stats']
        
    def __getatoms__(self, answer):
        stats = self.__getstats__()
        
        if 'Brave' in stats:
            return answer['Brave']
        elif 'Cautious' in stats:
            return answer['Cautious']
        else:    
            return answer['Value']
            
    def __getscore__(self, answer):
        if 'Opt' in answer:
            return answer['Opt']
        
    def __filteratoms__(self, atoms):
        return atoms
                
class ClaspHSolver(ClaspSolver):
    interface.implements(IClaspHSolver, IClaspSubsetMinimalSolver)
    
    def __filteratoms__(self, atoms):
        return filter(lambda atom: not atom.startswith('_'), atoms)
    
class ClaspDSolver(ClaspSolver):
    interface.implements(IClaspDSolver, IClaspSubsetMinimalSolver)
    
    def __getstats__(self):
        return self.json['Models']
        
class Clingo(ClaspSolver):
    interface.implements(IGrounderSolver)
    
    def __init__(self, prg, allowed_returncodes = [10,20,30]):
        super(Clingo, self).__init__(prg, allowed_returncodes)
        self.grounder = Gringo4(prg)
        self.solver = self
        
    def run(self, lp="", grounder_args=[], solver_args=[], adapter=None, termset_filter=None):
        if lp and '-' not in grounder_args:
            grounder_args.append('-')
        
        clingo_args = filter(lambda arg: not arg.startswith('--mode'), grounder_args + solver_args)
        self.execute(lp, *clingo_args)
        
        answers = list()
        with asp.Lexer() as lexer:
            with asp.ITermSetParser(lexer) as parser:
                for answer in self.answers():
                    ts = component.getMultiAdapter((answer, parser), asp.ITermSet)
                    if termset_filter:
                        ts = asp.TermSet(filter(termset_filter, ts))
                        
                    if adapter:
                        answers.append(adapter(ts))
                    else:
                        answers.append(ts)

        return answers

    def answers(self):
        calls = self.json['Calls']
        if 'Witnesses' not in self.json['Call'][calls - 1]:
            return
        
        for answer in self.json['Call'][calls - 1]['Witnesses']:
            atoms = self.__filteratoms__(self.__getatoms__(answer))
            score = self.__getscore__(answer)
            if score:
                ans = asp.AnswerSet(atoms, score)
            else:
                ans = asp.AnswerSet(atoms)
                
            yield ans

    @property
    def complete(self):
        return self.__getstats__()['More'] == "no"
                        
    def __getstats__(self):
        return self.json['Models']
        
    def __getatoms__(self, answer):
        if 'Value' in answer:
            return answer['Value']
        else:
            return []
