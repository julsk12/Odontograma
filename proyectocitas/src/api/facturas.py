from flask import Flask, Blueprint,  redirect, request, jsonify, json, session, render_template
from common.Toke import *
from config.db import db, app, ma

from Model.facturas import facturas, facturasSchema

routes_facturas = Blueprint("routes_facturas", __name__)

factura_schema = facturasSchema()
facturas_schema = facturasSchema(many=True)

#Datos de la tabla citas
@routes_facturas.route('/facturas', methods=['GET'])
def obtenerfacturas():    
    returnall = facturas.query.all()
    result_facturas = facturas_schema.dump(returnall)
    return jsonify(result_facturas)

@routes_facturas.route('/eliminarfacturas/<id>', methods=['GET'] )
def eliminarfacturas(id):
    factura = facturas.query.get(id)
    db.session.delete(factura)
    db.session.commit()
    return jsonify(factura_schema.dump(factura))

@routes_facturas.route('/savefacturas', methods=['POST'] )
def guardar_facturas():
    factura = request.json['id_paciente', 'id_odontologo', 'id_tratamiento ', 'fecha ', 'total']
    new_factura = facturas(factura)
    db.session.add(new_factura)
    db.session.commit()
    return redirect('/facturas')