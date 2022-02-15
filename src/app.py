from flask import Flask
from src.routes.routes import *

app = Flask(__name__)

#Rutas de la aplicaci[on]

app.add_url_rule(routes["hello_route"], view_func=routes["hello_controller"])