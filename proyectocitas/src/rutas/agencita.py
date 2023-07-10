from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
from common.Toke import *

routes_agencitas = Blueprint("routes_agencitas", __name__)


@routes_agencitas.route('/indexagendarcitas', methods=['GET'] )
def indexhom():
    token = session.get('token')
    vf = verificar_token(token)
    if vf['error'] == False:
        return render_template('/main/agendarcitas.html')
    else:
        return render_template('/index.html')

@routes_agencitas.route('/indexconsultarcitas', methods=['GET'] )
def indexhome():
    token = session.get('token')
    vf = verificar_token(token)
    if vf['error'] == False:
        return render_template('/main/consultarcitas.html')
    else:
        return render_template('/index.html')
    

