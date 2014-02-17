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
from pyzcasp import asp

class IGringoGrounder(asp.IGrounder):
    """
    gringo grounder
    """
    
class IGringo3(IGringoGrounder):
    """
    gringo 3 grounder
    """

class IGringo4(IGringoGrounder):
    """
    gringo 4 grounder
    """

class IClaspSolver(asp.ISolver):
    """
    clasp solver
    """
    
class IClasp2(IClaspSolver):
    """
    clasp 2 series
    """

class IClasp3(IClaspSolver):
    """
    clasp 3 series
    """

class IClaspHSolver(IClaspSolver):
    """
    hclasp solver
    """

class IClaspDSolver(IClaspSolver):
    """
    claspD solver
    """
    
class IClaspSubsetMinimalSolver(asp.ISubsetMinimalSolver):
    """
    Marker interface for clasp subset minimal solver
    """
    
class IMetaAnswerSet(asp.IAnswerSet):
    """
    """

class IMetaGrounderSolver(asp.IGrounderSolver):
    """
    """
    
    optimize = interface.Attribute("Optimization method as expected by metasp encodings")

class IGrounderSolver(asp.IGrounderSolver):
    """
    Marker interface for Potassco grounder & solver
    """
    