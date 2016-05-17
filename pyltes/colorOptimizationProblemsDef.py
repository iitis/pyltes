__author__ = 'mslabicki'

from PyGMO.problem import base
import numpy

class maximalThroughputProblemRR(base):
    def __init__(self, dim = 1):
        super().__init__(dim, dim)
        self.set_bounds(1, 3)
        self.__dim = dim
        self.siec = []

    def _objfun_impl(self, x):
        for i in range(len(x)):
            self.siec.bs[i].color = x[i]
        ueThroughputVector = self.siec.returnRealUEThroughputVectorRR()
        sumofThroughput = sum(ueThroughputVector)
        return (-sumofThroughput, )

class maximalThroughputProblemFS(base):
    def __init__(self, dim = 1):
        super().__init__(dim, dim)
        self.set_bounds(1, 3)
        self.__dim = dim
        self.siec = []

    def _objfun_impl(self, x):
        for i in range(len(x)):
            self.siec.bs[i].color = x[i]
        ueThroughputVector = self.siec.returnRealUEThroughputVectorFS()
        sumofThroughput = sum(ueThroughputVector)
        return (-sumofThroughput, )
