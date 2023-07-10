from config.db import db, app, ma

class Odon(db.Model):
    __tablename__ = "tblodontogramas"

    id = db.Column(db.Integer, primary_key=True)
    tratamiento_recomendado = db.Column(db.String(200))
    id_paciente = db.Column(db.Integer, db.ForeignKey('tblusuarios.id'))
    id_odontologo = db.Column(db.Integer, db.ForeignKey('tblusuarios.id'))
    fecha_consulta = db.Column(db.Date)
    descripcion = db.Column(db.Text)

    def __init__(self, tratamiento_recomendado, id_paciente, id_odontologo, fecha_consulta, descripcion):
        self.tratamiento_recomendado = tratamiento_recomendado
        self.id_paciente = id_paciente
        self.id_odontologo = id_odontologo
        self.fecha_consulta = fecha_consulta
        self.descripcion= descripcion

        with app.app_context():
            db.create_all()


class OdontoSchema(ma.Schema):
    class Meta:
        fields = ('id', 'tratamiento_recomendado', 'id_paciente', 'id_odontologo', 'fecha_consulta', 'descripcion')