from django.conf.urls.static import static
from django.urls import path

from . import views
from BuildSite import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('service', views.service, name='service'),
    path('service/<slug:service_slug>/', views.showService, name='serviceID'),
    path('service/category/<slug:category_id>/', views.showCategory, name='category'),
    path('contacts', views.contacts, name='contacts'),
    path('login', views.BuildLoginView.as_view(), name='login'),
    path('logout', views.Logout.as_view(), name='logout'),
    path('register', views.registerPage, name='register'),
    path('makeOrder/<str:id>/', views.makeOrder, name='makeOrder')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)