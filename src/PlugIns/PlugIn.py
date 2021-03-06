# Copyright (C) 2016 Deloitte Argentina.
# This file is part of CodexGigas - https://github.com/codexgigassys/
# See the file 'LICENSE' for copying permission.
from Sample import *


class PlugIn():

    def __init__(self, sample=None):
        self.modules = {}
        self.requires = []
        self.sample = sample

    def addModule(self, module):
        self.modules[module.getName()] = module

    def setModules(self, modules):
        self.modules = modules

    def _addRequiere(self, requiere):
        self.requires.append(requiere)

    def setSample(self, s):
        self.sample = s

    def _getLibrary(self, m):
        mod = self.modules.get(m)
        if(mod is None):
            return None
        mod.initialize(self.sample)
        lib = mod.getLibrary()
        return lib

    def getVersion(self):
        pass

    def getName(self):
        pass

    def process(self):
        pass

    def getPath(self):
        return self.getName()

    def _normalize(self, data):  # TODO remove this from here
        try:
            res = repr(hex(data))
        except TypeError:
            res = repr(data)
        return res
