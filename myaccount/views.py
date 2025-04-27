from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


def user_home(request):
    return HttpResponse('Welcome to User!')

# class UserSignupView(View):
#     def get(self, request):
#         form = 

