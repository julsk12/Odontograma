from flask import Flask, Blueprint,  redirect, request, jsonify, json, session, render_template
from common.Toke import *
from config.db import db, app, ma

from Model.citas import citas, citasSchema
from Model.Usuarios import Users

routes_citas = Blueprint("routes_citas", __name__)

cita_schema = citasSchema()
citas_Schema = citasSchema(many=True)

#Datos de la tabla citas
@routes_citas.route('/citas', methods=['GET'])
def obtenercitas():    
    returnall = citas.query.all()
    result_citas = citas_Schema.dump(returnall)
    return jsonify(result_citas)

@routes_citas.route('/eliminarcitas/<id>', methods=['GET'] )
def eliminarcitas(id):
    cita = citas.query.get(id)
    db.session.delete(cita)
    db.session.commit()
    return jsonify(cita_schema.dump(cita))

@routes_citas.route('/actualizarcitas', methods=['POST'] )
def actualizarcitas():
    id = request.json['id_cita']
    odontologo = request.json['id_odontologo']
    fecha = request.json['fecha']
    hora = request.json['hora']
    rcitas = citas.query.get(id)
    rcitas.odontologo = odontologo
    rcitas.fecha = fecha
    rcitas.hora = hora
    db.session.commit()
    return redirect('/citas')

@routes_citas.route('/savecitas', methods=['POST'] )
def guardar_citas():
    xcitas = request.json['id_paciente', 'id_odontologo', 'fecha', 'hora', 'nota']
    new_cita = citas(xcitas)
    db.session.add(new_cita)
    db.session.commit()
    return redirect('/citas')

@routes_citas.route('/guardarcitas', methods=['POST'] )
def guardarcitas():
    print("aaaiuda")
    nombreodonto = request.json["nombreodonto"]
    resultado = (db.session.query(Users).filter(Users.nombre==nombreodonto).first())
    id_paciente = request.json["id_paciente"]
    fecha= request.json["fecha"] 
    hora = request.json["hora"]
    nota = request.json["nota"]
    sede = request.json["sede"]
    if resultado is not None:
        id_odontologo = resultado.id
        new_cita = citas(id_paciente, id_odontologo, fecha, hora, nota, sede)
        db.session.add(new_cita)
        db.session.commit()
        return "bien"
    else:
        return "Error: El odontólogo no se encuentra en la base de datos"
    
@routes_citas.route('/cards', methods=['GET'])
def misdatos():
    datos= {}
    resultado = db.session.query(Users).filter(Users.id_roles == "2").all()
    users = []
    i = 0
    for usuarios in resultado:
        i += 1
        datos[i] = {
        'id':usuarios.id,
		'nombre':usuarios.nombre,
        'rol': usuarios.id_roles                      
        }
    users.append(datos)
    return jsonify(datos)

@routes_citas.route('/consultar', methods=['GET'])
def head():
    correo= session.get('correo_usuario')
    datos= {}
    resultado = (db.session.query(Users,citas)
                 .filter(Users.correo == correo, 
                citas.id_paciente == Users.id).all())  
    users = []
    i = 0
    for usuarios, donto in resultado:
        i += 1
        datos[i] = {
        'id':donto.id_cita,
		'id_paciente':donto.id_paciente,
		'id_odontologo':donto.id_odontologo,
		'fecha':str(donto.fecha),
		'hora':str(donto.hora),
		'nota': donto.nota,
        'sede': donto.sede
        }
    users.append(datos)
    for i in users[0]:
        odon_name = (db.session.query(Users)
                    .filter(Users.id==users[0][i]['id_odontologo']).all())
        datos[i]['nombre_odontologo'] = odon_name[0].nombre
        datos[i]['correo'] = odon_name[0].correo
    
    return jsonify(datos)


@routes_citas.route('/consultarodon', methods=['GET'])
def sal():
    correo= session.get('correo_usuario')
    citass={}
    datos= {}
    consul = db.session.query(Users).filter(Users.correo == correo).all()
    # resultado = (db.session.query(citas).all())  
    users = []
    i = 0
    a = 0
    for cor in consul:
        i += 1
        citass[i] = {
        'id':cor.id,
		'nombre':cor.nombre,
		'email':cor.correo
        }
    id_odon = citass[i]['id']
    
    odon_name = (db.session.query(citas)
                    .filter(citas.id_odontologo==id_odon).all())
    for cit in odon_name:
        a += 1
        datos[a] = {
        'id_citas':cit.id_cita,
		'id_paciente':cit.id_paciente,
		'fecha':str(cit.fecha),
		'hora':str(cit.hora),
        'sede':cit.cede
  
        }
        # datos[i]['id_paciente'] = odon_name[0].id_paciente
        # datos[i]['fecha'] = odon_name[0].fecha
        # datos[i]['hora'] = str(odon_name[0].hora)
        # datos[i]['sede'] = odon_name[0].sede       
    users.append(datos)

    for i in users[0]:
        odoncorre = (db.session.query(Users)
                    .filter(Users.id==users[0][i]['id_paciente']).all())
        datos[i]['nombre_paciente'] = odoncorre[0].nombre
    
    # print(odoncorre[0].correo, correo, type(odoncorre), '\n', datos)

    return jsonify(datos)

# @routes_citas.route('/eventoscalendar', methods=['GET'])
# def eve():
#     corre= session.get('correo_usuario')
#     citass={}
#     datos={}
#     consul = db.session.query(Users).filter(Users.correo == corre).all()
#     # resultado = (db.session.query(citas).all())  
#     users = []
#     i = 0
#     a = 0
#     for cor in consul:
#         i += 1
#         citass[i] = {
#         'id':cor.id,
# 		'nombre':cor.nombre,
# 		'email':cor.correo
#         }
#     id_odon = citass[i]['id']
    
#     odon_name = (db.session.query(citas)
#                     .filter(citas.id_odontologo==id_odon).all())
#     for cit in odon_name:
#         a += 1
#         datos[a] = {
#         'id_citas':cit.id_cita,
# 		'id_paciente':cit.id_paciente,
# 		'fecha':str(cit.fecha),
# 		'hora':str(cit.hora),
#         'sede':cit.cede
  
#         } 
#     users.append(datos)
               
#     for x in datos:
#         event = [
#     {
#     'todo': x.id_paciente,
#     'fecha': str(x.fecha),
#     'hora': str(x.hora)
#     }
#                 ]
#     for i in users[0]:
#         odoncorre = (db.session.query(Users)
#                     .filter(Users.id==users[0][i]['id_paciente']).all())
#         datos[i]['nombre_paciente'] = odoncorre[0].nombre
    
#     # print(odoncorre[0].correo, correo, type(odoncorre), '\n', datos)

#     return jsonify(event)


    
   