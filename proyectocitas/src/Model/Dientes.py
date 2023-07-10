from config.db import db, app, ma

class Diente(db.Model):
    __tablename__ = "tbldientes"

    id = db.Column(db.Integer, primary_key=True)
    posicion_diente = db.Column(db.Integer)
    seccion_diente = db.Column(db.Integer)
    tipo_diente = db.Column(db.String(200))
    tipo_daño = db.Column(db.Text)
    fecha_creacion = db.Column(db.Date)
    id_odontograma = db.Column(db.Integer, db.ForeignKey('tblodontogramas.id'))

    def __init__(self, posicion_diente, seccion_diente, fecha_nacimiento, tipo_diente, tipo_daño, direccion, fecha_registro, id_odontograma):
        self.posicion_diente = posicion_diente
        self.seccion_diente = seccion_diente
        self.fecha_nacimiento = fecha_nacimiento
        self.tipo_diente = tipo_diente
        self.tipo_daño = tipo_daño
        self.direccion= direccion
        self.fecha_registro = fecha_registro
        self.id_odontograma = id_odontograma

        with app.app_context():
            db.create_all()


class DienteSchema(ma.Schema):
    class Mea:
        fields = ('id', 'posicion_diente', 'seccion_diente', 'tipo_diente', 'tipo_daño','fecha_creacion', 'id_odontograma')