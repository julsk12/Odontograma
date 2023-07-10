from flask import Blueprint, request, jsonify, json
from common.Toke import *
from config.db import db, app, ma
from flask import Flask,  redirect, request, jsonify, json, session, render_template 
from sqlalchemy import text


class RolesUsuarios(db.Model):
    __tablename__ = "tblrolesusuario"


    id  = db.Column(db.Integer, primary_key=True)
    roles = db.Column(db.String(50))

    def __init__(self, roles):
        self.roles = roles
    
def create_roles():
    #verificamos si ya xien registros en la tabla
    if RolesUsuarios.query.count() == 0:
        #Crear registro de roles
        rolsecretaria = RolesUsuarios('Secretaria')
        rolodontologo = RolesUsuarios('Odontologo')
        rolpaciente = RolesUsuarios('Paciente')
        #Guardamos los registros
        db.session.add(rolsecretaria)
        db.session.add(rolodontologo)
        db.session.add(rolpaciente)
        db.session.commit()

def create_admins():
    # Verificar si ya existen registros en la tabla
    if RolesUsuarios.query.count() == 0:
        # Crear registros de administradores
        admin1 = RolesUsuarios("Secretaria")
        admin2 = RolesUsuarios("Odontologo")
        user = RolesUsuarios("Paciente")
        

        # Guardar los registros en la base de datos
        db.session.add(admin1)
        db.session.add(admin2)
        db.session.add(user)
        db.session.commit()

        # Reiniciar el valor del autoincremento del ID
        db.session.execute(text('ALTER TABLE tblrolesusuario AUTO_INCREMENT = 1;'))
        db.session.execute(text('SET @count = 0;'))
        db.session.execute(text('UPDATE tblrolesusuario SET tblrolesusuario.id = @count:= @count + 1;'))
        db.session.commit()

with app.app_context():
    db.create_all()
    create_roles()

class RolesSchema(ma.Schema):
    class Meta:
        fields = ('id','roles')