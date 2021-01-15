
import copy
import time
import math




class DataHolder:

	def __init__(self,fileName):
		self.board = []
		with open(fileName) as inputFile:
			lines = inputFile.readlines()
			self.gameMode = lines[0][0:-1]
			self.playerColor = lines[1][0:-1]
			self.givenTime = float(lines[2][0:-1])
			for i in range(3,19):
				if i != 18:
					self.board.append(lines[i][0:-1])
				else:
					self.board.append(lines[i])
