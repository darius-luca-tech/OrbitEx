from flask import Flask, render_template
from OrbitAlgorithm.test import Percentage

percentage = Percentage()

app = Flask(__name__, static_folder="F://Work&Projects//Atestate//OrbitEx//static//", template_folder="F://Work&Projects//Atestate//OrbitEx//templates//")

@app.route('/')
def mainPage():
    return render_template('index.html')

@app.route('/planets')
def planetsPage():
    #TO-DO: implement algortihm
    percentage.Orbits()
    return render_template('planets.html', earthPercentage = percentage.percentageDictionary["Earth"], moonPercentage = percentage.percentageDictionary["Moon"], marsPercentage = percentage.percentageDictionary["Mars"], uranusPercentage = percentage.percentageDictionary["Uranus"], neptunePercentage = percentage.percentageDictionary["Neptune"])

if __name__ == '__main__':
    app.run()