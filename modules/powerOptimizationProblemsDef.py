__author__ = 'mslabicki'

from PyGMO.problem import base
import numpy

class maximalThroughputProblemRR(base):
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

class maximalThroughputProblemFS(base):
    def __init__(self, dim = 1):
        super().__init__(dim, dim)
        self.set_bounds(10, 40)
        self.__dim = dim
        self.siec = []

    def _objfun_impl(self, x):
        for i in range(len(x)):
            self.siec.bs[i].outsidePower = x[i]
        ueThroughputVector = self.siec.returnRealUEThroughputVectorFS()
        sumofThroughput = sum(ueThroughputVector)
        return (-sumofThroughput, )

class medianThroughputProblemRR(base):
    def __init__(self, dim = 1):
        super().__init__(dim, dim)
        self.set_bounds(10, 40)
        self.__dim = dim
        self.siec = []

    def _objfun_impl(self, x):
        for i in range(len(x)):
            self.siec.bs[i].outsidePower = x[i]
        ueThroughputVector = self.siec.returnRealUEThroughputVectorRR()
        medianThroughput = numpy.median(ueThroughputVector)
        return (-medianThroughput, )

class medianThroughputProblemFS(base):
    def __init__(self, dim = 1):
        super().__init__(dim, dim)
        self.set_bounds(10, 40)
        self.__dim = dim
        self.siec = []

    def _objfun_impl(self, x):
        for i in range(len(x)):
            self.siec.bs[i].outsidePower = x[i]
        ueThroughputVector = self.siec.returnRealUEThroughputVectorFS()
        medianThroughput = numpy.median(ueThroughputVector)
        return (-medianThroughput, )

class minIqrProblemRR(base):
    def __init__(self, dim = 1):
        super().__init__(dim, dim)
        self.set_bounds(10, 40)
        self.__dim = dim
        self.siec = []

    def _objfun_impl(self, x):
        for i in range(len(x)):
            self.siec.bs[i].outsidePower = x[i]
        ueThroughputVector = self.siec.returnRealUEThroughputVectorRR()
        p25 = numpy.percentile(ueThroughputVector, 25)
        p75 = numpy.percentile(ueThroughputVector, 75)
        iqr = p75 - p25
        return (-iqr, )

class minIqrProblemFS(base):
    def __init__(self, dim = 1):
        super().__init__(dim, dim)
        self.set_bounds(10, 40)
        self.__dim = dim
        self.siec = []

    def _objfun_impl(self, x):
        for i in range(len(x)):
            self.siec.bs[i].outsidePower = x[i]
        ueThroughputVector = self.siec.returnRealUEThroughputVectorFS()
        p25 = numpy.percentile(ueThroughputVector, 25)
        p75 = numpy.percentile(ueThroughputVector, 75)
        iqr = p75 - p25
        return (-iqr, )

class maxTotalSINRProblem(base):
    def __init__(self, dim = 1):
        super().__init__(dim, dim)
        self.set_bounds(10, 40)
        self.__dim = dim
        self.siec = []

    def _objfun_impl(self, x):
        for i in range(len(x)):
            self.siec.bs[i].outsidePower = x[i]
        SINRVector = self.siec.calculateSINRVectorForAllUE()
        totalSINR = sum(SINRVector)
        return (-totalSINR, )

class maxMedianSINRProblem(base):
    def __init__(self, dim = 1):
        super().__init__(dim, dim)
        self.set_bounds(10, 40)
        self.__dim = dim
        self.siec = []

    def _objfun_impl(self, x):
        for i in range(len(x)):
            self.siec.bs[i].outsidePower = x[i]
        SINRVector = self.siec.calculateSINRVectorForAllUE()
        medianSINR = numpy.median(SINRVector)
        return (-medianSINR, )