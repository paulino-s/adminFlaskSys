from src.controllers.controller import *

routes = {
    "hello_route": "/", "hello_controller": HelloController.as_view("hello"),
}