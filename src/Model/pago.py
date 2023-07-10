from config.db import db, app, ma

class pagos(db.Model):
    __tablename__ = "tblpagos"

    id_pago = db.Column(db.Integer, primary_key=True)
    id_citas = db.Column(db.Integer, db.ForeignKey('tblcitas.id_cita'))
    id_tratamientos = db.Column(db.Integer, db.ForeignKey('tbltratamientos.id'))
    metodo = db.Column(db.String(200))
    fecha = db.Column(db.Date) 
    monto = db.Column(db.Integer)

    def __init__(self,id_paciente, id_factura,metodo, fecha, monto):
        self.id_paciente= id_paciente
        self.id_factura  = id_factura
        self.metodo = metodo
        self.fecha = fecha
        self.monto = monto
        

        with app.app_context():
            db.create_all()

class pagoSchema(ma.Schema):
    class Meta:
        fields = ('id_pago','id_paciente', 'id_factura', 'fecha', 'monto')