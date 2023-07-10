

from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template, flash, url_for, abort
from datetime import datetime, timedelta
from functools import wraps
from datetime import date
from datetime import datetime
from datetime import timedelta
from sqlalchemy import func, extract
from Model.Usuarios import Users
from Model.Odontogramas import Odon
from datetime import datetime, date
import calendar
from calendar import monthrange

from Model.Usuarios import Users, UsuariosSchema

now = datetime.now()

routes_HomeIndexLight = Blueprint("routes_HomeIndexLight", __name__)



@routes_HomeIndexLight.route('/indexHomeIndexLight', methods=['GET'])
def indexmainodontograma():
    id_roles = int(request.cookies.get('id_roles'))  # Obtener el valor de 'id_roles' de la cookie

    if id_roles == 2:
        return render_template('/main/Homeindexlight.html')
    else:
        abort(401)  # Acceso no autorizado

# ------------------------Aquí empizan la Validación del Token activo------------------------------

@routes_HomeIndexLight.route('/checktoken', methods=['GET'])
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





# ------------------------Aquí empizan las estadisticas del dashboard------------------------------
estimated_patients = 0
@routes_HomeIndexLight.route('/estimacion1', methods=['POST'])
def guardar_estimacion():
    global estimated_patients  # Accede a la variable global

    estimation = request.json.get('estimacion')  # Obtiene la estimación enviada por el usuario
    estimated_patients = int(estimation)  # Actualiza la variable global con la nueva estimación

    return 'Estimación guardada correctamente'
@routes_HomeIndexLight.route("/estadisticasdashboard", methods=["POST"])
def estadisticas():
    datos = {}
    paciente= estimated_patients/4
    correo = session.get('correo_usuario')
    print(correo)
    fecha_actual = date.today()
    primer_dia_mes = fecha_actual.replace(day=1)
    _, ultimo_dia_mes = calendar.monthrange(primer_dia_mes.year, primer_dia_mes.month)
    ultimo_dia_mes = primer_dia_mes.replace(day=ultimo_dia_mes)
    stats = []

    first_day = primer_dia_mes - timedelta(days=primer_dia_mes.weekday())
    i = 0
    while first_day <= ultimo_dia_mes:
        i += 1
        last_day = first_day + timedelta(days=6)

        num_pacientes = (
            db.session.query(func.count(Users.id))
            .join(Odon, Odon.id_odontologo == Users.id)
            .filter(
                Odon.fecha_consulta.between(first_day, last_day), Users.correo == correo
            )
            .scalar()
        )

        porcentaje = round((num_pacientes / paciente) * 100)
        print(porcentaje)
        datos[i] = {
            "semana": f'{first_day.strftime("%d/%m/%Y")} - {last_day.strftime("%d/%m/%Y")}',
            "pacientes_atendidos": num_pacientes,
            "porcentaje": porcentaje,
        }
        stats.append(datos)

        first_day = last_day + timedelta(days=1)

    return jsonify(datos)


@routes_HomeIndexLight.route("/total", methods=["GET"])
def estadisticasuser():
    datos = {}
    total_pacientes = (
        db.session.query(func.count(Users.id)).filter(Users.id_roles == "3").scalar()
    )
    datos["clientes"] = total_pacientes
    return jsonify(datos)


@routes_HomeIndexLight.route("/odontotal", methods=["GET"])
def estadisticaodon():
    datos = {}
    total_odontologos = (
        db.session.query(func.count(Users.id)).filter(Users.id_roles == "2").scalar()
    )
    stats = []
    datos["odontologo"] = total_odontologos
    stats.append(datos)
    return jsonify(datos)


@routes_HomeIndexLight.route("/paratratamientos", methods=["GET"])
def estadisticames():
    print("funciona")
    global estimated_patients
    datos = {}
    correo = session.get('correo_usuario')
    print(correo)
    fecha_actual = date.today()
    primer_dia_mes = date(fecha_actual.year, fecha_actual.month, 1)
    ultimo_dia_mes = date(
        fecha_actual.year,
        fecha_actual.month,
        calendar.monthrange(fecha_actual.year, fecha_actual.month)[1],
    )

    stats = []

    first_day = primer_dia_mes
    i = 0
    while first_day <= fecha_actual:
        i += 1
        last_day = date(
            first_day.year,
            first_day.month,
            calendar.monthrange(first_day.year, first_day.month)[1],
        )

        num_pacientes = (
            db.session.query(func.count(Users.id))
            .join(Odon, Odon.id_odontologo == Users.id)
            .filter(
                Odon.fecha_consulta.between(first_day, last_day), Users.correo == correo
            )
            .scalar()
        )

        porcentaje = round((num_pacientes / estimated_patients) * 100)

        datos[i] = {
            "mes": first_day.strftime("%B, %Y"),
            "pacientes_atendidos": num_pacientes,
            "porcentaje": porcentaje,
        }

        first_day = date(
            first_day.year + 1 if first_day.month == 12 else first_day.year,
            (first_day.month % 12) + 1,
            1,
        )
    stats.append(datos)
    print(stats)
    return jsonify(datos[1])
