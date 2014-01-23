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

from adapters import *
from interfaces import *
from utilities import *

from pyzcasp import asp
from zope import component

gsm = component.getGlobalSiteManager()

gsm.registerAdapter(MetaAnswerSet2TermSet)
gsm.registerAdapter(MetaGrounderSolver, (IGringoGrounder, IClaspDSolver,), IMetaGrounderSolver)

gsm.registerUtility(asp.EncodingRegistry(), asp.IEncodingRegistry, 'potassco')

root = __file__.rsplit('/', 1)[0]
reg = component.getUtility(asp.IEncodingRegistry, 'potassco')
reg.register_encoding('meta', root + '/encodings/meta.lp')
reg.register_encoding('metaD', root + '/encodings/metaD.lp')
reg.register_encoding('metaO', root + '/encodings/metaO.lp')