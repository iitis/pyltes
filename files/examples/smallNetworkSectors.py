from pyltes.network import CellularNetwork

network = CellularNetwork()
network.Generator.createHexagonalBSdeployment(1666, numberOfBS=36, omnidirectionalAntennas=False, SFR=False)
network.setPowerInAllBS(40)

network.Generator.insertUErandomly(300)
network.connectUsersToTheBestBS()

network.Printer.drawNetwork(fillMethod="Sectors", filename="36AntSectorsMap")

