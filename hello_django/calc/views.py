from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


class IndexView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('calc')


class Index(View):
    def calc(self, request, *args, **kwargs):
        return
