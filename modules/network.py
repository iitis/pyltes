__author__ = 'Mariusz Słabicki, Konrad Połys'

from modules import devices
from modules import generator
from modules import printer
from modules import powerConfigurator
from modules import colorConfigurator
import math
import random
import pickle
import copy

from statsmodels.distributions.empirical_distribution import ECDF

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
        self.initialTemperature = 300
        self.balanceLevel = 0.4
        self.timeLengthOfAlgorithm = -1
        self.optimizationFunctionResults = None
        self.Generator = generator.Generator(self)
        self.Printer = printer.Printer(self)
        self.powerConfigurator = powerConfigurator.pygmoPowerConfigurator(self)
        self.colorConfigurator = colorConfigurator.pygmoColorConfigurator(self)

    def saveNetworkToFile(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self, f)

    def loadNetworkFromFile(self, filename):
        with open(filename, 'rb') as f:
            network = pickle.load(f)
        return network

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
            bs.insidePower = insidePowerLevel
            bs.outsidePower = outsidePowerLevel

    def setRandomPowerInAllBS(self, powerLevel):
        for bs in self.bs:
            bs.insidePower = random.randint(0, powerLevel) - 3
            bs.outsidePower = bs.insidePower + 3

    def setSmallestPossiblePowerInAllBS(self):
        for bs in self.bs:
            if bs.type == "MakroCell":
                bs.insidePower = self.minTxPower - 3
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

    def calculateAMSnodes(self, BS_vector, SINR_min):
        AMS_vector = []
        for ue in self.ue:
            sinr = ue.calculateSINR(BS_vector)
            if(sinr < SINR_min):
                AMS_vector.append(ue)
        return AMS_vector

    def calculateAMSValues(self, ue_AMS_vector, bs_vector):
        ams_values = []
        for node in ue_AMS_vector:
            ams_values.append(node.calculateSINR(bs_vector))
        return ams_values

    def calculateAMSCostValue(self, ams_values_arg):
        if len(ams_values_arg) == 0:
            return 1000
        ecdf = ECDF(ams_values_arg)
        for value in ams_values_arg:
            if ecdf(value) >= 0.5:
                return -1*value

    def returnRealAvgUEThroughputPerBsRR(self):
        numberOfConnectedUEToBS = []
        throughputSumPerBS = []
        max_UE_throughput_vector = []
        real_UE_throughput_vector = []
        realAvgUEThroughputPerBs = []
        for i in range(len(self.bs)):
            numberOfConnectedUEToBS.append([0,0])
            throughputSumPerBS.append([0,0])
            realAvgUEThroughputPerBs.append(0)
        for ue in self.ue:
            max_UE_throughput = ue.calculateMaxThroughputOfTheNode(self.bs) # need to be first to know where UE is
            if (ue.inside):
                numberOfConnectedUEToBS[ue.connectedToBS][0] += 1
            else:
                numberOfConnectedUEToBS[ue.connectedToBS][1] += 1
            max_UE_throughput_vector.append(max_UE_throughput)
            real_UE_throughput_vector.append(0)
        for i in range(len(self.ue)):
            if (self.ue[i].inside):
                real_UE_throughput_vector[i] = max_UE_throughput_vector[i] / numberOfConnectedUEToBS[self.ue[i].connectedToBS][0]
                throughputSumPerBS[self.ue[i].connectedToBS][0] += real_UE_throughput_vector[i]
            else:
                real_UE_throughput_vector[i] = max_UE_throughput_vector[i] / numberOfConnectedUEToBS[self.ue[i].connectedToBS][1]
                throughputSumPerBS[self.ue[i].connectedToBS][1] += real_UE_throughput_vector[i]
        for i in range(len(self.bs)):
            if (numberOfConnectedUEToBS[i][0] > 0):
                realAvgUEThroughputPerBs[i] += throughputSumPerBS[i][0] / numberOfConnectedUEToBS[i][0]
            if (numberOfConnectedUEToBS[i][1] > 0):
                realAvgUEThroughputPerBs[i] += throughputSumPerBS[i][1] / numberOfConnectedUEToBS[i][1]
            realAvgUEThroughputPerBs[i] /= 2.0

        return realAvgUEThroughputPerBs

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

    def returnRealUEThroughputVectorFS2in1(self):
        sumOfInvThroughputPerBS = []
        real_UE_throughput_vector = []
        for i in range(len(self.bs)):
            sumOfInvThroughputPerBS.append(0)
        for ue in self.ue:
            ue_throughput = ue.calculateMaxThroughputOfTheNode(self.bs)
            if ue_throughput == 0:
                sumOfInvThroughputPerBS[ue.connectedToBS] += 1
            else:
                sumOfInvThroughputPerBS[ue.connectedToBS] += 1.0 / ue_throughput
        for ue in self.ue:
            ue_throughput = ue.calculateMaxThroughputOfTheNode(self.bs)
            if ue_throughput == 0:
                weight = 1.0 / sumOfInvThroughputPerBS[ue.connectedToBS]
            else:
                weight = ((1.0 / ue_throughput) / sumOfInvThroughputPerBS[ue.connectedToBS])
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

    def returnBSconfig(self):
        networkConfig = []
        for i in range(len(self.bs)):
            bsConfig = []
            bsConfig.append(self.bs[i].ID)
            bsConfig.append(self.bs[i].Rc)
            bsConfig.append(self.bs[i].mi)
            bsConfig.append(self.bs[i].color)
            bsConfig.append(self.bs[i].insidePower)
            bsConfig.append(self.bs[i].outsidePower)
            networkConfig.append(bsConfig)
        return networkConfig

    def calculateIfSollutionCanBeAccepted(self, bs_vector):
        ue_copy = copy.deepcopy(self.ue)
        bs_copy = copy.deepcopy(self.bs)
        self.bs = copy.deepcopy(bs_vector)
        self.connectUsersToTheBestBS()

        numberOfConnectedUE = []
        for bs in bs_vector:
            number = 0
            numberOfConnectedUE.append(number)
        for ue in self.ue:
            numberOfConnectedUE[ue.connectedToBS] = numberOfConnectedUE[ue.connectedToBS] + 1

        avg_ue_per_bs = len(self.ue) / len(self.bs)
        avg_acceptable_diff = (avg_ue_per_bs * self.balanceLevel)**2
        total_max_dev_level = len(self.bs) * avg_acceptable_diff
        current_dev_level = 0

        for number in numberOfConnectedUE:
            current_dev_level = current_dev_level + (avg_ue_per_bs - number)**2
        self.ue = copy.deepcopy(ue_copy)
        self.bs = copy.deepcopy(bs_copy)
        if current_dev_level < total_max_dev_level:
            return True
        else:
            return False

    def returnAllBSinRange(self, x, y, txrange):
        choosen_BS_vector = []
        for bs in self.bs:
            if math.sqrt((x-bs.x)**2+(y-bs.y)**2) <= txrange:
                choosen_BS_vector.append(copy.deepcopy(bs.ID))
        return choosen_BS_vector

    def simulatedAnnaealing_from_article(self, SINR_threshold):
        costValue = []
        currentSollution = copy.deepcopy(self.bs)
        theBestSollution = copy.deepcopy(self.bs)
        ams_nodes = self.calculateAMSnodes(self.bs, SINR_threshold)
        ams_values = self.calculateAMSValues(ams_nodes, self.bs)
        C = self.calculateAMSCostValue(ams_values)
        C_best = C
        back_step_configs = []
        neighbor_list = []
        B = 50
        Iams = 10
        T = self.initialTemperature
        p = []

        terminalCounter = 300
        while terminalCounter > 0:
            equilibriumCounter = 10
            if len(ams_nodes) > 0:
                while equilibriumCounter > 0:
                    equilibriumCounter = equilibriumCounter - 1
                    neighbor_list.clear()
                    for i in range(0, int(len(self.bs))):
                        nodeToChange = random.randint(0, int(len(self.bs))-1)
                        newNeighbor = copy.deepcopy(currentSollution)
                        if self.bs[nodeToChange].type == "MakroCell":
                            newNeighbor[nodeToChange].power = random.randint(self.minTxPower, self.maxTxPower)
                        if self.bs[nodeToChange].type == "FemtoCell":
                            newNeighbor[nodeToChange].power = random.randint(self.minFemtoTxPower, self.maxFemtoTxPower)
                        #if self.calculateIfSollutionCanBeAccepted(newNeighbor) == False:
                        #    continue
                        neighbor_list.append(newNeighbor)
                    for neighbor in neighbor_list:
                        amsValuesForThisNeighbor = self.calculateAMSValues(ams_nodes, newNeighbor)
                        costOfThisNeighbor = self.calculateAMSCostValue(amsValuesForThisNeighbor)
                        p = 0.0
                        if C <= costOfThisNeighbor:
                            p = math.exp((C-costOfThisNeighbor)/T)
                        else:
                            p = 1
                        if(p > random.uniform(0, 1)):
                            currentSollution = copy.deepcopy(neighbor)
                            C = costOfThisNeighbor
                            if C < C_best:
                                B = 50
                                theBestSollution = copy.deepcopy(neighbor)
                                C_best = C
                                back_step_configs.append(theBestSollution)
                                if len(back_step_configs) > 4:
                                    del back_step_configs[0]
            B = B-1
            Iams = Iams-1
            T = T*0.95
            if B == 0:
                B = 50
                if(len(back_step_configs) > 3):
                    currentSollution = copy.deepcopy(back_step_configs[random.randint(0, len(back_step_configs)-2)])
            if Iams == 0:
                Iams = 10
                ams_nodes = self.calculateAMSnodes(currentSollution, SINR_threshold)
            terminalCounter = terminalCounter - 1
            costValue.append(C_best)
        counter = 0
        powers = []
        for bs in theBestSollution:
            powers.append(bs.power)
        for bs in self.bs:
            bs.power = powers[counter]
            counter = counter + 1
        return C_best

    def simulatedAnnaealing_from_article_mod(self):
        costValue = []
        currentSollution = copy.deepcopy(self.bs)
        theBestSollution = copy.deepcopy(self.bs)
        ams_nodes = copy.deepcopy(self.ue)
        ams_values = self.calculateAMSValues(ams_nodes, self.bs)
        C = self.calculateAMSCostValue(ams_values)
        C_best = C
        back_step_configs = []
        neighbor_list = []
        B = 50
        T = self.initialTemperature
        p = []

        terminalCounter = 300
        while terminalCounter > 0:
            equilibriumCounter = 10
            while equilibriumCounter > 0:
                equilibriumCounter = equilibriumCounter - 1
                neighbor_list.clear()
                for i in range(0, int(len(self.bs))):
                    nodeToChange = random.randint(0, int(len(self.bs))-1)
                    newNeighbor = copy.deepcopy(currentSollution)
                    if self.bs[nodeToChange].type == "MakroCell":
                        newNeighbor[nodeToChange].power = random.randint(self.minTxPower, self.maxTxPower)
                    if self.bs[nodeToChange].type == "FemtoCell":
                        newNeighbor[nodeToChange].power = random.randint(self.minFemtoTxPower, self.maxFemtoTxPower)
                    neighbor_list.append(newNeighbor)
                for neighbor in neighbor_list:
                    amsValuesForThisNeighbor = self.calculateAMSValues(ams_nodes, newNeighbor)
                    costOfThisNeighbor = self.calculateAMSCostValue(amsValuesForThisNeighbor)
                    p = 0.0
                    if C <= costOfThisNeighbor:
                        p = math.exp((C-costOfThisNeighbor)/T)
                    else:
                        p = 1
                    if(p > random.uniform(0, 1)):
                        currentSollution = copy.deepcopy(neighbor)
                        C = costOfThisNeighbor
                        if C < C_best:
                            B = 50
                            theBestSollution = copy.deepcopy(neighbor)
                            C_best = C
                            back_step_configs.append(theBestSollution)
                            if len(back_step_configs) > 4:
                                del back_step_configs[0]
            B = B-1
            T = T*0.95
            if B == 0:
                B = 50
                if(len(back_step_configs) > 3):
                    currentSollution = copy.deepcopy(back_step_configs[random.randint(0, len(back_step_configs)-2)])
            terminalCounter = terminalCounter - 1
            costValue.append(C_best)
        powers = []
        for bs in theBestSollution:
            powers.append(bs.power)
        counter = 0
        for bs in self.bs:
            bs.power = powers[counter]
            counter = counter + 1
        return C_best

    def simulatedAnnaealing_RR_as_CS(self):
        costValue = []
        currentSollution = copy.deepcopy(self.bs)
        theBestSollution = copy.deepcopy(self.bs)
        C = -1*self.calculateSumOfThroughputRoundRobin(self.bs)
        C_best = C
        back_step_configs = []
        neighbor_list = []
        B = 50
        T = self.initialTemperature

        terminalCounter = 300
        while terminalCounter > 0:
            equilibriumCounter = 10
            while equilibriumCounter > 0:
                equilibriumCounter = equilibriumCounter - 1
                neighbor_list.clear()
                for i in range(0, len(self.bs)):
                    nodeToChange = random.randint(0, len(self.bs)-1)
                    newNeighbor = copy.deepcopy(currentSollution)
                    if self.bs[nodeToChange].type == "MakroCell":
                        newNeighbor[nodeToChange].power = random.randint(self.minTxPower, self.maxTxPower)
                    if self.bs[nodeToChange].type == "FemtoCell":
                        newNeighbor[nodeToChange].power = random.randint(self.minFemtoTxPower, self.maxFemtoTxPower)
                    neighbor_list.append(newNeighbor)
                for neighbor in neighbor_list:
                    costOfThisNeighbor = -1*self.calculateSumOfThroughputRoundRobin(neighbor)
                    p = 0.0
                    if C <= costOfThisNeighbor:
                        p = math.exp((C-costOfThisNeighbor)/T)
                    else:
                        p = 1
                    if(p > random.uniform(0, 1)):
                        currentSollution = copy.deepcopy(neighbor)
                        C = costOfThisNeighbor
                        if C < C_best:
                            B = 50
                            theBestSollution = copy.deepcopy(neighbor)
                            C_best = C
                            back_step_configs.append(theBestSollution)
                            if len(back_step_configs) > 4:
                                del back_step_configs[0]
            B = B-1
            T = T*0.99
            if B == 0:
                B = 50
                if(len(back_step_configs) > 3):
                    currentSollution = copy.deepcopy(back_step_configs[random.randint(0, len(back_step_configs)-2)])
            terminalCounter = terminalCounter - 1
            costValue.append(C_best)
        powers = []
        for bs in theBestSollution:
            powers.append(bs.power)
        counter = 0
        for bs in self.bs:
            bs.power = powers[counter]
            counter = counter + 1
        return C_best

    def simulatedAnnaealing_RR_as_CS_Bounded_Area(self, x_pos, y_pos, txrange):
        costValue = []
        currentSollution = copy.deepcopy(self.bs)
        theBestSollution = copy.deepcopy(self.bs)
        C = -1*self.calculateSumOfThroughputRoundRobin(self.bs)
        C_best = C
        back_step_configs = []
        neighbor_list = []
        B = 50
        T = self.initialTemperature
        possible_BS_to_change = self.returnAllBSinRange(x_pos, y_pos, txrange)
        terminalCounter = 300

        while terminalCounter > 0:
            equilibriumCounter = 10
            while equilibriumCounter > 0:
                equilibriumCounter = equilibriumCounter - 1
                neighbor_list.clear()
                for i in possible_BS_to_change:
                    nodeToChange =  possible_BS_to_change[random.randint(0, len(possible_BS_to_change)-1)]
                    newNeighbor = copy.deepcopy(currentSollution)
                    if self.bs[nodeToChange].type == "MakroCell":
                        newNeighbor[nodeToChange].power = random.randint(self.minTxPower, self.maxTxPower)
                    if self.bs[nodeToChange].type == "FemtoCell":
                        newNeighbor[nodeToChange].power = random.randint(self.minFemtoTxPower, self.maxFemtoTxPower)
                    neighbor_list.append(newNeighbor)
                for neighbor in neighbor_list:
                    costOfThisNeighbor = -1*self.calculateSumOfThroughputRoundRobin(neighbor)
                    p = 0.0
                    if C <= costOfThisNeighbor:
                        p = math.exp((C-costOfThisNeighbor)/T)
                    else:
                        p = 1
                    if(p > random.uniform(0, 1)):
                        currentSollution = copy.deepcopy(neighbor)
                        C = costOfThisNeighbor
                        if C < C_best:
                            B = 50
                            theBestSollution = copy.deepcopy(neighbor)
                            C_best = C
                            back_step_configs.append(theBestSollution)
                            if len(back_step_configs) > 4:
                                del back_step_configs[0]
            B = B-1
            T = T*0.99
            if B == 0:
                B = 50
                if(len(back_step_configs) > 3):
                    currentSollution = copy.deepcopy(back_step_configs[random.randint(0, len(back_step_configs)-2)])
            terminalCounter = terminalCounter - 1
            costValue.append(C_best)
        powers = []
        for bs in theBestSollution:
            powers.append(bs.power)
            print(bs.power, end=' ')
        print("")
        counter = 0
        for bs in self.bs:
            bs.power = powers[counter]
            counter = counter + 1
        return C_best

    def simulatedAnnaealing_FairThroughput_as_CS(self):
        costValue = []
        currentSollution = copy.deepcopy(self.bs)
        theBestSollution = copy.deepcopy(self.bs)
        C = -1*self.calculateSumOfThroughputFairThroughput(self.bs)
        C_best = C
        back_step_configs = []
        neighbor_list = []
        B = 50
        T = self.initialTemperature
        p = []

        terminalCounter = 300
        while terminalCounter > 0:
            equilibriumCounter = 10
            while equilibriumCounter > 0:
                equilibriumCounter = equilibriumCounter - 1
                neighbor_list.clear()
                for i in range(0, len(self.bs)):
                    nodeToChange = random.randint(0, len(self.bs)-1)
                    newNeighbor = copy.deepcopy(currentSollution)
                    if self.bs[nodeToChange].type == "MakroCell":
                        newNeighbor[nodeToChange].power = random.randint(self.minTxPower, self.maxTxPower)
                    if self.bs[nodeToChange].type == "FemtoCell":
                        newNeighbor[nodeToChange].power = random.randint(self.minFemtoTxPower, self.maxFemtoTxPower)
                    neighbor_list.append(newNeighbor)
                for neighbor in neighbor_list:
                    costOfThisNeighbor = -1*self.calculateSumOfThroughputFairThroughput(neighbor)
                    p = 0.0
                    if C <= costOfThisNeighbor:
                        p = math.exp((C-costOfThisNeighbor)/T)
                    else:
                        p = 1
                    if(p > random.uniform(0, 1)):
                        currentSollution = copy.deepcopy(neighbor)
                        C = costOfThisNeighbor
                        if C < C_best:
                            B = 50
                            theBestSollution = copy.deepcopy(neighbor)
                            C_best = C
                            back_step_configs.append(theBestSollution)
                            if len(back_step_configs) > 4:
                                del back_step_configs[0]
            B = B-1
            T = T*0.99
            if B == 0:
                B = 50
                if(len(back_step_configs) > 3):
                    currentSollution = copy.deepcopy(back_step_configs[random.randint(0, len(back_step_configs)-2)])
            terminalCounter = terminalCounter - 1
            costValue.append(C_best)
        powers = []
        for bs in theBestSollution:
            powers.append(bs.power)
        counter = 0
        for bs in self.bs:
            bs.power = powers[counter]
            counter = counter + 1
        return C_best

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