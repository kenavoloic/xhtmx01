from django.shortcuts import render
from django.contrib.auth.decorators import login_required, login_not_required
# tables2
from django_tables2 import SingleTableView
from django_tables2.config import RequestConfig
from .models import Ville
from .tables import VilleTable

#@login_required
def accueil(request):
    #villes = request.utilisateur.villes.all().order_by('-created_at')
    # villes = request.user.villes.all().order_by('-created_at')
    villes = request.user.villes.all().order_by('nom')
    contexte = {'villes': villes}
    return render(request, 'configurations/liste.html', contexte)

@login_not_required
def connexion(request):
    return HttpResponse("Connexion...")

