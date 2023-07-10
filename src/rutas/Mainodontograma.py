from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
from datetime import datetime
from Model.Usuarios import UsuariosSchema, Users
routes_mainodontograma = Blueprint("routes_mainodontograma", __name__)


@routes_mainodontograma.route('/indexmainodontograma', methods=['GET'] )
def indexmainodontograma():
    
    return render_template('/main/MainOdontograma.html')

# ------------------------Aquí empizan la Validación del Token activo------------------------------

@routes_mainodontograma.route('/checktoken', methods=['GET'])
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
