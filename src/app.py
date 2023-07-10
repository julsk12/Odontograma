# import os
# import time
# import threading
# import signal
# import sys
# import subprocess
# import pkg_resources

# # Códigos de colores
# ERROR_COLOR = '\033[91m'
# SUCCESS_COLOR = '\033[92m'
# END_COLOR = '\033[0m'

# # Línea de separación
# SEPARATOR_LINE = '-' * 50

# def verificar_instalacion_virtualenv():
#     print(f'{SEPARATOR_LINE}\nPaso 1\n{SEPARATOR_LINE}')
#     print('Verificando la instalación de virtualenv por 5 segundos...')
#     time.sleep(5)
#     try:
#         output = os.popen('pip show virtualenv').read()
#         if output:
#             print(f'{SUCCESS_COLOR}El paso 1 ya está completado.{END_COLOR}')
#         else:
#             print(f'{ERROR_COLOR}Instalando virtualenv...{END_COLOR}')
#             ruta_instalacion = os.path.join(os.getcwd(), 'env')  # Ruta de instalación en la carpeta principal
#             os.system(f'pip install virtualenv --target={ruta_instalacion}')
#             print(f'{SUCCESS_COLOR}El paso 1 se completó correctamente.{END_COLOR}')
#     except Exception as e:
#         print(f'{ERROR_COLOR}Ocurrió un error al verificar la instalación:{END_COLOR}')
#         print(e)

# def verificar_entorno_virtual():
#     print(f'{SEPARATOR_LINE}\nPaso 2\n{SEPARATOR_LINE}')
#     print(f'{SUCCESS_COLOR}Verificando el entorno virtual por 5 segundos...{END_COLOR}')
#     time.sleep(5)
#     env_folder = os.path.join(os.path.dirname(os.getcwd()), 'env')
#     if not os.path.exists(env_folder):
#         print(f'{ERROR_COLOR}No se encontró el entorno virtual.{END_COLOR}')
#         print(f'{ERROR_COLOR}Creando el entorno virtual...{END_COLOR}')
#         os.system(f'virtualenv {env_folder}')
#         print(f'{SUCCESS_COLOR}El entorno virtual se creó correctamente.{END_COLOR}')
#     else:
#         print(f'{SUCCESS_COLOR}El paso 2 ya está completado.{END_COLOR}')

# def activar_entorno_virtual():
#     print(f'{SEPARATOR_LINE}\nPaso 3\n{SEPARATOR_LINE}')
#     print(f'{SUCCESS_COLOR}Activando el entorno virtual...{END_COLOR}')

#     activate_script = os.path.join(os.path.dirname(os.getcwd()), 'env', 'Scripts', 'activate.bat')
#     subprocess.call(activate_script, shell=True)

#     # Verificar si el entorno virtual se activó correctamente
#     if 'VIRTUAL_ENV' in os.environ:
#         print(f'{SUCCESS_COLOR}El entorno virtual se activó correctamente.{END_COLOR}')
#     else:
#         print(f'{ERROR_COLOR}No se está activo.{END_COLOR}')
#         print(f'{SUCCESS_COLOR}Activando...{END_COLOR}')
#         subprocess.call(activate_script, shell=True)
#         print(f'{SUCCESS_COLOR}Activación exitosa{END_COLOR}')

# def verificar_dependencias():
#     print(f'{SEPARATOR_LINE}\nPaso 4\n{SEPARATOR_LINE}')
#     print('Verificando la instalación de las dependencias esenciales...')
#     dependencies = [
#         'flask', 'flask-sqlalchemy', 'flask-marshmallow',
#         'marshmallow', 'pymysql'
#     ]
    
