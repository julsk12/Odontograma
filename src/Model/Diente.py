from config.db import db, app, ma

class Diente(db.Model):
    __tablename__ = "tbldientes"

    id = db.Column(db.Integer, primary_key=True)
    Numero_diente = db.Column(db.Integer)
    seccion_diente = db.Column(db.String(50))
    estado_diente = db.Column(db.String(50))
    observaciones = db.Column(db.String(50))
    tratamiento = db.Column(db.String(50))
    fecha_registro = db.Column(db.Date)
    id_odontograma = db.Column(db.Integer, db.ForeignKey('tblodontogramas.id'))

    def __init__(self, Numero_diente, seccion_diente, estado_diente, observaciones, tratamiento, fecha_registro, id_odontograma):
        self.Numero_diente = Numero_diente
        self.seccion_diente = seccion_diente
        self.estado_diente = estado_diente
        self.observaciones = observaciones
        self.tratamiento = tratamiento
        self.fecha_registro = fecha_registro
        self.id_odontograma = id_odontograma

        with app.app_context():
            db.create_all()


class DienteSchema(ma.Schema):
    class Meta:
        fields = ('id', 'Numero_diente', 'seccion_diente', 'estado_diente', 'observaciones', 'tratamiento', 'fecha_registro','id_odontograma')
