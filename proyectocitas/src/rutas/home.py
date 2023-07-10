from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
from common.Toke import *
from Model.Usuarios import Users
from Model.citas import citas


routes_home = Blueprint("routes_home", __name__)
events = [{
        'todo': 'la fiesta de hoy',
        'fecha': '2023-06-17',         
          },
        {
        'todo': 'la fiesta',
        'fecha': '2023-06-16',     
          },
]

@routes_home.route('/eventoscalendar')
def eve():
    print("aaaaaaaaaaaaaaalllllllllhoooo")
    global events
    corre= session.get('correo_usuario')
    citass={}
    datos={}
    consul = db.session.query(Users).filter(Users.correo == corre).all()
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
    users.append(datos)
               
    for x in datos:
        events = [
    {
    'todo': x.id_paciente,
    'fecha': str(x.fecha),
    'hora': str(x.hora),
    }
                ]
    for i in users[0]:
        odoncorre = (db.session.query(Users)
                    .filter(Users.id==users[0][i]['id_paciente']).all())
        datos[i]['nombre_paciente'] = odoncorre[0].nombre
    
    # print(odoncorre[0].correo, correo, type(odoncorre), '\n', datos)
    print(events)
    return jsonify(events)

    
@routes_home.route("/index", methods=['GET'] )
def index():
    return render_template('/main/homepaciente.html')

@routes_home.route("/algo")
def otr():
    return "Buenos dias estrellitas, la tierra les dice hola"


if __name__ == '__main__':
    
    app.run(debug=True, port=5000, host='0.0.0.0')

@routes_home.route('/indexpaciente', methods=['GET'] )
def indexhome():
    token = session.get('token')
    vf = verificar_token(token)
    if vf['error'] == False:
        return render_template('/main/homepaciente.html')
    else:
        return render_template('/index.html')
    

#-----------------------------Agendar citas------------------------------

@routes_home.route('/indexagendarcitas', methods=['GET'] )
def indexagendar():
    token = session.get('token')
    vf = verificar_token(token)
    if vf['error'] == False:
        return render_template('/main/agendarcitas.html')
    else:
        return vf

@routes_home.route('/indexodontologo', methods=['GET'] )
def indexhomeodon():
    token = session.get('token')
    vf = verificar_token(token)
    if vf['error'] == False:
        return render_template('/main/homeodontologo.html')
    else:
        return render_template('/index.html')
    

@routes_home.route('/indexsecretaria', methods=['GET'] )
def indexsecretaria():    
    token = session.get('token')
    vf = verificar_token(token)
    if vf['error'] == False:
        return render_template('/main/homesecretaria.html')
    else:
        return render_template('/index.html')

@routes_home.route('/indexestadisticas', methods=['GET'] )
def indexestadistica():
    token = session.get('token')
    vf = verificar_token(token)
    if vf['error'] == False:
        return render_template('/main/estaodon.html')
    else:
        return render_template('/index.html')
    

@routes_home.route('/indexestratamientos', methods=['GET'] )
def indexestratamientos():
    token = session.get('token')
    vf = verificar_token(token)
    if vf['error'] == False:
        return render_template('/main/tratamientos.html')

    else:
        return render_template('/index.html')
    
@routes_home.route('/indexeactualizar', methods=['GET'] )
def indexdatos():
    token = session.get('token')
    vf = verificar_token(token)
    if vf['error'] == False:
        return render_template('/main/actualizardatos.html')
    else:
        return render_template('/index.html')
    

@routes_home.route('/indexconsultar', methods=['GET'] )
def indexconsultar():
    token = session.get('token')
    vf = verificar_token(token)
    if vf['error'] == False:
        return render_template('/main/consultarcitas.html')
    else:
        return render_template('/index.html')
    

@routes_home.route('/indexmisdatos', methods=['GET'] )
def indexmisdatos():
    token = session.get('token')
    vf = verificar_token(token)
    if vf['error'] == False:
        return render_template('/main/misdatos.html')
    else:
        return render_template('/index.html')



@routes_home.route('/indexmisdatas', methods=['GET'] )
def indexmisdatas():
    token = session.get('token')
    vf = verificar_token(token)
    if vf['error'] == False:
        return render_template('/main/misdatas.html')
    else:
        return render_template('/index.html')
    

@routes_home.route('/indexhistorial', methods=['GET'] )
def indexhistorial():
    token = session.get('token')
    vf = verificar_token(token)
    if vf['error'] == False:
        return render_template('/main/historial_clinico.html')
    else:
        return render_template('/index.html')
    

