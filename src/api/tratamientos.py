from flask import Flask, Blueprint,  redirect, request, jsonify, json, session, render_template
from common.Toke import *
from config.db import db, app, ma

from Model.Tratamientos import Trata, TratamientosSchema
from Model.Usuarios import Users
from Model.Odontogramas import Odon
from Model.Diente import Diente

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
    id=request.json['id']
    nombre = request.json['nombre']
    descripcion = request.json['descripcion']
    duracion = request.json['duracion']
    costo = request.json['costo']
    print(nombre, descripcion, duracion,costo)
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
		'nombre':trat.nombre,
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
        id_odontologo = datos[i]['id_odontologo']
        id_user = datos[i]['id']
    odon_name = (db.session.query(Users)
                 .filter(Users.id==id_odontologo).all())  
    for odon in odon_name:
        datos[i]['nombre_odontologo'] = odon.nombre
        
    otro = (db.session.query(Odon, Diente)
            .filter(Odon.id_paciente == id_user, 
                    Diente.id_odontograma==Odon.id).all())
    for oton, dien in otro:
        datos[i]['tratamiento'] = oton.tratamiento_recomendado
        datos[i]['descripcion'] = oton.descripcion
        datos[i]['fecha_creacion'] = dien.fecha_creacion

        tratamiento = datos[i]['tratamiento']
    ultimo = (db.session.query(Trata)
            .filter(Trata.nombre_tratamiento == tratamiento).all())
    
    for trat in ultimo:
        datos[i]['duracion'] = trat.duracion
        datos[i]['costo'] = trat.costo
    
    trato.append(datos)
    return jsonify(datos)

@routes_tratamientos.route('/eliminarT', methods=['DELETE'] )
def eliminarperso():
    id = request.json['id']
    ced = Trata.query.filter_by(id=id).first()
    if ced:
        db.session.delete(ced)
        db.session.commit()
        print(id)
        print(ced)
        return 'Registro eliminado', 200
    else:
        return 'Registro no encontrado', 404