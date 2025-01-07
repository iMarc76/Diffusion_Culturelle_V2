from django.shortcuts import render
from artiste.models import Spectacle



def infosSpectacle(request):
    spectacles = Spectacle.objects.select_related('artiste').all()
    return render(request, 'infos.html', {'spectacles': spectacles})



