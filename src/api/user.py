from datetime import datetime
from common.Toke import *
from config.db import db, app, ma
from flask import (Flask,Blueprint,redirect,request,jsonify,json,session,render_template,)
from sqlalchemy import func, extract
from Model.Usuarios import Users, UsuariosSchema
from Model.RolesUsuario import RolesUsuarios
from Model.citas import citas
from Model.Odontogramas import Odon
from datetime import datetime, date
import calendar
from calendar import monthrange
from flask import Flask, Blueprint, redirect, request, jsonify, json, session, render_template
from Model.Usuarios import Users, UsuariosSchema

now = datetime.now()
routes_user = Blueprint("routes_user", __name__)

# usuario
Usuario_Schema = UsuariosSchema()
Usuarios_Schema = UsuariosSchema(many=True)


@routes_user.route('/Usuarios', methods=['GET'])
def usuarios():    
    returnall = Users.query.all()
    resultado_usuarios = Usuarios_Schema.dump(returnall)
    return jsonify(resultado_usuarios)


# crud de usuarios
@routes_user.route("/eliminar_Users/<id>", methods=["GET"])
def eliminar_users(id):
    id_user = Users.query.get(id)
    db.session.delete(id_user)
    db.session.commit()
    return jsonify(UsuariosSchema.dump(id_user))


@routes_user.route("/actualizarUsers", methods=["POST"])
def actualizar_users():
    id = request.json["id"]
    nombre = request.json["nombre"]
    fecha_nacimiento = request.json["fecha_nacimiento"]
    correo = request.json["correo"]
    password = request.json["password"]
    telefono = request.json["telefono"]
    direccion = request.json["direccion"]
    fecha_registro = request.json["fecha_registro"]
    fecha_actualizacion = request.json["fecha_actualizacion"]
    users = Users.query.get(id)
    users.nombre = nombre
    users.fecha_nacimiento = fecha_nacimiento
    users.correo = correo
    users.telefono = telefono
    users.password = password
    users.direccion = direccion
    users.fecha_registro = fecha_registro
    users.fecha_actualizacion = fecha_actualizacion
    db.session.commit()
    return redirect("/Usuarios")


@routes_user.route("/save_Users", methods=["POST"])
def guardar_Users():
    usuarios = request.json[
        "id, nombre, fecha_nacimiento, correo, password, telefono, direccion,fecha_registro, fecha_actualizacion,id_roles"
    ]
    new_Users = Users(usuarios)
    db.session.add(new_Users)
    db.session.commit()
    return redirect("/Usuarios")


@routes_user.route("/save_registro", methods=["POST"])
def registrar():
    id = request.form["id"]
    nombre = request.form["nombre"]
    fecha_nacimiento= request.form["fecha_nacimiento"] 
    correo = request.form["correo"]
    password = request.form["password"]
    telefono=request.form["telefono"]
    direccion= request.form["direccion"]
    fecha_registro = now.date()
    id_roles = request.form["id_roles"]
    new_registro = Users(id, nombre, fecha_nacimiento, correo, password, telefono, direccion, fecha_registro, "", id_roles)
    db.session.add(new_registro)
    db.session.commit()
    return ""


@app.route("/login", methods=["POST"])
def login():
        dct = request.json
        correo = request.json["correo"]
        password = request.json["password"]
        resultado = (
        db.session.query(Users, RolesUsuarios)
        .filter(
            Users.correo == correo,
            Users.password == password,
            Users.id_roles == RolesUsuarios.id
        ).first()
        )

        # Busca el usuario en la base de datos
        if not resultado:
            return "a" #jsonify({"": ""+})

        # Si el inicio de sesión es exitoso, redirige al usuario a la vista correspondiente en función de su id_roles
        if resultado.RolesUsuarios.roles == 1:
            session['correo_usuario'] = correo
            return jsonify({"rol": "Secretaria"})
            # return redirect("/fronted/indexagendarcitas")
        elif resultado.RolesUsuarios.roles == 2:
            # session['correo_usuario'] = correo
            return jsonify({"rol": "Odontologo"})
        elif resultado.RolesUsuarios.roles == 3:
            session['correo_usuario'] = correo
            return jsonify({"rol": "Paciente"})
            # return redirect("/main/homepaciente.html")

@routes_user.route('/misdatos', methods=['GET'])
def misdatos():
    correo= session.get('correo_usuario')
    datos= {}
    resultado = db.session.query(Users).select_from(Users).filter(Users.correo == correo).all()
    users = []
    i = 0
    for usuarios in resultado:
        i += 1
        datos[i] = {
        'id':usuarios.id,
		'nombre':usuarios.nombre,
		'fecha_nacimiento':usuarios.fecha_nacimiento,
		'correo':usuarios.correo,
		'password':usuarios.password,
		'telefono':usuarios.telefono,
		'direccion': usuarios.direccion,              
		'fecha_registro': usuarios.fecha_registro,
        'rol': usuarios.id_roles                      
        }
    users.append(datos)
    return jsonify(datos)

