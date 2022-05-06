from flask import Flask, abort, render_template, request
import json
import os
app=Flask(__name__)

with open("MSX.json") as fichero:
    datos=json.load(fichero)

@app.route('/', methods=["GET"])
def inicio():
    return render_template('inicio.html')

port=os.environ["PORT"]
app.run('0.0.0.0', int(port), debug=False)

#app.run('0.0.0.0', debug=True)
