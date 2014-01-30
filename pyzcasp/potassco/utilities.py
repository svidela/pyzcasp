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

import json, subprocess

from zope import component, interface

from pyzcasp import asp

from interfaces import *
from impl import *

class GringoGrounder(asp.Process):
    interface.implements(IGringoGrounder)
    
class ClaspSolver(asp.Process):
    interface.implements(IClaspSolver)
    
    def __init__(self, prg, allowed_returncodes = [10,20,30]):
        super(ClaspSolver, self).__init__(prg, allowed_returncodes)
        
    def execute(self, stdin, *args):
        args = [arg for arg in args if not arg.startswith('--outf')]        
        args.append('--outf=2')
        
        try:
            stdout, code = super(ClaspSolver, self).execute(stdin, *args)
            self.json = json.loads(stdout)
                        
        except asp.ProcessError as e:
            if e.code == 11: # INTERRUPTED
                stdout = e.stdout
                code = e.code
                self.json = json.loads(stdout)

        self.SATISFIABLE = self.json['Result'] == "SATISFIABLE"
        return stdout, code
        
    def answers(self):
        if 'Witnesses' not in self.json:
            return

        for answer in self.json['Witnesses']:
            atoms = self.__filteratoms__(self.__getatoms__(answer))
            score = self.__getscore__(answer)
            if score:
                yield asp.AnswerSet(atoms, score)
            else:
                yield asp.AnswerSet(atoms)
                
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
