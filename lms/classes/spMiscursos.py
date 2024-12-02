from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from lms.models import *
from django.db import connection

def ListarMiscursos(request,usern):
    with connection.cursor() as cursor:
        cursor.callproc('ListarMiscursos', usern)
        results = cursor.fetchall()
    return results