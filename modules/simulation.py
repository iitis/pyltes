__author__ = 'mslabicki'

import matplotlib
matplotlib.use('Agg')

from modules.network import CellularNetwork
from modules import devices

import copy

minTxPower = 10
maxTxPower = 40
initialTemperature = 300
beginningPowerInBS = 10
numberOfIterations = 30
numberOfParallelProcesses = 15

def addOneBSTower(network_par, x_pos, y_pos):
    for i in range(3):
        bs = devices.BS()
        bs.x = x_pos
        bs.y = y_pos
        bs.angle = i * 120
        bs.ID = len(network_par.bs)
        bs.turnedOn = True
        network_par.bs.append(copy.deepcopy(bs))

def turnOffBSTower(network_par, bs1, bs2, bs3):
    network_par.bs[bs1].turnedOn = False
    network_par.bs[bs2].turnedOn = False
    network_par.bs[bs3].turnedOn = False

def prepareNetwork(networkTopo, bsPos, bsNumber, uePos, ueNumber):
    siec = CellularNetwork()
    siec.setPowerInAllBS(10)
    if bsPos == "BSGrid":
        if bsNumber == 12:
            siec.Generator.createhexagonal12BSdeployment(666)
        if bsNumber == 36:
            siec.Generator.createhexagonal36BSdeployment(666)
    if bsPos == "BSHannover":
        siec.Generator.loadDeploymentFromFile("han_network_processed.csv")

    if uePos == "UEGrid":
        siec.Generator.insertUEingrid(ueNumber)
    if uePos == "UERandom":
        siec.Generator.insertUErandomly(ueNumber)

    if networkTopo == "BSAdded":
        if bsPos == 'BSGrid':
            addOneBSTower(siec, (siec.bs[18].x + siec.bs[15].x)/2, (siec.bs[18].y + siec.bs[15].y)/2)
        if bsPos == 'BSHannover':
            x_new = 191/451 * siec.constraintAreaMaxX
            y_new = 524/752 * siec.constraintAreaMaxY
            addOneBSTower(siec, x_new, y_new)

    if networkTopo == "BSRemoved":
            if bsPos == 'BSGrid':
                turnOffBSTower(siec, 18, 19, 20)
            if bsPos == 'BSHannover':
                turnOffBSTower(siec, 36, 37, 38)
    return siec