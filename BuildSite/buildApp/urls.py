from django.conf.urls.static import static
from django.urls import path

from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('service', views.service, name='service'),
    path('buildHome', views.buildHome, name='buildHome'),
    path('contacts', views.contacts, name='contacts'),
    path('login', views.BuildLoginView.as_view(), name='login'),
    path('logout', views.Logout.as_view(), name='logout'),
    path('register', views.registerPage, name='register'),
]
