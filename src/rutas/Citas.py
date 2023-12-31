from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template,abort
from datetime import datetime
from Model.Odontogramas import Odon, OdontoSchema
from Model.Usuarios import Users, UsuariosSchema
routes_CitaPlantilla = Blueprint("routes_CitaPlantilla", __name__)

@routes_CitaPlantilla.route('/IndexCita', methods=['GET'])
def IndexCita():
    id_roles = int(request.cookies.get('id_roles'))  # Obtener el valor de 'id_roles' de la cookie

    if id_roles == 2:
        return render_template('/main/Citas.html')
    else:
        abort(401)  # Acceso no autorizado


@routes_CitaPlantilla.route('/checktoken', methods=['GET'])
def checktoken():
    user_id = session.get('user_id')
    if user_id:
        user = Registro.query.get(user_id)

        if user:
            print('Token Expiration:', user.token_expiration)
            now = datetime.now()
            print('Current Datetime:', now)

            auth_header = request.headers.get('Authorization', '')
            token = auth_header.replace('Bearer ', '') if auth_header.startswith('Bearer ') else None

            if user.token == token:
                # El token coincide
                if user.is_token_valid():
                    print('Is Token Valid: True')
                    return jsonify({'token_expired': False}), 200

                # Token expirado, eliminarlo del objeto del usuario
                user.delete_token()
                print('Token deleted from user object')
                return jsonify({'token_expired': True, 'token': user.token, 'token_expiration': user.token_expiration}), 401

    print('Is Token Valid: False')
    return jsonify({'token_expired': True}), 401


@routes_CitaPlantilla.route('/consultargrama', methods=['GET'])
def sal():
    print("one a monment")
    # correo= session.get('correo_usuario')
    citass={}
    datos= {}
    consul = db.session.query(Users).filter(Users.id_roles == 3).all()
    # resultado = (db.session.query(citas).all())  
    users = []
    i = 0
    a = 0
    for cor in consul:
        i += 1
        datos[i] = {
        'id':cor.id,
		'nombre':cor.nombre,
		'email':cor.correo
        }
    users.append(datos)
    print(datos)
    return jsonify(datos)


@routes_CitaPlantilla.route('/consultabusqueda', methods=['POST'])
def sol():
    # correo= session.get('correo_usuario')
    busca=request.json['busca']
    print("buscar", busca)
    datos= {}
    consul = db.session.query(Users).filter(Users.id==busca, Users.id_roles==3).all()
    print("la consulta es:", consul)
    # resultado = (db.session.query(citas).all())  
    users = []
    i = 0
    a = 0
    for cor in consul:
        i += 1
        datos[i] = {
        'id':cor.id,
		'nombre':cor.nombre,
		'email':cor.correo
        }
    users.append(datos)
    print("no está entrando")
    return jsonify(datos)


@routes_CitaPlantilla.route('/consultanombre', methods=['POST'])
def arena():
    # correo= session.get('correo_usuario')
    busca=request.json['busca']
    print("buscar", busca)
    datos= {}
    consul = db.session.query(Users).filter(Users.nombre==busca, Users.id_roles==3).all()
    print("la consulta es:", consul)
    # resultado = (db.session.query(citas).all())  
    users = []
    i = 0
    a = 0
    for cor in consul:
        i += 1
        datos[i] = {
        'id':cor.id,
		'nombre':cor.nombre,
		'email':cor.correo
        }
    users.append(datos)
    print("no está entrando, en la segunda")
    return jsonify(datos)
