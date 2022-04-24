from datetime import date, datetime , timedelta
import re
import json

class Percentage:
	def __init__(self):
		self.OrbitPerihelion
		self.NewOrbitPerihelion
		self.percentage
		self.planetDictionary = {}
		self.planetArray = []

Percentage.OrbitPerihelion = 0
Percentage.NewOrbitPerihelion = 0
Percentage.planetArrray = ["Earth", "Moon", "Mars", "Uranus"]
Percentage.planetDictionary = {"Earth" : 365, "Moon" : 27, "Mars" : 687, "Uranus" : 30768}
Percentage.current_year = date.today().year
Percentage.today = int(datetime.today().strftime("%d"))
Percentage.thisMonth = int(datetime.today().strftime("%m"))
Percentage.ora = int(datetime.today().strftime("%H"))
Percentage.minut = int(datetime.today().strftime("%M"))
Percentage.secunda = int(datetime.today().strftime("%S"))

def Orbits():
	for planetName in Percentage.planetDictionary:
		
		with open("Orbit.json", "r") as O:
			orbit = json.load(O)
			thisYear = orbit[planetName]

			for i in thisYear:
				for j in range(0, len(thisYear[str(i)])):
					d0Year = i
					d0Year = int(d0Year)
					d0Month = thisYear[i][j][5:7]
					d0Month = int(d0Month)
					d0Day = thisYear[i][j][8:10]
					d0Day = int(d0Day)
					d0 = date(d0Year, d0Month, d0Day)

					d1 = date(Percentage.current_year, Percentage.thisMonth, Percentage.today)
					d1 = d1 + timedelta(days = 1)
					if(d0 >= d1 - timedelta(days = Percentage.planetDictionary[planetName]) and d0 <= d1):
						Percentage.OrbitPerihelion = d0

			for i in thisYear:
				for j in range(0, len(thisYear[str(i)])):
					d0Year = i
					d0Year = int(d0Year)
					d0Month = thisYear[i][j][5:7]
					d0Month = int(d0Month)
					d0Day = thisYear[i][j][8:10]
					d0Day = int(d0Day)
					d0 = date(d0Year, d0Month, d0Day)

					d1 = date(Percentage.current_year, Percentage.thisMonth, Percentage.today)
					d1 = d1 + timedelta(days = 1)

					if (d0 <= d1 + timedelta(days = Percentage.planetDictionary[planetName]) and d0 >= d1):
						Percentage.NewOrbitPerihelion = d0
						d1 = date(Percentage.current_year, Percentage.thisMonth, Percentage.today)

						d3 = Percentage.NewOrbitPerihelion - Percentage.OrbitPerihelion
						d3 = str(d3)
						d3 = d3.split()
						d3 = int(d3[0])
						d3 = d3 + 1

						ValuePercent = d3 / 100
						delta = d1 - Percentage.OrbitPerihelion
						delta = str(delta)
						delta = delta.split()
						delta = delta[0]

						new = re.sub("[^0-9]", "", str(delta))
						new = str(new)
						new = new[:6]
						new = int(new)

						Percentage.percentage = new / ValuePercent
						Percentage.percentage = round(Percentage.percentage, 2)
						print(str(Percentage.percentage) + " - " + planetName)

Orbits()