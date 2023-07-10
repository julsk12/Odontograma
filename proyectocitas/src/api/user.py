from datetime import datetime
from common.Toke import *
from config.db import db, app, ma
from flask import (
    Flask,
    Blueprint,
    redirect,
    request,
    jsonify,
    json,
    session,
    render_template,
)
from sqlalchemy import func, extract
from Model.Usuarios import Users, UsuariosSchema
from Model.RolesUsuario import RolesUsuarios
from Model.citas import citas
now = datetime.now()
routes_user = Blueprint("routes_user", __name__)

# usuario
Usuario_Schema = UsuariosSchema()
Usuarios_Schema = UsuariosSchema(many=True)

@routes_user.route("/Usuarios", methods=["GET"])
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
    print(usuarios)
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
        user_token = correo
        pass_token = password
        # Llamada a la función generar_token para obtener el token y los datos
        tokeng = generar_token(user_token, pass_token)
        token = tokeng['token']
        vf = verificar_token(token)
        if vf['error'] == False:
            # Busca el usuario en la base de datos
            if not resultado:
                return "a" #jsonify({"": ""+})

            # Si el inicio de sesión es exitoso, redirige al usuario a la vista correspondiente en función de su id_roles
        if resultado.RolesUsuarios.roles == "Secretaria":
                session['correo_usuario'] = correo
                session['token'] = token
                return jsonify({"rol": "Secretaria"})

            # return redirect("/fronted/indexagendarcitas")
        elif resultado.RolesUsuarios.roles == "Odontologo":
                session['token'] = token
                session['correo_usuario'] = correo
                return jsonify({"rol": "Odontologo"})

                # return redirect("/main/homeodontologo.html")
        elif resultado.RolesUsuarios.roles == "Paciente":
                session['token'] = token
                session['correo_usuario'] = correo
                return jsonify({"rol": "Paciente"})

                # return redirect("/main/homepaciente.html")
        else:
             return vf

        

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
    print(correo)
    stats = []

    first_day = fecha_inicio - timedelta(days=fecha_inicio.weekday())
    i=0
    while first_day <= fecha_fin:
        i += 1
        last_day = first_day + timedelta(days=6)

        num_pacientes = db.session.query(func.count(Users.id)).join(citas, citas.id_odontologo == Users.id).\
            filter(citas.fecha.between(first_day, last_day), Users.correo==correo).scalar()

        porcentaje = round((num_pacientes / 10) * 100)
        print(porcentaje)
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
    print(correo)
    stats = []

    numDmes=(fecha_fin - fecha_inicio).days+1

    first_day = fecha_inicio.replace(day=1)
    last_day = fecha_inicio.replace(day=28) + timedelta(days=4)
    ultiDmes= last_day -  timedelta(days=last_day.day)

    num_pacientes = db.session.query(func.count(Users.id)).join(citas, citas.id_odontologo == Users.id).\
            filter(citas.fecha.between(first_day, last_day), Users.correo==correo).scalar()

    porcentaje = round((num_pacientes / 40) * 100)

    

    datos={
            'mes': first_day.strftime('%B  %Y'),
            'pacientes_atendidos': num_pacientes,
            'porcentaje': porcentaje
        }
    
    return jsonify(datos)

@routes_user.route('/actualizardatos', methods=['POST'] )
def actualizardatos():
    correo= session.get('correo_usuario')
    resultado = (db.session.query(Users).filter(Users.correo==correo).first())
    nombre = request.json['nombre']
    correoo =request.json['correo']
    telefono= request.json['telefono']
    direccion= request.json['direccion']
    password= request.json['password']
    fecha_actualizacion = now.date()
    print(nombre, correo, telefono, correoo, password)
    
    if resultado is not None:
        id=resultado.id
        fecha_nacimiento=resultado.fecha_nacimiento
        fecha_registro =resultado.fecha_registro
        users = Users.query.filter_by(correo=correo).first()
        users.id = id
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

@routes_user.route('/cerrar_sesion', methods=['POST'])
def cerrar_sesion():
    print("llego")
    datos = request.json
    dato = datos['sesion']
    if dato == "sesion_cerrada":
        if 'token' in session:
            print("elimino")
            del session['token']
            return ""
        else:
            return ""

@routes_user.route('/movimiento', methods=['POST'])
def movimiento():
    datos = request.json
    dato = datos['movi']
    if dato == "se movio":
            token = session.get('token')
            vf = verificar_token(token)
            if vf['error'] == False:
                print("token valido")
                return ""
            else:
                print("token vencido")
                return "algo"

    
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
