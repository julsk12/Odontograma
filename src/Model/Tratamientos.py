from config.db import db, app, ma

class Trata(db.Model):
    __tablename__ = "tbltratamientos"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(200))
    descripcion = db.Column(db.Text)
    duracion = db.Column(db.Integer)
    costo = db.Column(db.Double)

    def __init__(self, nombre, descripcion, duracion, costo):
        self.nombre = nombre
        self.descripcion = descripcion
        self.duracion = duracion
        self.costo= costo

        with app.app_context():
            db.create_all()


class TratamientosSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nombre', 'descripcion', 'duracion', 'costo')