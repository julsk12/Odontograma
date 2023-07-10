from flask import Flask, Blueprint,  redirect, request, jsonify, json, session, render_template
from common.Toke import *
from config.db import db, app, ma

from Model.Tratamientos import Trata, TratamientosSchema
from Model.Usuarios import Users
from Model.Odontogramas import Odon
from Model.Dientes import Diente

routes_tratamientos = Blueprint("routes_tratamientos", __name__)

tratamiento_schema = TratamientosSchema()
tratamientos_schema = TratamientosSchema(many=True)

@routes_tratamientos.route('/tratamientos', methods=['GET'])
def obtenertrata():    
    returnall = Trata.query.all()
    result_trata = tratamientos_schema.dump(returnall)
    return jsonify(result_trata)

@routes_tratamientos.route('/eliminartratamientos/<id>', methods=['GET'] )
def eliminartrata(id):
    trata = Trata.query.get(id)
    db.session.delete(trata)
    db.session.commit()
    return jsonify(tratamiento_schema.dump(trata))

@routes_tratamientos.route('/actualizartratamientos', methods=['POST'] )
def actualizartrata():
    nombre = request.json['nombre']
    descripcion = request.json['descripcion']
    duracion = request.json['duracion']
    costo = request.json['costo']
    trata = Trata.query.get(id)
    trata.nombre = nombre
    trata.descripcion = descripcion
    trata.duracion = duracion
    trata.costo = costo
    db.session.commit()
    return redirect('/tratamientos')

@routes_tratamientos.route('/savetratamientos', methods=['POST'] )
def guardar_trata():
    trata = request.json['nombre', 'descripcion', 'duracion', 'costo']
    new_trata = Trata(trata)
    db.session.add(new_trata)
    db.session.commit()
    return redirect('/tratamientos')

@routes_tratamientos.route("/guardartrat", methods=["POST"])
def tratamiento():
    nombre_tratamiento = request.json["nombre_tratamiento"]
    descripcion= request.json["descripcion"] 
    duracion = request.json["duracion"]
    costo = request.json["costo"]
    new_tratamiento = Trata(nombre_tratamiento, descripcion, duracion, costo)
    db.session.add(new_tratamiento)
    db.session.commit()
    return ""

@routes_tratamientos.route('/alltratamientos', methods=['GET'])
def mistrata():
    datos= {}
    resultado = db.session.query(Trata).all()
    trato = []
    i = 0
    for trat in resultado:
        i += 1
        datos[i] = {
        'id':trat.id,
		'nombre':trat.nombre_tratamiento,
		'descripcion':trat.descripcion,
		'duracion':trat.duracion,
		'costo':trat.costo      
        }
    trato.append(datos)
    return jsonify(datos)

@routes_tratamientos.route('/mistratamientos', methods=['GET'])
def head():
    correo= session.get('correo_usuario')
    datos= {}
    resultado = (db.session.query(Users,Odon)
                 .filter(Users.correo == correo, 
                Odon.id_paciente == Users.id).all())  
    trato = []
    i = 0
    for usuarios, donto in resultado:
        i += 1
        datos[i] = {
        'id':usuarios.id,
		'nombre':usuarios.nombre,              
        'id_odontologo': donto.id_odontologo
        }
      
        trato.append(datos)
    return jsonify(datos)