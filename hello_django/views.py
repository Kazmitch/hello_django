from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView, View
from django.urls import reverse


class Index(View):

    template_name = 'index.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['who'] = 'World'
    #     return context

    def get(self, request):
        return redirect('calc', a=40, b=2)
