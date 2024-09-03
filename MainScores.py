from flask import Flask, render_template
import json
from os import path

filename = './Scores.json'
def loadData():
   if path.isfile(filename) is False:
      raise Exception("File not found")
   else:
      with open(filename) as json_file:
         data = json.load(json_file)
         return data

app = Flask(__name__)

@app.route('/')
def home():
   pList = loadData()
   return render_template('home.html')

@app.route('/worldOfGames')
def worldOfGames():
   pList = loadData()
   return render_template('worldOfGames.html')

@app.route('/scores/')
def scores():
    pList = loadData()
    return render_template('scores.html', pList = pList)

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000)