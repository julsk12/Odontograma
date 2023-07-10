from flask import Flask, Blueprint,  redirect, request, jsonify, json, session, render_template
from common.Toke import *
from config.db import *

from Model.Diente import Diente,DienteSchema
from Model.Odontogramas import Odon, OdontoSchema

routes_dientes = Blueprint("routes_dientes", __name__)
#Roles
diente_schema = DienteSchema()
Dientes_schema = DienteSchema(many=True)

@routes_dientes.route('/Dientes', methods=['GET'])
def Dientee(): 
    iduser = request.args.get('iduser')
    
    # Realizar la consulta filtrando por el id del usuario
    returnall = db.session.query(Diente).join(Odon).filter(Odon.id_paciente == iduser).all()
    
    # Serializar los resultados utilizando el esquema correspondiente
    resultado_dientes = Dientes_schema.dump(returnall)
    
    return jsonify(resultado_dientes)

@routes_dientes.route('/savedientes', methods=['POST'])
def guardar_diente():
    id_odontologo = session.get('user_id')
    numerodiente = request.json['numerodiente']
    secciondiente = request.json['secciondiente']
    estadodiente = request.json['estadodiente']
    observaciondiente = request.json['observaciondiente']
    tratamiento = request.json['Tratamiento']
    fecha = request.json['fecha']
    iduser = request.json['iduser']
    print(id_odontologo)
    print(iduser)
    
    resultado = db.session.query(Odon).filter(Odon.id_paciente == iduser, Odon.id_odontologo == id_odontologo).order_by(-Odon.fecha_consulta).first()
    if resultado is not None:
        new_diente = Diente(numerodiente, secciondiente, estadodiente, observaciondiente, tratamiento, fecha, resultado.id)
        db.session.add(new_diente)
        db.session.commit()
        return jsonify({'message': 'Registro de datos exitoso'})
    else:
        return jsonify({'message': 'Identificacion no registrada o invalida'})


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
