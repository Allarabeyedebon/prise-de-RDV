from django.contrib import admin

from RV_App.models import *

# Register your models here.
class AdminClient(admin.ModelAdmin):
    list_display = ('nom', 'email', 'prenom','typeCompte', 'photo')

class AdminAgence(admin.ModelAdmin):
    list_display = ('nom', 'local', 'photo')

class AdminGestionnaire(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'disponibilite', 'email', 'photo')

class AdminRDV(admin.ModelAdmin):
    list_display = ('client', 'gestionnaire', 'typeProbleme', 'description')
class AdminService(admin.ModelAdmin):
    list_display = ('nom', 'description', 'dateAjout','dateModif','photo')


admin.site.register(Client, AdminClient)
admin.site.register(RDV, AdminRDV)
admin.site.register(Agence, AdminAgence)
admin.site.register(Gestionnaire, AdminGestionnaire)
admin.site.register(Service, AdminService)


