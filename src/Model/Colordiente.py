from config.db import db, app, ma

class Colores(db.Model):
    __tablename__ = "tblcolordiente"

    id = db.Column(db.Integer, primary_key=True)
    toothNumber = db.Column(db.Integer)
    partNumber = db.Column(db.Integer)
    color = db.Column(db.Integer)
    id_odontograma = db.Column(db.Integer, db.ForeignKey('tblodontogramas.id'))

    def __init__(self, toothNumber, partNumber, color, id_odontograma):
        self.toothNumber = toothNumber
        self.partNumber = partNumber
        self.color = color
        self.id_odontograma = id_odontograma

        with app.app_context():
            db.create_all()


class ColoresSchema(ma.Schema):
    class Meta:
        fields = ('id', 'toothNumber', 'partNumber', 'color', 'id_odontograma')