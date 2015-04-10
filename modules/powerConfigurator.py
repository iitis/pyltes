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

class pygmoPowerConfigurator:
    def __init__(self,parent):
        self.parent = parent

    def findPowersMaxThrRR(self, sgaGenerations = 100, numberOfThreads = 11, numOfIndividuals = 10, evolveTimes = 10):
        prob = maximalThroughputProblemRR(dim=len(self.parent.bs))
        prob.siec = copy.deepcopy(self.parent)
        algo = algorithm.sga(gen=sgaGenerations)
        archi = archipelago(algo, prob, numberOfThreads, numOfIndividuals)
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
        for i in range(len(self.parent.bs)):
            self.parent.bs[i].outsidePower = archi[islandNumber].population.champion.x[i]

    def findPowersMaxThrFS(self, sgaGenerations = 100, numberOfThreads = 11, numOfIndividuals = 10, evolveTimes = 10):
        prob = maximalThroughputProblemFS(dim=len(self.parent.bs))
        prob.siec = copy.deepcopy(self.parent)
        algo = algorithm.sga(gen=sgaGenerations)
        archi = archipelago(algo, prob, numberOfThreads, numOfIndividuals)
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
        for i in range(len(self.parent.bs)):
            self.parent.bs[i].outsidePower = archi[islandNumber].population.champion.x[i]

    def findPowersMedianThrRR(self, sgaGenerations = 100, numberOfThreads = 11, numOfIndividuals = 10, evolveTimes = 10):
        prob = medianThroughputProblemRR(dim=len(self.parent.bs))
        prob.siec = copy.deepcopy(self.parent)
        algo = algorithm.sga(gen=sgaGenerations)
        archi = archipelago(algo, prob, numberOfThreads, numOfIndividuals)
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
        for i in range(len(self.parent.bs)):
            self.parent.bs[i].outsidePower = archi[islandNumber].population.champion.x[i]

    def findPowersMedianThrFS(self, sgaGenerations = 100, numberOfThreads = 11, numOfIndividuals = 10, evolveTimes = 10):
        prob = medianThroughputProblemFS(dim=len(self.parent.bs))
        prob.siec = copy.deepcopy(self.parent)
        algo = algorithm.sga(gen=sgaGenerations)
        archi = archipelago(algo, prob, numberOfThreads, numOfIndividuals)
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
        for i in range(len(self.parent.bs)):
            self.parent.bs[i].outsidePower = archi[islandNumber].population.champion.x[i]

    def findMinIqrThrRR(self, sgaGenerations = 100, numberOfThreads = 11, numOfIndividuals = 10, evolveTimes = 10):
        prob = minIqrProblemRR(dim=len(self.parent.bs))
        prob.siec = copy.deepcopy(self.parent)
        algo = algorithm.sga(gen=sgaGenerations)
        archi = archipelago(algo, prob, numberOfThreads, numOfIndividuals)
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
        for i in range(len(self.parent.bs)):
            self.parent.bs[i].outsidePower = archi[islandNumber].population.champion.x[i]

    def findMinIqrThrFS(self, sgaGenerations = 100, numberOfThreads = 11, numOfIndividuals = 10, evolveTimes = 10):
        prob = minIqrProblemFS(dim=len(self.parent.bs))
        prob.siec = copy.deepcopy(self.parent)
        algo = algorithm.sga(gen=sgaGenerations)
        archi = archipelago(algo, prob, numberOfThreads, numOfIndividuals)
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
        for i in range(len(self.parent.bs)):
            self.parent.bs[i].outsidePower = archi[islandNumber].population.champion.x[i]

    def findPowersMaxTotalSINR(self, sgaGenerations = 100, numberOfThreads = 11, numOfIndividuals = 10, evolveTimes = 10):
        prob = maxTotalSINRProblem(dim=len(self.parent.bs))
        prob.siec = copy.deepcopy(self.parent)
        algo = algorithm.sga(gen=sgaGenerations)
        archi = archipelago(algo, prob, numberOfThreads, numOfIndividuals)
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
        for i in range(len(self.parent.bs)):
            self.parent.bs[i].outsidePower = archi[islandNumber].population.champion.x[i]

    def findPowersMaxMedianSINR(self, sgaGenerations = 100, numberOfThreads = 11, numOfIndividuals = 10, evolveTimes = 10):
        prob = maxMedianSINRProblem(dim=len(self.parent.bs))
        prob.siec = copy.deepcopy(self.parent)
        algo = algorithm.sga(gen=sgaGenerations)
        archi = archipelago(algo, prob, numberOfThreads, numOfIndividuals)
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
        for i in range(len(self.parent.bs)):
            self.parent.bs[i].outsidePower = archi[islandNumber].population.champion.x[i]