@routes_home.route('/indexcalendario', methods=['GET'] )
def indexcalendario():
    print("aaaaaaaaaaaaaaalllllllllhoooo")
    global events
    corre = session.get('correo_usuario')
    citass = {}
    datos = {}
    consul = db.session.query(Users).filter(Users.correo == corre).all()
    users = []
    i = 0
    a = 0
    for cor in consul:
        i += 1
        citass[i] = {
            'id': cor.id,
            'nombre': cor.nombre,
            'email': cor.correo
        }
    id_odon = citass[i]['id']

    odon_name = (db.session.query(citas)
                    .filter(citas.id_odontologo == id_odon).all())
    for cit in odon_name:
        a += 1
        datos[a] = {
            'id_citas': cit.id_cita,
            'id_paciente': cit.id_paciente,
            'fecha': str(cit.fecha),
            'hora': str(cit.hora),
            'sede': cit.sede
        }
    users.append(datos)

    for i in users[0]:
        odoncorre = (db.session.query(Users)
                     .filter(Users.id == users[0][i]['id_paciente']).all())
        datos[i]['nombre_paciente'] = odoncorre[0].nombre

    events = []

    for x in datos.values():
        event = {
            'todo': x['nombre_paciente'],
            'fecha': x['fecha'],
            'hora': x['hora'],
        }
        events.append(event)

    print(events)
    return render_template('/main/calendario.html', events=events)

@routes_home.route('/indexactu', methods=['GET'] )
def indexactualizar():
    token = session.get('token')
    vf = verificar_token(token)
    if vf['error'] == False:
        return render_template('/main/actualizar.html')
    else:
        return render_template('/index.html')
    

@routes_home.route('/indexmidato', methods=['GET'] )
def indexmidato():
    token = session.get('token')
    vf = verificar_token(token)
    if vf['error'] == False:
        return render_template('/main/midato.html')
    else:
        return render_template('/index.html')


@routes_home.route('/indextrat', methods=['GET'] )
def indextrat():
    token = session.get('token')
    vf = verificar_token(token)
    if vf['error'] == False:
        return render_template('/main/tratamientosform.html')
    else:
        return render_template('/index.html')


@routes_home.route('/indexactualizardata', methods=['GET'] )
def indexactualizardata():
    token = session.get('token')
    vf = verificar_token(token)
    if vf['error'] == False:
        return render_template('/main/actualizadata.html')
    else:
        return render_template('/index.html')


@routes_home.route('/indexvertrat', methods=['GET'] )
def indexver():
    token = session.get('token')
    vf = verificar_token(token)
    if vf['error'] == False:
        return render_template('/main/alltratamientos.html')
    else:
        return render_template('/index.html')


@routes_home.route('/indexprueba', methods=['GET'] )
def indexprueba():
    token = session.get('token')
    vf = verificar_token(token)
    if vf['error'] == False:
        return render_template('/main/consultarodon.html')
    else:
        return render_template('/index.html')

@routes_home.route('/indexpago', methods=['GET'] )
def indexpago():
    token = session.get('token')
    vf = verificar_token(token)
    if vf['error'] == False:
        return render_template('/main/pagos_pasarela.html')
    else:
        return render_template('/index.html')


@routes_home.route('/indexcertificados', methods=['GET'] )
def indexcertificados():
    token = session.get('token')
    vf = verificar_token(token)
    if vf['error'] == False:
        return render_template('/main/certificaciones.html')
    else:
        return render_template('/index.html')

@routes_home.route('/indexcalendario_secretaria', methods=['GET'] )
def indexcalendario_secretaria():
    print("aaaaaaaaaaaaaaalllllllllhoooo")
    global events
    citass = {}
    datos = {}
    consul = db.session.query(Users).filter(Users.id_roles == 2).all()
    users = []
    i = 0
    a = 0
    odon_name = (db.session.query(citas).all())
    for cit in odon_name:
        a += 1
        datos[a] = {
            'id_citas': cit.id_cita,
            'id_paciente': cit.id_paciente,
            'fecha': str(cit.fecha),
            'hora': str(cit.hora),
            'sede': cit.sede
        }
    users.append(datos)

    for i in users[0]:
        odoncorre = (db.session.query(Users)
                     .filter(Users.id == users[0][i]['id_paciente']).all())
        datos[i]['nombre_paciente'] = odoncorre[0].nombre

    events = []

    for x in datos.values():
        event = {
            'todo': x['nombre_paciente'],
            'fecha': x['fecha'],
            'hora': x['hora'],
        }
        events.append(event)

    print(events)
    return render_template('/main/calendario_secre.html', events=events)

@routes_home.route('/indexmisodon', methods=['GET'] )
def indexmisodon():
    return render_template('/main/Dentistas.html')

@routes_home.route('/indexmispac', methods=['GET'] )
def indexmispac():
    return render_template('/main/pacienteO.html')
