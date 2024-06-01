# from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.

@api_view(['GET'])
def getData(request):
    person = {'Surname':'Fuentiblanca', 'FirstName':'Igy Luis','MiddleName':' Veloso','Address':'424 Kamatsili St. Tondo, Manila','Phone no':'09618527194'}
    return Response(person)