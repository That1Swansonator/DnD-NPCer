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

# This definition receives a !dice command from bot.py and rolls a d4, d6, d8, d10, d12, or d20
def roll_dice(cmd):
	command = str(cmd)
	indexer = len(command)
	multiplier = int(command[indexer-1])  # The multiplier limit is 9. Rolls over 9 is invalid

	if command.__contains__("d4"):
		roll = 0
		while multiplier > 0:
			roll += rand.randint(1, 4)
			multiplier = multiplier - 1
		return roll

	elif command.__contains__("d6"):
		roll = 0
		while multiplier > 0:
				roll += rand.randint(1, 6)
				multiplier = multiplier - 1
		return roll

	elif command.__contains__("d8"):
		roll = 0
		while multiplier > 0:
			roll += rand.randint(1, 8)
			multiplier = multiplier - 1
		return roll
	elif command.__contains__("d12"):
		roll = 0
		while multiplier > 0:
			roll += rand.randint(1, 12)
			multiplier = multiplier - 1
		return roll

	elif command.__contains__("d20"):
		roll = 0
		while multiplier > 0:
			roll += rand.randint(1, 20)
			multiplier = multiplier - 1
		return roll

	elif command.__contains__("d100"):
		roll = 0
		while multiplier > 0:
			roll += rand.randint(1, 100)
			multiplier = multiplier - 1
		return roll

	else:
		return "Dice Command Not Valid"


# Wilderness Combat Encounter Table
def wild_combat():
	d20 = rand.randint(0,19)
	# print(str(d20))
	tab = pd.read_csv("wilderness_combat.csv")  # Wilderness encounter table from excel to DataFrame
	return tab.iloc[[d20]]

