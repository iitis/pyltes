__author__ = 'Mariusz Slabicki, Konrad Polys'

from pyltes import devices
from pyltes import generator
from pyltes import printer

import math
import random
import pickle
import copy


class CellularNetwork:
    """Class describing cellular network"""
    def __init__(self):
        self.ue = []
        self.bs = []
        self.obstacles = []
        self.constraintAreaMaxX = []
        self.constraintAreaMaxY = []
        self.radius = []
        self.minTxPower = 10
        self.maxTxPower = 40
        self.minFemtoTxPower = 3
        self.maxFemtoTxPower = 10
        self.optimizationFunctionResults = None
        self.Generator = generator.Generator(self)
        self.Printer = printer.Printer(self)
        self.powerConfigurator = []
        self.colorConfigurator = []
	
    def loadPowerConfigurator(self):
        from pyltes import powerConfigurator
        self.powerConfigurator = powerConfigurator.pygmoPowerConfigurator(self)

    def loadColorConfigurator(self):
        from modules import colorConfigurator
        self.colorConfigurator = colorConfigurator.pygmoColorConfigurator(self)

    def saveNetworkToFile(self, filename):
        with open(filename+".pnf", 'wb') as f:
            pickle.dump(self, f)

    @classmethod
    def loadNetworkFromFile(cls, filename):
        with open(filename+".pnf", 'rb') as f:
            return pickle.load(f)
	
    def addOneBSTower(self, x_pos, y_pos, omnidirectional = False):
        if omnidirectional == False:
            for i in range(3):
                bs = devices.BS()
                bs.x = x_pos
                bs.y = y_pos
                bs.insidePower = 37
                bs.outsidePower = 40
                bs.angle = i * 120
                bs.ID = len(self.bs)
                bs.turnedOn = True
                self.bs.append(copy.deepcopy(bs))
	
    def printPowersInBS(self):
        powers = []
        for bs in self.bs:
            powers.append(bs.outsidePower)
        print(powers)

    def connectUsersToNearestBS(self):
        for ue in self.ue:
            ue.connectToNearestBS(self.bs)

    def connectUsersToTheBestBS(self):
        for ue in self.ue:
            ue.connectToTheBestBS(self.bs)

    def setPowerInAllBS(self, outsidePowerLevel, insidePowerLevel=None):
        if (insidePowerLevel==None):
            insidePowerLevel = outsidePowerLevel - 3
        for bs in self.bs:
            if bs.useSFR:
                bs.insidePower = insidePowerLevel
                bs.outsidePower = outsidePowerLevel
            else:
                bs.insidePower = outsidePowerLevel
                bs.outsidePower = outsidePowerLevel

    def setRandomPowerInAllBS(self, powerLevel):
        for bs in self.bs:
            if bs.useSFR:
                bs.insidePower = random.randint(0, powerLevel) - 3
                bs.outsidePower = bs.insidePower + 3
            else:
                bs.outsidePower = random.randint(0, powerLevel)
                bs.insidePower = bs.outsidePower

    def setSmallestPossiblePowerInAllBS(self):
        for bs in self.bs:
            if bs.type == "MakroCell":
                if bs.useSFR:
                    bs.insidePower = self.minTxPower - 3
                    bs.outsidePower = self.minTxPower
                else:
                    bs.insidePower = self.minTxPower
                    bs.outsidePower = self.minTxPower
            if bs.type == "FemtoCell":
                bs.power == self.minFemtoTxPower

    def setHighestPossiblePowerInAllBS(self):
        for bs in self.bs:
            if bs.type == "MakroCell":
                bs.outsidePower = self.maxTxPower
            if bs.type == "FemtoCell":
                bs.power == self.maxFemtoTxPower

    def setMiInAllBS(self, mi):
        for bs in self.bs:
            bs.mi = mi

    def setColorRandomlyInAllBS(self):
        for bs in self.bs:
            bs.color = random.randint(1,3)

    def setColorInAllBS(self, color):
        for bs in self.bs:
            bs.color = color

    def getColorInAllBS(self):
        for bs in self.bs:
            print(bs.ID, bs.color)

    def setColorInBS(self, bs, color):
        self.bs[bs].color = color

    def setRcInAllBS(self, Rc):
        for bs in self.bs:
            bs.Rc = Rc

    def calculateSINRVectorForAllUE(self):
        temp_measured_vector = []
        for ue in self.ue:
            for bs in self.bs:
                if bs.ID == ue.connectedToBS:
                    calculatedSINR = ue.calculateSINR(self.bs)
                    temp_measured_vector.append(calculatedSINR)
        return temp_measured_vector

    def returnRealUEThroughputVectorRR(self):
        numberOfConnectedUEToBS = []
        max_UE_throughput_vector = []
        real_UE_throughput_vector = []
        for i in range(len(self.bs)):
            numberOfConnectedUEToBS.append([0,0])
        for ue in self.ue:
            max_UE_throughput = ue.calculateMaxThroughputOfTheNode(self.bs) # need to be first to know where UE is
            if (ue.inside):
                numberOfConnectedUEToBS[ue.connectedToBS][0] += 1
            else:
                numberOfConnectedUEToBS[ue.connectedToBS][1] += 1
            max_UE_throughput_vector.append(max_UE_throughput)
            real_UE_throughput_vector.append(max_UE_throughput)
        for i in range(len(self.ue)):
            if (self.ue[i].inside):
                real_UE_throughput_vector[i] = max_UE_throughput_vector[i] / numberOfConnectedUEToBS[self.ue[i].connectedToBS][0]
            else:
                real_UE_throughput_vector[i] = max_UE_throughput_vector[i] / numberOfConnectedUEToBS[self.ue[i].connectedToBS][1]
        return real_UE_throughput_vector

    def returnRealUEThroughputVectorFS(self):
        sumOfInvThroughputPerBS = []
        real_UE_throughput_vector = []
        for i in range(len(self.bs)):
            sumOfInvThroughputPerBS.append([0,0])
        for ue in self.ue:
            ue_throughput = ue.calculateMaxThroughputOfTheNode(self.bs)
            if ue_throughput == 0:
                if (ue.inside):
                    sumOfInvThroughputPerBS[ue.connectedToBS][0] += 1
                else:
                    sumOfInvThroughputPerBS[ue.connectedToBS][1] += 1
            else:
                if (ue.inside):
                    sumOfInvThroughputPerBS[ue.connectedToBS][0] += 1.0 / ue_throughput
                else:
                    sumOfInvThroughputPerBS[ue.connectedToBS][1] += 1.0 / ue_throughput
        for ue in self.ue:
            ue_throughput = ue.calculateMaxThroughputOfTheNode(self.bs)
            if ue_throughput == 0:
                if (ue.inside):
                    weight = 1.0 / sumOfInvThroughputPerBS[ue.connectedToBS][0]
                else:
                    weight = 1.0 / sumOfInvThroughputPerBS[ue.connectedToBS][1]
            else:
                if (ue.inside):
                    weight = ((1.0 / ue_throughput) / sumOfInvThroughputPerBS[ue.connectedToBS][0])
                else:
                    weight = ((1.0 / ue_throughput) / sumOfInvThroughputPerBS[ue.connectedToBS][1])
            real_UE_throughput_vector.append(weight * ue_throughput)
        return real_UE_throughput_vector

    def returnNumberOfUEperBS(self):
        numberOfConnectedUEToBS = []
        for i in range(len(self.bs)):
            zero = 0
            numberOfConnectedUEToBS.append(zero)
        for ue in self.ue:
            numberOfConnectedUEToBS[ue.connectedToBS] += 1
        return numberOfConnectedUEToBS

    def returnAllBSinRange(self, x, y, txrange):
        choosen_BS_vector = []
        for bs in self.bs:
            if math.sqrt((x-bs.x)**2+(y-bs.y)**2) <= txrange:
                choosen_BS_vector.append(copy.deepcopy(bs.ID))
        return choosen_BS_vector

    def returnSumOfThroughput(self, bsnumber, step):
        ue = devices.UE()
        sumOfInternalThroughput = 0
        internalBS = 0
        sumOfExternalThroughput = 0
        externalBS = 0
        for x in range(0, round(self.constraintAreaMaxX), step):
            for y in range(0, round(self.constraintAreaMaxY), step):
                ue.x = x
                ue.y = y
                ue.connectToNearestBS(self.bs)
                if ue.connectedToBS == bsnumber:
                    #if ue.distanceToBS(self.bs[bsnumber]) < self.bs[bsnumber].mi * self.bs[bsnumber].Rc:
                    if ue.inside:
                        sumOfInternalThroughput = sumOfInternalThroughput + ue.calculateMaxThroughputOfTheNode(self.bs)
                        internalBS = internalBS + 1
                    else:
                        sumOfExternalThroughput = sumOfExternalThroughput + ue.calculateMaxThroughputOfTheNode(self.bs)
                        externalBS = externalBS + 1
        if externalBS != 0:
            sumOfExternalThroughput = sumOfExternalThroughput/externalBS
        if internalBS != 0:
            sumOfInternalThroughput = sumOfInternalThroughput/internalBS
        sumOfThroughput = sumOfExternalThroughput + sumOfInternalThroughput
        return sumOfThroughput
