__author__ = 'Mariusz'

import math
import csv
import random
from modules import devices

class Generator:
    """Class that generates network deployment"""
    def __init__(self,parent):
        self.parent = parent

    def createhexagonal6BSdeployment(self, radius):
        numberofbs = 6
        d_x = math.sqrt(3)/2 * radius
        d_y = radius/2
        H_hex = 2 * radius
        W_hex = radius * math.sqrt(3)
        self.parent.radius = radius
        self.parent.constraintAreaMaxX = 3.5 * W_hex
        self.parent.constraintAreaMaxY = H_hex + 1.5 * radius
        for i in range(0, numberofbs):
            bs = devices.BS()
            bs.ID = i
            bs.turnedOn = True
            self.parent.bs.append(bs)

        for sector_nb in range(0, 3):
            self.parent.bs[sector_nb].x = 2 * d_x
            self.parent.bs[sector_nb].y = (1) * H_hex - d_y
            self.parent.bs[sector_nb].angle = sector_nb * 120
        for sector_nb in range(0, 3):
            self.parent.bs[3 + sector_nb].x = 5 * d_x
            self.parent.bs[3 + sector_nb].y = H_hex
            self.parent.bs[3 + sector_nb].angle = 60 + 120 * sector_nb

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

    def create3BSdeployment(self, radius):
        numberofbs = 3
        d_x = math.sqrt(3)/2 * radius
        d_y = radius/2
        H_hex = 2 * radius
        W_hex = radius * math.sqrt(3)
        self.parent.radius = radius
        self.parent.constraintAreaMaxX = 2 * W_hex
        self.parent.constraintAreaMaxY = H_hex + 1.5 * radius
        for i in range(0, numberofbs):
            bs = devices.BS()
            bs.ID = i
            bs.turnedOn = True
            self.parent.bs.append(bs)

        for sector_nb in range(0, 3):
            self.parent.bs[sector_nb].x = 2 * d_x
            self.parent.bs[sector_nb].y = (1) * H_hex - d_y
            self.parent.bs[sector_nb].angle = sector_nb * 120

    def createhexagonal12BSdeployment(self, radius):
        numberofbs = 12
        d_x = math.sqrt(3)/2 * radius
        d_y = radius/2
        H_hex = 2 * radius
        W_hex = radius * math.sqrt(3)
        self.parent.radius = radius
        self.parent.constraintAreaMaxX = 3.5 * W_hex
        self.parent.constraintAreaMaxY = 2 * H_hex + 2.5 * radius
        for i in range(0, numberofbs):
            bs = devices.BS()
            bs.ID = i
            bs.turnedOn = True
            self.parent.bs.append(bs)

        for sector_nb in range(0, 3):
            self.parent.bs[sector_nb].x = 2 * d_x
            self.parent.bs[sector_nb].y = (1) * H_hex - d_y
            self.parent.bs[sector_nb].angle = sector_nb * 120
        for sector_nb in range(0, 3):
            self.parent.bs[3 + sector_nb].x = 5 * d_x
            self.parent.bs[3 + sector_nb].y = H_hex
            self.parent.bs[3 + sector_nb].angle = 60 + 120 * sector_nb
        for sector_nb in range(0, 3):
            self.parent.bs[6 + sector_nb].x = 2 * d_x
            self.parent.bs[6 + sector_nb].y = (2.5) * H_hex - d_y
            self.parent.bs[6 + sector_nb].angle = sector_nb * 120
        for sector_nb in range(0, 3):
            self.parent.bs[9 + sector_nb].x = 5 * d_x
            self.parent.bs[9 + sector_nb].y = (2.5) * H_hex
            self.parent.bs[9 + sector_nb].angle = 60 + 120 * sector_nb

    def createhexagonal36BSdeployment(self, radius):
        numberofbs = 36
        d_x = math.sqrt(3)/2 * radius
        d_y = radius/2
        H_hex = 2 * radius
        W_hex = radius * math.sqrt(3)
        self.parent.radius = radius
        self.parent.constraintAreaMaxX = 6.5 * W_hex
        self.parent.constraintAreaMaxY = 3 * H_hex + 3.5 * radius
        for i in range(0, numberofbs):
            bs = devices.BS()
            bs.ID = i
            bs.turnedOn = True
            self.parent.bs.append(bs)

        for row_number in range(0, 3):
            for sector_nb in range(0, 3):
                self.parent.bs[12*row_number + 0 + sector_nb].x = 2 * d_x
                self.parent.bs[12*row_number + 0 + sector_nb].y = (1 + row_number) * H_hex - d_y + row_number * radius
                self.parent.bs[12*row_number + 0 + sector_nb].angle = sector_nb * 120
            for sector_nb in range(0, 3):
                self.parent.bs[12*row_number + 3 + sector_nb].x = 5 * d_x
                self.parent.bs[12*row_number + 3 + sector_nb].y = H_hex + row_number * (radius + H_hex)
                self.parent.bs[12*row_number + 3 + sector_nb].angle = 60 + 120 * sector_nb
            for sector_nb in range(0, 3):
                self.parent.bs[12*row_number + 6 + sector_nb].x = 8 * d_x
                self.parent.bs[12*row_number + 6 + sector_nb].y = (1 + row_number) * H_hex - d_y + row_number * radius
                self.parent.bs[12*row_number + 6 + sector_nb].angle = sector_nb * 120
            for sector_nb in range(0, 3):
                self.parent.bs[12*row_number + 9 + sector_nb].x = 11 * d_x
                self.parent.bs[12*row_number + 9 + sector_nb].y = H_hex + row_number * (radius + H_hex)
                self.parent.bs[12*row_number + 9 + sector_nb].angle = 60 + 120 * sector_nb

    def createhexagonal60BSdeployment(self, radius):
        numberofbs = 60
        d_x = math.sqrt(3)/2 * radius
        d_y = radius/2
        H_hex = 2 * radius
        W_hex = radius * math.sqrt(3)
        self.parent.radius = radius
        self.parent.constraintAreaMaxX = 8 * W_hex
        self.parent.constraintAreaMaxY = 4 * H_hex + 4.5 * radius
        for i in range(0, numberofbs):
            bs = devices.BS()
            bs.ID = i
            bs.turnedOn = True
            self.parent.bs.append(bs)

        for row_number in range(0, 4):
            for sector_nb in range(0, 3):
                self.parent.bs[15*row_number + 0 + sector_nb].x = 2 * d_x
                self.parent.bs[15*row_number + 0 + sector_nb].y = (1 + row_number) * H_hex - d_y + row_number * radius
                self.parent.bs[15*row_number + 0 + sector_nb].angle = sector_nb * 120
            for sector_nb in range(0, 3):
                self.parent.bs[15*row_number + 3 + sector_nb].x = 5 * d_x
                self.parent.bs[15*row_number + 3 + sector_nb].y = H_hex + row_number * (radius + H_hex)
                self.parent.bs[15*row_number + 3 + sector_nb].angle = 60 + 120 * sector_nb
            for sector_nb in range(0, 3):
                self.parent.bs[15*row_number + 6 + sector_nb].x = 8 * d_x
                self.parent.bs[15*row_number + 6 + sector_nb].y = (1 + row_number) * H_hex - d_y + row_number * radius
                self.parent.bs[15*row_number + 6 + sector_nb].angle = sector_nb * 120
            for sector_nb in range(0, 3):
                self.parent.bs[15*row_number + 9 + sector_nb].x = 11 * d_x
                self.parent.bs[15*row_number + 9 + sector_nb].y = H_hex + row_number * (radius + H_hex)
                self.parent.bs[15*row_number + 9 + sector_nb].angle = 60 + 120 * sector_nb
            for sector_nb in range(0, 3):
                self.parent.bs[15*row_number + 12 + sector_nb].x = 14 * d_x
                self.parent.bs[15*row_number + 12 + sector_nb].y = (1 + row_number) * H_hex - d_y + row_number * radius
                self.parent.bs[15*row_number + 12 + sector_nb].angle = 60 + 120 * sector_nb

    def createhexagonal75BSdeployment(self, radius):
        numberofbs = 75
        d_x = math.sqrt(3)/2 * radius
        d_y = radius/2
        H_hex = 2 * radius
        W_hex = radius * math.sqrt(3)
        self.parent.radius = radius
        self.parent.constraintAreaMaxX = 8 * W_hex
        self.parent.constraintAreaMaxY = 4 * H_hex + 7.5 * radius
        for i in range(0, numberofbs):
            bs = devices.BS()
            bs.ID = i
            bs.turnedOn = True
            self.parent.bs.append(bs)

        for row_number in range(0, 5):
            for sector_nb in range(0, 3):
                self.parent.bs[15*row_number + 0 + sector_nb].x = 2 * d_x
                self.parent.bs[15*row_number + 0 + sector_nb].y = (1 + row_number) * H_hex - d_y + row_number * radius
                self.parent.bs[15*row_number + 0 + sector_nb].angle = sector_nb * 120
            for sector_nb in range(0, 3):
                self.parent.bs[15*row_number + 3 + sector_nb].x = 5 * d_x
                self.parent.bs[15*row_number + 3 + sector_nb].y = H_hex + row_number * (radius + H_hex)
                self.parent.bs[15*row_number + 3 + sector_nb].angle = 60 + 120 * sector_nb
            for sector_nb in range(0, 3):
                self.parent.bs[15*row_number + 6 + sector_nb].x = 8 * d_x
                self.parent.bs[15*row_number + 6 + sector_nb].y = (1 + row_number) * H_hex - d_y + row_number * radius
                self.parent.bs[15*row_number + 6 + sector_nb].angle = sector_nb * 120
            for sector_nb in range(0, 3):
                self.parent.bs[15*row_number + 9 + sector_nb].x = 11 * d_x
                self.parent.bs[15*row_number + 9 + sector_nb].y = H_hex + row_number * (radius + H_hex)
                self.parent.bs[15*row_number + 9 + sector_nb].angle = 60 + 120 * sector_nb
            for sector_nb in range(0, 3):
                self.parent.bs[15*row_number + 12 + sector_nb].x = 14 * d_x
                self.parent.bs[15*row_number + 12 + sector_nb].y = (1 + row_number) * H_hex - d_y + row_number * radius
                self.parent.bs[15*row_number + 12 + sector_nb].angle = 60 + 120 * sector_nb

    def createhexagonal108BSdeployment(self, radius):
        numberofbs = 108
        d_x = math.sqrt(3)/2 * radius
        d_y = radius/2
        H_hex = 2 * radius
        W_hex = radius * math.sqrt(3)
        self.parent.radius = radius
        self.parent.constraintAreaMaxX = 9.5 * W_hex
        self.parent.constraintAreaMaxY = 6 * H_hex + 6.5 * radius
        for i in range(0, numberofbs):
            bs = devices.BS()
            bs.ID = i
            bs.turnedOn = True
            self.parent.bs.append(bs)

        for row_number in range(0, 6):
            for sector_nb in range(0, 3):
                self.parent.bs[18*row_number + 0 + sector_nb].x = 2 * d_x
                self.parent.bs[18*row_number + 0 + sector_nb].y = (1 + row_number) * H_hex - d_y + row_number * radius
                self.parent.bs[18*row_number + 0 + sector_nb].angle = sector_nb * 120
            for sector_nb in range(0, 3):
                self.parent.bs[18*row_number + 3 + sector_nb].x = 5 * d_x
                self.parent.bs[18*row_number + 3 + sector_nb].y = H_hex + row_number * (radius + H_hex)
                self.parent.bs[18*row_number + 3 + sector_nb].angle = 60 + 120 * sector_nb
            for sector_nb in range(0, 3):
                self.parent.bs[18*row_number + 6 + sector_nb].x = 8 * d_x
                self.parent.bs[18*row_number + 6 + sector_nb].y = (1 + row_number) * H_hex - d_y + row_number * radius
                self.parent.bs[18*row_number + 6 + sector_nb].angle = sector_nb * 120
            for sector_nb in range(0, 3):
                self.parent.bs[18*row_number + 9 + sector_nb].x = 11 * d_x
                self.parent.bs[18*row_number + 9 + sector_nb].y = H_hex + row_number * (radius + H_hex)
                self.parent.bs[18*row_number + 9 + sector_nb].angle = 60 + 120 * sector_nb
            for sector_nb in range(0, 3):
                self.parent.bs[18*row_number + 12 + sector_nb].x = 14 * d_x
                self.parent.bs[18*row_number + 12 + sector_nb].y = (1 + row_number) * H_hex - d_y + row_number * radius
                self.parent.bs[18*row_number + 12 + sector_nb].angle = 60 + 120 * sector_nb
            for sector_nb in range(0, 3):
                self.parent.bs[18*row_number + 15 + sector_nb].x = 17 * d_x
                self.parent.bs[18*row_number + 15 + sector_nb].y = H_hex + row_number * (radius + H_hex)
                self.parent.bs[18*row_number + 15 + sector_nb].angle = 60 + 120 * sector_nb

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
            self.parent.bs.append(bs)

    def loadNetworkAndObstaclesFromFile(self, filename):
        network = csv.reader(open(filename), delimiter=';', quotechar='|')
        for row in network:
            if row[0] == "x_size_real":
                self.parent.constraintAreaMaxX = int(row[1])*10
            if row[0] == "y_size_real":
                self.parent.constraintAreaMaxY = int(row[1])*10
            if row[0] == "x_size_map":
                x_size_map = int(row[1])
            if row[0] == "y_size_map":
                y_size_map = int(row[1])
            if row[0] == "wall":
                obstacle = []
                obstacle.append(float(row[1])/x_size_map*self.parent.constraintAreaMaxX)
                obstacle.append(float(row[2])/y_size_map*self.parent.constraintAreaMaxY)
                obstacle.append(float(row[3])/x_size_map*self.parent.constraintAreaMaxX)
                obstacle.append(float(row[4])/y_size_map*self.parent.constraintAreaMaxY)
                obstacle.append(float(row[5]))
                self.parent.obstacles.append(obstacle)
            if row[0] == "bs":
                bs = devices.BS()
                bs.x = float(float(row[1])/x_size_map*self.parent.constraintAreaMaxX)
                bs.y = float(float(row[2])/y_size_map*self.parent.constraintAreaMaxY)
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
