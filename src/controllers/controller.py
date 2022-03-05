from http.client import ImproperConnectionState
from flask.views import MethodView
from src.db import mysql

class IndexController(MethodView):
    def get(seft):
        return "HelloWorld!"