from django.shortcuts import render
from lms.models import *
from django.db import connection

def listamiscursos(usern):
    try:
        with connection.cursor() as cursor:
            cursor.execute('call ListarMiscursos(%s)', usern)
            results = cursor.fetchall()
        return results
    finally:
        cursor.close()