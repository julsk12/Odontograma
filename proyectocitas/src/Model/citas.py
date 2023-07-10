from config.db import db, app, ma

class citas(db.Model):
    __tablename__ = "tblcitas"

    id_cita = db.Column(db.Integer, primary_key=True)
    id_paciente = db.Column(db.Integer, db.ForeignKey('tblusuarios.id'))
    id_odontologo = db.Column(db.Integer, db.ForeignKey('tblusuarios.id'))
    fecha = db.Column(db.Date) 
    hora = db.Column(db.Time)
    nota = db.Column(db.String(500))
    sede = db.Column(db.String(200))

    def __init__(self, id_paciente,id_odontologo, fecha, hora, nota, sede):
        self.id_paciente = id_paciente
        self.id_odontologo= id_odontologo
        self.nota = nota
        self.fecha = fecha
        self.hora  = hora
        self.sede = sede

        with app.app_context():
            db.create_all()


class citasSchema(ma.Schema):
    class Meta:
        fields = ('id','id_paciente', 'id_odontologo', 'nota', 'hora', 'fecha', 'sede')