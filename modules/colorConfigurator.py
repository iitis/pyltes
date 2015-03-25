__author__ = 'Mariusz Słabicki, Konrad Połys'

from PyGMO import *
from modules.colorOptimizationProblemsDef import maximalThroughputProblemRR
from modules.colorOptimizationProblemsDef import maximalThroughputProblemFS

import copy

numberOfThreads = 4

class pygmoColorConfigurator:
    def __init__(self,parent):
        self.parent = parent

    def findColorsMaxThrRR(self,gen):
        prob = maximalThroughputProblemRR(dim=len(self.parent.bs))
        prob.siec = copy.deepcopy(self.parent)
        algo = algorithm.sga(gen=gen) # 100
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
            self.parent.bs[i].color = archi[islandNumber].population.champion.x[i]

    def findColorsMaxThrRR_SEA(self,gen):
        prob = maximalThroughputProblemRR(dim=len(self.parent.bs))
        prob.siec = copy.deepcopy(self.parent)
        algo = algorithm.sea(gen=gen)
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
            self.parent.bs[i].color = archi[islandNumber].population.champion.x[i]

    def findColorsMaxThrFS(self,gen):
        prob = maximalThroughputProblemFS(dim=len(self.parent.bs))
        prob.siec = copy.deepcopy(self.parent)
        algo = algorithm.sga(gen=gen) # 100
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
            self.parent.bs[i].color = archi[islandNumber].population.champion.x[i]

    def findColorsMaxThrFS_SEA(self,gen):
        prob = maximalThroughputProblemFS(dim=len(self.parent.bs))
        prob.siec = copy.deepcopy(self.parent)
        algo = algorithm.sea(gen=gen)
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
            self.parent.bs[i].color = archi[islandNumber].population.champion.x[i]