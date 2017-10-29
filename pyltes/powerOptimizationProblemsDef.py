__author__ = 'mslabicki'

# from PyGMO.problem import base
import numpy as np

class maximalThroughputProblemRR:
    def __init__(self, networkInstance, dim, lowerTxLimit, upperTxLimit):
        self.dim = dim
        self.networkInstance = networkInstance
        self.lowerLimitsVector = []
        self.upperLimitsVector = []
        for i in range(dim):
            self.lowerLimitsVector.append(lowerTxLimit)
            self.upperLimitsVector.append(upperTxLimit)

    def fitness(self, x):
        for i in range(len(x)):
            self.networkInstance.bs[i].outsidePower = x[i]
        ueThroughputVector = self.networkInstance.returnRealUEThroughputVectorRR()
        objectiveValue = sum(ueThroughputVector)
        return (-objectiveValue, )

    def get_bounds(self):
        return self.lowerLimitsVector, self.upperLimitsVector

    def get_nix(self):
        return self.dim


# class maximalThroughputProblemRR(base):
#     def __init__(self, dim = 1):
#         super().__init__(dim, dim)
#         self.set_bounds(10, 40)
#         self.__dim = dim
#         self.siec = []
#
#     def _objfun_impl(self, x):
#         for i in range(len(x)):
#             self.siec.bs[i].outsidePower = x[i]
#         ueThroughputVector = self.siec.returnRealUEThroughputVectorRR()
#         objectiveValue = sum(ueThroughputVector)
#         return (-objectiveValue, )

# class local_maximalThroughputProblemRR(base):
#     def __init__(self, dim = 1):
#         super().__init__(dim, dim)
#         self.set_bounds(10, 40)
#         self.__dim = dim
#         self.siec = []
#         self.bsList = []
#
#     def _objfun_impl(self, x):
#         for i in range(len(x)):
#             self.siec.bs[int(self.bsList[i])].outsidePower = x[i]
#         ueThroughputVector = self.siec.returnRealUEThroughputVectorRR()
#         objectiveValue = sum(ueThroughputVector)
#         return (-objectiveValue, )
#
# class maximalMedianThrProblemRR(base):
#     def __init__(self, dim = 1):
#         super().__init__(dim, dim)
#         self.set_bounds(10, 40)
#         self.__dim = dim
#         self.siec = []
#
#     def _objfun_impl(self, x):
#         for i in range(len(x)):
#             self.siec.bs[i].outsidePower = x[i]
#         ueThroughputVector = self.siec.returnRealUEThroughputVectorRR()
#         objectiveValue = np.median(ueThroughputVector)
#         return (-objectiveValue, )
#
# class local_maximalMedianThrProblemRR(base):
#     def __init__(self, dim = 1):
#         super().__init__(dim, dim)
#         self.set_bounds(10, 40)
#         self.__dim = dim
#         self.siec = []
#         self.bsList = []
#
#     def _objfun_impl(self, x):
#         for i in range(len(x)):
#             self.siec.bs[int(self.bsList[i])].outsidePower = x[i]
#         ueThroughputVector = self.siec.returnRealUEThroughputVectorRR()
#         objectiveValue = np.median(ueThroughputVector)
#         return (-objectiveValue, )
#
# class minInterQuartileRangeroblemRR(base):
#     def __init__(self, dim = 1):
#         super().__init__(dim, dim)
#         self.set_bounds(10, 40)
#         self.__dim = dim
#         self.siec = []
#
#     def _objfun_impl(self, x):
#         for i in range(len(x)):
#             self.siec.bs[i].outsidePower = x[i]
#         ueThroughputVector = self.siec.returnRealUEThroughputVectorRR()
#         objectiveValue = np.percentile(ueThroughputVector, 75) - np.percentile(ueThroughputVector, 25)
#         return (-objectiveValue, )
#
# class local_minInterQuartileRangeroblemRR(base):
#     def __init__(self, dim = 1):
#         super().__init__(dim, dim)
#         self.set_bounds(10, 40)
#         self.__dim = dim
#         self.siec = []
#         self.bsList = []
#
#     def _objfun_impl(self, x):
#         for i in range(len(x)):
#             self.siec.bs[int(self.bsList[i])].outsidePower = x[i]
#         ueThroughputVector = self.siec.returnRealUEThroughputVectorRR()
#         objectiveValue = np.percentile(ueThroughputVector, 75) - np.percentile(ueThroughputVector, 25)
#         return (-objectiveValue, )