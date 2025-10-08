from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band

def hello(request):
    bands = Band.objects.all()
    return HttpResponse(f"""
                        <h1> Voici mes groupes preferés: </h1>
                        <ul>
                            <li>{bands[0].name}</li>
                            <li>{bands[1].name}</li>
                            <li>{bands[2].name}</li>
                            <li></li>
                            <li></li>
                        </ul>
""")

def about(request):
    return HttpResponse("<p>Bienvenue sur notre page apropos</p>")

def listing(request):
    return HttpResponse("<h2>Voici notre liste des produits</h2>")

def contact(request):
    return HttpResponse('<h2>Bienvenue sur notre page de contacts</h2>')