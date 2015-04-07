__author__ = 'mslabicki'

from PyGMO import *
from modules.powerOptimizationProblemsDef import maximalThroughputProblemRR
from modules.powerOptimizationProblemsDef import maximalThroughputProblemFS
from modules.powerOptimizationProblemsDef import medianThroughputProblemRR
from modules.powerOptimizationProblemsDef import medianThroughputProblemFS
from modules.powerOptimizationProblemsDef import minIqrProblemRR
from modules.powerOptimizationProblemsDef import minIqrProblemFS
from modules.powerOptimizationProblemsDef import maxTotalSINRProblem
from modules.powerOptimizationProblemsDef import maxMedianSINRProblem

import copy

numberOfThreads = 11

class pygmoPowerConfigurator:
    def __init__(self,parent):
        self.parent = parent

    def findPowersMaxThrRR(self):
        prob = maximalThroughputProblemRR(dim=len(self.parent.bs))
        prob.siec = copy.deepcopy(self.parent)
        algo = algorithm.sga(gen=100)
        archi = archipelago(algo, prob, numberOfThreads, 10)
        archi.evolve(10)
        archi.join()
        theBestCostF = 0
        islandNumber = -1
        islandCounter = 0
        for island in archi:
            if theBestCostF > island.population.champion.f[0]:
                theBestCostF = island.population.champion.f[0]
                islandNumber = islandCounter
            islandCounter = islandCounter + 1
        for i in range(len(self.parent.bs)):
            self.parent.bs[i].outsidePower = archi[islandNumber].population.champion.x[i]

    def findPowersMaxThrFS(self):
        prob = maximalThroughputProblemFS(dim=len(self.parent.bs))
        prob.siec = copy.deepcopy(self.parent)
        algo = algorithm.sga(gen=100)
        archi = archipelago(algo, prob, numberOfThreads, 10)
        archi.evolve(10)
        archi.join()
        theBestCostF = 0
        islandNumber = -1
        islandCounter = 0
        for island in archi:
            if theBestCostF > island.population.champion.f[0]:
                theBestCostF = island.population.champion.f[0]
                islandNumber = islandCounter
            islandCounter = islandCounter + 1
        for i in range(len(self.parent.bs)):
            self.parent.bs[i].outsidePower = archi[islandNumber].population.champion.x[i]

    def findPowersMedianThrRR(self):
        prob = medianThroughputProblemRR(dim=len(self.parent.bs))
        prob.siec = copy.deepcopy(self.parent)
        algo = algorithm.sga(gen=100)
        archi = archipelago(algo, prob, numberOfThreads, 10)
        archi.evolve(10)
        archi.join()
        theBestCostF = 0
        islandNumber = -1
        islandCounter = 0
        for island in archi:
            if theBestCostF > island.population.champion.f[0]:
                theBestCostF = island.population.champion.f[0]
                islandNumber = islandCounter
            islandCounter = islandCounter + 1
        for i in range(len(self.parent.bs)):
            self.parent.bs[i].outsidePower = archi[islandNumber].population.champion.x[i]

    def findPowersMedianThrFS(self):
        prob = medianThroughputProblemFS(dim=len(self.parent.bs))
        prob.siec = copy.deepcopy(self.parent)
        algo = algorithm.sga(gen=100)
        archi = archipelago(algo, prob, numberOfThreads, 10)
        archi.evolve(10)
        archi.join()
        theBestCostF = 0
        islandNumber = -1
        islandCounter = 0
        for island in archi:
            if theBestCostF > island.population.champion.f[0]:
                theBestCostF = island.population.champion.f[0]
                islandNumber = islandCounter
            islandCounter = islandCounter + 1
        for i in range(len(self.parent.bs)):
            self.parent.bs[i].outsidePower = archi[islandNumber].population.champion.x[i]

    def findMinIqrThrRR(self):
        prob = minIqrProblemRR(dim=len(self.parent.bs))
        prob.siec = copy.deepcopy(self.parent)
        algo = algorithm.sga(gen=100)
        archi = archipelago(algo, prob, numberOfThreads, 10)
        archi.evolve(10)
        archi.join()
        theBestCostF = 0
        islandNumber = -1
        islandCounter = 0
        for island in archi:
            if theBestCostF > island.population.champion.f[0]:
                theBestCostF = island.population.champion.f[0]
                islandNumber = islandCounter
            islandCounter = islandCounter + 1
        for i in range(len(self.parent.bs)):
            self.parent.bs[i].outsidePower = archi[islandNumber].population.champion.x[i]

    def findMinIqrThrFS(self):
        prob = minIqrProblemFS(dim=len(self.parent.bs))
        prob.siec = copy.deepcopy(self.parent)
        algo = algorithm.sga(gen=100)
        archi = archipelago(algo, prob, numberOfThreads, 10)
        archi.evolve(10)
        archi.join()
        theBestCostF = 0
        islandNumber = -1
        islandCounter = 0
        for island in archi:
            if theBestCostF > island.population.champion.f[0]:
                theBestCostF = island.population.champion.f[0]
                islandNumber = islandCounter
            islandCounter = islandCounter + 1
        for i in range(len(self.parent.bs)):
            self.parent.bs[i].outsidePower = archi[islandNumber].population.champion.x[i]

    def findPowersMaxTotalSINR(self):
        prob = maxTotalSINRProblem(dim=len(self.parent.bs))
        prob.siec = copy.deepcopy(self.parent)
        algo = algorithm.sga(gen=100)
        archi = archipelago(algo, prob, numberOfThreads, 10)
        archi.evolve(10)
        archi.join()
        theBestCostF = 0
        islandNumber = -1
        islandCounter = 0
        for island in archi:
            if theBestCostF > island.population.champion.f[0]:
                theBestCostF = island.population.champion.f[0]
                islandNumber = islandCounter
            islandCounter = islandCounter + 1
        for i in range(len(self.parent.bs)):
            self.parent.bs[i].outsidePower = archi[islandNumber].population.champion.x[i]

    def findPowersMaxMedianSINR(self):
        prob = maxMedianSINRProblem(dim=len(self.parent.bs))
        prob.siec = copy.deepcopy(self.parent)
        algo = algorithm.sga(gen=100)
        archi = archipelago(algo, prob, numberOfThreads, 10)
        archi.evolve(10)
        archi.join()
        theBestCostF = 0
        islandNumber = -1
        islandCounter = 0
        for island in archi:
            if theBestCostF > island.population.champion.f[0]:
                theBestCostF = island.population.champion.f[0]
                islandNumber = islandCounter
            islandCounter = islandCounter + 1
        for i in range(len(self.parent.bs)):
            self.parent.bs[i].outsidePower = archi[islandNumber].population.champion.x[i]