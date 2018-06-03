from django.urls import path

from . import views

urlpatterns = [
    path('render/<str:expr>', views.renderlatex, name='render_latex'),
]
