from django.urls import path

from . import views

app_name = 'menu'

urlpatterns = [
    path('', views.index, name='main_menu'),
    path('menu/<path:path>/', views.draw_menu, name='draw'),
]
