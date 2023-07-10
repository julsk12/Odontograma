from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template, abort
from datetime import datetime
import random
from Model.Usuarios import Users, UsuariosSchema
from Model.RolesUsuario import RolesUsuarios, RolesSchema

routes_Pacientes = Blueprint("routes_Pacientes", __name__)


@routes_Pacientes.route('/IndexPacientes', methods=['GET'])
def IndexPacientes():
    id_roles = int(request.cookies.get('id_roles'))  # Obtener el valor de 'id_roles' de la cookie

    if id_roles == 2:
        return render_template('/main/Pacientes.html')
    else:
        abort(401)  # Acceso no autorizado

@routes_Pacientes.route('/guardapacientes', methods=['POST'])
def save_customers():
    fullid = request.form['fullid']
    fullname = request.form['fullname']
    fullfecha_nacimiento = request.form['fullfecha_nacimiento']
    fullcorreo = request.form['fullcorreo']
    fullpassword = request.form['fullpassword']
    fulltelefono = request.form['fulltelefono']
    fulldireccion = request.form['fulldireccion']

    existing_user = Users.query.filter(
        (Users.id == fullid) |
        (Users.correo == fullcorreo) |
        (Users.nombre == fullname) |
        (Users.password == fullpassword)
    ).first()
    
    if existing_user:
        response_body = {
            'message': 'El ID, correo electrónico o nombre ya están registrados'
        }
        status = 400
        headers = {'Content-Type': 'application/json'}
        return jsonify(response_body), status, headers


    

    # Obtener la dirección IP del usuario que se está registrando
    direccion_ip = request.remote_addr

    fecha_registro = datetime.now()

    # GUARDADO DE ROL en la tabla tblrolesusuarios
    rol_id = guardar_rol('Paciente')

    new_user = Users(
        id=fullid,
        nombre=fullname,
        fecha_nacimiento=fullfecha_nacimiento,
        correo=fullcorreo,
        password=fullpassword,
        telefono=fulltelefono,
        direccion=fulldireccion,
        fecha_registro=fecha_registro,
        direccion_ip=direccion_ip,
        id_roles=rol_id
    )
    db.session.add(new_user)
    db.session.commit()

    response_body = {
        'message': 'Registro guardado exitosamente'
    }
    status = 200
    headers = {'Content-Type': 'application/json'}

    return jsonify(response_body), status, headers

def guardar_rol(nombre_rol):
    # Buscar el rol en la tabla tblrolesusuarios por el nombre
    rol = RolesUsuarios.query.filter_by(roles=nombre_rol).first()

    if rol is None:
        nuevo_rol = RolesUsuarios(roles=nombre_rol)
        db.session.add(nuevo_rol)
        db.session.commit()
        return nuevo_rol.id

    return rol.id


# ------------------------Aquí empizan la Validación del Token activo------------------------------

@routes_Pacientes.route('/checktoken', methods=['GET'])
def checktoken():
    user_id = session.get('user_id')
    if user_id:
        user = Users.query.get(user_id)

        if user:
            print('Token Expiration:', user.token_expiration)
            now = datetime.now()
            print('Current Datetime:', now)

            if user.token == request.headers.get('Authorization')[7:]:
                if user.is_token_valid():
                    print('Is Token Valid: True')
                    return jsonify({'token_expired': False}), 200

                # Token expired or does not exist, remove it from the user object
                user.token = None
                user.token_expiration = None
                db.session.commit()  # Confirmar los cambios en la base de datos
                print('Token deleted from user object')

    print('Is Token Valid: False')
    return jsonify({'token_expired': True}), 401

# ------------------------Fin de la Validación del Token activo------------------------------




@routes_Pacientes.route('/indexpac', methods=['GET'])
def indexpac():
    id_roles = int(request.cookies.get('id_roles'))  # Obtener el valor de 'id_roles' de la cookie

    if id_roles == 1:
        return render_template('/main/pacienteO.html')
    else:
        abort(401)  # Acceso no autorizado