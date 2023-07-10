
#from api.user import *
from flask import Flask,  redirect, request, jsonify, json, session, render_template
from config.db import db, app, ma
from common.Toke import *



from api.roles import routes_roles
from api.pago import  routes_pagos
from api.Deta_pagos import routes_dpagos
from api.tratamientos import routes_tratamientos
from api.facturas import routes_facturas
from api.citas import routes_citas
from api.odontograma import routes_odonto
from api.dientes import routes_dientes
from api.HistorialClinico import routes_historial
from api.user import routes_user

from rutas.home import routes_home
from rutas.agencita import routes_agencitas

app.register_blueprint(routes_roles, url_prefix="/api")
app.register_blueprint(routes_tratamientos, url_prefix="/api")
app.register_blueprint(routes_user, url_prefix="/api")
app.register_blueprint(routes_citas, url_prefix="/api")
app.register_blueprint(routes_pagos, url_prefix="/api")
app.register_blueprint(routes_facturas, url_prefix="/api")
app.register_blueprint(routes_odonto, url_prefix="/api")
app.register_blueprint(routes_historial, url_prefix="/api")
app.register_blueprint(routes_dientes, url_prefix="/api")
app.register_blueprint(routes_dpagos, url_prefix="/api")
app.register_blueprint(routes_home, url_prefix="/fronted")
app.register_blueprint(routes_agencitas, url_prefix="/fronted")

# app.register_blueprint(routes_agencitas, url_prefix="/fronted")

#------------------------------------------------
@app.route("/", methods=["GET"])
def index():
    return render_template('/index.html')

@app.route("/algo")
def otr():
    return render_template('/main/homeodontologo.html',)

# @app.route('/indexagendarcitas', methods=['GET'] )
# def indexhome():
#     return render_template('/main/agendarcitas.html')

if __name__ == '__main__':
   # load_dotenv()
    app.run(debug=True, port=5000, host='0.0.0.0')
    


#<----------------------------------------------------------------->
'''
@app.route('/consultar3tabla', methods=['GET'])
def consultar3tablas():
    datos= {}
    resultado = db.session.query(Employee,Department, Company). \
        select_from(Employee).join(Department).join(Company).all()
    i=0
    for employee,department,company  in resultado:
        i+=1
        datos[i]={
           
                'Ename': employee.name,
                'Dname': department.name,
                'Cname': company.name          
        }
    print(datos)
    return "Algo"
'''