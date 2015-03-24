__author__ = 'mslabicki'

import matplotlib
matplotlib.use('Agg')

from modules.network import CellularNetwork
from modules import devices

import time
import copy

minTxPower = 10
maxTxPower = 40
minFemtoTxPower = 3
maxFemtoTxPower = 10
initialTemperature = 300
beginningPowerInBS = 10
numberOfIterations = 30
numberOfParallelProcesses = 15


def generateOneTestbed(bs_deployment, bs_number, hex_radius, ue_deployment, ue_number):
    network_ref = CellularNetwork()
    if bs_deployment == "BSGrid":
        if bs_number == 36:
            network_ref.Generator.createhexagonal36BSdeployment(hex_radius)
        if bs_number == 108:
            network_ref.Generator.createhexagonal108BSdeployment(hex_radius)

    # if bs_deployment == "BSHannover":
    #     network_ref.Generator.loadDeploymentFromFile("han_network_processed.csv")

    if ue_deployment == "UEGrid":
        network_ref.Generator.insertUEingrid(ue_number)

    if ue_deployment == "UERandom":
        network_ref.Generator.insertUErandomly(ue_number)

    network_ref.minTxPower = minTxPower
    network_ref.maxTxPower = maxTxPower
    network_ref.minFemtoTxPower = minFemtoTxPower
    network_ref.maxFemtoTxPower = maxFemtoTxPower
    network_ref.initialTemperature = initialTemperature

    return network_ref

def addFemtoCell(network_par, x_pos, y_pos):
    for i in range(3):
        bs = devices.BS()
        bs.x = x_pos
        bs.y = y_pos
        bs.angle = i * 120
        bs.type = "FemtoCell"
        bs.power = minFemtoTxPower
        bs.ID = len(network_par.bs)
        bs.turnedOn = True
        network_par.bs.append(copy.deepcopy(bs))

def doSimulations(network_par, networkname):
    print("Siec z dopasowaniem SA_RR")
    network_par.setSmallestPossiblePowerInAllBS()
    network_par.connectUsersToNearestBS()
    network_par.optimizationFunctionResults = network_par.simulatedAnnaealing_RR_as_CS()
    network_par.connectUsersToTheBestBS()
    network_par.saveNetworkToFile(str(networkname) + "_RR.pickle")
    network_par.Printer.drawHistogramOfUEThroughput(str(networkname) + "_throughput_RR.pdf")
    network_par.Printer.drawHistogramOfSetPowers(str(networkname) + "_powers_RR.pdf")
    network_par.Printer.drawHeatmapWithStuff(str(networkname) + "_network_RR.pdf")

    # print("Siec z dopasowaniem SA_FS")
    # network_par.setSmallestPossiblePowerInAllBS()
    # network_par.connectUsersToNearestBS()
    # network_par.optimizationFunctionResults = network_par.simulatedAnnaealing_FairThroughput_as_CS()
    # network_par.connectUsersToTheBestBS()
    # network_par.saveNetworkToFile(str(networkname) + "_network_FS.pickle")
    # network_par.Printer.drawHistogramOfUEThroughput(str(networkname) + "_throughput_FS.pdf")
    # network_par.Printer.drawHistogramOfSetPowers(str(networkname) + "_powers_FS.pdf")
    # network_par.Printer.drawHeatmapWithStuff(str(networkname) + "_network_FS.pdf")