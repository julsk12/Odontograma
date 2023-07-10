from config.db import db, app, ma

class facturas(db.Model):
    __tablename__ = "tblfacturas"

    id_factura = db.Column(db.Integer, primary_key=True)
    id_pago = db.Column(db.Integer, db.ForeignKey('tblpagos.id_pago'))
    fecha = db.Column(db.Date) 
    total = db.Column(db.Integer)

    def __init__(self,id_pago, fecha, total):
        self.id_pago= id_pago
        self.fecha = fecha
        self.total = total
        

        with app.app_context():
            db.create_all()

class facturasSchema(ma.Schema):
    class Meta:
        fields = ('id_factura','id_pago', 'fecha', 'total')