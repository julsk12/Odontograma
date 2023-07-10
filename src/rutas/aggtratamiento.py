from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template, abort
from datetime import date
from datetime import datetime
from datetime import timedelta
from sqlalchemy import func, extract
from Model.Usuarios import Users, UsuariosSchema
from Model.RolesUsuario import RolesUsuarios
from Model.citas import citas
from Model.Odontogramas import Odon
from datetime import datetime, date
import calendar
from calendar import monthrange


now = datetime.now()

routes_indexagg = Blueprint("routes_indexagg", __name__)




@routes_indexagg.route('/indexagg', methods=['GET'])
def indexmainodontograma():
    id_roles = int(request.cookies.get('id_roles'))  # Obtener el valor de 'id_roles' de la cookie

    if id_roles == 1:
        return render_template('/main/aggtratamientos.html')
    else:
        abort(401)  # Acceso no autorizado


# ------------------------Aquí empizan la Validación del Token activo------------------------------

@routes_indexagg.route('/checktoken', methods=['GET'])
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