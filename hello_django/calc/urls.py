from django.urls import path
from hello_django.calc.views import IndexView, Index

urlpatterns = [
    path('', IndexView.as_view()),
    path('<int:a>/<int:b>', Index.as_view(), name='calc')
]
