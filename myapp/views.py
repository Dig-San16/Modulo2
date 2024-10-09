from django.shortcuts import render

# Create your views here
from django.http import HttpResponse
from django.views import View

class PostView(View):
    def post(self, request, *args, **kwargs):
        return HttpResponse("Hello, world!")
