from config.db import db, app, ma

class Dpagos(db.Model):
    __tablename__ = "tbldeta_pagos"

    id = db.Column(db.Integer, primary_key=True)
    id_pago = db.Column(db.Integer, db.ForeignKey('tblpagos.id_pago'))
    id_tratamientos = db.Column(db.Integer, db.ForeignKey('tbltratamientos.id'))
    fecha= db.Column(db.Date)

    def __init__(self, id_pago, id_tratamientos, fecha):
        self.id_pago = id_pago
        self.id_tratamientos = id_tratamientos
        self.fecha = fecha

        with app.app_context():
            db.create_all()


class DpagoSchema(ma.Schema):
    class Meta:
        fields = ('id', 'id_pago', 'id_tratamientos', 'fecha')