from flask import Flask, render_template

app = Flask(__name__, static_folder="F://Work&Projects//Atestate//OrbitEx//static//", template_folder="F://Work&Projects//Atestate//OrbitEx//templates//")

@app.route('/')
def mainPage():
    return render_template('index.html')

@app.route('/planets')
def planetsPage():
    return render_template('planets.html')

if __name__ == '__main__':
    app.run()