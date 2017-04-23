from django.conf.urls import url
from . import views #importa del actual paquete

urlpatterns = [
    url(r'^$', views.index, name='index')]


