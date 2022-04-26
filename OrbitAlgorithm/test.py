from datetime import date, datetime , timedelta
import re
import json

class Percentage:
	def __init__(self):
		self.current_year = date.today().year
		self.today = int(datetime.today().strftime("%d"))
		self.thisMonth = int(datetime.today().strftime("%m"))
		self.ora = int(datetime.today().strftime("%H"))
		self.minut = int(datetime.today().strftime("%M"))
		self.secunda = int(datetime.today().strftime("%S"))

		self.result = 0
		self.OrbitPerihelion = 0
		self.NewOrbitPerihelion = 0
		self.percentageDictionary = {}
		self.planetDictionary = {"Earth" : 365, "Moon" : 27, "Mars" : 687, "Uranus" : 30768, "Neptune" : 60195}
		self.planetArray = ["Earth", "Moon", "Mars", "Uranus", "Neptune"]


	def Orbits(self):
		for planetName in self.planetDictionary:
			
			with open("OrbitAlgorithm/Orbit.json", "r") as O:
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

						d1 = date(self.current_year, self.thisMonth, self.today)
						d1 = d1 + timedelta(days = 1)
						if(d0 >= d1 - timedelta(days = self.planetDictionary[planetName]) and d0 <= d1):
							self.OrbitPerihelion = d0

				for i in thisYear:
					for j in range(0, len(thisYear[str(i)])):
						d0Year = i
						d0Year = int(d0Year)
						d0Month = thisYear[i][j][5:7]
						d0Month = int(d0Month)
						d0Day = thisYear[i][j][8:10]
						d0Day = int(d0Day)
						d0 = date(d0Year, d0Month, d0Day)

						d1 = date(self.current_year, self.thisMonth, self.today)
						d1 = d1 + timedelta(days = 1)

						if (d0 <= d1 + timedelta(days = self.planetDictionary[planetName]) and d0 >= d1):
							self.NewOrbitPerihelion = d0
							d1 = date(self.current_year, self.thisMonth, self.today)

							d3 = self.NewOrbitPerihelion - self.OrbitPerihelion
							d3 = str(d3)
							d3 = d3.split()
							d3 = int(d3[0])
							d3 = d3 + 1

							ValuePercent = d3 / 100
							delta = d1 - self.OrbitPerihelion
							delta = str(delta)
							delta = delta.split()
							delta = delta[0]

							new = re.sub("[^0-9]", "", str(delta))
							new = str(new)
							new = new[:6]
							new = int(new)

							self.result = new / ValuePercent
							self.result = round(self.result, 2)
							# print(str(self.self) + " - " + planetName + " - " + str(new))
							self.percentageDictionary[planetName] = self.result

	def showPercentage(self):
		for key, value in self.percentageDictionary.items():
			print(key, value)


percentage = Percentage()
percentage.Orbits()
percentage.showPercentage()

