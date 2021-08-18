from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


class IndexView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('calc')


class Index(View):

    def get(self, request, a, b, *args, **kwargs):
        return render(request, 'calc/sum.html', context={'result': a + b, 'who': 'Ivan'})


class History(View):

    def get(self, request):
        pass