#     for dependency in dependencies:
#         print(f'Verificando {dependency}...')
#         try:
#             output = os.popen(f'pip show {dependency}').read()
#             if output:
#                 print(f'{SUCCESS_COLOR}{dependency} está instalado.{END_COLOR}')
#             else:
#                 print(f'{ERROR_COLOR}{dependency} no está instalado.{END_COLOR}')
#                 print(f'{SUCCESS_COLOR}Instalando {dependency}...{END_COLOR}')
#                 os.system(f'pip install {dependency}')
#                 print(f'{SUCCESS_COLOR}{dependency} se instaló correctamente.{END_COLOR}')
#         except Exception as e:
#             print(f'{ERROR_COLOR}Ocurrió un error al verificar {dependency}:{END_COLOR}')
#             print(e)

# def input_with_timeout(prompt, timeout):
#     result = [None]
#     event = threading.Event()

#     def input_thread():
#         try:
#             result[0] = input(prompt)
#         except EOFError:
#             pass
#         finally:
#             event.set()

#     input_thread = threading.Thread(target=input_thread)
#     input_thread.start()

#     event.wait(timeout)

#     return result[0]

# def paso_4():
#     print(f'{SEPARATOR_LINE}\nPaso 5-Anexo de Dependencia\n{SEPARATOR_LINE}')
#     print('¿Deseas agregar otras dependencias? (Sí/No)')
#     answer = input_with_timeout('> ', 5)

#     if answer is None:
#         print(f'{SUCCESS_COLOR}No se proporcionó ninguna respuesta. Pasando al siguiente paso.{END_COLOR}')
#         return

#     if answer.lower() == 'sí' or answer.lower() == 'si':
#         print('¿Cuántas dependencias deseas agregar?')
#         try:
#             num_dependencies = int(input_with_timeout('> ', 5))
#             for i in range(num_dependencies):
#                 print(f'Ingresa el nombre de la dependencia #{i+1}:')
#                 dependency_name = input_with_timeout('> ', 5)
#                 print(f'{SUCCESS_COLOR}Instalando {dependency_name}...{END_COLOR}')
#                 os.system(f'pip install {dependency_name}')
#                 print(f'{SUCCESS_COLOR}{dependency_name} se instaló correctamente.{END_COLOR}')
#         except (TypeError, ValueError):
#             print(f'{ERROR_COLOR}Respuesta inválida. Pasando al siguiente paso.{END_COLOR}')
#     else:
#         print(f'{SUCCESS_COLOR}No se agregaron dependencias adicionales. Pasando al siguiente paso.{END_COLOR}')

# def verificar_requirements():
#     required_libraries = [
#         'flask==2.0.1',
#         'flask-sqlalchemy==2.5.1',
#         'flask-marshmallow==0.15.1',
#         'marshmallow==3.13.0',
#         'pymysql==1.0.2'
#     ]

#     librerias_faltantes = []
#     for libreria in required_libraries:
#         libreria_nombre, libreria_version = libreria.split('==')
#         try:
#             __import__(libreria_nombre)
#         except ImportError:
#             librerias_faltantes.append(libreria)

#     if librerias_faltantes:
#         print('Faltan las siguientes librerías requeridas:')
#         for libreria in librerias_faltantes:
#             print(libreria)
#         generar_requirements_txt(librerias_faltantes)
#         print('Instalando las dependencias desde requirements.txt...')
#         os.system('pip install -r requirements.txt')
#     else:
#         print('Todas las librerías requeridas ya están instaladas.')

# def generar_requirements_txt(librerias_faltantes):
#     ruta_proyecto = os.path.dirname(os.path.abspath(__file__))
#     ruta_requirements = os.path.join(ruta_proyecto, '..', 'requirements.txt')
#     with open(ruta_requirements, 'w') as file:
#         for libreria in librerias_faltantes:
#             file.write(libreria + '\n')

# def handle_interrupt(signal, frame):
#     print(f'\n{ERROR_COLOR}La ejecución del programa fue interrumpida.{END_COLOR}')
#     os._exit(1)

# signal.signal(signal.SIGINT, handle_interrupt)

# verificar_instalacion_virtualenv()

# # Verificar el entorno virtual
# verificar_entorno_virtual()

# # Activar el entorno virtual
# activar_entorno_virtual()

