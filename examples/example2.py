from django.core.wsgi import get_wsgi_application

import os

def critico(id):
    global x;
    x = x + id
    print("Hilo = " + str(id) + " => " + str(x))
    x = 1