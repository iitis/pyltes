from pyltes.network import CellularNetwork

network = CellularNetwork()
network.Generator.create1BSnetwork(1666)

network.Generator.insertUErandomly(20)
network.connectUsersToTheBestBS()

network.Printer.drawHistogramOfUEThroughput("thrHistogram")
network.Printer.drawNetwork(fillMethod="SINR", filename="sinrMap")
