from flask import Flask, Blueprint,  redirect, request, jsonify, json, session, render_template
from config.db import *

from Model.Odontogramas import Odon, OdontoSchema
from Model.Colordiente import Colores, ColoresSchema

routes_colordientes = Blueprint("routes_colordientes", __name__)
#Roles
Colordiente_schema = ColoresSchema()
colordientes_schema = ColoresSchema(many=True)

@routes_colordientes.route('/Colordientes', methods=['GET'])
def Coloriente():    
    returnall = Colores.query.all()
   
    resultado_dientes = colordientes_schema.dump(returnall)
    print(resultado_dientes)
    return jsonify(resultado_dientes)

@routes_colordientes.route('/savecolor', methods=['POST'])
def save_datacolor():
    tooth_number = request.json['toothNumber']
    part_number = request.json['partNumber']
    color = request.json['color']
    iduser = request.json['iduser']
    print(iduser)
    print(tooth_number)
    actualizar = Colores.query.filter_by(toothNumber=tooth_number, partNumber=part_number).first()

    if actualizar:
        actualizar.color = color
        db.session.commit()
        return jsonify(message='Datos actualizado exitosamente')
    else:
        resultado = db.session.query(Odon).filter(Odon.id_paciente == iduser).order_by(-Odon.fecha_consulta).first()
        if resultado is not None:
            new_diente = Colores(tooth_number, part_number, color, resultado.id)
            db.session.add(new_diente)
            db.session.commit()
            return jsonify(message='Datos guardados exitosamente')
        else:
            return jsonify(message='Error al guardar los datos')
        # return jsonify(message='Error al actualizar los los datos')
    print(resultado)
    
@routes_colordientes.route('/getcolores', methods=['GET'])
def obtenerColores():
    iduser = request.args.get('iduser')
    print(iduser)

    resultado = db.session.query(Colores).join(Odon).filter(Odon.id_paciente == iduser).all()

    colores = []
    for entry in resultado:
        color = {
            'toothNumber': entry.toothNumber,
            'partNumber': entry.partNumber,
            'color': entry.color
        }
        colores.append(color)

    return jsonify(colores)

@routes_colordientes.route('/eliminardiente', methods=['POST'])
def eliminardiente():
    tooth_number = request.json['toothNumber']
    iduser = request.json['iduser']

    resultado = db.session.query(Colores).join(Odon).filter(Odon.id_paciente == iduser).all()
    
    if resultado:
        # Buscar el registro en la tabla Colores que coincide con el número de diente
        colores = Colores.query.filter_by(toothNumber=tooth_number, id_odontograma=iduser).first()

        # Verificar si se encontró un registro
        if colores is not None:
            # Eliminar el registro de la tabla Colores
            db.session.delete(colores)
            db.session.commit()
            return jsonify({'message': 'El color del diente fue eliminado correctamente.'})
        else:
            return jsonify({'message': 'No se encontró ningún diente con el número especificado.'})
    return jsonify({'message': 'Consulta exitosa.'})