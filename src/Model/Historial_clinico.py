from config.db import db, app, ma

class Historial(db.Model):
    __tablename__ = "tblhistorial_clinico"

    id = db.Column(db.Integer, primary_key=True)
    id_paciente = db.Column(db.Integer, db.ForeignKey('tblusuarios.id'))
    id_tratamiento = db.Column(db.Integer, db.ForeignKey('tbltratamientos.id'))
    medicamentos = db.Column(db.String(300))
    diagnostico = db.Column(db.String(500))
    fecha_creacion = db.Column(db.Date)

    def __init__(self, medicamentos, diagnostico, id_tratamiento, fecha_creacion, id_paciente):
        self.medicamentos = medicamentos
        self.diagnostico = diagnostico
        self.id_tratamiento= id_tratamiento
        self.fecha_creacion = fecha_creacion
        self.id_paciente = id_paciente

        with app.app_context():
            db.create_all()


class HistorialesSchema(ma.Schema):
    class Meta:
        fields = ('id','id_paciente', 'id_tratamiento', 'medicamentos', 'diagnostico', 'fecha_creacion')