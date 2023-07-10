from flask import Flask, Blueprint,  redirect, request, jsonify, json, session, render_template
from common.Toke import *
from config.db import db, app, ma

from Model.pago import pagos, pagoSchema

routes_pagos = Blueprint("routes_pagos", __name__)

pago_schema = pagoSchema()
pagos_schema = pagoSchema(many=True)

#Datos de la tabla citas
@routes_pagos.route('/pagos', methods=['GET'])
def obtenerpagos():    
    returnall = pagos.query.all()
    result_pagos = pagos_schema.dump(returnall)
    return jsonify(result_pagos)

@routes_pagos.route('/eliminarpagos/<id>', methods=['GET'] )
def eliminarpagos(id):
    pago = pagos.query.get(id)
    db.session.delete(pago)
    db.session.commit()
    return jsonify(pago_schema.dump(pago))

@routes_pagos.route('/actualizarpagos', methods=['POST'] )
def actualizarcitas():
    id = request.json['id_pago']
    paciente = request.json['id_paciente']
    factura = request.json['id_factura']
    metodo = request.json['metodo']
    fecha = request.json['fecha']
    monto = request.json['monto']
    rcitas = pagos.query.get(id)
    rcitas.paciente = paciente
    rcitas.factura = factura
    rcitas.metodo = metodo
    rcitas.fecha = fecha
    rcitas.monto = monto
    db.session.commit()
    return redirect('/pagos')

@routes_pagos.route('/savepago', methods=['POST'] )
def guardar_pago():
    gpagos = request.json['id_paciente', 'id_factura', 'metodo', 'fecha', 'monto']
    new_pago = pagos(gpagos)
    db.session.add(new_pago)
    db.session.commit()
    return redirect('/pagos')