from flask import Flask, abort, render_template, request
import json
import os
app=Flask(__name__)

with open("MSX.json") as fichero:
    datos=json.load(fichero)

@app.route('/', methods=["GET"])
def inicio():
    return render_template('inicio.html')
    
@app.route('/juegos', methods=["GET", "POST"])
def juegos():
    if request.method == "GET":
        lista_categoria=[]
        for juegos in datos:
            lista_categoria.append(juegos["categoria"])
        return render_template('juegos.html', lista_categoria=set(lista_categoria))
    else:
        nombre_juego=request.form.get("nombre")
        categoria=request.form.get("categorias")
        lista_nombres=[]
        lista_desarrolladores=[]
        lista_ids=[]
        lista_categoria=[]
        for juegos in datos:
            lista_categoria.append(juegos["categoria"])
            if nombre_juego == "" and str(juegos["categoria"]) == categoria:
                lista_desarrolladores.append(juegos["desarrollador"])
                lista_nombres.append(juegos["nombre"])
                lista_ids.append(juegos["id"])
            elif str(juegos["nombre"]).startswith(nombre_juego) and str(juegos["categoria"]) == categoria:
                lista_desarrolladores.append(juegos["desarrollador"])
                lista_nombres.append(juegos["nombre"])
                lista_ids.append(juegos["id"])
        return render_template("juegos.html", nombre_juego=nombre_juego, lista_nombres=lista_nombres, lista_desarrolladores=lista_desarrolladores, lista_ids=lista_ids, lista_categoria=set(lista_categoria))

port=os.environ["PORT"]
app.run('0.0.0.0', int(port), debug=False)

#app.run('0.0.0.0', debug=True)
