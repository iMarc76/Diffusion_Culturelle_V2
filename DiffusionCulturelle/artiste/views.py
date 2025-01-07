from .forms import ArtisteForm, SpectacleForm, LieuForm, DateForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from artiste.models import Spectacle


@login_required
def spectacle(request):
    if request.method == 'POST':
        form_art = ArtisteForm(request.POST)
        form_spec = SpectacleForm(request.POST, request.FILES)
        form_lieu = LieuForm(request.POST)


        if form_art.is_valid() and form_spec.is_valid() and form_lieu.is_valid():
            artiste = form_art.save()
            lieu = form_lieu.save()
            spectacle = form_spec.save(commit=False)
            spectacle.animation = form_spec.cleaned_data['animation'] == 'True'
            spectacle.artiste = artiste
            spectacle.lieu = lieu
            spectacle.user = request.user
            spectacle.save()
            return render(request, 'ajout_date.html')
        else:
            print("Erreurs ArtisteForm:", form_art.errors)
            print("Erreurs SpectacleForm:", form_spec.errors)
            print("Erreurs SpectacleForm:", form_lieu.errors)


    else:
        form_art = ArtisteForm()
        form_spec = SpectacleForm()
        form_lieu = LieuForm()


    return render(request, 'ajout_spectacle.html', {'form_art': form_art, 'form_spec': form_spec, 'form_lieu': form_lieu})


def date(request):
    spectaclesByUser=""
    if request.method == "POST":
        form_date = DateForm(request.POST)
        spectacle_id = request.POST.get('spectacle_id')
        confirm = "Votre date a bien été ajoutée"

        if form_date.is_valid():
            date_instance = form_date.save(commit=False)
            date_instance.spectacle_id = spectacle_id
            form_date.save()
            return render(request, 'ajout_date.html', {'msg': confirm})

        else:
            print("Erreurs DateFrom:", form_date.errors)

    else:
        form_date = DateForm()
        spectaclesByUser = Spectacle.objects.filter(user=request.user)

    return render(request, 'ajout_date.html', {'form_date': form_date, 'spectaclesByUser': spectaclesByUser})



def home(request):

    return render(request, 'home.html')



















