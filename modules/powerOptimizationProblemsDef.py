__author__ = 'mslabicki'

from PyGMO.problem import base
import numpy

class maximalThroughputProblemRR_const(base):
    def __init__(self, dim = 1):
        super().__init__(dim, dim)
        self.set_bounds(10, 40)
        self.__dim = dim
        self.siec = []

    def _objfun_impl(self, x):
        for i in range(len(x)):
            self.siec.bs[i].outsidePower = x[i]
        ueThroughputVector = self.siec.returnRealUEThroughputVectorRR()
        sumofThroughput = sum(ueThroughputVector)
        return (-sumofThroughput, )

class local_maximalThroughputProblemRR_const(base):
    def __init__(self, dim = 1):
        super().__init__(dim, dim)
        self.set_bounds(10, 40)
        self.__dim = dim
        self.siec = []
        self.bsList = []

    def _objfun_impl(self, x):
        for i in range(len(x)):
            self.siec.bs[int(self.bsList[i])].outsidePower = x[i]
        ueThroughputVector = self.siec.returnRealUEThroughputVectorRR()
        sumofThroughput = sum(ueThroughputVector)
        return (-sumofThroughput, )

class maximalThroughputProblemRR_thebest(base):
    def __init__(self, dim = 1):
        super().__init__(dim, dim)
        self.set_bounds(10, 40)
        self.__dim = dim
        self.siec = []

    def _objfun_impl(self, x):
        for i in range(len(x)):
            self.siec.bs[i].outsidePower = x[i]
        self.siec.connectUsersToTheBestBS()
        ueThroughputVector = self.siec.returnRealUEThroughputVectorRR()
        sumofThroughput = sum(ueThroughputVector)
        return (-sumofThroughput, )

class local_maximalThroughputProblemRR_thebest(base):
    def __init__(self, dim = 1):
        super().__init__(dim, dim)
        self.set_bounds(10, 40)
        self.__dim = dim
        self.siec = []
        self.bsList = []

    def _objfun_impl(self, x):
        for i in range(len(x)):
            self.siec.bs[int(self.bsList[i])].outsidePower = x[i]
        self.siec.connectUsersToTheBestBS()
        ueThroughputVector = self.siec.returnRealUEThroughputVectorRR()
        sumofThroughput = sum(ueThroughputVector)
        return (-sumofThroughput, )