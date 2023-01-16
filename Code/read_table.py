# read_table.py implements a pandas dataframe that reads a selected d100 or d20 table from an excel file or sql database
# Should work universally, regardless of implementation.
# initialization
import discord
import numpy as np
import pandas as pd
import random as rand

# Constructor def
def read_table():
	print("Module Active")

# This definition receives a command and rolls a d4, d6, d8, d10, d12, or d20
def roll_dice(cmd):
	command = str(cmd)
	indexer = len(command)
	multiplier = int(command[indexer-1])
	print(multiplier)

	if command.__contains__("d4"):
		roll = rand.randint(1, 4)
		return roll

	elif command.__contains__("d6"):
		roll = 0
		if multiplier > 1:
			while multiplier > 0:
				print("roll: " + str(roll) + "@ multiplier" + str(multiplier))
				roll += rand.randint(1, 6)
				multiplier -= multiplier
		else:
			roll = rand.randint(1, 6)

		return roll

	else:
		return "Dice Command Not Valid"


# Wilderness Combat Encounter Table
def wild_combat():
	d20 = rand.randint(0,19)
	# print(str(d20))
	tab = pd.read_csv("wilderness_combat.csv")  # Wilderness encounter table from excel to DataFrame
	return tab.iloc[[d20]]

