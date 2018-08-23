from django.conf import settings
import requests
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from coinbase.wallet.client import OAuthClient,Client

# Create your views here.
def index(request):
    return render(request, 'Ali/main.html')

def status(request):
    texbox = request.POST['texbox']
    return render(request, "Ali/action.html",{'texbox':texbox})

def forcoin(request):
    ClientId = "77d5af4941ffd6d5f0c9149e2e303a1c28d9f44c09b63694d6f2f608c60947c0"
    Clientsecret = "4395c36b93aa972ab4c6da2278cdca48f93e8551d0b13ee502552e249db90eb4"
    code = request.GET.get('code','')
    r2 = requests.post("https://api.coinbase.com/oauth/token", data={"grant_type": "authorization_code", "code": code, "client_id": ClientId, "client_secret": Clientsecret, "redirect_uri": "http://127.0.0.1:8000/Ali/forcoin/"})
    r3 = r2.json()
    a = OAuthClient(r3['access_token'], r3['refresh_token'])
    b = a.get_spot_price().amount
    c = a.get_historic_prices(currency_pair= 'BTC-USD', period='day')['prices']
    user = a.get_current_user().name
    useremail = a.get_current_user().email
    access = a.refresh()['access_token']
    refresh = a.refresh()['refresh_token']

    price = []
    price2 = []
    time = []
    dif1 = []

    for i in range(1,21):
        price.append(float(c[i]['price']))
        price2.append(float(c[i-1]['price']))
        dif1.append(round(price[i-1]-price2[i-1],2))
        time.append(c[i]['time'])

    coinpt = zip(price, dif1, time)

    context = {
        'code':code,
        'price':b,
        'coinprice':price,
        'time':time,
        'coinpt':coinpt,
        'user':user,
        'useremail':useremail,
        'access':access,
        'refresh':refresh,
    }

    return render(request, 'Ali/forcoin.html', context)