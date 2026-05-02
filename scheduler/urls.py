from django.urls import path
from . import views

urlpatterns = [
    path('',          views.landing,      name='landing'),
    path('dashboard/', views.index,       name='index'),
    path('login/',    views.login_view,   name='login'),
    path('logout/',   views.logout_view,  name='logout'),
    path('generate/', views.generate,     name='generate'),
]
