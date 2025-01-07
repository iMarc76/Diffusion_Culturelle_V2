from django.db import models
from django.conf import settings


class Artiste(models.Model):
    nom = models.fields.CharField(max_length=100)
    prenom = models.fields.CharField(max_length=100)
    email = models.EmailField(max_length=254, default='name@example.com')
    website = models.fields.URLField(null=False)
    date_creation = models.DateTimeField(auto_now_add=True)

class Lieu(models.Model):
    nom_lieu = models.fields.CharField(max_length=100)
    rue = models.fields.CharField(max_length=100)
    num = models.fields.IntegerField()
    cp = models.fields.IntegerField()
    ville = models.fields.CharField(max_length=100)


class Spectacle(models.Model):
    class Genre(models.TextChoices):
        Genre = "Genre"
        Cirque_art_forain_de_la_rue = 'Cirque_art_et_forain_de_la_rue'
        Compte_poesie_et_litterature = 'Compte_poesie_et_litterature'

    class Public(models.TextChoices):
        Public = 'Public'
        Jeunes = 'Jeunes'
        Adultes = 'Adultes'

    artiste = models.ForeignKey(Artiste, null=True, on_delete=models.SET_NULL)
    lieu = models.ForeignKey(Lieu, null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    titre = models.fields.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/')
    description = models.fields.CharField(max_length=1000)
    genre = models.fields.CharField(choices=Genre.choices, max_length=50, default=Genre.Genre)
    public = models.fields.CharField(choices=Public.choices, max_length=50, default=Public.Public)
    animation = models.BooleanField(default=False)
    duree = models.fields.CharField(max_length=50, null=True)


class Date(models.Model):
    date = models.DateTimeField()
    spectacle = models.ForeignKey(Spectacle, null=True, on_delete=models.SET_NULL)


