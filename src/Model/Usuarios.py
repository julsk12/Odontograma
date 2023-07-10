from flask import Blueprint, request, jsonify, json
from common.Toke import *
from config.db import db, app, ma
from flask import Flask,  redirect, request, jsonify, json, session, render_template 
import secrets

class Users(db.Model):
    __tablename__ = "tblusuarios"

    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    nombre = db.Column(db.String(200))
    fecha_nacimiento = db.Column(db.Date)
    correo = db.Column(db.String(200))
    password = db.Column(db.String(200))
    telefono = db.Column(db.String(200))
    direccion = db.Column(db.String(200))
    fecha_registro = db.Column(db.DateTime, nullable=False)
    token = db.Column(db.String(50))
    token_expiration = db.Column(db.DateTime)
    direccion_ip = db.Column(db.String(50)) 
    id_roles = db.Column(db.Integer, db.ForeignKey('tblrolesusuario.id'))

    def __init__(self, id, nombre, fecha_nacimiento, correo, password, telefono, direccion, fecha_registro, direccion_ip, id_roles):
        self.id = id
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento
        self.correo = correo
        self.password = password
        self.telefono = telefono
        self.direccion= direccion
        self.fecha_registro = fecha_registro
        self.direccion_ip = direccion_ip
        self.id_roles = id_roles

    def generate_token(self):
        self.token = secrets.token_hex(16)
        self.token_expiration = datetime.now() + timedelta(minutes=5)

    def is_token_valid(self):
        return datetime.now() <= self.token_expiration
    
    
    with app.app_context():
            db.create_all()
    
    # def delete_token(self):
    #     self.token = None
    #     self.token_expiration = None
    #     db.session.commit()


class UsuariosSchema(ma.Schema):
    class Meta:
        fields = ('id','nombre', 'fecha_nacimiento', 'correo', 'password', 'telefono', 'direccion'
                  'fecha_registro', 'direccion_ip', 'id_roles')
