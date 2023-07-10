from flask import Flask, Blueprint,  redirect, request, jsonify, json, session, render_template
from common.Toke import *
from config.db import db, app, ma

from Model.Dientes import Diente,DienteSchema

routes_dientes = Blueprint("routes_dientes", __name__)
#Roles
diente_schema = DienteSchema()
Dientes_schema = DienteSchema(many=True)

@routes_dientes.route('/indexdiente', methods=['GET'] )
def indexdiente():
    
    return "Hola Mundo!!" 

@routes_dientes.route('/Dientes', methods=['GET'])
def Dientee():    
    returnall = Diente.query.all()
   
    resultado_dientes = Dientes_schema.dump(returnall)
    return jsonify(resultado_dientes)


@routes_dientes.route('/savedientes', methods=['POST'] )
def guardar_diente():
    posicion_diente = request.json['posicion_diente']
    seccion_diente = request.json['seccion_diente']
    tipo_diente = request.json['tipo_diente']
    tipo_daño = request.json['tipo_daño']
    fecha_creacion = request.json['fecha_creacion']
    id_odontograma =request.json['id_odontograma']

    new_diente = Diente(posicion_diente, seccion_diente, tipo_diente, tipo_daño, fecha_creacion, id_odontograma)
    db.session.add(new_diente)
    db.session.commit()
    return redirect('/Dientes')


@routes_dientes.route('/eliminar/<id>', methods=['GET'] )
def eliminar(id):
    id = Diente.query.get(id)
    db.session.delete(id)
    db.session.commit()
    return jsonify(Dientes_schema.dump(id)) 

@routes_dientes.route('/actualizar', methods=['POST'] )
def actualizar():
    posicion_diente = request.json['posicion_diente']
    seccion_diente = request.json['seccion_diente']
    tipo_diente = request.json['tipo_diente']
    tipo_daño = request.json['tipo_daño']
    fecha_creacion = request.json['fecha_creacion']
    id_odontograma =request.json['id_odontograma']
    diente = Diente.query.get(id)
    diente.posicion_diente = posicion_diente
    diente.seccion_diente = seccion_diente
    diente.tipo_diente = tipo_diente
    diente.tipo_daño = tipo_daño
    diente.fecha_creacion= fecha_creacion
    diente.id_odontograma =id_odontograma
    db.session.commit()
    return redirect('/Diente')