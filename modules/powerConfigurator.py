__author__ = 'mslabicki'

from PyGMO import *
from modules.powerOptimizationProblemsDef import maximalThroughputProblemRR_const
from modules.powerOptimizationProblemsDef import local_maximalThroughputProblemRR_const
from modules.powerOptimizationProblemsDef import maximalThroughputProblemRR_thebest
from modules.powerOptimizationProblemsDef import local_maximalThroughputProblemRR_thebest

import copy
import math
import numpy as np

class pygmoPowerConfigurator:
    def __init__(self,parent):
        self.parent = parent

    def findPowersMaxThrRR(self, connections="const", sgaGenerations = 100, numberOfThreads = 11, numOfIndividuals = 10, evolveTimes = 10, method="global", x_arg=None, y_arg=None, expectedSignalLoss_arg=None):
        if method == "local":
            if x_arg == None:
                x = self.parent.constraintAreaMaxX/2
            else:
                x = x_arg
            if y_arg == None:
                y = self.parent.constraintAreaMaxY/2
            else:
                y = y_arg
            if expectedSignalLoss_arg == None:
                maxDistance = min(self.parent.constraintAreaMaxX/2, self.parent.constraintAreaMaxY/2)
            else:
                maxDistance = returnDistanceFromSNR(expectedSignalLoss_arg)
            localBsVector = []
            for bs in self.parent.bs:
                if math.sqrt((bs.x - x)**2 + (bs.y - y)**2) < maxDistance:
                    row = []
                    row.append(int(bs.ID))
                    row.append(math.sqrt((bs.x - x)**2 + (bs.y - y)**2))
                    localBsVector.append(row)
            localBsVector = np.asarray(localBsVector)

        if method == "local" and connections == "const":
            prob = local_maximalThroughputProblemRR_const(dim=len(localBsVector))
            for i in range(len(localBsVector)):
                prob.bsList.append(localBsVector[i,0])

        if method == "local" and connections == "theBest":
            prob = local_maximalThroughputProblemRR_thebest(dim=len(localBsVector))
            for i in range(len(localBsVector)):
                prob.bsList.append(localBsVector[i,0])

        if method == "global" and connections == "const":
            prob = maximalThroughputProblemRR_const(dim=len(self.parent.bs))

        if method == "global" and connections == "theBest":
            prob = maximalThroughputProblemRR_thebest(dim=len(self.parent.bs))

        prob.siec = copy.deepcopy(self.parent)
        algo = algorithm.sga(gen=sgaGenerations)
        archi = archipelago(algo, prob, numberOfThreads, numOfIndividuals, topology = topology.barabasi_albert())
        archi.evolve(evolveTimes)
        archi.join()
        theBestCostF = 0
        islandNumber = -1
        islandCounter = 0
        for island in archi:
            if theBestCostF > island.population.champion.f[0]:
                theBestCostF = island.population.champion.f[0]
                islandNumber = islandCounter
            islandCounter = islandCounter + 1
        if method == "global":
            for i in range(len(self.parent.bs)):
                self.parent.bs[i].outsidePower = archi[islandNumber].population.champion.x[i]
        if method == "local":
            for i in range(len(prob.bsList)):
                self.parent.bs[int(prob.bsList[i])].outsidePower = archi[islandNumber].population.champion.x[i]
            return len(localBsVector)

def returnDistanceFromSNR(expectedSignalLoss):
    lambda_val = 0.142758313333
    a = 4.0
    b = 0.0065
    c = 17.1
    d = 10.8
    s = 15.8

    ht = 40
    hr = 1.5
    f = 2.1
    gamma = a - b*ht + c/ht
    Xf = 6 * math.log10( f/2 )
    Xh = -d * math.log10( hr/2 )

    R0 = 100.0
    R0p = R0 * pow(10.0,-( (Xf+Xh) / (10*gamma) ))

    bandwidth=20
    k = 1.3806488 * math.pow(10, -23)
    T = 293.0
    BW = bandwidth * 1000 * 1000
    N = 10*math.log10(k*T) + 10*math.log10(BW)

    alpha = 20 * math.log10( (4*math.pi*R0p) / lambda_val )
    R = R0 * math.pow(10, (expectedSignalLoss - alpha-Xf-Xh-s - N)/(10*gamma))

    return R