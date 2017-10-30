__author__ = 'mslabicki'

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

class local_maximalThroughputProblemRR:
    def __init__(self, networkInstance, dim, lowerTxLimit, upperTxLimit, localListBS):
        self.dim = dim
        self.networkInstance = networkInstance
        self.lowerLimitsVector = []
        self.upperLimitsVector = []
        self.bsList = localListBS
        for i in range(dim):
            self.lowerLimitsVector.append(lowerTxLimit)
            self.upperLimitsVector.append(upperTxLimit)

    def fitness(self, x):
        for i in range(len(x)):
            self.networkInstance.bs[int(self.bsList[i])].outsidePower = x[i]
        ueThroughputVector = self.networkInstance.returnRealUEThroughputVectorRR()
        objectiveValue = sum(ueThroughputVector)
        return (-objectiveValue, )

    def get_bounds(self):
        return self.lowerLimitsVector, self.upperLimitsVector

    def get_nix(self):
        return self.dim

class maximalMedianThrProblemRR:
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
        objectiveValue = np.median(ueThroughputVector)
        return (-objectiveValue, )

    def get_bounds(self):
        return self.lowerLimitsVector, self.upperLimitsVector

    def get_nix(self):
        return self.dim

class local_maximalMedianThrProblemRR:
    def __init__(self, networkInstance, dim, lowerTxLimit, upperTxLimit, localListBS):
        self.dim = dim
        self.networkInstance = networkInstance
        self.lowerLimitsVector = []
        self.upperLimitsVector = []
        self.bsList = localListBS
        for i in range(dim):
            self.lowerLimitsVector.append(lowerTxLimit)
            self.upperLimitsVector.append(upperTxLimit)

    def fitness(self, x):
        for i in range(len(x)):
            self.networkInstance.bs[int(self.bsList[i])].outsidePower = x[i]
        ueThroughputVector = self.networkInstance.returnRealUEThroughputVectorRR()
        objectiveValue = np.median(ueThroughputVector)
        return (-objectiveValue, )

    def get_bounds(self):
        return self.lowerLimitsVector, self.upperLimitsVector

    def get_nix(self):
        return self.dim

class minInterQuartileRangeroblemRR:
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
        objectiveValue = np.percentile(ueThroughputVector, 75) - np.percentile(ueThroughputVector, 25)
        return (-objectiveValue, )

    def get_bounds(self):
        return self.lowerLimitsVector, self.upperLimitsVector

    def get_nix(self):
        return self.dim

class local_minInterQuartileRangeroblemRR:
    def __init__(self, networkInstance, dim, lowerTxLimit, upperTxLimit, localListBS):
        self.dim = dim
        self.networkInstance = networkInstance
        self.lowerLimitsVector = []
        self.upperLimitsVector = []
        self.bsList = localListBS
        for i in range(dim):
            self.lowerLimitsVector.append(lowerTxLimit)
            self.upperLimitsVector.append(upperTxLimit)

    def fitness(self, x):
        for i in range(len(x)):
            self.networkInstance.bs[int(self.bsList[i])].outsidePower = x[i]
        ueThroughputVector = self.networkInstance.returnRealUEThroughputVectorRR()
        objectiveValue = np.percentile(ueThroughputVector, 75) - np.percentile(ueThroughputVector, 25)
        return (-objectiveValue, )

    def get_bounds(self):
        return self.lowerLimitsVector, self.upperLimitsVector

    def get_nix(self):
        return self.dim