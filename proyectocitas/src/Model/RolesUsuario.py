from config.db import db, app, ma 


class RolesUsuarios(db.Model):
    __tablename__ = "tblrolesusuario"
    id  = db.Column(db.Integer, primary_key=True)
    roles = db.Column(db.String(50))

    def __init__(self, roles):
        self.roles = roles
        
def create_roles():
    #verificamos si ya xien registros en la tabla
    if RolesUsuarios.query.count() == 0:
        #Crear registro de roles
        rolsecretaria = RolesUsuarios('Secretaria')
        rolodontologo = RolesUsuarios('Odontologo')
        rolpaciente = RolesUsuarios('Paciente')
        #Guardamos los registros
        db.session.add(rolsecretaria)
        db.session.add(rolodontologo)
        db.session.add(rolpaciente)
        db.session.commit()


with app.app_context():
   db.create_all()
   create_roles()


class RolesSchema(ma.Schema):
    class Meta:
        fields = ('id','roles')