from django.shortcuts import render
from rest_framework import views
from rest_framework.response import Response

class HelloWorldView(views.APIView):
    def get(self, request, *args, **kwargs):
        return Response({"message": "Hello, world!"})
