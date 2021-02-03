"""
Copyright (c) 2018, Jairus Martin.

Distributed under the terms of the MIT License.

The full license is in the file LICENSE, distributed with this software.

Created on Jun 19, 2018

@author: jrm
"""
import sys
from atom.api import Atom, Member, Str, Int, Float, Value


def DynamicModel(obj, label="value"):
    """ Create a model """
    if isinstance(obj, Member):
        #: No value is set try to get the default
        return obj.validate_mode[1]()  # Umm... should use default?
    if isinstance(obj, Atom):
        return obj
    members = {}
    typemap = {
        int: Int,
        float: Float,
        str: Str,
    }

    if sys.version_info.major < 3:
        typemap[unicode] = Str

    if isinstance(obj,Value):
        members[label] = obj
    elif type(obj) in typemap:
        members[label] = typemap[type(obj)](default=obj)
    Model = type('Model', (Atom,), members)
    return Model()
