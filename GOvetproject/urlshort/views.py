from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from django.core import serializers
from django.contrib import messages
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.db import connection
from .models import URLData
from .forms import URLDataForm
from .serializers import URLDataSerializers
from django.shortcuts import redirect
import sqlite3
import string
import random

# Declare Key Variables
BASE_LIST = '0123456789abcdefghijklmnopqrstuvwxyz./:'
BASE_DICT = dict((c, idx) for idx, c in enumerate(BASE_LIST))
service_url = '127.0.0.1'


class FullURLView(viewsets.ModelViewSet):
    queryset = URLData.objects.all()
    serializers_class = URLDataSerializers


def base_encode(integer, alphabet=BASE_LIST):  # Convert ID to FullURL
    if integer == 0:
        return alphabet[0]
    arr = []
    base = len(alphabet)
    while integer:
        integer, rem = divmod(integer, base)
        arr.append(alphabet[rem])
    arr.reverse()
    return ''.join(arr)


def base_decode(request, reverse_base=BASE_DICT):  # Convert Full URL to ID
    long_url = request
    length = len(reverse_base)
    ret = 0
    for i, c in enumerate(long_url[::-1]):
        ret += (length ** i) * reverse_base[c]
    return ret


def shortChars():  # Get Shortened URL endpoint
    short_list_char = '0123456789' + string.ascii_letters
    return ''.join([random.choice(short_list_char) for i in range(10)])


def checkIDExists(ID):  # Check to see if ID already exists in DB
    sc = str(shortChars())
    retrieved_ids = list(URLData.objects.values_list('URLID', flat=True))
    if str(ID) in retrieved_ids:  # Do not create a new ID if one already exists
        surl = URLData.objects.all().filter(URLID=str(ID))[0].ShortURL  # Grab everything on page, strip URL ID
        mess = f"Record Already Exists. The Shortened Link is: {service_url}/{surl}"
    else:
        url = URLData(URLID=ID, ShortURL=sc)
        url.save()
        mess = f"Congratulations! Your shortened URL is {service_url}/{sc}"
    return mess


def redirect_short_url(request, short_url):
    redirect_url = service_url + '/shorten'
    try:
        url_id = URLData.objects.all().filter(ShortURL=short_url)[0].URLID
        redirect_url = base_encode(int(url_id))
    except Exception as e:
        print(e)
    return redirect(redirect_url)


def appendPrefix(entry):
    match = ['http', 'https']
    if any(x in entry for x in match):
        return entry
    else:
        return 'https://' + str(entry)


# Serializer
def get_form(request):
    if request.method == 'POST':  # User's entered URL
        form = URLDataForm(request.POST)
        if form.is_valid():
            fullurl = form.cleaned_data['EnterURL']
            fullurladj = appendPrefix(fullurl)
            id = base_decode(fullurladj.lower())  # Convert URL entry to lowercase
            messages.success(request, f'{checkIDExists(id)}')  # Inform user the URL was created
    form = URLDataForm()
    return render(request, 'myform/form.html', {'form': form})
