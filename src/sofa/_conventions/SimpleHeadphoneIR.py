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

from .base import _Base

from .. import _data as data
from .. import _rooms as rooms

import numpy as np

### incomplete! Requires extending the data access to include per-measurement strings
class SimpleHeadphoneIR(_Base):
    name = "SimpleHeadphoneIR"
    version = "0.2"
    def __init__(self):
        _Base.__init__(self)
        self.default_objects["Source"]["coordinates"].Position = [0,0,1]
        self.default_objects["Source"]["system"] = data.spatial.Coordinates.System.Spherical
        self.default_objects["Emitter"]["count"] = 2
        self.default_objects["Receiver"]["count"] = 2

        self.head_radius = 0.09

        self.conditions["must have 2 Emitters"] = lambda name, info_states, count: name != "Emitter" or count == 2
        self.conditions["must have 2 Receivers"] = lambda name, info_states, count: name != "Receiver" or count == 2

    def add_metadata(self, dataset):
        _Base.add_general_defaults(dataset)

        dataset.SOFAConventions = self.name
        dataset.SOFAConventionsVersion = self.version
        dataset.DataType = "FIR"
        dataset.RoomType = rooms.types.FreeField.value
        dataset.DatabaseName = ""
        dataset.ListenerShortName = ""
        return

    def set_default_spatial_values(self, spobj):
        _Base._set_default_spatial_values(self, spobj)

        self.set_default_Emitter(spobj)
        self.set_default_Receiver(spobj)
        return
    
    def set_default_Emitter(self, spobj):
        if spobj.name != "Emitter": return
        spobj.Position.set_values([[0,self.head_radius,0], [0,-self.head_radius,0]], dim_order=("E", "C"), repeat_dim=("M"))
    def set_default_Receiver(self, spobj):
        if spobj.name != "Receiver": return
        spobj.Position.set_values([[0,self.head_radius,0], [0,-self.head_radius,0]], dim_order=("R", "C"), repeat_dim=("M"))