# # Verificar las dependencias
# verificar_dependencias()

# # Paso 4 - Anexo de Dependencia
# paso_4()

# # Verificar las dependencias nuevamente
# verificar_requirements()


from flask import Flask,  redirect, request, jsonify, json, session, render_template
from config.db import db, app, ma
#https://docs.sqlalchemy.org/en/14/core/type_basics.html
#https://flask.palletsprojects.com/en/2.2.x/

#Importar routes API
from api.tratamientos import routes_tratamientos
from api.dientes import *
from api.Colordiente import *
from api.odontograma import routes_odonto
from api.facturas import routes_facturas
from api.HistorialClinico import routes_historial
from api.Deta_pagos import routes_dpagos
from api.pago import  routes_pagos
from api.citas import routes_citas
from api.user import routes_user
from api.roles import routes_roles

#rutas | ¡¡¡RECUERDA PRIMERO IMPORTAR LA RUTA Y DESPUÉS AGREGARLO EN LA UBICACION DE RUTAS!!!! |
from rutas.odontograma import routes_odontograma
from rutas.Login import routes_login
from rutas.Mainodontograma import routes_mainodontograma
from rutas.Homeindexlight import routes_HomeIndexLight
from rutas.Citas import routes_CitaPlantilla
from rutas.Tratamientos import routes_Tratamientos
from rutas.Dentistas import routes_Dentistas
from rutas.Pacientes import routes_Pacientes
from rutas.Historial import routes_Historial
from rutas.Homeindexsecretaria import routes_HomeIndexS
from rutas.aggtratamiento import routes_indexagg
from rutas.odontologoS import routes_odon
#ubicacion del api
app.register_blueprint(routes_roles, url_prefix="/api")
app.register_blueprint(routes_dientes, url_prefix="/api")
app.register_blueprint(routes_colordientes, url_prefix="/api")
app.register_blueprint(routes_citas, url_prefix="/api")
app.register_blueprint(routes_facturas, url_prefix="/api")
app.register_blueprint(routes_historial, url_prefix="/api")
app.register_blueprint(routes_tratamientos, url_prefix="/api")
app.register_blueprint(routes_pagos, url_prefix="/api")
app.register_blueprint(routes_user, url_prefix="/api")
app.register_blueprint(routes_odonto, url_prefix="/api")

#ubicacion rutas
app.register_blueprint(routes_odontograma, url_prefix="/fronted")
app.register_blueprint(routes_login, url_prefix="/fronted")
app.register_blueprint(routes_mainodontograma, url_prefix="/fronted")
app.register_blueprint(routes_HomeIndexLight, url_prefix="/fronted")
app.register_blueprint(routes_CitaPlantilla, url_prefix="/fronted")
app.register_blueprint(routes_Tratamientos, url_prefix="/fronted")
app.register_blueprint(routes_Dentistas, url_prefix="/fronted")
app.register_blueprint(routes_Pacientes, url_prefix="/fronted")
app.register_blueprint(routes_Historial, url_prefix="/fronted")
app.register_blueprint(routes_HomeIndexS, url_prefix="/fronted")
app.register_blueprint(routes_indexagg, url_prefix="/fronted")
app.register_blueprint(routes_odon, url_prefix="/fronted")



@app.route("/")
def index():
    titulo= "Pagina Principal"
    return render_template('main/MainOdontograma.html', titles=titulo)

@app.route('/datos')
def obtener_datos():
    # Obtener datos de la sesión
    id_odontologo = session.get('user_id')
    correo_usuario = session.get('correo_usuario')
    nombre = session.get('nombre_usuario')
    return f'Id: {id_odontologo}, Nombre: {nombre}, Correo: {correo_usuario}'



@app.route("/algo")
def otr():
    return "hola mondongo del master-v2"

# Datos de la tabla de Editoriales
if __name__ == '__main__':
   # load_dotenv()
    app.run(debug=True, port=5000, host='0.0.0.0')