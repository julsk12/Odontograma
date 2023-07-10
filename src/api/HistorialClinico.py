from flask import Flask, Blueprint,  redirect, request, jsonify, json, session, render_template
from common.Toke import *
from config.db import db, app, ma
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

from Model.Historial_clinico import Historial,  HistorialesSchema
from Model.Tratamientos import Trata
from Model.Usuarios import Users
from Model.Diente import Diente
from Model.Odontogramas import Odon

routes_historial = Blueprint("routes_historial", __name__)

Historial_schema = HistorialesSchema()
Historiales_Schema = HistorialesSchema(many=True)

#Datos de la tabla citas
@routes_historial.route('/Historial', methods=['GET'])
def obtenerhistorial():    
    returnall = Historial.query.all()
    result_Historial = Historiales_Schema.dump(returnall)
    return jsonify(result_Historial)

@routes_historial.route('/eliminarhistorial/<id>', methods=['GET'] )
def eliminarhistorial(id):
    historial = Historial.query.get(id)
    db.session.delete(historial)
    db.session.commit()
    return jsonify(Historial_schema.dump(historial))

@routes_historial.route('/actualizarhistorial', methods=['POST'] )
def actualizarhistorial():
    id = request.json['id']
    paciente = request.json['id_paciente']
    tratamiento = request.json['id_tratamiento']
    medicamentos = request.json['medicamentos']
    diagnostico = request.json['diagnostico']
    fecha_creacion = request.json['fecha_creacion']
    rhistorial = Historial.query.get(id)
    rhistorial.paciente = paciente
    rhistorial.tratamiento = tratamiento
    rhistorial.medicamentos = medicamentos
    rhistorial.diagnostico = diagnostico
    rhistorial.fecha_creacion = fecha_creacion
    db.session.commit()
    return redirect('/Historial')

@routes_historial.route('/savehistorial', methods=['POST'] )
def guardar_historial():
    historial = request.json['id_paciente', 'id_odontologo', 'fecha', 'hora', 'nota']
    new_historial = Historial(historial)
    db.session.add(new_historial)
    db.session.commit()
    return redirect('/Historial')

@routes_historial.route('/head', methods=['GET'])
def head():
    correo= session.get('correo_usuario')
    datos= {}
    resultado = (db.session.query(Users,Odon)
                 .filter(Users.correo == correo, 
                Odon.id_paciente == Users.id).all())  
    users = []
    i = 0
    for usuarios, donto in resultado:
        i += 1
        users.append(datos)
        datos[i] = {
        'id':usuarios.id,
		'nombre':usuarios.nombre,
		'fecha_nacimiento':usuarios.fecha_nacimiento,
		'correo':usuarios.correo,
		'telefono':usuarios.telefono,
		'direccion': usuarios.direccion,              
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
        datos[i]['diente'] = dien.posicion_diente
        datos[i]['tipo_daño'] = dien.tipo_daño
        datos[i]['fecha_creacion'] = dien.fecha_creacion

        tratamiento = datos[i]['tratamiento']
    ultimo = (db.session.query(Trata)
            .filter(Trata.nombre_tratamiento == tratamiento).all())
    
    for trat in ultimo:
        datos[i]['duracion'] = trat.duracion
         
    print(users)
    return jsonify(datos)

@routes_historial.route('/sendemail', methods=['POST'])
def send_email():
    print("si está entrando")
    correo= session.get('correo_usuario')
    pdfData = request.json.get('pdfData')
    print(pdfData)
    # Configuración del correo electrónico
    from_email = 'odontologicpgerente@gmail.com'
    to_email = correo
    subject = 'Adjunto historial clinico'
    print(to_email)
    # Crear el mensaje de correo
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Adjuntar el PDF al mensaje
    attachment = MIMEBase('application', 'octet-stream')
    attachment.set_payload(pdfData)
    encoders.encode_base64(attachment)
    attachment.add_header('Content-Disposition', 'attachment', filename='Test.pdf')
    msg.attach(attachment)

    # Configurar el servidor SMTP y enviar el correo electrónico
    smtp_host = 'odontologicpgerente@gmail.com'
    smtp_port = 587
    smtp_username = 'Gerente Odontologico'
    smtp_password = 'panconqueso123'

    try:
        server = smtplib.SMTP(smtp_host, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.send_message(msg)
        server.quit()
        return jsonify({'message': 'Correo electrónico enviado correctamente'})
    except Exception as e:
        return jsonify({'message': 'Error al enviar el correo electrónico', 'error': str(e)}), 500


@routes_historial.route('/head2', methods=['POST'])
def head2():
    print("I try")
    id = request.json['id']
    datos = {}
    resultado = db.session.query(Users, Odon).filter(Odon.id_paciente == id, Odon.id_paciente == Users.id).all()
    users = []
    i = 0
    id_odontologo = None  # Default value
    id_user = None  # Default value
    tratamiento = None  # Default value
    for usuarios, donto in resultado:
        i += 1
        datos[i] = {
            'id': usuarios.id,
            'nombre': usuarios.nombre,
            'fecha_nacimiento': usuarios.fecha_nacimiento,
            'correo': usuarios.correo,
            'telefono': usuarios.telefono,
            'direccion': usuarios.direccion,
            'id_odontologo': donto.id_odontologo
        }
        id_odontologo = datos[i]['id_odontologo']
        id_user = datos[i]['id']
    odon_name = db.session.query(Users).filter(Users.id == id_odontologo).all()
    for odon in odon_name:
        datos[i]['nombre_odontologo'] = odon.nombre

    otro = db.session.query(Odon, Diente).filter(Odon.id_paciente == id_user, Diente.id_odontograma == Odon.id).all()
    for oton, dien in otro:
        datos[i]['diente'] = dien.Numero_diente
        datos[i]['tipo_daño'] = dien.estado_diente
        datos[i]['fecha_creacion'] = dien.fecha_registro
        datos[i]['tratamiento'] = dien.tratamiento

        tratamiento = datos[i]['tratamiento']
    ultimo = db.session.query(Trata).filter(Trata.nombre == tratamiento).all()

    for trat in ultimo:
        datos[i]['duracion'] = trat.duracion

    print(users)
    return jsonify(datos)
