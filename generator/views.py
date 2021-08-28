from django.shortcuts import render
# render passs a template that turn into httpresponse
from django.http import HttpResponse
import secrets
import string

def home(request):
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')
 
def password(request):
    aPassword= ''
    characters = list(string.ascii_lowercase)
    if request.GET.get('uppercase'):
        characters.extend(list(string.ascii_uppercase))
    if request.GET.get('special'):
        characters.extend(list('/#@$%&?+-*;'))
    if request.GET.get('numbers'):
        characters.extend(list(string.digits))
    length = int(request.GET.get("length", 5)) #if no value is given, a default 5 letter password will print
    # random.shuffle(characters)
    for _ in range(length):
        aPassword += ''.join(secrets.choice(characters))
    return render(request, 'generator/password.html', {'password':aPassword})


