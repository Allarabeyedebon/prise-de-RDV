from django.contrib import admin
from django.urls import path
from .views import *



urlpatterns = [
    path('', home_view, name= 'index'),
    path('agence/', agence_view, name= 'agence'),
    path('gestionnaire/', gestionnaire_view, name= 'gestionnaire'),
    path('detail_agence/<agence_id>',detail_agence_view, name='detail_agence'),
    path('detail_gestionnaire/<gestionnaire_id>',detail_gestionnaire_view, name='detail_gestionnaire'),
    
   
   
]
admin.site.site_header = "Bienvenues au systeme de planification de Rendez-Vous "

admin.site.site_title = "systeme de gestion de planification de Rendez-Vous"

admin.site.index_title = "Espace Administrateur"