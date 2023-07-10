from config.db import db, app, ma

class Trata(db.Model):
    __tablename__ = "tbltratamientos"

    id = db.Column(db.Integer, primary_key=True)
    nombre_tratamiento = db.Column(db.String(200))
    descripcion = db.Column(db.Text)
    duracion = db.Column(db.String(200))
    costo = db.Column(db.Double)

    def __init__(self, nombre_tratamiento, descripcion, duracion, costo):
        self.nombre_tratamiento = nombre_tratamiento
        self.descripcion = descripcion
        self.duracion = duracion
        self.costo= costo

        with app.app_context():
            db.create_all()


class TratamientosSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nombre_tratamiento', 'descripcion', 'duracion', 'costo')