from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template, abort
from datetime import datetime
routes_Historial = Blueprint("routes_Historial", __name__)
from Model.Usuarios import Users, UsuariosSchema


@routes_Historial.route('/IndexHistorial', methods=['GET'])
def IndexHistorial():
    id_roles = int(request.cookies.get('id_roles'))  # Obtener el valor de 'id_roles' de la cookie

    if id_roles == 1 & 2:
        return render_template('/main/Historial.html')
    else:
        abort(401)  # Acceso no autorizado

# @routes_Historial.route('/ShowUsers', methods=['GET'] )
# def Show_Users():


#     ArrayUser = {}
#     resultado = db.session.query(Registro).select_from(Registro).all()
#     User=0
#     Array = []

#     for atributos in resultado:
#         User+=1	       
#         ArrayUser[User] = {
#         'id':atributos.id,
# 		'NombreCompleto':atributos.NombreCompleto,
# 		'CorreoElectronico':atributos.CorreoElectronico,                                                    
# 		'Rol':atributos.Rol,                                                    
# 		'Contrasena':atributos.Contrasena,                                                                                                       
#         }
#         Array.append(ArrayUser)
#     return jsonify(ArrayUser)


# ------------------------Aquí empizan la Validación del Token activo------------------------------

@routes_Historial.route('/checktoken', methods=['GET'])
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