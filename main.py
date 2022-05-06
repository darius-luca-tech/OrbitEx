from flask import Flask, render_template
from OrbitAlgorithm.algorithm import Percentage

percentage = Percentage()
percentage.Orbits()

app = Flask(__name__, static_folder="F://Work&Projects//Atestate//OrbitEx//static//", template_folder="F://Work&Projects//Atestate//OrbitEx//templates//")

@app.route('/')
def mainPage():
    percentage.Orbits()
    return render_template('index.html')

@app.route('/planets')
def planetsPage():

    return render_template(
        'planets.html', 
        earthPercentage = percentage.percentageDictionary["Earth"], 
        moonPercentage = percentage.percentageDictionary["Moon"], 
        marsPercentage = percentage.percentageDictionary["Mars"], 
        uranusPercentage = percentage.percentageDictionary["Uranus"], 
        neptunePercentage = percentage.percentageDictionary["Neptune"],
        venusPercentage = percentage.percentageDictionary["Venus"],
        mercuryPercentage = percentage.percentageDictionary["Mercury"],
        jupiterPercentage = percentage.percentageDictionary["Jupiter"],
        saturnPercentage = percentage.percentageDictionary["Saturn"])

@app.route('/comets')
def commetsPage():
    return render_template(
        'comets.html', 
        halleyPercentage = percentage.percentageDictionary["Halley"],
        enckePercentage = percentage.percentageDictionary["Encke"],
        fayePercentage = percentage.percentageDictionary["Faye"])

@app.route('/dwarf')
def dwarfPage():
    return render_template(
        'dwarf.html', 
        plutoPercentage = percentage.percentageDictionary["Pluto"],
        ceresPercentage = percentage.percentageDictionary["Ceres"],
        haumeaPercentage = percentage.percentageDictionary["Haumea"],
        makemakePercentage = percentage.percentageDictionary["Makemake"],
        erisPercentage = percentage.percentageDictionary["Eris"])

if __name__ == '__main__':
    app.run()