from config.db import db, app, ma

class Users(db.Model):
    __tablename__ = "tblusuarios"

    id = db.Column(db.Integer, primary_key=True, autoincrement = False)
    nombre = db.Column(db.String(200))
    fecha_nacimiento = db.Column(db.String(200))
    correo = db.Column(db.String(200))
    password = db.Column(db.String(200))
    telefono = db.Column(db.Integer)
    direccion = db.Column(db.String(200))
    fecha_registro = db.Column(db.Date)
    fecha_actualizacion = db.Column(db.Date)
    id_roles = db.Column(db.Integer, db.ForeignKey('tblrolesusuario.id'))


    def __init__(self, id, nombre, fecha_nacimiento, correo, password, telefono, direccion, fecha_registro,fecha_actualizacion, id_roles):
        self.id = id
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento
        self.correo = correo
        self.password = password
        self.telefono = telefono
        self.direccion= direccion
        self.fecha_registro = fecha_registro
        self.fecha_actualizacion = fecha_actualizacion
        self.id_roles = id_roles

with app.app_context():
    db.create_all()


class UsuariosSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nombre', 'fecha_nacimiento', 'correo', 'password', 'telefono', 'direccion'
                  'fecha_registro', 'fecha_actualizacion', 'id_roles')


