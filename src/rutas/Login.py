from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template, url_for, flash, sessions, make_response
from common.Toke import *
from random import randint
import smtplib
import email
from datetime import datetime, timezone
import secrets
import hashlib
from flask import sessions
import random
from datetime import datetime
import socket
from Model.Usuarios import Users, UsuariosSchema
from Model.RolesUsuario import RolesUsuarios, RolesSchema

routes_login = Blueprint("routes_login", __name__)


@routes_login.route('/indexlogin', methods=['GET'] )
def indexlogin():
    
    return render_template('/main/LoginandRegister.html')


@routes_login.route('/guardaruser', methods=['POST'])
def save_user():
    fullid = request.form['fullid']
    fullname = request.form['fullname']
    fullfecha_nacimiento = request.form['fullfecha_nacimiento']
    fullcorreo = request.form['fullcorreo']
    fullpassword = request.form['fullpassword']
    fulltelefono = request.form['fulltelefono']
    fulldireccion = request.form['fulldireccion']
    rol_id = int(request.form['rol_id'])  # Obtener el ID de rol seleccionado

    # Verificar si el ID ya existe en la base de datos
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

    # Obtener la dirección IP del usuario
    direccion_ip = request.remote_addr

    fecha_registro = datetime.now()

    new_user = Users(id=fullid, nombre=fullname, fecha_nacimiento=fullfecha_nacimiento, correo=fullcorreo,
                     password=fullpassword, telefono=fulltelefono, direccion=fulldireccion, fecha_registro=fecha_registro,
                     direccion_ip=direccion_ip, id_roles=rol_id)

    db.session.add(new_user)
    db.session.commit()

    response_body = {
        'message': 'Registro guardado exitosamente'
    }
    status = 200
    headers = {'Content-Type': 'application/json'}

    return jsonify(response_body), status, headers




@routes_login.route('/login', methods=['POST'])
def login():
    fullcorreo = request.json['fullcorreo']
    fullpassword = request.json['fullpassword']

    # Verificar si el usuario y la contraseña son válidos en la base de datos
    user = Users.query.filter_by(correo=fullcorreo, password=fullpassword).first()

    if user:
        if user.token and not user.is_token_valid():
            # El token ha expirado
            user.generate_token()  # Generar un nuevo token
            db.session.commit()
            response_body = {'message': 'Tus credenciales han expirado', 'token': user.token}
            status = 200
        else:
            # Las credenciales son válidas y el token es válido o no existe
            session['user_id'] = user.id
            session['correo_usuario'] = fullcorreo
            session['nombre_usuario'] = user.nombre
            if not user.token:
                user.generate_token()
            db.session.commit()
            response_body = {'message': 'Inicio de sesión exitoso', 'token': user.token, 'id_roles': user.id_roles}
            status = 200
    else:
        # Credenciales inválidas
        response_body = {'message': 'Credenciales inválidas'}
        status = 401

    response = make_response(jsonify(response_body), status)
    response.set_cookie('id_roles', str(user.id_roles))  # Configurar la cookie 'id_roles'
    return response


@routes_login.route('/verificarcorreo', methods=['POST'])
def verificarcorreo():
    fullcorreo = request.json['fullcorreo']
    user1 = Users.query.filter_by(correo=fullcorreo).first()
    if user1:
        # Si el correo electrónico existe en la base de datos, devuelve el mensaje de éxito
        session['user_id'] = user1.id
        response_body = {'message': 'El correo electrónico existe en la base de datos'}
        status = 200
    else:
        # Si el correo electrónico no existe en la base de datos, devuelve el mensaje de error
        response_body = {'message': 'El correo electrónico no existe en la base de datos'}
        status = 401
    headers = {'Content-Type': 'application/json'}
    return jsonify(response_body), status, headers


