#read_table.py implements a pandas dataframe that reads a selected d100 or d20 table from an excel file or sql database
#Should work universally, regardless of implementation.
#intialization
import discord
import numpy as np
import pandas as pd
import random as rand

#Constuctor def
def read_table():
	print("Module Active")

#Wilderness Combat Encounter Table
def wild_combat():
	d20 = rand.randint(0,19)
	tab = pd.read_csv("wilderness_combat.csv") #Wilderness encounter table from excel to DataFrame
	print(tab)

wild_combat() #Testing to see if this function works as intended