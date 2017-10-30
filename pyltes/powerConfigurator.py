__author__ = 'mslabicki'

import pygmo as pg
#
from pyltes.powerOptimizationProblemsDef import maximalThroughputProblemRR
from pyltes.powerOptimizationProblemsDef import local_maximalThroughputProblemRR
from pyltes.powerOptimizationProblemsDef import maximalMedianThrProblemRR
from pyltes.powerOptimizationProblemsDef import local_maximalMedianThrProblemRR
# from pyltes.powerOptimizationProblemsDef import minInterQuartileRangeroblemRR
# from pyltes.powerOptimizationProblemsDef import local_minInterQuartileRangeroblemRR

import copy
import math
import numpy as np

class pygmoPowerConfigurator:
    def __init__(self,parent):
        self.parent = parent

    def findPowersRR(self, objectiveFunction="averageThr", sgaGenerations = 100, numberOfThreads = 11, numOfIndividuals = 10, evolveTimes = 10, method="global", x_arg=None, y_arg=None, expectedSignalLoss_arg=None):
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
        if objectiveFunction == "averageThr":
            if method == "local":
                localListBS = []
                for i in range(len(localBsVector)):
                    localListBS.append(localBsVector[i,0])
                prob = pg.problem(local_maximalThroughputProblemRR(dim=len(localBsVector), networkInstance=self.parent, lowerTxLimit=self.parent.minTxPower, upperTxLimit=self.parent.maxTxPower, localListBS=localListBS))

            if method == "global":
                prob = pg.problem(maximalThroughputProblemRR(dim=len(self.parent.bs), networkInstance=self.parent, lowerTxLimit=self.parent.minTxPower, upperTxLimit=self.parent.maxTxPower))

        if objectiveFunction == "medianThr":
            if method == "local":
                localListBS = []
                for i in range(len(localBsVector)):
                    localListBS.append(localBsVector[i,0])
                prob = pg.problem(local_maximalMedianThrProblemRR(dim=len(localBsVector), networkInstance=self.parent, lowerTxLimit=self.parent.minTxPower, upperTxLimit=self.parent.maxTxPower, localListBS=localListBS))

            if method == "global":
                prob = pg.problem(maximalMedianThrProblemRR(dim=len(self.parent.bs), networkInstance=self.parent, lowerTxLimit=self.parent.minTxPower, upperTxLimit=self.parent.maxTxPower))

        if objectiveFunction == "minIQRthr":
            if method == "local":
                prob = local_minInterQuartileRangeroblemRR(dim=len(localBsVector))
                for i in range(len(localBsVector)):
                    prob.bsList.append(localBsVector[i,0])

            if method == "global":
                prob = minInterQuartileRangeroblemRR(dim=len(self.parent.bs))

        prob.siec = copy.deepcopy(self.parent)
        # algo = algorithm.sga(gen=sgaGenerations)
        algo = pg.algorithm(pg.sga(gen=sgaGenerations))
        # archi = archipelago(algo, prob, numberOfThreads, numOfIndividuals, topology = topology.barabasi_albert())
        # archi.evolve(evolveTimes)
        # archi.join()
        population = pg.population(prob, numOfIndividuals)
        population = algo.evolve(population)

        theBestCostF = 0
        islandNumber = -1
        islandCounter = 0
        # for island in archi:
        #     if theBestCostF > island.population.champion.f[0]:
        #         theBestCostF = island.population.champion.f[0]
        #         islandNumber = islandCounter
        #     islandCounter = islandCounter + 1

        if method == "global":
            for i in range(len(self.parent.bs)):
                self.parent.bs[i].outsidePower = population.champion_x[i]
        if method == "local":
            for i in range(len(localListBS)):
                # self.parent.bs[int(prob.bsList[i])].outsidePower = archi[islandNumber].population.champion.x[i]
                self.parent.bs[int(localListBS[i])].outsidePower = population.champion_x[i]
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
