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

from zope import component

from interfaces import *
from impl import *
        
class Process(object):
    interface.implements(IProcess)
    
    def __init__(self, prg, allowed_returncodes = [0]):
        self.prg = prg
        self.allowed_returncodes = allowed_returncodes
        
    def execute(self, stdin, *args):
        try:
            self.__popen = subprocess.Popen([self.prg] + list(args), stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
                
        except OSError, e:
            if e.errno == 2:
                raise Exception('Program \'%s\' not found' % self.prg)
            else: 
                raise e
                
        (stdout, stderr) = self.__popen.communicate(stdin)
        
        if self.__popen.returncode not in self.allowed_returncodes:
            raise Exception("Return code %d not allowd for %s. %s" % (self.__popen.returncode, self.prg, stderr))
            
        return stdout

class Solver(Process):
    interface.implements(ISolver)
    
    def answers(self):
        raise NotImplementedError("This is an abstract solver")
        
    def __getstats__(self):
        raise NotImplementedError("This is an abstract solver")
        
    def __getatoms__(self, answer):
        raise NotImplementedError("This is an abstract solver")
        
    def __filteratoms__(self, atoms):
        raise NotImplementedError("This is an abstract solver")

class Grounder(Process):
    interface.implements(IGrounder)


class EncodingRegistry(object):
    interface.implements(IEncodingRegistry)
    
    def __init__(self):
        super(EncodingRegistry, self).__init__()
        
        self.__registry = {}
    
    def register_encoding(self, name, path):
        self.__registry[name] = path
        
    def get_encoding(self, name):
        try:
            return self.__registry[name]
        except KeyError,e:
            raise KeyError("No encoding registered with name %s" % e)
        