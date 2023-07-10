from config.db import db, app, ma

class citas(db.Model):
    __tablename__ = "tblcitas"

    id_cita = db.Column(db.Integer, primary_key=True)
    id_paciente = db.Column(db.Integer, db.ForeignKey('tblusuarios.id'))
    id_odontologo = db.Column(db.Integer, db.ForeignKey('tblusuarios.id'))
    fecha = db.Column(db.Date) 
    hora = db.Column(db.Time)
    nota = db.Column(db.String(500))

    def __init__(self, nota,id_odontologo, hora, fecha, id_paciente):
        self.nota = nota
        self.id_odontologo= id_odontologo
        self.hora  = hora
        self.fecha = fecha
        self.id_paciente = id_paciente

        with app.app_context():
            db.create_all()

class citasSchema(ma.Schema):
    class Meta:
        fields = ('id','id_paciente', 'id_odontologo', 'nota', 'hora', 'fecha')