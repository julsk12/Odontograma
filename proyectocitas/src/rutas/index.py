from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
from Model.Usuarios import Users
from common.Toke import *
routes_index = Blueprint("routes_index", __name__)


