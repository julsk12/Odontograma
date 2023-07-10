# from flask import Flask, Blueprint,  redirect, request, jsonify, json, session, render_template
# from common.Toke import *
# from config.db import db, app, ma

# from Model.Odontogramas import Odon, OdontoSchema

# routes_odonto = Blueprint("routes_odonto", __name__)
# #Roles
# odonto_schema = OdontoSchema()
# Odonto_schema = OdontoSchema(many=True)

# @routes_odonto.route('/indexodonto', methods=['GET'] )
# def indexdiente():
    
#     return "Hola Mundo!!" 

# @routes_odonto.route('/Odontograma', methods=['GET'])
# def Dientee():    
#     returnall = Odon.query.all()
   
#     resultado_odonto = Odonto_schema.dump(returnall)
#     return jsonify(resultado_odonto)


# @routes_odonto.route('/saveodonto', methods=['POST'] )
# def guardar_odon():
#     tratamiento_recomendado = request.json['tratamineto_recomendado']
#     id_paciente = request.json['id_paciente']
#     id_odontologo = request.json['id_odontologo']
#     fecha_consulta = request.json['fecha_consulta']
#     descripcion = request.json['descripcion']

#     new_odonto = Odon(tratamiento_recomendado, id_paciente, id_odontologo, fecha_consulta, descripcion)
#     db.session.add(new_odonto)
#     db.session.commit()
#     return redirect('/Odontograma')


# @routes_odonto.route('/eliminarodonto/<id>', methods=['GET'] )
# def eliminar_odon(id):
#     id = Odon.query.get(id)
#     db.session.delete(id)
#     db.session.commit()
#     return jsonify(Odonto_schema.dump(id)) 

# @routes_odonto.route('/actualizarodonto', methods=['POST'] )
# def actualizar_odon():
#     tratamiento_recomendado = request.json['tratamineto_recomendado']
#     id_paciente = request.json['id_paciente']
#     id_odontologo = request.json['id_odontologo']
#     fecha_consulta = request.json['fecha_consulta']
#     descripcion = request.json['descripcion']
#     odonto = Odon.query.get(id)
#     odonto.tratamiento_recomendado = tratamiento_recomendado
#     odonto.id_paciente = id_paciente
#     odonto.id_odontologo = id_odontologo
#     odonto.fecha_consulta = fecha_consulta
#     odonto.descripcion = descripcion
#     db.session.commit()
#     return redirect('/Odontograma')