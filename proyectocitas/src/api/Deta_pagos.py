from flask import Flask, Blueprint,  redirect, request, jsonify, json, session, render_template
from common.Toke import *
from config.db import db, app, ma

from Model.Deta_pagos import Dpagos, DpagoSchema

routes_dpagos = Blueprint("routes_dpagos", __name__)
#Roles
dpago_schema = DpagoSchema()
Dpagos_schema = DpagoSchema(many=True)

@routes_dpagos.route('/indexdpagos', methods=['GET'] )
def indexdiente():
    
    return "Hola Mundo!!" 

@routes_dpagos.route('/Dpagos', methods=['GET'])
def Dpago():    
    returnall = Dpago.query.all()
   
    resultado_dpagos = dpago_schema.dump(returnall)
    return jsonify(resultado_dpagos)


@routes_dpagos.route('/savedpagos', methods=['POST'] )
def guardar_dpágos():
    
    id_pago = request.json['id_pago']
    id_tratamientos = request.json['id_tratamientos']
    fecha= request.json['fecha']

    new_dpago = Dpago(id_pago, id_tratamientos, fecha)
    db.session.add(new_dpago)
    db.session.commit()
    return redirect('/Dpagos')


@routes_dpagos.route('/eliminar/<id>', methods=['GET'] )
def eliminar(id):
    id = Dpago.query.get(id)
    db.session.delete(id)
    db.session.commit()
    return jsonify(Dpagos_schema.dump(id)) 

@routes_dpagos.route('/actualizar', methods=['POST'] )
def actualizar():
    id_pago = request.json['id_pago']
    id_tratamientos = request.json['id_tratamientos']
    fecha= request.json['fecha']
    dpagos = Dpagos.query.get(id)
    dpagos.id_pago = id_pago
    dpagos.id_tratamientos = id_tratamientos
    dpagos.fecha = fecha
    db.session.commit()
    return redirect('/Dpagos')