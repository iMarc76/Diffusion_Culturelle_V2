from django.contrib import admin
from django.urls import path
from artiste.views import spectacle, date, home
from programmateur.views import infosSpectacle
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
    path('spectacle/', spectacle, name='spectacle'),
    path('infos-spectacles/', infosSpectacle, name='infos-spectacles'),
    path('date/', date, name='ajout-date'),
    path('home/', home, name='home')

]
