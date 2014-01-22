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

import os, tempfile
from zope import component
from ply import lex
import re

from interfaces import *

class NativeAtom(object):
    interface.implements(INativeAtom)
    
    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        return str(self.name)
        
    def __eq__(self, other):
        return self.name == other.name
        
    def __ne__(self, other):
        return self.name != other.name
                
class Term(object):
    interface.implements(ITerm)
    
    def __init__(self, predicate, arguments=[]):
        self.__pred = predicate
        self.__args = map(lambda arg: (isinstance(arg, basestring) and '"'+arg+'"') or arg, arguments)
    
    @property
    def pred(self):
        return self.__pred
    
    @property
    def args(self):
        return self.__args
        
    def arg(self, n):
        return (isinstance(self.__args[n], basestring) and self.__args[n][1:-1]) or self.__args[n]
            
    def __repr__(self):
        if len(self.args) == 0:
            return "Term(%s)" % (repr(self.__pred),)
        else:
            return "Term(%s,[%s])" % (repr(self.__pred),",".join(map(repr, self.__args)))
    
    def __str__(self):
        if len(self.__args) == 0:
            return self.__pred
        else:
            return self.__pred + "(" + ",".join(map(str, self.__args)) + ")"
    
    def __hash__(self):
        return tuple([self.__pred] + self.__args).__hash__()
    
    def __eq__(self,other):
        return self.__pred == other.pred and self.__args == other.args

class TermSet(set):
    interface.implements(ITermSet)
    
    def __init__(self, terms=[]):
        super(TermSet, self).__init__(terms)
        
    def to_file(self, filename=None):
        if filename:
            file = open(filename,'w')
        else:
            fd, filename = tempfile.mkstemp('.lp')
            file = os.fdopen(fd,'w')
            cleaner = component.getUtility(ICleaner)
            cleaner.collect_file(filename)
            
        for term in self:
            file.write(str(term) + '.\n')
            
        file.close()
        return filename

class AnswerSet(object):
    interface.implements(IAnswerSet)
    
    def __init__(self, atoms=[], score=None):
        super(AnswerSet, self).__init__()
        self.atoms = atoms
        self.score = score
        
class Lexer(object):
    interface.implements(ILexer)
    
    STRING  = 'STRING'
    IDENT   = 'IDENT'
    MIDENT  = 'MIDENT'
    NUM     = 'NUM'
    LP      = 'LP'
    RP      = 'RP'
    COMMA   = 'COMMA'
    SPACE   = 'SPACE'

    # Tokens
    t_STRING = r'"[^"\\]*(?:\\.[^"\\]*)*"' #r'"((\\")|[^"])*"'
    t_IDENT = r'[a-zA-Z_][a-zA-Z0-9_]*'
    t_MIDENT = r'-[a-zA-Z_][a-zA-Z0-9_]*'
    t_NUM = r'-?[0-9]+'
    t_LP = r'\('
    t_RP = r'\)'
    t_COMMA = r','
    t_SPACE = r'[ \t\.]+'

    tokens = (STRING, IDENT, MIDENT, NUM, LP, RP, COMMA, SPACE)
    
    def __init__(self):
        super(Lexer, self).__init__()
        self.lexer = lex.lex(object=self, optimize=1)
        
    def __enter__(self):
        return self
        
    def __exit__(self, type, value, traceback):
        if os.path.isfile("lextab.py"):
            os.remove("lextab.py")
            
        if os.path.isfile("lextab.pyc"):
            os.remove("lextab.pyc")
        
    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += t.value.count("\n")

    def t_error(self, t):
        print "Illegal character '%s'" % t.value[0]
        t.lexer.skip(1)


def cleanrun(fn):
    def decorator(*args, **kwargs):
        fn(*args, **kwargs)
        cleaner = component.getUtility(ICleaner)
        cleaner.clean_files()

    return decorator
