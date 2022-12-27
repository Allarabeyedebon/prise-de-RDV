from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from django.urls import reverse_lazy





def home_view(request):
    context = {}
    template = 'index.html'
    return render(request, template, context)


def gestionnaire_view(request):
    gestionnaires = Gestionnaire.objects.all()
    context = {'gestionnaires' : gestionnaires}
    template = 'gestionnaire.html'
    return render(request, template, context)    


def agence_view(request):
    agences  = Agence.objects.all()
    context = {'agences' : agences}
    template = 'agence.html'
    return render(request, template, context)


def detail_agence_view(request, agence_id):
    agence = Agence.objects.get(pk=agence_id)
    context = {'agence' : agence}
    template = 'detail_agence.html'
    return render(request, template, context)

def detail_gestionnaire_view(request, gestionnaire_id):
    gestionnaire = Gestionnaire.objects.get(pk=gestionnaire_id)
    context = {'gestionnaire' : gestionnaire}
    template = 'detail_gestionnaire.html'
    return render(request, template, context)
    





    
# @login_required
# def cart_add(request, id):
#     cart = Cart(request)
#     product = Menu.objects.get(id=id)
#     cart.add(product=product)
#     return redirect(request.META['HTTP_REFERER'])




# @login_required
# def item_clear(request, id):
#     cart = Cart(request)
#     product = Menu.objects.get(id=id)
#     cart.remove(product)
#     return redirect("cart_detail")
    




# @login_required
# def item_increment(request, id):
#     cart = Cart(request)
#     product = Menu.objects.get(id=id)
#     cart.add(product=product)
#     return redirect("cart_detail")



@login_required
def cart_ajouter_view(request, id=id):
    compte_id = get_object_or_404(Compte, id=id)
    if Panier.objects.filter(compte=compte_id).exists():
        return messages.error(request, "Client exist deja")
    
    print("==============Client exist deja===========")
    print(compte_id.heure)
    print(request.user)
    
    total = _id.heure
    usere = request.user
    Panier.objects.create(
        compte=compte_id,
        gestionnaire=usere.email,
        total=total
    )
    return redirect(request.META['HTTP_REFERER'])
    

""" 
def index(request):
    gestionnaires = Gestionnaire.objects.all()
    agences  = Agence.objects.all()
    context = {
        'gestionnaires' : gestionnaires, 
        'agences' : agences
        }
    template = 'index.html'
    return render(request, template, context)
 """