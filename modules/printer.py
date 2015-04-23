__author__ = 'Mariusz'

from modules import devices
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import math

class Printer:
    """Class that prints network deployment"""
    def __init__(self,parent):
        self.parent = parent

    def drawNetworkWithCircles(self):
        bs_x_locations = []
        bs_y_locations = []
        for bs in self.parent.bs:
            bs_x_locations.append(bs.x)
            bs_y_locations.append(bs.y)
        ue_x_locations = []
        ue_y_locations = []
        for ue in self.parent.ue:
            ue_x_locations.append(ue.x)
            ue_y_locations.append(ue.y)
        rect1 = plt.Rectangle((0,0), self.parent.constraintAreaMaxX, self.parent.constraintAreaMaxY, color='black', fill=False)
        plt.gca().add_patch(rect1)
        plt.axis('equal')
        for bs in self.parent.bs:
            if bs.ID in [0, 6, 12, 18, 24, 30]:
                circleu = plt.Circle([bs.x, bs.y + self.parent.radius], self.parent.radius, fill=False)
                plt.gca().add_patch(circleu)
                circlel = plt.Circle([bs.x - math.sqrt(3)/2 * self.parent.radius , bs.y - self.parent.radius/2], self.parent.radius, fill=False)
                plt.gca().add_patch(circlel)
                circler = plt.Circle([bs.x + math.sqrt(3)/2 * self.parent.radius , bs.y - self.parent.radius/2], self.parent.radius, fill=False)
                plt.gca().add_patch(circler)
            if bs.ID in [3, 9, 15, 21, 27, 33]:
                circled = plt.Circle([bs.x, bs.y - self.parent.radius], self.parent.radius, fill=False)
                plt.gca().add_patch(circled)
                circlel = plt.Circle([bs.x - math.sqrt(3)/2 * self.parent.radius , bs.y + self.parent.radius/2], self.parent.radius, fill=False)
                plt.gca().add_patch(circlel)
                circler = plt.Circle([bs.x + math.sqrt(3)/2 * self.parent.radius , bs.y + self.parent.radius/2], self.parent.radius, fill=False)
                plt.gca().add_patch(circler)
        plt.plot(bs_x_locations, bs_y_locations, 'r^', ue_x_locations, ue_y_locations, 'b*', markersize=10)
        plt.axis([0, self.parent.constraintAreaMaxX, 0, self.parent.constraintAreaMaxY])
        plt.show()

    def drawNetworkWithConnections(self):
        bs_x_locations = []
        bs_y_locations = []
        for bs in self.parent.bs:
            bs_x_locations.append(bs.x)
            bs_y_locations.append(bs.y)
        ue_x_locations = []
        ue_y_locations = []
        for ue in self.parent.ue:
            ue_x_locations.append(ue.x)
            ue_y_locations.append(ue.y)
        rect1 = plt.Rectangle((0,0), self.parent.constraintAreaMaxX, self.parent.constraintAreaMaxY, color='black', fill=False)
        plt.gca().add_patch(rect1)
        plt.axis('equal')
        for ue in self.parent.ue:
            plt.arrow(ue.x, ue.y, self.parent.bs[ue.connectedToBS].x - ue.x, self.parent.bs[ue.connectedToBS].y - ue.y)
        plt.plot(bs_x_locations, bs_y_locations, 'r^', ue_x_locations, ue_y_locations, 'b*', markersize=10)
        plt.axis([0, self.parent.constraintAreaMaxX, 0, self.parent.constraintAreaMaxY])
        plt.show()

    def drawRSSIHeatmap(self):
        bs_x_locations = []
        bs_y_locations = []
        for bs in self.parent.bs:
            bs_x_locations.append(bs.x)
            bs_y_locations.append(bs.y)
        ue_x_locations = []
        ue_y_locations = []
        for ue in self.parent.ue:
            ue_x_locations.append(ue.x)
            ue_y_locations.append(ue.y)
        rect1 = plt.Rectangle((0,0), self.parent.constraintAreaMaxX, self.parent.constraintAreaMaxY, color='black', fill=False)
        plt.gca().add_patch(rect1)
        plt.axis('equal')
        for ue in self.parent.ue:
            plt.arrow(ue.x, ue.y, self.parent.bs[ue.connectedToBS].x - ue.x, self.parent.bs[ue.connectedToBS].y - ue.y)
        plt.plot(bs_x_locations, bs_y_locations, 'r^', ue_x_locations, ue_y_locations, 'b*', markersize=10)
        plt.axis([0, self.parent.constraintAreaMaxX, 0, self.parent.constraintAreaMaxY])
        plt.show()

    def drawNetworkWithCirclesAndConnections(self):
        bs_x_locations = []
        bs_y_locations = []
        for bs in self.parent.bs:
            bs_x_locations.append(bs.x)
            bs_y_locations.append(bs.y)
        ue_x_locations = []
        ue_y_locations = []
        for ue in self.parent.ue:
            ue_x_locations.append(ue.x)
            ue_y_locations.append(ue.y)
        rect1 = plt.Rectangle((0,0), self.parent.constraintAreaMaxX, self.parent.constraintAreaMaxY, color='black', fill=False)
        plt.gca().add_patch(rect1)
        plt.axis('equal')
        for bs in self.parent.bs:
            if bs.ID in [0, 6, 12, 18, 24, 30]:
                circleu = plt.Circle([bs.x, bs.y + self.parent.radius], self.parent.radius, fill=False)
                plt.gca().add_patch(circleu)
                circlel = plt.Circle([bs.x - math.sqrt(3)/2 * self.parent.radius , bs.y - self.parent.radius/2], self.parent.radius, fill=False)
                plt.gca().add_patch(circlel)
                circler = plt.Circle([bs.x + math.sqrt(3)/2 * self.parent.radius , bs.y - self.parent.radius/2], self.parent.radius, fill=False)
                plt.gca().add_patch(circler)
            if bs.ID in [3, 9, 15, 21, 27, 33]:
                circled = plt.Circle([bs.x, bs.y - self.parent.radius], self.parent.radius, fill=False)
                plt.gca().add_patch(circled)
                circlel = plt.Circle([bs.x - math.sqrt(3)/2 * self.parent.radius , bs.y + self.parent.radius/2], self.parent.radius, fill=False)
                plt.gca().add_patch(circlel)
                circler = plt.Circle([bs.x + math.sqrt(3)/2 * self.parent.radius , bs.y + self.parent.radius/2], self.parent.radius, fill=False)
                plt.gca().add_patch(circler)
        for ue in self.parent.ue:
            plt.arrow(ue.x, ue.y, self.parent.bs[ue.connectedToBS].x - ue.x, self.parent.bs[ue.connectedToBS].y - ue.y)
        plt.plot(bs_x_locations, bs_y_locations, 'r^', ue_x_locations, ue_y_locations, 'b*', markersize=10)
        plt.axis([0, self.parent.constraintAreaMaxX, 0, self.parent.constraintAreaMaxY])
        plt.show()

    def drawNetworkWithArrows(self):
        bs_x_locations = []
        bs_y_locations = []
        for bs in self.parent.bs:
            bs_x_locations.append(bs.x)
            bs_y_locations.append(bs.y)
        ue_x_locations = []
        ue_y_locations = []
        plt.figure(1, figsize=(8, 8))
        for ue in self.parent.ue:
            ue_x_locations.append(ue.x)
            ue_y_locations.append(ue.y)
        rect1 = plt.Rectangle((0,0), self.parent.constraintAreaMaxX, self.parent.constraintAreaMaxY, color='black', fill=False)
        plt.gca().add_patch(rect1)
        plt.axis('equal')
        for bs in self.parent.bs:
            if bs.ID in [0, 6, 12, 18, 24, 30]:
                #circleu = plt.Circle([bs.x, bs.y + self.parent.radius], self.parent.radius, fill=False)
                #plt.gca().add_patch(circleu)
                arrowd = plt.arrow(bs.x, bs.y, 0, -self.parent.radius, linestyle="dotted")
                plt.gca().add_patch(arrowd)
                arrowl = plt.arrow(bs.x, bs.y, -math.sqrt(3)/2 * self.parent.radius , self.parent.radius/2, linestyle="dotted")
                plt.gca().add_patch(arrowl)
                arrowp = plt.arrow(bs.x, bs.y, +math.sqrt(3)/2 * self.parent.radius , self.parent.radius/2, linestyle="dotted")
                plt.gca().add_patch(arrowp)
            if bs.ID in [3, 9, 15, 21, 27, 33]:
                arrowu = plt.arrow(bs.x, bs.y, 0, self.parent.radius, linestyle="dotted")
                plt.gca().add_patch(arrowu)
                arrowl = plt.arrow(bs.x, bs.y, -math.sqrt(3)/2 * self.parent.radius , -self.parent.radius/2, linestyle="dotted")
                plt.gca().add_patch(arrowl)
                arrowp = plt.arrow(bs.x, bs.y, +math.sqrt(3)/2 * self.parent.radius , -self.parent.radius/2, linestyle="dotted")
                plt.gca().add_patch(arrowp)
        # for ue in self.parent.ue:
        #     plt.arrow(ue.x, ue.y, self.parent.bs[ue.connectedToBS].x - ue.x, self.parent.bs[ue.connectedToBS].y - ue.y)
        plt.plot(bs_x_locations, bs_y_locations, 'r^', ue_x_locations, ue_y_locations, 'b*', markersize=10)
        plt.axis([0, self.parent.constraintAreaMaxX, 0, self.parent.constraintAreaMaxY])
        #plt.show()
        return plt

    def drawHeatmap(self):
        color_table = []
        for i in range(36):
            color_table.append([255/(i+1), 255/(i+1), 255/(i+1)])
        ue = devices.UE()
        x_list = []
        y_list = []
        color_list = []
        cm = plt.cm.get_cmap('RdYlBu')
        for x in range(0, round(self.parent.constraintAreaMaxX), 50):
            for y in range(0, round(self.parent.constraintAreaMaxY), 50):
                RSSI_best = -1000
                BS_best = -1
                for bs in self.parent.bs:
                    ue.x = x
                    ue.y = y
                    if ue.isSeenFromBS(bs) == False:
                        continue
                    ue.connectedToBS = bs.ID
                    temp_RSSI = ue.calculateSINR(self.parent.bs)
                    if temp_RSSI > RSSI_best:
                        RSSI_best = temp_RSSI
                        BS_best = bs.ID
                x_list.append(x)
                y_list.append(y)
                color_list.append(BS_best)
        plt.scatter(x_list, y_list, c=color_list, cmap=cm, s=30, marker = "8", linewidths=0)

    def returnFig(self):
        bs_x_locations = []
        bs_y_locations = []
        for bs in self.bs:
            bs_x_locations.append(bs.x)
            bs_y_locations.append(bs.y)
        ue_x_locations = []
        ue_y_locations = []
        for ue in self.ue:
            ue_x_locations.append(ue.x)
            ue_y_locations.append(ue.y)
        rect1 = plt.Rectangle((0,0), self.constraintAreaMaxX, self.constraintAreaMaxY, color='black', fill=False)
        main_draw = plt.figure()
        main_draw.gca().add_patch(rect1)
        ax = plt.axis('equal')
        for bs in self.bs:
            if bs.ID in [0, 6, 12, 18, 24, 30]:
                circleu = plt.Circle([bs.x, bs.y + self.radius], self.radius, fill=False)
                main_draw.gca().add_patch(circleu)
                circlel = plt.Circle([bs.x - math.sqrt(3)/2 * self.radius , bs.y - self.radius/2], self.radius, fill=False)
                main_draw.gca().add_patch(circlel)
                circler = plt.Circle([bs.x + math.sqrt(3)/2 * self.radius , bs.y - self.radius/2], self.radius, fill=False)
                main_draw.gca().add_patch(circler)
            if bs.ID in [3, 9, 15, 21, 27, 33]:
                circled = plt.Circle([bs.x, bs.y - self.radius], self.radius, fill=False)
                main_draw.gca().add_patch(circled)
                circlel = plt.Circle([bs.x - math.sqrt(3)/2 * self.radius , bs.y + self.radius/2], self.radius, fill=False)
                main_draw.gca().add_patch(circlel)
                circler = plt.Circle([bs.x + math.sqrt(3)/2 * self.radius , bs.y + self.radius/2], self.radius, fill=False)
                main_draw.gca().add_patch(circler)
        for ue in self.ue:
            arrow = plt.arrow(ue.x, ue.y, self.bs[ue.connectedToBS].x - ue.x, self.bs[ue.connectedToBS].y - ue.y)
            main_draw.gca().add_patch(arrow)
        plt.plot(bs_x_locations, bs_y_locations, 'r^', ue_x_locations, ue_y_locations, 'b*', markersize=10)
        plt.axis([0, self.constraintAreaMaxX, 0, self.constraintAreaMaxY])
        return main_draw

    def returnHeatmapWithStuff(self):
        color_table = []
        for i in range(len(self.parent.bs)):
            color_table.append([255/(i+1), 255/(i+1), 255/(i+1)])
        ue = devices.UE()
        x_list = []
        y_list = []
        color_list = []
        cm = plt.cm.get_cmap('Spectral')
        main_draw = plt.figure(1, figsize=(8, 8))
        ax = main_draw.add_subplot(111)
        for x in range(0, round(self.parent.constraintAreaMaxX), 15):
            for y in range(0, round(self.parent.constraintAreaMaxY), 15):
                RSSI_best = -1000
                BS_best = -1
                for bs in self.parent.bs:
                    ue.x = x
                    ue.y = y
                    if ue.isSeenFromBS(bs) == False:
                        continue
                    ue.connectedToBS = bs.ID
                    temp_RSSI = ue.calculateSINR(self.parent.bs)
                    if temp_RSSI > RSSI_best:
                        RSSI_best = temp_RSSI
                        BS_best = bs.ID
                x_list.append(x)
                y_list.append(y)
                color_list.append(BS_best)
        ax.scatter(x_list, y_list, c=color_list, cmap=cm, s=14, marker = "s", edgecolors='None')
        bs_x_locations = []
        bs_y_locations = []
        for bs in self.parent.bs:
            bs_x_locations.append(bs.x)
            bs_y_locations.append(bs.y)
        ue_x_locations = []
        ue_y_locations = []
        for ue in self.parent.ue:
            ue_x_locations.append(ue.x)
            ue_y_locations.append(ue.y)
        rect1 = plt.Rectangle((0,0), self.parent.constraintAreaMaxX, self.parent.constraintAreaMaxY, color='black', fill=False)
        ax.add_patch(rect1)
        ax.axis('equal')
        for ue in self.parent.ue:
            ax.arrow(ue.x, ue.y, self.parent.bs[ue.connectedToBS].x - ue.x, self.parent.bs[ue.connectedToBS].y - ue.y)
        ax.plot(bs_x_locations, bs_y_locations, 'r^', ue_x_locations, ue_y_locations, 'b*', color="black", markersize=10)
        ax.axis([0, self.parent.constraintAreaMaxX, 0, self.parent.constraintAreaMaxY])
        ax.axis('off')
        return main_draw

    def drawHistogramOfUEThroughput(self, filename):
        thr_vector = self.parent.returnRealUEThroughputVectorRR()
        thr_MBit = [x / (1024*1024) for x in thr_vector]
        plt.hist(thr_MBit, bins=np.arange(0, (25 + 1), 0.25))
        plt.xlim(0, 25)
        # plt.savefig(filename, format="pdf", dpi=300)
        plt.savefig(filename+".png", format="png", dpi=300)
        plt.clf()

    def drawHistogramOfSetPowers(self, filename):
        power_vector = []
        for bs in self.parent.bs:
            power_vector.append(bs.outsidePower)
        plt.hist(power_vector, bins=np.arange(self.parent.minFemtoTxPower, self.parent.maxTxPower + 1, 1))
        plt.xlim(0, 100)
        # plt.savefig(filename, format="pdf", dpi=300)
        plt.savefig(filename+".png", format="png", dpi=300)
        plt.clf()

    def drawHeatmapWithStuff(self, filename):
        color_table = []
        for i in range(len(self.parent.bs)):
            color_table.append([255/(i+1), 255/(i+1), 255/(i+1)])
        ue = devices.UE()
        x_list = []
        y_list = []
        color_list = []
        cm = plt.cm.get_cmap('Spectral')
        main_draw = plt.figure(1, figsize=(8, 8))
        ax = main_draw.add_subplot(111)
        for x in range(0, round(self.parent.constraintAreaMaxX), round(self.parent.constraintAreaMaxX/200)):
            for y in range(0, round(self.parent.constraintAreaMaxY), round(self.parent.constraintAreaMaxY/200)):
                RSSI_best = -1000
                BS_best = -1
                for bs in self.parent.bs:
                    ue.x = x
                    ue.y = y
                    if ue.isSeenFromBS(bs) == False:
                        continue
                    ue.connectedToBS = bs.ID
                    temp_RSSI = ue.calculateSINR(self.parent.bs)
                    if temp_RSSI > RSSI_best:
                        RSSI_best = temp_RSSI
                        BS_best = bs.ID
                x_list.append(x)
                y_list.append(y)
                color_list.append(BS_best)
        ax.scatter(x_list, y_list, c=color_list, cmap=cm, s=14, marker = "s", edgecolors='None')
        bs_x_locations = []
        bs_y_locations = []
        for bs in self.parent.bs:
            bs_x_locations.append(bs.x)
            bs_y_locations.append(bs.y)
        ue_x_locations = []
        ue_y_locations = []
        for ue in self.parent.ue:
            ue_x_locations.append(ue.x)
            ue_y_locations.append(ue.y)
        rect1 = plt.Rectangle((0,0), self.parent.constraintAreaMaxX, self.parent.constraintAreaMaxY, color='black', fill=False)
        ax.add_patch(rect1)
        ax.axis('equal')
        for ue in self.parent.ue:
            ax.arrow(ue.x, ue.y, self.parent.bs[ue.connectedToBS].x - ue.x, self.parent.bs[ue.connectedToBS].y - ue.y)
        ax.plot(bs_x_locations, bs_y_locations, 'r^', ue_x_locations, ue_y_locations, 'b*', color="black", markersize=10)
        ax.axis([0, self.parent.constraintAreaMaxX, 0, self.parent.constraintAreaMaxY])
        ax.axis('off')
        # main_draw.savefig(filename, format="pdf", dpi=300)
        main_draw.savefig(filename+".png", format="png", dpi=300)
        plt.clf()

    def drawSINRHeatmap(self, filename, nodenumber):
        color_table = []
        for i in range(len(self.parent.bs)):
            color_table.append([255/(i+1), 255/(i+1), 255/(i+1)])
        ue = devices.UE()
        x_list = []
        y_list = []
        color_list = []
        cm = plt.cm.get_cmap('Spectral')
        #cm = plt.cm.get_cmap('Paired')
        # cm = plt.cm.get_cmap('binary')
        main_draw = plt.figure(1, figsize=(8, 8))
        ax = main_draw.add_subplot(111)
        for x in range(0, round(self.parent.constraintAreaMaxX), 15):
            for y in range(0, round(self.parent.constraintAreaMaxY), 15):
                ue.x = x
                ue.y = y
                ue.connectedToBS = nodenumber
                SINR = ue.calculateSINR(self.parent.bs)
                x_list.append(x)
                y_list.append(y)
                color_list.append(SINR)
        scatter = ax.scatter(x_list, y_list, c=color_list, cmap=cm, s=15, marker = "s", edgecolors='None')
        bs_x_locations = []
        bs_y_locations = []
        for bs in self.parent.bs:
            bs_x_locations.append(bs.x)
            bs_y_locations.append(bs.y)
        rect1 = plt.Rectangle((0,0), self.parent.constraintAreaMaxX, self.parent.constraintAreaMaxY, color='black', fill=False)
        ax.add_patch(rect1)
        ax.axis('equal')
        ax.plot(bs_x_locations, bs_y_locations, 'r^', color="black", markersize=4)
        ax.axis([0, self.parent.constraintAreaMaxX, 0, self.parent.constraintAreaMaxY])
        ax.axis('off')

        cbar = plt.colorbar(scatter)
        #cbar.set_clim(-60, 50)
        #cbar.ax.set_yticklabels(['0','1','2','>3'])
        #cbar.set_label('# of contacts', rotation=270)
        # main_draw.savefig(filename+".pdf", format="pdf", dpi=300)
        main_draw.savefig(filename+".png", format="png", dpi=300)
        plt.clf()

    def drawSINRHeatmapAroundBS(self, filename, nodeNumber, drawingSize = 15):
        color_table = []
        for i in range(len(self.parent.bs)):
            color_table.append([255/(i+1), 255/(i+1), 255/(i+1)])
        ue = devices.UE()
        x_list = []
        y_list = []
        color_list = []
        cm = plt.cm.get_cmap('Spectral')
        #cm = plt.cm.get_cmap('Paired')
        # cm = plt.cm.get_cmap('binary')
        main_draw = plt.figure(1, figsize=(8, 8))
        ax = main_draw.add_subplot(111)
        for x in range(0, round(self.parent.constraintAreaMaxX), drawingSize):
            for y in range(0, round(self.parent.constraintAreaMaxY), drawingSize):
                ue.x = x
                ue.y = y
                ue.connectedToBS = nodeNumber
                SINR = ue.calculateSINR(self.parent.bs, self.parent.obstacles)
                x_list.append(x)
                y_list.append(y)
                color_list.append(SINR)
        scatter = ax.scatter(x_list, y_list, c=color_list, cmap=cm, s=15, marker = "s", edgecolors='None')
        bs_x_locations = []
        bs_y_locations = []
        for bs in self.parent.bs:
            bs_x_locations.append(bs.x)
            bs_y_locations.append(bs.y)
        rect1 = plt.Rectangle((0,0), self.parent.constraintAreaMaxX, self.parent.constraintAreaMaxY, color='black', fill=False)
        ax.add_patch(rect1)
        ax.axis('equal')
        for obstacle in self.parent.obstacles:
            ax.arrow(obstacle[0], obstacle[1], obstacle[2] - obstacle[0], obstacle[3] - obstacle[1])
        ax.plot(bs_x_locations, bs_y_locations, 'r^', color="black", markersize=4)
        ax.axis([0, self.parent.constraintAreaMaxX, 0, self.parent.constraintAreaMaxY])
        ax.axis('off')

        cbar = plt.colorbar(scatter)
        #cbar.set_clim(-60, 50)
        #cbar.ax.set_yticklabels(['0','1','2','>3'])
        #cbar.set_label('# of contacts', rotation=270)
        # main_draw.savefig(filename+".pdf", format="pdf", dpi=300)
        main_draw.savefig(filename+".png", format="png", dpi=300)
        plt.clf()

    def drawBitrateHeatmap(self, filename, nodenumber):
        color_table = []
        for i in range(len(self.parent.bs)):
            color_table.append([255/(i+1), 255/(i+1), 255/(i+1)])
        ue = devices.UE()
        x_list = []
        y_list = []
        color_list = []
        cm = plt.cm.get_cmap('Spectral')
        # cm = plt.cm.get_cmap('Paired')
        # cm = plt.cm.get_cmap('binary')
        #cm = plt.cm.get_cmap('prism')
        main_draw = plt.figure(1, figsize=(8, 8))
        ax = main_draw.add_subplot(111)
        for x in range(0, round(self.parent.constraintAreaMaxX), 25):
            for y in range(0, round(self.parent.constraintAreaMaxY), 25):
                ue.x = x
                ue.y = y
                ue.connectedToBS = nodenumber
                bitrate = ue.calculateMaxThroughputOfTheNode(self.parent.bs)
                x_list.append(x)
                y_list.append(y)
                color_list.append(bitrate/8/1024/1024)
        scatter = ax.scatter(x_list, y_list, c=color_list, cmap=cm, s=50, marker = "s", edgecolors='None')
        bs_x_locations = []
        bs_y_locations = []
        for bs in self.parent.bs:
            bs_x_locations.append(bs.x)
            bs_y_locations.append(bs.y)
        rect1 = plt.Rectangle((0,0), self.parent.constraintAreaMaxX, self.parent.constraintAreaMaxY, color='black', fill=False)
        ax.add_patch(rect1)
        ax.axis('equal')
        ax.plot(bs_x_locations, bs_y_locations, 'r^', color="black", markersize=4)
        ax.axis([0, self.parent.constraintAreaMaxX, 0, self.parent.constraintAreaMaxY])
        ax.axis('off')

        cbar = plt.colorbar(scatter)
        #cbar.set_clim(0, 20)
        # main_draw.savefig(filename+".pdf", format="pdf", dpi=300)
        main_draw.savefig(filename+".png", format="png", dpi=300)
        plt.clf()

    def drawSINRcut(self, filename, nodenumber):
        ue = devices.UE()
        x_list = []
        y_list = []
        color_list = []
        #cm = plt.cm.get_cmap('Spectral')
        #cm = plt.cm.get_cmap('Paired')
        cm = plt.cm.get_cmap('binary')
        #cm = plt.cm.get_cmap('prism')
        main_draw = plt.figure(1, figsize=(16, 8))
        ax = main_draw.add_subplot(111)
        y = self.parent.constraintAreaMaxY/2
        for x in range(0, round(self.parent.constraintAreaMaxX), 1):
            ue.x = x
            ue.y = y
            ue.connectedToBS = nodenumber
            SINR = ue.calculateSINR(self.parent.bs)
            x_list.append(x)
            y_list.append(y)
            color_list.append(SINR)
        ax.plot(x_list, color_list)
        main_draw.savefig(filename+".pdf", format="pdf", dpi=300)
        main_draw.savefig(filename+".png", format="png", dpi=300)
        plt.clf()

    def drawBitratecut(self, filename, nodenumber):
        ue = devices.UE()
        x_list = []
        y_list = []
        color_list = []
        #cm = plt.cm.get_cmap('Spectral')
        #cm = plt.cm.get_cmap('Paired')
        cm = plt.cm.get_cmap('binary')
        #cm = plt.cm.get_cmap('prism')
        main_draw = plt.figure(1, figsize=(16, 8))
        ax = main_draw.add_subplot(111)
        y = self.parent.constraintAreaMaxY/2
        for x in range(0, round(self.parent.constraintAreaMaxX), 1):
            ue.x = x
            ue.y = y
            ue.connectedToBS = nodenumber
            thr = ue.calculateMaxThroughputOfTheNode(self.parent.bs)/8/1024/1024
            x_list.append(x)
            y_list.append(thr)
        ax.plot(x_list, y_list)
        main_draw.savefig(filename+".pdf", format="pdf", dpi=300)
        main_draw.savefig(filename+".png", format="png", dpi=300)
        plt.clf()

    def drawBSHex(self, filename, nodenumber):
        color_table = []
        for i in range(len(self.parent.bs)):
            color_table.append([255/(i+1), 255/(i+1), 255/(i+1)])
        ue = devices.UE()
        x_list_internal = []
        y_list_internal = []
        x_list_external = []
        y_list_external = []
        color_list = []
        #cm = plt.cm.get_cmap('Spectral')
        #cm = plt.cm.get_cmap('Paired')
        cm = plt.cm.get_cmap('binary')
        #cm = plt.cm.get_cmap('prism')
        main_draw = plt.figure(1, figsize=(8, 8))
        ax = main_draw.add_subplot(111)
        for x in range(0, round(self.parent.constraintAreaMaxX), 25):
            for y in range(0, round(self.parent.constraintAreaMaxY), 25):
                ue.x = x
                ue.y = y
                ue.connectToNearestBS(self.parent.bs)
                if ue.connectedToBS == nodenumber:
                    if ue.distanceToBS(self.parent.bs[nodenumber]) < self.parent.bs[nodenumber].mi * self.parent.bs[nodenumber].Rc:
                        x_list_internal.append(x)
                        y_list_internal.append(y)
                    else:
                        x_list_external.append(x)
                        y_list_external.append(y)
        ax.scatter(x_list_internal, y_list_internal, s = 1, color='blue')
        ax.scatter(x_list_external, y_list_external, s = 1, color='red')
        rect1 = plt.Rectangle((0,0), self.parent.constraintAreaMaxX, self.parent.constraintAreaMaxY, color='black', fill=False)
        ax.add_patch(rect1)
        ax.axis('equal')
        ax.axis([0, self.parent.constraintAreaMaxX, 0, self.parent.constraintAreaMaxY])
        ax.axis('off')

        # main_draw.savefig(filename+".pdf", format="pdf", dpi=300)
        main_draw.savefig(filename+".png", format="png", dpi=300)
        plt.clf()

    def drawNearestBsSINRHeatmap(self, filename):
        color_table = []
        for i in range(len(self.parent.bs)):
            color_table.append([255/(i+1), 255/(i+1), 255/(i+1)])
        ue = devices.UE(self.parent)
        x_list = []
        y_list = []
        color_list = []
        in_x_list = []
        in_y_list = []
        out_x_list = []
        out_y_list = []
        cm = plt.cm.get_cmap('Spectral')
        main_draw = plt.figure(1, figsize=(8, 8))
        ax = main_draw.add_subplot(111)

        for x in range(0, round(self.parent.constraintAreaMaxX), 15):
            for y in range(0, round(self.parent.constraintAreaMaxY), 15):
                ue.x = x
                ue.y = y
                ue.connectToNearestBS(self.parent.bs)
                SINR = ue.calculateSINR(self.parent.bs)
                x_list.append(x)
                y_list.append(y)
                color_list.append(SINR)
                if (ue.inside==True):
                    in_x_list.append(x)
                    in_y_list.append(y)
                if (ue.inside==False):
                    out_x_list.append(x)
                    out_y_list.append(y)
        scatter = ax.scatter(x_list, y_list, c=color_list, cmap=cm, s=15, marker="s", edgecolors='None')

        bs_x_locations = []
        bs_y_locations = []
        for bs in self.parent.bs:
            bs_x_locations.append(bs.x)
            bs_y_locations.append(bs.y)
        rect1 = plt.Rectangle((0,0), self.parent.constraintAreaMaxX, self.parent.constraintAreaMaxY, color='black', fill=False)
        ax.add_patch(rect1)
        ax.axis('equal')
        ax.plot(bs_x_locations, bs_y_locations, 'r^', color="black", markersize=4)
        ax.axis([0, self.parent.constraintAreaMaxX, 0, self.parent.constraintAreaMaxY])
        ax.axis('off')

        cbar = plt.colorbar(scatter)
        #cbar.set_clim(-60, 50)
        #cbar.ax.set_yticklabels(['0','1','2','>3'])
        #cbar.set_label('# of contacts', rotation=270)
        # main_draw.savefig(filename+".pdf", format="pdf", dpi=300)
        main_draw.savefig(filename+".png", format="png", dpi=300)
        plt.clf()

        # cm = plt.cm.get_cmap('brg')
        main_draw = plt.figure(1, figsize=(8, 8))
        ax = main_draw.add_subplot(111)
        # ax.scatter(x_list, y_list, c=inout_list, cmap=cm, s=15, marker="s", edgecolors='None')

        ax.scatter(in_x_list, in_y_list, s=1, color="red")
        ax.scatter(out_x_list, out_y_list, s=1, color="blue")

        rect1 = plt.Rectangle((0,0), self.parent.constraintAreaMaxX, self.parent.constraintAreaMaxY, color='black', fill=False)
        ax.add_patch(rect1)
        ax.axis('equal')
        ax.plot(bs_x_locations, bs_y_locations, 'r^', color="black", markersize=4)
        ax.axis([0, self.parent.constraintAreaMaxX, 0, self.parent.constraintAreaMaxY])
        ax.axis('off')
        main_draw.savefig("helper_"+filename+".png", format="png", dpi=300)
        plt.clf()

    

    def drawStrongestBsSINRHeatmap(self, filename):
        color_table = []
        for i in range(len(self.parent.bs)):
            color_table.append([255/(i+1), 255/(i+1), 255/(i+1)])
        ue = devices.UE()
        x_list = []
        y_list = []
        color_list = []
        cm = plt.cm.get_cmap('Spectral')
        #cm = plt.cm.get_cmap('Paired')
        # cm = plt.cm.get_cmap('binary')
        main_draw = plt.figure(1, figsize=(8, 8))
        ax = main_draw.add_subplot(111)
        for x in range(0, round(self.parent.constraintAreaMaxX), 15):
            for y in range(0, round(self.parent.constraintAreaMaxY), 15):
                ue.x = x
                ue.y = y
                ue.connectToTheBestBS(self.parent.bs)
                SINR = ue.calculateSINR(self.parent.bs)
                x_list.append(x)
                y_list.append(y)
                color_list.append(SINR)
        scatter = ax.scatter(x_list, y_list, c=color_list, cmap=cm, s=15, marker = "s", edgecolors='None')
        bs_x_locations = []
        bs_y_locations = []
        for bs in self.parent.bs:
            bs_x_locations.append(bs.x)
            bs_y_locations.append(bs.y)
        rect1 = plt.Rectangle((0,0), self.parent.constraintAreaMaxX, self.parent.constraintAreaMaxY, color='black', fill=False)
        ax.add_patch(rect1)
        ax.axis('equal')
        ax.plot(bs_x_locations, bs_y_locations, 'r^', color="black", markersize=4)
        ax.axis([0, self.parent.constraintAreaMaxX, 0, self.parent.constraintAreaMaxY])
        ax.axis('off')

        cbar = plt.colorbar(scatter)
        #cbar.set_clim(-60, 50)
        #cbar.ax.set_yticklabels(['0','1','2','>3'])
        #cbar.set_label('# of contacts', rotation=270)
        # main_draw.savefig(filename+".pdf", format="pdf", dpi=300)
        main_draw.savefig(filename+".png", format="png", dpi=300)
        plt.clf()

    def drawNetworkWithColors(self, filename):
        main_draw = plt.figure(1, figsize=(8, 8))
        ax = main_draw.add_subplot(111)
        rect = plt.Rectangle((0,0), self.parent.constraintAreaMaxX, self.parent.constraintAreaMaxY, color='black', fill=False)
        ax.add_patch(rect)
        for bs in self.parent.bs:
            # ax.scatter(bs.x, bs.y, s=13, color="black")
            if (bs.color==1):
                c="red"
            elif (bs.color==2):
                c="green"
            else:
                c="blue"
            circle = plt.Circle([bs.x, bs.y], bs.Rc*0.5, fill=c, color=c, linewidth=3)
            ax.add_patch(circle)

            circle = plt.Circle([bs.x, bs.y], bs.Rc, fill=False, color="grey", linewidth=0.1)
            ax.add_patch(circle)

            circle = plt.Circle([bs.x, bs.y], bs.Rc*0.05, fill="black", color="black", linewidth=0.1)
            ax.add_patch(circle)
            # ax.scatter(bs.x, bs.y, s=13, color="black")
        ax.axis('equal')
        ax.axis([0, self.parent.constraintAreaMaxX, 0, self.parent.constraintAreaMaxY])
        ax.axis('off')
        main_draw.savefig(filename+".png", format="png", dpi=300)
        plt.clf()

    def drawNetworkColorsMap(self, filename):
        main_draw = plt.figure(1, figsize=(8, 8))
        ax = main_draw.add_subplot(111)
        rect = plt.Rectangle((0,0), self.parent.constraintAreaMaxX, self.parent.constraintAreaMaxY, color='black', fill=False)
        ax.add_patch(rect)
        ue = devices.UE()
        for x in range(0, round(self.parent.constraintAreaMaxX), 30):
            for y in range(0, round(self.parent.constraintAreaMaxY), 30):
                ue.x = x
                ue.y = y
                ue.connectToTheBestBS(self.parent.bs)
                bsColor = self.parent.bs[ue.connectedToBS].color
                if (bsColor==1):
                    c="red"
                elif (bsColor==2):
                    c="green"
                else:
                    c="blue"
                ax.scatter(ue.x, ue.y, s=10, color=c)
        ax.axis('equal')
        ax.axis([0, self.parent.constraintAreaMaxX, 0, self.parent.constraintAreaMaxY])
        ax.axis('off')
        main_draw.savefig(filename+".png", format="png", dpi=300)
        plt.clf()