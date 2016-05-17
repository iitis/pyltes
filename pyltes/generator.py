__author__ = 'Mariusz Slabicki, Konrad Połys'

import math
import csv
import random
from pyltes import devices

class Generator:
    """Class that generates network deployment"""
    def __init__(self,parent):
        self.parent = parent

    def create1BSnetwork(self, radius):
        H_hex = 2 * radius
        W_hex = radius * math.sqrt(3)
        self.parent.radius = radius
        self.parent.constraintAreaMaxX = 2 * W_hex
        self.parent.constraintAreaMaxY = H_hex + 1.5 * radius
        bs = devices.BS()
        bs.ID = 0
        bs.turnedOn = True
        bs.x = self.parent.constraintAreaMaxX/2
        bs.y = self.parent.constraintAreaMaxY/2
        self.parent.bs.append(bs)


    def createHexagonalBSdeployment(self, radius, numberOfBS = 36, omnidirectionalAntennas = False, SFR = False):
        d_x = math.sqrt(3)/2 * radius
        d_y = radius/2
        H_hex = 2 * radius
        W_hex = radius * math.sqrt(3)
        self.parent.radius = radius
        if numberOfBS == 36:
            self.parent.constraintAreaMaxX = 6.5 * W_hex
            self.parent.constraintAreaMaxY = 3 * H_hex + 3.5 * radius
        if numberOfBS == 75:
            self.parent.constraintAreaMaxX = 8 * W_hex
            self.parent.constraintAreaMaxY = 4 * H_hex + 7.5 * radius
        if numberOfBS == 90:
            self.parent.constraintAreaMaxX = 9.5 * W_hex
            self.parent.constraintAreaMaxY = 4 * H_hex + 7.5 * radius
        if numberOfBS == 108:
            self.parent.constraintAreaMaxX = 9.5 * W_hex
            self.parent.constraintAreaMaxY = 6 * H_hex + 6.5 * radius
        for i in range(0, numberOfBS):
            bs = devices.BS()
            bs.ID = i
            bs.turnedOn = True
            self.omnidirectionalAntenna = omnidirectionalAntennas
            self.useSFR = SFR
            self.parent.bs.append(bs)

        if numberOfBS == 36:
            numberOfRows = 3
            numberOfColumns = 4
            multiplier = 12
        if numberOfBS == 75:
            numberOfRows = 5
            numberOfColumns = 5
            multiplier = 15
        if numberOfBS == 90:
            numberOfRows = 5
            numberOfColumns = 6
            multiplier = 18
        if numberOfBS == 108:
            numberOfRows = 6
            numberOfColumns = 6
            multiplier = 18

        for row_number in range(0, numberOfRows):
            for column_number  in range(0, numberOfColumns):
                for sector_nb in range(0, 3):
                    self.parent.bs[multiplier*row_number + 3*column_number + sector_nb].x = (3*(column_number+1)-1) * d_x
                    self.parent.bs[multiplier*row_number + 3*column_number + sector_nb].y = (1 + row_number) * H_hex - d_y + row_number * radius
                    self.parent.bs[multiplier*row_number + 3*column_number + sector_nb].angle = sector_nb * 120
                    if column_number % 2 == 1:
                        self.parent.bs[multiplier*row_number + 3*column_number + sector_nb].x = (3*(column_number+1)-1) * d_x
                        self.parent.bs[multiplier*row_number + 3*column_number + sector_nb].y += d_y
                        self.parent.bs[multiplier*row_number + 3*column_number + sector_nb].angle += 60

    def loadDeploymentFromFile(self, filename):
        self.parent.constraintAreaMaxX = 3000
        self.parent.constraintAreaMaxY = 5000
        network = csv.reader(open(filename), delimiter=';', quotechar='|')
        bs_number = 0
        for row in network:
            bs = devices.BS()
            bs.x = float(row[1])
            bs.y = float(row[2])
            bs.x = bs.x - 8500
            bs.y = bs.y - 11000
            bs.ID = bs_number
            bs_number +=1
            bs.angle = float(row[4])
            bs.turnedOn = True
            if (len(row)>12):
                bs.color = int(row[12])
            else:
                bs.color = 1
            self.parent.bs.append(bs)

    def loadNetworkAndObstaclesFromFile(self, filename):
        network = csv.reader(open(filename), delimiter=';', quotechar='|')
        for row in network:
            if row[0] == "x_size_real":
                self.parent.constraintAreaMaxX = float(row[1])
            if row[0] == "y_size_real":
                self.parent.constraintAreaMaxY = float(row[1])
            if row[0] == "x_size_map":
                x_size_map = float(row[1])
            if row[0] == "y_size_map":
                y_size_map = float(row[1])
            if row[0] == "wall":
                obstacle = []
                obstacle.append(float(row[1])/x_size_map*self.parent.constraintAreaMaxX)
                obstacle.append(self.parent.constraintAreaMaxY - float(row[2])/y_size_map*self.parent.constraintAreaMaxY)
                obstacle.append(float(row[3])/x_size_map*self.parent.constraintAreaMaxX)
                obstacle.append(self.parent.constraintAreaMaxY - float(row[4])/y_size_map*self.parent.constraintAreaMaxY)
                obstacle.append(float(row[5]))
                self.parent.obstacles.append(obstacle)
            if row[0] == "bs":
                bs = devices.BS()
                bs.x = float(float(row[1])/x_size_map*self.parent.constraintAreaMaxX)
                bs.y = float(self.parent.constraintAreaMaxY - float(row[2])/y_size_map*self.parent.constraintAreaMaxY)
                bs.ID = int(row[3])
                bs.turnedOn = True
                self.parent.bs.append(bs)

    def insertUEingrid(self, numberOfDevices):
        numberOfNodesInRow = math.ceil(math.sqrt(numberOfDevices))
        number = 0
        x_step = int(self.parent.constraintAreaMaxX)/numberOfNodesInRow
        y_step = int(self.parent.constraintAreaMaxY)/numberOfNodesInRow
        for x_pos in range(0, numberOfNodesInRow):
            for y_pos in range(0, numberOfNodesInRow):
                ue = devices.UE()
                ue.ID = number
                ue.x = 0.5*x_step + (x_pos*x_step)
                ue.y = 0.5*y_step + (y_pos*y_step)
                self.parent.ue.append(ue)
                number = number+1

    def insertUErandomly(self, numberOfDevices):
        number = 0
        for i in range(0, numberOfDevices):
            ue = devices.UE()
            ue.ID = number
            ue.x = random.uniform(0, self.parent.constraintAreaMaxX)
            ue.y = random.uniform(0, self.parent.constraintAreaMaxY)
            self.parent.ue.append(ue)
            number = number+1