#OJO SI QUIERE REINCIAR LOS ID MODIFICAR U ORDENAR SU POSICION DEBO USAR ESTE CONSULTA EN MI MYSQL#
# SET @autoid :=0;
# update nombre_de_tu_tabla set id= @autoid := (@autoid+1);
# alter table nombre_de_tu_tabla AUTO_increment = 1;
#----------------------------------------------------------#

@routes_login.route('/forgotpassword', methods=['POST'])
def forgotpassword():
    fullcorreo = request.json['fullcorreo']

    # Check if the user has exceeded the request limit
    now = datetime.now(timezone.utc)  # Convert to offset-aware datetime in UTC
    elapsed_time = timedelta(minutes=5)  # Valor predeterminado de 5 minutos
    request_count = 0


    if 'last_request_time' in session and 'request_count' in session:
        last_request_time = session['last_request_time']
        request_count = session['request_count']
        elapsed_time = now - last_request_time

        # Calculate the time remaining until the limit resets
        time_to_wait = timedelta(minutes=5 + (request_count - 1)) - elapsed_time
        hours = time_to_wait.seconds // 3600
        minutes = (time_to_wait.seconds % 3600) // 60
        seconds = time_to_wait.seconds % 60

        if elapsed_time < timedelta(minutes=5 + (request_count - 1)) and request_count >= 5:
            return jsonify({'message': f'Too many requests. Please try again in {hours} hour(s), {minutes} minute(s), and {seconds} second(s).', 'time_to_wait': time_to_wait.total_seconds()}), 429

    # Check if the user exists in the database
    user = Users.query.filter_by(correo=fullcorreo).first()
    print(fullcorreo)
    if user:
        # Generate a verification code based on the user's email hash
        code_list = random.sample(range(10), 4)
        code = ''.join(str(digit) for digit in code_list)

        # Save the code in the session
        session['verification_code'] = code

        # Send an email to the user with the code
        sender_email = 'denteloofficial@gmail.com'
        sender_password = 'nyppfccmwhalhdyx'
        receiver_email = fullcorreo
        message = f'Subject: Verification Code\n\nYour verification code is: {code}'
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, message)

        # Reset the request count if the time has elapsed
        if elapsed_time >= timedelta(minutes=5 + (request_count - 1)):
            session['request_count'] = 1
        else:
            # Update the session with the request count and the last request time
            session['request_count'] = session.get('request_count', 0) + 1
        session['last_request_time'] = now

        return jsonify({'message': 'Verification code sent.'})
    else:
        return jsonify({'message': 'Email not found.'}), 404


    
    
@routes_login.route('/verificarcode', methods=['POST'])
def verificarcode():
    verification_code = request.json['verification_code']
    stored_code = session.get('verification_code')
    
    if verification_code == stored_code:
        # Si el código es correcto, redireccionar al usuario a la página de cambio de contraseña
        response_body = {'message': 'Código verificado correctamente'}
        status = 200
        session.pop('verification_code', None)
        return jsonify(response_body), status
    else:
        # Si el código no es correcto, devolver un error
        response_body = {'message': 'El código ingresado es incorrecto. Inténtalo de nuevo.'}
        status = 401
        return jsonify(response_body), status
    

@routes_login.route('/actualizar_contrasena', methods=['POST'])
def actualizar_contrasena():
    correo = request.json['email']
    nueva_contrasena = request.json['nueva_contrasena']
    print(correo)
    print(nueva_contrasena)

    usuario = Users.query.filter_by(correo=correo).first()

    if usuario:
        usuario.password = nueva_contrasena
        db.session.commit()
        return "Contraseña actualizada correctamente"
    else:
        return "Usuario no encontrado"
    
@routes_login.route('/obtener_datos', methods=['POST'])
def obtener_datos():
    fullemail = request.json['fullemail']
    users = Users.query.filter_by(correo=fullemail).first()
    
    if users:
        Users_schema = UsuariosSchema()
        datos = Users_schema.dump(Users)
        return jsonify(datos)
    
    return jsonify({'mensaje': 'Correo electrónico no encontrado'}), 404

    

