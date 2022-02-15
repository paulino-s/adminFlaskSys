from http.client import ImproperConnectionState
from flask.views import MethodView

class HelloController(MethodView):

    def get(seft):
        return "HelloWorld!"