@app.route('/estadisticas', methods=['POST'])
def estadisticas():
    datos= {}
    correo= session.get('correo_usuario')
    fecha_inicio = datetime.strptime(request.json['fecha_inicio'], '%Y-%m-%d').date()
    fecha_fin = datetime.strptime(request.json['fecha_fin'], '%Y-%m-%d').date()
    stats = []

    first_day = fecha_inicio - timedelta(days=fecha_inicio.weekday())
    i=0
    while first_day <= fecha_fin:
        i += 1
        last_day = first_day + timedelta(days=6)

        num_pacientes = db.session.query(func.count(Users.id)).join(citas, citas.id_odontologo == Users.id).\
            filter(citas.fecha.between(first_day, last_day), Users.correo==correo).scalar()

        porcentaje = round((num_pacientes / 10) * 100)
        datos[i] ={
            'semana': f'{first_day.strftime("%d/%m/%Y")} - {last_day.strftime("%d/%m/%Y")}',
            'pacientes_atendidos': num_pacientes,
            'porcentaje': porcentaje
        }
        stats.append(datos)

        first_day = last_day + timedelta(days=1)

    return jsonify(datos)

@app.route('/estadisticasmensuales', methods=['POST'])
def estadisticames():
    datos= {}
    correo= session.get('correo_usuario')
    fecha_inicio = datetime.strptime(request.json['fecha_inicio'], '%Y-%m-%d').date()
    fecha_fin = datetime.strptime(request.json['fecha_fin'], '%Y-%m-%d').date()
    stats = []

    numDmes=(fecha_fin - fecha_inicio).days+1

    first_day = fecha_inicio.replace(day=1)
    last_day = fecha_inicio.replace(day=28) + timedelta(days=4)
    ultiDmes= last_day -  timedelta(days=last_day.day)

    num_pacientes = db.session.query(func.count(Users.id)).join(Odon, Odon.id_odontologo == Users.id).\
            filter(Odon.fecha.between(first_day, last_day), Users.correo==correo).scalar()

    porcentaje = round((num_pacientes / 40) * 100)

    

    datos={
            'mes': first_day.strftime('%B  %Y'),
            'pacientes_atendidos': num_pacientes,
            'porcentaje': porcentaje
        }
    
    return jsonify(datos)

@routes_user.route('/actualizardatos', methods=['POST'] )
def actualizardatos():
    idvalue = request.json['id']
    print(idvalue)
    resultado = Users.query.filter(Users.id==idvalue).first()
    print(resultado)
    nombre = request.json['nombre']
    correoo =request.json['correo']
    telefono= request.json['telefono']
    direccion= request.json['direccion']
    password= request.json['password']
    fecha_actualizacion = now.date()
    
    if resultado is not None:
        fecha_nacimiento=resultado.fecha_nacimiento
        fecha_registro =resultado.fecha_registro
        users = Users.query.filter(Users.id==idvalue).first()
        users.id = idvalue
        users.nombre = nombre
        users.fecha_nacimiento = fecha_nacimiento
        users.correo = correoo
        users.password= password
        users.telefono = telefono
        users.direccion= direccion
        users.fecha_registro=fecha_registro
        users.fecha_actualizacion= fecha_actualizacion
        db.session.commit()
        return "Datos actualizados correctamente"
    else:
        return "Error: No se actualizaron los datos"
    


# ------------------------------tabla odntologos-----------------------------------------
@routes_user.route('/misodon', methods=['GET'])
def misodon():
    datos= {}
    resultado = db.session.query(Users).filter(Users.id_roles == 2).all()
    users = []
    i = 0
    for usuarios in resultado:
        i += 1
        datos[i] = {
        'id':usuarios.id,
		'nombre':usuarios.nombre,
		'fecha_nacimiento':usuarios.fecha_nacimiento,
		'correo':usuarios.correo,
		'telefono':usuarios.telefono
        }
    users.append(datos)
    return jsonify(datos)

@routes_user.route('/mispac', methods=['GET'])
def mispac():
    datos= {}
    resultado = db.session.query(Users).filter(Users.id_roles == 3).all()
    users = []
    i = 0
    for usuarios in resultado:
        i += 1
        datos[i] = {
        'id':usuarios.id,
		'nombre':usuarios.nombre,
		'fecha_nacimiento':usuarios.fecha_nacimiento,
		'correo':usuarios.correo,
		'telefono':usuarios.telefono
        }
    users.append(datos)
    return jsonify(datos)

@routes_user.route('/misecret', methods=['GET'])
def miSc():
    datos= {}
    resultado = db.session.query(Users).filter(Users.id_roles == 1).all()
    users = []
    i = 0
    for usuarios in resultado:
        i += 1
        datos[i] = {
        'id':usuarios.id,
		'nombre':usuarios.nombre,
		'fecha_nacimiento':usuarios.fecha_nacimiento,
		'correo':usuarios.correo,
		'telefono':usuarios.telefono
        }
    users.append(datos)
    return jsonify(datos)

@routes_user.route('/eliminarU', methods=['DELETE'] )
def eliminarperso():
    id = request.json['id']
    ced = Users.query.filter_by(id=id).first()
    if ced:
        db.session.delete(ced)
        db.session.commit()
        print(id)
        print(ced)
        return 'Registro eliminado', 200
    else:
        return 'Registro no encontrado', 404