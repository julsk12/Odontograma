from config.db import db, app, ma

class Odon(db.Model):
    __tablename__ = "tblodontogramas"

    id = db.Column(db.Integer, primary_key=True)
    id_paciente = db.Column(db.Integer, db.ForeignKey('tblusuarios.id'))
    id_odontologo = db.Column(db.Integer, db.ForeignKey('tblusuarios.id'))
    fecha_consulta = db.Column(db.Date)

    def __init__(self, id_paciente, id_odontologo, fecha_consulta):
        self.id_paciente = id_paciente
        self.id_odontologo = id_odontologo
        self.fecha_consulta = fecha_consulta

        with app.app_context():
            db.create_all()


class OdontoSchema(ma.Schema):
    class Meta:
        fields = ('id', 'id_paciente', 'id_odontologo', 'fecha_consulta')