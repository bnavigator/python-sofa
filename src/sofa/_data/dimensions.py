# Copyright (c) 2019 Jannika Lossner
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from enum import Enum
from . import spatial

default_units = {
    spatial.Coordinates.System.Cartesian : "meter",
    spatial.Coordinates.System.Spherical : "degree, degree, meter",
    "frequency" : "hertz"
    }

class DimensionAccess:
    """Access the .sofa file's dimensions"""
    def __init__(self, dataset):
        self.dataset = dataset
        return
    
    @property
    def I(self): 
        """Scalar dimension"""
        return self.dataset.dimensions["I"].size
    
    @property
    def C(self): 
        """Coordinate dimension"""
        return self.dataset.dimensions["C"].size
    @property
    def M(self): 
        """Number of measurements"""
        return self.dataset.dimensions["M"].size
    @property
    def R(self): 
        """Number of receivers"""
        return self.dataset.dimensions["R"].size
    @property
    def E(self): 
        """Number of emitters"""
        return self.dataset.dimensions["E"].size
    @property
    def N(self): 
        """Number of data samples per measurement"""
        return self.dataset.dimensions["N"].size
    @property
    def S(self): 
        """Largest data string size"""
        return self.dataset.dimensions["S"].size
    
class Definitions:
    def Listener(varies=False):
        if varies: return ("M","C",)
        return ("I","C",)
    def Source(varies=False):
        if varies: return ("M","C",)
        return ("I","C",)
    
    
    def Receiver(varies=False):
        if varies: return ("R","C","M",)
        return ("R","C","I",)
    def Emitter(varies=False):
        if varies: return ("E","C","M",)
        return ("E","C","I",)
    
    
    def RoomCorner(varies=False):
        if varies: return ("M","C",)
        return ("I","C",)
    
    
    def DataValues(datatype):
        if datatype is "FIRE": return ("M","R","E","N",)
        return ("M","R","N",)
    def DataDelay(datatype, varies=False):
        tup = ("I","R",)
        if varies: tup = ("M","R",)
        if datatype is "FIRE": return tup+("E",)
        return tup
    def DataSamplingRate(datatype):
        return ("I",)
    def DataFrequencies(datatype):
        return ("N",)
    
    names = {
        "Receiver" : "R",
        "Emitter" : "E"
        }
