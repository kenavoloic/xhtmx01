from django.shortcuts import render
from django.contrib.auth.decorators import login_required, login_not_required

#@login_required
def accueil(request):
    #villes = request.utilisateur.villes.all().order_by('-created_at')
    villes = request.user.villes.all().order_by('-created_at')
    contexte = {'villes': villes}
    return render(request, 'configurations/liste.html', contexte)

@login_not_required
def connexion(request):
    return HttpResponse("Connexion...")
