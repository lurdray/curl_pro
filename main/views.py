from django.contrib import messages
from django.shortcuts import (HttpResponse, HttpResponseRedirect,
                            get_object_or_404, redirect, render)
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required




from django.core.mail import send_mail

from datetime import datetime
import datetime as dt
import requests

#from .forms import UserForm

from datetime import datetime
from requests import Request, Session
import json
import time
from datetime import datetime, timedelta


import asyncio
import requests



async def DekatronCoredao():
    coredao = requests.get("https://api.dexscreener.com/latest/dex/tokens/0x40375C92d9FAf44d2f9db9Bd9ba41a3317a2404f")
            
    coredaodekatron = coredao.json()
    coredaopairs = coredaodekatron["pairs"][0]
    coredaobaseToken = coredaopairs["baseToken"]
    coredaopriceNative = coredaopairs["priceNative"]
    coredaopriceUsd = coredaopairs["priceUsd"]
    coredaovolume = coredaopairs["volume"]
    coredaopriceChange = coredaopairs["priceChange"]
    coredaofdv = coredaopairs["fdv"]

    return coredaobaseToken, coredaopriceNative, coredaopriceUsd, coredaovolume, coredaopriceChange, coredaofdv

async def DekatronIce():
    ice = requests.get("https://api.dexscreener.com/latest/dex/tokens/0xb999ea90607a826a3e6e6646b404c3c7d11fa39d")
    icedekatron = ice.json()
    icepairs = icedekatron["pairs"][0]
    icebaseToken = icepairs["baseToken"]
    icepriceNative = icepairs["priceNative"]
    icepriceUsd = icepairs["priceUsd"]
    icevolume = icepairs["volume"]
    icepriceChange = icepairs["priceChange"]
    icefdv = icepairs["fdv"]

    return icebaseToken, icepriceNative, icepriceUsd, icevolume, icepriceChange, icefdv


async def DekatronBow():
    bow = requests.get("https://api.dexscreener.com/latest/dex/tokens/0x1a639e150d2210A4BE4a5F0857A9151B241E7AE4")
    bowdekatron = bow.json()
    bowpairs = bowdekatron["pairs"][0]
    bowbaseToken = bowpairs["baseToken"]
    bowpriceNative = bowpairs["priceNative"]
    bowpriceUsd = bowpairs["priceUsd"]
    bowvolume = bowpairs["volume"]
    bowpriceChange = bowpairs["priceChange"]
    bowfdv = bowpairs["fdv"]

    return bowbaseToken, bowpriceNative, bowpriceUsd, bowvolume, bowpriceChange, bowfdv

async def DekatronShadow():
    shadow = requests.get("https://api.dexscreener.com/latest/dex/tokens/0xddBa66C1eBA873e26Ac0215Ca44892a07d83aDF5")
    shadowdekatron = shadow.json()
    shadowpairs = shadowdekatron["pairs"][0]
    shadowbaseToken = shadowpairs["baseToken"]
    shadowpriceNative = shadowpairs["priceNative"]
    shadowpriceUsd = shadowpairs["priceUsd"]
    shadowvolume = shadowpairs["volume"]
    shadowpriceChange = shadowpairs["priceChange"]
    shadowfdv = shadowpairs["fdv"]
    shadowlogo = "https://shadowswap.xyz/favicon.ico"

    return shadowbaseToken, shadowpriceNative, shadowpriceUsd, shadowvolume, shadowpriceChange, shadowfdv, shadowlogo


async def DekatronCoreid():
    coreid = requests.get("https://api.dexscreener.com/latest/dex/tokens/0x000000000e1d682cc39abe9b32285fdea1255374")
    coreiddekatron = coreid.json()
    coreidpairs = coreiddekatron["pairs"][0]
    coreidbaseToken = coreidpairs["baseToken"]
    coreidpriceNative = coreidpairs["priceNative"]
    coreidpriceUsd = coreidpairs["priceUsd"]
    coreidvolume = coreidpairs["volume"]
    coreidpriceChange = coreidpairs["priceChange"]
    coreidfdv = coreidpairs["fdv"]

    return coreidbaseToken, coreidpriceNative, coreidpriceUsd, coreidvolume, coreidpriceChange, coreidfdv



async def DekatronWoof():
    woof = requests.get("https://api.dexscreener.com/latest/dex/tokens/0x5C44d3D2312AbA4d5F2406A98Bf374Bc76455092")
    woofdekatron = woof.json()
    woofpairs = woofdekatron["pairs"][0]
    woofbaseToken = woofpairs["baseToken"]
    woofpriceNative = woofpairs["priceNative"]
    woofpriceUsd = woofpairs["priceUsd"]
    woofvolume = woofpairs["volume"]
    woofpriceChange = woofpairs["priceChange"]
    wooffdv = woofpairs["fdv"]

    return woofbaseToken, woofpriceNative, woofpriceUsd, woofvolume, woofpriceChange, wooffdv


async def DekatronUnity():
    unity = requests.get("https://api.dexscreener.com/latest/dex/tokens/0x496Bb259D0117E89B2e73433524e9838c3073e60")
    unitydekatron = unity.json()
    unitypairs = unitydekatron["pairs"][0]
    unitybaseToken = unitypairs["baseToken"]
    unitypriceNative = unitypairs["priceNative"]
    unitypriceUsd = unitypairs["priceUsd"]
    unityvolume = unitypairs["volume"]
    unitypriceChange = unitypairs["priceChange"]
    unityfdv = unitypairs["fdv"]

    return unitybaseToken, unitypriceNative, unitypriceUsd, unityvolume, unitypriceChange, unityfdv

async def DekatronSpoon():
    spoon = requests.get("https://api.dexscreener.com/latest/dex/tokens/0x66B96135d0c639D53e1f23b7a5849F6022883b41")
    spoondekatron = spoon.json()
    spoonpairs = spoondekatron["pairs"][0]
    spoonbaseToken = spoonpairs["baseToken"]
    spoonpriceNative = spoonpairs["priceNative"]
    spoonpriceUsd = spoonpairs["priceUsd"]
    spoonvolume = spoonpairs["volume"]
    spoonpriceChange = spoonpairs["priceChange"]
    spoonfdv = spoonpairs["fdv"] 

    return spoonbaseToken, spoonpriceNative, spoonpriceUsd, spoonvolume, spoonpriceChange, spoonfdv


async def DekatronCdc():
    cdc = requests.get("https://api.dexscreener.com/latest/dex/tokens/0x8bab1Ef0F175F6d7EBCE79ee277BA091832F6429")
    cdcdekatron = cdc.json()
    cdcpairs = cdcdekatron["pairs"][0]
    cdcbaseToken = cdcpairs["baseToken"]
    cdcpriceNative = cdcpairs["priceNative"]
    cdcpriceUsd = cdcpairs["priceUsd"]
    cdcvolume = cdcpairs["volume"]
    cdcpriceChange = cdcpairs["priceChange"]
    cdcfdv = cdcpairs["fdv"]

    return cdcbaseToken, cdcpriceNative, cdcpriceUsd, cdcvolume, cdcpriceChange, cdcfdv
    
async def DekatronPepe():
    pepe = requests.get("https://api.dexscreener.com/latest/dex/tokens/0x9B944a707cfDE49b7c0a9593f88b17Dc2C05DB78")
    pepedekatron = pepe.json()
    pepepairs = pepedekatron["pairs"][0]
    pepebaseToken = pepepairs["baseToken"]
    pepepriceNative = pepepairs["priceNative"]
    pepepriceUsd = pepepairs["priceUsd"]
    pepevolume = pepepairs["volume"]
    pepepriceChange = pepepairs["priceChange"]
    pepefdv = pepepairs["fdv"]

    return pepebaseToken, pepepriceNative, pepepriceUsd, pepevolume, pepepriceChange, pepefdv 

async def DekatronMiidas():
    miidas = requests.get("https://api.dexscreener.com/latest/dex/tokens/0xcfd38184c30832917A2871695F91e5e61bBD41fF")
    miidasdekatron = miidas.json()
    miidaspairs = miidasdekatron["pairs"][0]
    miidasbaseToken = miidaspairs["baseToken"]
    miidaspriceNative = miidaspairs["priceNative"]
    miidaspriceUsd = miidaspairs["priceUsd"]
    miidasvolume = miidaspairs["volume"]
    miidaspriceChange = miidaspairs["priceChange"]
    miidasfdv = miidaspairs["fdv"]

    return miidasbaseToken, miidaspriceNative, miidaspriceUsd, miidasvolume, miidaspriceChange, miidasfdv 
    
async def DekatronScore():
    score = requests.get("https://api.dexscreener.com/latest/dex/tokens/0xe191a4d47A6be111C75139757CDDBb61BEEd88FB")
    scoredekatron = score.json()
    scorepairs = scoredekatron["pairs"][0]
    scorebaseToken = scorepairs["baseToken"]
    scorepriceNative = scorepairs["priceNative"]
    scorepriceUsd = scorepairs["priceUsd"]
    scorevolume = scorepairs["volume"]
    scorepriceChange = scorepairs["priceChange"]
    scorefdv = scorepairs["fdv"]

    return scorebaseToken, scorepriceNative, scorepriceUsd, scorevolume, scorepriceChange, scorefdv
    
async def DekatronBlock():
    block = requests.get("https://api.dexscreener.com/latest/dex/tokens/0xbFf24592345094DFA4d6f75aFF5BE79AbCbC9bD9")
    blockdekatron = block.json()
    blockpairs = blockdekatron["pairs"][0]
    blockbaseToken = blockpairs["baseToken"]
    blockpriceNative = blockpairs["priceNative"]
    blockpriceUsd = blockpairs["priceUsd"]
    blockvolume = blockpairs["volume"]
    blockpriceChange = blockpairs["priceChange"]
    blockfdv = blockpairs["fdv"]

    return blockbaseToken, blockpriceNative, blockpriceUsd, blockvolume, blockpriceChange, blockfdv
    
async def DekatronDc():
    dc = requests.get("https://api.dexscreener.com/latest/dex/tokens/0x979A34f98b9a1bF2B38fD18f5c038423e4902db9")
    dcdekatron = dc.json()
    dcpairs = dcdekatron["pairs"][0]
    dcbaseToken = dcpairs["baseToken"]
    dcpriceNative = dcpairs["priceNative"]
    dcpriceUsd = dcpairs["priceUsd"]
    dcvolume = dcpairs["volume"]
    dcpriceChange = dcpairs["priceChange"]
    dcfdv = dcpairs["fdv"]

    return dcbaseToken, dcpriceNative, dcpriceUsd, dcvolume, dcpriceChange, dcfdv
    
async def DekatronMap():
    map = requests.get("https://api.dexscreener.com/latest/dex/tokens/0xAB82f8b18ea7929815076F152b8Fd24F8b267274")
    mapdekatron = map.json()
    mappairs = mapdekatron["pairs"][0]
    mapbaseToken = mappairs["baseToken"]
    mappriceNative = mappairs["priceNative"]
    mappriceUsd = mappairs["priceUsd"]
    mapvolume = mappairs["volume"]
    mappriceChange = mappairs["priceChange"]
    mapfdv = mappairs["fdv"]

    return mapbaseToken, mappriceNative, mappriceUsd, mapvolume, mappriceChange, mapfdv
    
async def DekatronIgnore():
    ignorefud = requests.get("https://api.dexscreener.com/latest/dex/tokens/0x98564E70c7fCC6d947fFE6d9EfeD5ba68b306F2E")
    ignorefuddekatron = ignorefud.json()
    ignorefudpairs = ignorefuddekatron["pairs"][0]
    ignorefudbaseToken = ignorefudpairs["baseToken"]
    ignorefudpriceNative = ignorefudpairs["priceNative"]
    ignorefudpriceUsd = ignorefudpairs["priceUsd"]
    ignorefudvolume = ignorefudpairs["volume"]
    ignorefudpriceChange = ignorefudpairs["priceChange"]
    ignorefudfdv = ignorefudpairs["fdv"]

    return ignorefudbaseToken, ignorefudpriceNative, ignorefudpriceUsd, ignorefudvolume, ignorefudpriceChange, ignorefudfdv

async def DekatronYpc():
    ypc = requests.get("https://api.dexscreener.com/latest/dex/tokens/0xDC2393dc10734BF153153038943a5deB42b209cd")
    ypcdekatron = ypc.json()
    ypcpairs = ypcdekatron["pairs"][0]
    ypcbaseToken = ypcpairs["baseToken"]
    ypcpriceNative = ypcpairs["priceNative"]
    ypcpriceUsd = ypcpairs["priceUsd"]
    ypcvolume = ypcpairs["volume"]
    ypcpriceChange = ypcpairs["priceChange"]
    ypcfdv = ypcpairs["fdv"]

    return ypcbaseToken, ypcpriceNative, ypcpriceUsd, ypcvolume, ypcpriceChange, ypcfdv 

async def DekatronHobo():
    hobo = requests.get("https://api.dexscreener.com/latest/dex/tokens/0x25100C0083e8E53b1cb264E978522bd477011A0d")
    hobodekatron = hobo.json()
    hobopairs = hobodekatron["pairs"][0]
    hobobaseToken = hobopairs["baseToken"]
    hobopriceNative = hobopairs["priceNative"]
    hobopriceUsd = hobopairs["priceUsd"]
    hobovolume = hobopairs["volume"]
    hobopriceChange = hobopairs["priceChange"]
    hobofdv = hobopairs["fdv"]

    return hobobaseToken, hobopriceNative, hobopriceUsd, hobovolume, hobopriceChange, hobofdv
    
async def DekatronLfg():
    lfgswap = requests.get("https://api.dexscreener.com/latest/dex/tokens/0xF7a0b80681eC935d6dd9f3Af9826E68B99897d6D")
    lfgswapdekatron = lfgswap.json()
    lfgswappairs = lfgswapdekatron["pairs"][0]
    lfgswapbaseToken = lfgswappairs["baseToken"]
    lfgswappriceNative = lfgswappairs["priceNative"]
    lfgswappriceUsd = lfgswappairs["priceUsd"]
    lfgswapvolume = lfgswappairs["volume"]
    lfgswappriceChange = lfgswappairs["priceChange"]
    lfgswapfdv = lfgswappairs["fdv"]

    return lfgswapbaseToken, lfgswappriceNative, lfgswappriceUsd, lfgswapvolume, lfgswappriceChange, lfgswapfdv
    
async def DekatronCrest():
    crest = requests.get("https://api.dexscreener.com/latest/dex/tokens/0xcFE4C0783d103C44f403Bb287d29af0bAE5D4E84")
    crestdekatron = crest.json()
    crestpairs = crestdekatron["pairs"][0]
    crestbaseToken = crestpairs["baseToken"]
    crestpriceNative = crestpairs["priceNative"]
    crestpriceUsd = crestpairs["priceUsd"]
    crestvolume = crestpairs["volume"]
    crestpriceChange = crestpairs["priceChange"]
    crestfdv = crestpairs["fdv"]

    return crestbaseToken, crestpriceNative, crestpriceUsd, crestvolume, crestpriceChange, crestfdv
    
async def DekatronCshare():
    cshare = requests.get("https://api.dexscreener.com/latest/dex/tokens/0x6501cCA79ca8D6F68784f2345c9a379951e30A05")
    csharedekatron = cshare.json()
    csharepairs = csharedekatron["pairs"][0]
    csharebaseToken = csharepairs["baseToken"]
    csharepriceNative = csharepairs["priceNative"]
    csharepriceUsd = csharepairs["priceUsd"]
    csharevolume = csharepairs["volume"]
    csharepriceChange = csharepairs["priceChange"]
    csharefdv = csharepairs["fdv"]

    return csharebaseToken, csharepriceNative, csharepriceUsd, csharevolume, csharepriceChange, csharefdv
    
async def DekatronCtomb():
    ctomb = requests.get("https://api.dexscreener.com/latest/dex/tokens/0xC830a752eef79F2D66a36645A70fB0bA176b4Cea")
    ctombdekatron = ctomb.json()
    ctombpairs = ctombdekatron["pairs"][0]
    ctombbaseToken = ctombpairs["baseToken"]
    ctombpriceNative = ctombpairs["priceNative"]
    ctombpriceUsd = ctombpairs["priceUsd"]
    ctombvolume = ctombpairs["volume"]
    ctombpriceChange = ctombpairs["priceChange"]
    ctombfdv = ctombpairs["fdv"]

    return ctombbaseToken, ctombpriceNative, ctombpriceUsd, ctombvolume, ctombpriceChange, ctombfdv
    
async def DekatronWord():
    word = requests.get("https://api.dexscreener.com/latest/dex/tokens/0xAA7912C028E058e4bD90Bcbb9fB41C27DbcC3245")
    worddekatron = word.json()
    wordpairs = worddekatron["pairs"][0]
    wordbaseToken = wordpairs["baseToken"]
    wordpriceNative = wordpairs["priceNative"]
    wordpriceUsd = wordpairs["priceUsd"]
    wordvolume = wordpairs["volume"]
    wordpriceChange = wordpairs["priceChange"]
    wordfdv = wordpairs["fdv"]

    return wordbaseToken, wordpriceNative, wordpriceUsd, wordvolume, wordpriceChange, wordfdv
    
async def DekatronRoyale():
    royale = requests.get("https://api.dexscreener.com/latest/dex/tokens/0xA7c0B19645B653B4373E3592C84fce8C64D89E8F")
    royaledekatron = royale.json()
    royalepairs = royaledekatron["pairs"][0]
    royalebaseToken = royalepairs["baseToken"]
    royalepriceNative = royalepairs["priceNative"]
    royalepriceUsd = royalepairs["priceUsd"]
    royalevolume = royalepairs["volume"]
    royalepriceChange = royalepairs["priceChange"]
    royalefdv = royalepairs["fdv"]

    return royalebaseToken, royalepriceNative, royalepriceUsd, royalevolume, royalepriceChange, royalefdv
    
async def DekatronYfi():
    yfi = requests.get("https://api.dexscreener.com/latest/dex/tokens/0x9c765C62ad538011c2aAd815CaAeEc94551fbE9D")
    yfidekatron = yfi.json()
    yfipairs = yfidekatron["pairs"][0]
    yfibaseToken = yfipairs["baseToken"]
    yfipriceNative = yfipairs["priceNative"]
    yfipriceUsd =yfipairs["priceUsd"]
    yfivolume = yfipairs["volume"]
    yfipriceChange = yfipairs["priceChange"]
    yfifdv = yfipairs["fdv"]

    return yfibaseToken, yfipriceNative, yfipriceUsd, yfivolume, yfipriceChange, yfifdv
    
async def DekatronData():
    data = requests.get("https://api.dexscreener.com/latest/dex/tokens/0xc0E49f8C615d3d4c245970F6Dc528E4A47d69a44").json()
    pairs = data['pairs']
    token_list = []
    for pair in pairs:
        if pair['baseToken']['name'].lower() != 'icecream':
            token_list.append({
                'name': pair['baseToken']['name'],
                'address': pair['baseToken']['address'],
                'price': pair['priceUsd'],
                'symbol': pair['baseToken']['symbol'],
                'volume': pair['volume']
                })
            
    return token_list


def ConnectMetamaskManualView(request):
    if request.method == "POST":
        wallet = request.POST.get("wallet")
        request.session["wallet"] = wallet
        
        return HttpResponseRedirect(reverse("main:portfolio"))
        

    else:

        context = {}
        return render(request, "main/connect_metamask_manual.html", context)
        
def ConnectMetamaskManualBView(request):
    if request.method == "POST":
        wallet = request.POST.get("wallet")
        request.session["wallet"] = wallet
        
        return HttpResponseRedirect(reverse("main:brise_portfolio"))
        

    else:

        context = {}
        return render(request, "main/connect_metamask_bitgert_manual.html", context)
        
def ConnectMetamaskManualBscView(request):
    if request.method == "POST":
        wallet = request.POST.get("wallet")
        request.session["wallet"] = wallet
        
        return HttpResponseRedirect(reverse("main:bscportfolio"))
        

    else:

        context = {}
        return render(request, "main/connect_metamask_bsc_manual.html", context)
        
def ConnectMetamaskManualCoreView(request):
    if request.method == "POST":
        wallet = request.POST.get("wallet")
        request.session["wallet"] = wallet
        
        return HttpResponseRedirect(reverse("main:coreportfolio"))
        

    else:

        context = {}
        return render(request, "main/connect_metamask_core_manual.html", context)
        
        
def ConnectMetamaskManualCantoView(request):
    if request.method == "POST":
        wallet = request.POST.get("wallet")
        request.session["wallet"] = wallet
        
        return HttpResponseRedirect(reverse("main:wcanto_portfolio"))
        

    else:

        context = {}
        return render(request, "main/connect_metamask_canto_manual.html", context)
        
def ConnectMetamaskView(request):
    if request.method == "POST":
        wallet = request.POST.get("wallet")
        request.session["wallet"] = wallet
        
        return HttpResponseRedirect(reverse("main:portfolio"))
        

    else:

        context = {}
        return render(request, "main/connect_metamask.html", context)
        
def BitgertConnectMetamaskView(request):
    if request.method == "POST":
        wallet = request.POST.get("wallet")
        request.session["wallet"] = wallet
        
        return HttpResponseRedirect(reverse("main:brise_portfolio"))
        

    else:

        context = {}
        return render(request, "main/connect_metamask_bitgert.html", context)
        
def BscConnectMetamaskView(request):
    if request.method == "POST":
        wallet = request.POST.get("wallet")
        request.session["wallet"] = wallet
        
        return HttpResponseRedirect(reverse("main:bscportfolio"))
        

    else:

        context = {}
        return render(request, "main/connect_metamask_bsc.html", context)
        
def CoreConnectMetamaskView(request):
    if request.method == "POST":
        wallet = request.POST.get("wallet")
        request.session["wallet"] = wallet
        
        return HttpResponseRedirect(reverse("main:coreportfolio"))
        

    else:

        context = {}
        return render(request, "main/connect_metamask_core.html", context)
        
def CantoConnectMetamaskView(request):
    if request.method == "POST":
        wallet = request.POST.get("wallet")
        request.session["wallet"] = wallet
        
        return HttpResponseRedirect(reverse("main:wcanto_portfolio"))
        

    else:

        context = {}
        return render(request, "main/connect_metamask_canto.html", context)

def BrisePortfolioView(request):
    if request.method == "POST":
        pass

    else:
        try:
            total = 0
            wallet = request.session["wallet"]
            
            resp = requests.get("https://api.iotexchartapp.com/bitrise-get-balance/%s/" % str(wallet)).json()
            data = resp["data"]
            
            for item in data:
                total += float(item['total_price'])

            #return HttpResponse(data)
            context = {"data": data, "total": total, "wallet": wallet}
            return render(request, "main/brise_portfolio.html", context)
            
        except:
            return HttpResponseRedirect(reverse("main:bitgert_portfolio"))
            
def BscPortfolioView(request):
    if request.method == "POST":
        pass

    else:
        try:
            total = 0
            wallet = request.session["wallet"]
            
            resp = requests.get("https://api.iotexchartapp.com/bsc-get-balance/%s/" % str(wallet)).json()
            data = resp["data"]
            
            for item in data:
                total += float(item['total_price'])

            #return HttpResponse(data)
            context = {"data": data, "total": total, "wallet": wallet}
            return render(request, "main/bscportfolio.html", context)
            
        except:
            return HttpResponseRedirect(reverse("main:bsc_portfolio"))
            
def CorePortfolioView(request):
    if request.method == "POST":
        pass

    else:
        try:
            total = 0
            wallet = request.session["wallet"]
            
            resp = requests.get("https://api.iotexchartapp.com/coredao-get-balance/%s/" % str(wallet)).json()
            data = resp["data"]
            
            for item in data:
                total += float(item['total_price'])

            #return HttpResponse(data)
            context = {"data": data, "total": total, "wallet": wallet}
            return render(request, "main/coreportfolio.html", context)
            
        except:
            return HttpResponseRedirect(reverse("main:core_portfolio"))
            
def WCantoPortfolioView(request):
    if request.method == "POST":
        pass

    else:
        try:
            total = 0
            wallet = request.session["wallet"]
            
            resp = requests.get("https://api.iotexchartapp.com/canto-get-balance/%s/" % str(wallet)).json()
            data = resp["data"]
            
            for item in data:
                total += float(item['total_price'])

            #return HttpResponse(data)
            context = {"data": data, "total": total, "wallet": wallet}
            return render(request, "main/canto_portfolio.html", context)
            
        except:
            return HttpResponseRedirect(reverse("main:canto_portfolio"))


def PortfolioView(request):
    if request.method == "POST":
        pass

    else:
        try:
            total = 0
            wallet = request.session["wallet"]
            
            resp = requests.get("https://api.iotexchartapp.com/loop-get-balance/%s/" % str(wallet)).json()
            data = resp["data"]
            
            for item in data:
                total += float(item['total_price'])

            #return HttpResponse(data)
            context = {"data": data, "total": total, "wallet": wallet}
            return render(request, "main/portfolio.html", context)
            
        except:
            return HttpResponseRedirect(reverse("main:your_portfolio"))



def NoneView(request):
    if request.method == "POST":
        address_db = [
        "0x27b45bCC26e01Ed50B4080A405D1c492FEe89d63",
        "0xce186ad6430e2fe494a22c9edbd4c68794a28b35",
        "0xb999ea90607a826a3e6e6646b404c3c7d11fa39d",
        "0x8fff93e810a2edaafc326edee51071da9d398e83",
        "0x826551890dc65655a0aceca109ab11abdbd7a07b",
        "0x43a8a925c1930A313D283359184A64c51a2bc0E9",
        "0x28b9aed756de31b6b362aa0f23211d13093ebb79",
        "0x81bCEa03678D1CEF4830942227720D542Aa15817",
        "0xddBa66C1eBA873e26Ac0215Ca44892a07d83aDF5",
        "0x1a639e150d2210A4BE4a5F0857A9151B241E7AE4",
        "0xb999ea90607a826a3e6e6646b404c3c7d11fa39d",
        "0x000000000e1d682cc39abe9b32285fdea1255374",
        "0xcFE4C0783d103C44f403Bb287d29af0bAE5D4E84",
        "0xe191a4d47A6be111C75139757CDDBb61BEEd88FB",
        "0xF7a0b80681eC935d6dd9f3Af9826E68B99897d6D",
        "0xAc9B3614Dd28c4ca72853CA996Ab76F03Db73Fb4",
        "0x979A34f98b9a1bF2B38fD18f5c038423e4902db9",
        "0x7621c97683A3b0499EC156bD257E44175e793bb1",
        "0x7469bae0b0bc80a208eb0946121b5aff686a6ac2",
        "0xBb790D1e8A2d34e9d846bb00EA0b0380813375EE",
        "0xf69399158cbA7b92089317814E60C5AF867fEaB6",
        "0xbFf24592345094DFA4d6f75aFF5BE79AbCbC9bD9",
        "0xE8dEC1bFC7BF572D60403c609d6589715d2a23fC",
        "0x25100C0083e8E53b1cb264E978522bd477011A0d",
        "0x5C44d3D2312AbA4d5F2406A98Bf374Bc76455092",
        "0xAA7912C028E058e4bD90Bcbb9fB41C27DbcC3245",
        "0xA20b3B97df3a02f9185175760300a06B4e0A2C05",
        "0x6F8BF0Ca89b8936AA498c7A2C75815Eecca328F3",
        "0x6501cca79ca8d6f68784f2345c9a379951e30a05",
        "0xC830a752eef79F2D66a36645A70fB0bA176b4Cea",
        "0x8afb52de791a19873c3097195ef04d48ed93fe14",
        "0x5aE225fa6573903CA58E26Cd4171B87060CeEAA2",
        "0xDBa57074B81CD0630D7960dFAA370972C5E1A6D9",
        "0xA7c0B19645B653B4373E3592C84fce8C64D89E8F",
        "0xcfd38184c30832917A2871695F91e5e61bBD41fF",
        "0x496Bb259D0117E89B2e73433524e9838c3073e60",
        "0x40375C92d9FAf44d2f9db9Bd9ba41a3317a2404f",
        "0x66B96135d0c639D53e1f23b7a5849F6022883b41",
        "0x8bab1Ef0F175F6d7EBCE79ee277BA091832F6429",
        "0x9B944a707cfDE49b7c0a9593f88b17Dc2C05DB78",
        "0xAB82f8b18ea7929815076F152b8Fd24F8b267274",
        "0x9c765C62ad538011c2aAd815CaAeEc94551fbE9D",
        ]

        name_db = ["Doken Super Chain (DSC)", "LoopNetwork (LOOP)", "IceCreamSwap (ICE)", "Bitgert (BRISE)", "Canto (Canto)", "Navis (NVS)", "Lunagens (LUNG)", "ShadowSwap (SHADOW)", "Coredao (CORE)", "Archerswap (BOW)", "Icecreamswap (ICE)", "Coreid (coreid)", "Crest Protocol (CPT)", "Yieldz (YZ)", "LFGSwap (LFG)", "Happy Token (HAPPY)", "3DCity (3dc)", "AI Core Token (Aicore)", "Aiinu (Aiinu)", "Akio Inu (Akio)", "Avocado Baby (Avo)", "BlockVerse (Block)", "Bitvexa (btv)", "Hobo Universe (Hobo)", "Woof (Woof)", "Starlybooks (Word)", "Staked Core (SCore)", "Core Bunny (cbunny)", "Core Share (cshare)", "CoreTomb (ctomb)", "Emperor (emperor)", "FlashX Max (FSXM)", "Green Ranger (GR)", "MemeRoyale (Royale)", "Miidas (miidas)", "Unity Core (Unity)", "Spoon (Poon)", "Coredoge (CDC)", "Pepe Token (pepe)", "4D Twin Maps (Map)", "YFI (YFI)"]

        status = False
        result = None
        url = "none"

        query = request.POST.get("query")

        if query[0]+query[1] == "0x":
            for item in address_db:
                if query == item:
                    result = item
                    url = GetUrlViaAddress(result)


        for item in name_db:
            if query == item or query in item:
                result = item

                url = GetUrlViaName(result)


        if url == "none":
            #return HttpResponse(str(query))
            url = f"https://app.geckoterminal.com/api/p1/core/pools/%s" % (query)
            response = requests.get(url)
            if response.status_code == 404:
                return HttpResponseRedirect(reverse("main:token_details",args=[query,]))
            else:
                return HttpResponseRedirect(reverse("main:token_detail",args=[query,]))

        return HttpResponseRedirect(reverse("main:%s" % (url)))
        


    else:
        
        
        coredao = requests.get("https://api.dexscreener.com/latest/dex/tokens/0x40375C92d9FAf44d2f9db9Bd9ba41a3317a2404f")
        
        coredaodekatron = coredao.json()
        coredaopairs = coredaodekatron["pairs"][5]
        coredaobaseToken = coredaopairs["baseToken"]
        coredaopriceNative = coredaopairs["priceNative"]
        coredaopriceUsd = coredaopairs["priceUsd"]
        coredaovolume = coredaopairs["volume"]
        coredaopriceChange = coredaopairs["priceChange"]
        coredaofdv = coredaopairs["fdv"]
        
        ice = requests.get("https://api.dexscreener.com/latest/dex/tokens/0xb999ea90607a826a3e6e6646b404c3c7d11fa39d")
        icedekatron = ice.json()
        icepairs = icedekatron["pairs"][0]
        icebaseToken = icepairs["baseToken"]
        icepriceNative = icepairs["priceNative"]
        icepriceUsd = icepairs["priceUsd"]
        icevolume = icepairs["volume"]
        icepriceChange = icepairs["priceChange"]
        icefdv = icepairs["fdv"]
        
        bitrise = requests.get("https://api.dexscreener.com/latest/dex/tokens/0x8fff93e810a2edaafc326edee51071da9d398e83")
        bitrisedekatron = bitrise.json()
        bitrisepairs = bitrisedekatron["pairs"][0]
        bitrisebaseToken = bitrisepairs["baseToken"]
        bitrisepriceNative = bitrisepairs["priceNative"]
        bitrisepriceUsd = bitrisepairs["priceUsd"]
        bitrisevolume = bitrisepairs["volume"]
        bitrisepriceChange = bitrisepairs["priceChange"]
        bitrisefdv = bitrisepairs["fdv"]
        
        
        
        
        
        
        
        
        
        navis = requests.get("https://api.dexscreener.com/latest/dex/tokens/0x43a8a925c1930A313D283359184A64c51a2bc0E9")
        navisdekatron = navis.json()
        navispairs = navisdekatron["pairs"][0]
        navisbaseToken = navispairs["baseToken"]
        navispriceNative = navispairs["priceNative"]
        navispriceUsd = navispairs["priceUsd"]
        navisvolume = navispairs["volume"]
        navispriceChange = navispairs["priceChange"]
        navisfdv = navispairs["fdv"]
        
        bow = requests.get("https://api.dexscreener.com/latest/dex/tokens/0x1a639e150d2210A4BE4a5F0857A9151B241E7AE4")
        bowdekatron = bow.json()
        bowpairs = bowdekatron["pairs"][0]
        bowbaseToken = bowpairs["baseToken"]
        bowpriceNative = bowpairs["priceNative"]
        bowpriceUsd = bowpairs["priceUsd"]
        bowvolume = bowpairs["volume"]
        bowpriceChange = bowpairs["priceChange"]
        bowfdv = bowpairs["fdv"]
        
        shadow = requests.get("https://api.dexscreener.com/latest/dex/tokens/0xddBa66C1eBA873e26Ac0215Ca44892a07d83aDF5")
        shadowdekatron = shadow.json()
        shadowpairs = shadowdekatron["pairs"][0]
        shadowbaseToken = shadowpairs["baseToken"]
        shadowpriceNative = shadowpairs["priceNative"]
        shadowpriceUsd = shadowpairs["priceUsd"]
        shadowvolume = shadowpairs["volume"]
        shadowpriceChange = shadowpairs["priceChange"]
        shadowfdv = shadowpairs["fdv"]
        
        coreid = requests.get("https://api.dexscreener.com/latest/dex/tokens/0x000000000e1d682cc39abe9b32285fdea1255374")
        coreiddekatron = coreid.json()
        coreidpairs = coreiddekatron["pairs"][0]
        coreidbaseToken = coreidpairs["baseToken"]
        coreidpriceNative = coreidpairs["priceNative"]
        coreidpriceUsd = coreidpairs["priceUsd"]
        coreidvolume = coreidpairs["volume"]
        coreidpriceChange = coreidpairs["priceChange"]
        coreidfdv = coreidpairs["fdv"]
        
        crest = requests.get("https://api.dexscreener.com/latest/dex/tokens/0xcFE4C0783d103C44f403Bb287d29af0bAE5D4E84")
        crestdekatron = crest.json()
        crestpairs = crestdekatron["pairs"][0]
        crestbaseToken = crestpairs["baseToken"]
        crestpriceNative = crestpairs["priceNative"]
        crestpriceUsd = crestpairs["priceUsd"]
        crestvolume = crestpairs["volume"]
        crestpriceChange = crestpairs["priceChange"]
        crestfdv = crestpairs["fdv"]
        
        yields = requests.get("https://api.dexscreener.com/latest/dex/tokens/0xe191a4d47A6be111C75139757CDDBb61BEEd88FB")
        yieldsdekatron = yields.json()
        yieldspairs = yieldsdekatron["pairs"][0]
        yieldsbaseToken = yieldspairs["baseToken"]
        yieldspriceNative = yieldspairs["priceNative"]
        yieldspriceUsd = yieldspairs["priceUsd"]
        yieldsvolume = yieldspairs["volume"]
        yieldspriceChange = yieldspairs["priceChange"]
        yieldsfdv = yieldspairs["fdv"]
        
        lfgswap = requests.get("https://api.dexscreener.com/latest/dex/tokens/0xF7a0b80681eC935d6dd9f3Af9826E68B99897d6D")
        lfgswapdekatron = lfgswap.json()
        lfgswappairs = lfgswapdekatron["pairs"][0]
        lfgswapbaseToken = lfgswappairs["baseToken"]
        lfgswappriceNative = lfgswappairs["priceNative"]
        lfgswappriceUsd = lfgswappairs["priceUsd"]
        lfgswapvolume = lfgswappairs["volume"]
        lfgswappriceChange = lfgswappairs["priceChange"]
        lfgswapfdv = lfgswappairs["fdv"]
        
        happy = requests.get("https://api.dexscreener.com/latest/dex/tokens/0xAc9B3614Dd28c4ca72853CA996Ab76F03Db73Fb4")
        happydekatron = happy.json()
        happypairs = happydekatron["pairs"][0]
        happybaseToken = happypairs["baseToken"]
        happypriceNative = happypairs["priceNative"]
        happypriceUsd = happypairs["priceUsd"]
        happyvolume = happypairs["volume"]
        happypriceChange = happypairs["priceChange"]
        happyfdv = happypairs["fdv"]
        
        lung = requests.get("https://api.dexscreener.com/latest/dex/tokens/0x28b9aed756de31b6b362aa0f23211d13093ebb79")
        lungdekatron = lung.json()
        lungpairs = lungdekatron["pairs"][0]
        lungbaseToken = lungpairs["baseToken"]
        lungpriceNative = lungpairs["priceNative"]
        lungpriceUsd = lungpairs["priceUsd"]
        lungvolume = lungpairs["volume"]
        lungpriceChange = lungpairs["priceChange"]
        lungfdv = lungpairs["fdv"]
        
        ignorefud = requests.get("https://api.dexscreener.com/latest/dex/tokens/0x98564E70c7fCC6d947fFE6d9EfeD5ba68b306F2E")
        ignorefuddekatron = ignorefud.json()
        ignorefudpairs = ignorefuddekatron["pairs"][0]
        ignorefudbaseToken = ignorefudpairs["baseToken"]
        ignorefudpriceNative = ignorefudpairs["priceNative"]
        ignorefudpriceUsd = ignorefudpairs["priceUsd"]
        ignorefudvolume = ignorefudpairs["volume"]
        ignorefudpriceChange = ignorefudpairs["priceChange"]
        ignorefudfdv = ignorefudpairs["fdv"]
        
        ypc = requests.get("https://api.dexscreener.com/latest/dex/tokens/0xDC2393dc10734BF153153038943a5deB42b209cd")
        ypcdekatron = ypc.json()
        ypcpairs = ypcdekatron["pairs"][0]
        ypcbaseToken = ypcpairs["baseToken"]
        ypcpriceNative = ypcpairs["priceNative"]
        ypcpriceUsd = ypcpairs["priceUsd"]
        ypcvolume = ypcpairs["volume"]
        ypcpriceChange = ypcpairs["priceChange"]
        ypcfdv = ypcpairs["fdv"]
        
        woof = requests.get("https://api.dexscreener.com/latest/dex/tokens/0x5C44d3D2312AbA4d5F2406A98Bf374Bc76455092")
        woofdekatron = woof.json()
        woofpairs = woofdekatron["pairs"][0]
        woofbaseToken = woofpairs["baseToken"]
        woofpriceNative = woofpairs["priceNative"]
        woofpriceUsd = woofpairs["priceUsd"]
        woofvolume = woofpairs["volume"]
        woofpriceChange = woofpairs["priceChange"]
        wooffdv = woofpairs["fdv"]
        
        score = requests.get("https://api.dexscreener.com/latest/dex/tokens/0xA20b3B97df3a02f9185175760300a06B4e0A2C05")
        scoredekatron = score.json()
        scorepairs = scoredekatron["pairs"][0]
        scorebaseToken = scorepairs["baseToken"]
        scorepriceNative = scorepairs["priceNative"]
        scorepriceUsd = scorepairs["priceUsd"]
        scorevolume = scorepairs["volume"]
        scorepriceChange = scorepairs["priceChange"]
        scorefdv = scorepairs["fdv"]
        
        dc = requests.get("https://api.dexscreener.com/latest/dex/tokens/0x979A34f98b9a1bF2B38fD18f5c038423e4902db9")
        dcdekatron = dc.json()
        dcpairs = dcdekatron["pairs"][0]
        dcbaseToken = dcpairs["baseToken"]
        dcpriceNative = dcpairs["priceNative"]
        dcpriceUsd = dcpairs["priceUsd"]
        dcvolume = dcpairs["volume"]
        dcpriceChange = dcpairs["priceChange"]
        dcfdv = dcpairs["fdv"]
        
        aicore = requests.get("https://api.dexscreener.com/latest/dex/tokens/0x7621c97683A3b0499EC156bD257E44175e793bb1")
        aicoredekatron = aicore.json()
        aicorepairs = aicoredekatron["pairs"][0]
        aicorebaseToken = aicorepairs["baseToken"]
        aicorepriceNative = aicorepairs["priceNative"]
        aicorepriceUsd = aicorepairs["priceUsd"]
        aicorevolume = aicorepairs["volume"]
        aicorepriceChange = aicorepairs["priceChange"]
        aicorefdv = aicorepairs["fdv"] 
        
        hobo = requests.get("https://api.dexscreener.com/latest/dex/tokens/0x25100C0083e8E53b1cb264E978522bd477011A0d")
        hobodekatron = hobo.json()
        hobopairs = hobodekatron["pairs"][0]
        hobobaseToken = hobopairs["baseToken"]
        hobopriceNative = hobopairs["priceNative"]
        hobopriceUsd = hobopairs["priceUsd"]
        hobovolume = hobopairs["volume"]
        hobopriceChange = hobopairs["priceChange"]
        hobofdv = hobopairs["fdv"]  
        
        miidas = requests.get("https://api.dexscreener.com/latest/dex/tokens/0xcfd38184c30832917A2871695F91e5e61bBD41fF")
        miidasdekatron = miidas.json()
        miidaspairs = miidasdekatron["pairs"][0]
        miidasbaseToken = miidaspairs["baseToken"]
        miidaspriceNative = miidaspairs["priceNative"]
        miidaspriceUsd = miidaspairs["priceUsd"]
        miidasvolume = miidaspairs["volume"]
        miidaspriceChange = miidaspairs["priceChange"]
        miidasfdv = miidaspairs["fdv"]
        
        spoon = requests.get("https://api.dexscreener.com/latest/dex/tokens/0x66B96135d0c639D53e1f23b7a5849F6022883b41")
        spoondekatron = spoon.json()
        spoonpairs = spoondekatron["pairs"][0]
        spoonbaseToken = spoonpairs["baseToken"]
        spoonpriceNative = spoonpairs["priceNative"]
        spoonpriceUsd = spoonpairs["priceUsd"]
        spoonvolume = spoonpairs["volume"]
        spoonpriceChange = spoonpairs["priceChange"]
        spoonfdv = spoonpairs["fdv"]
        
        unity = requests.get("https://api.dexscreener.com/latest/dex/tokens/0x496Bb259D0117E89B2e73433524e9838c3073e60")
        unitydekatron = unity.json()
        unitypairs = unitydekatron["pairs"][0]
        unitybaseToken = unitypairs["baseToken"]
        unitypriceNative = unitypairs["priceNative"]
        unitypriceUsd = unitypairs["priceUsd"]
        unityvolume = unitypairs["volume"]
        unitypriceChange = unitypairs["priceChange"]
        unityfdv = unitypairs["fdv"]
        
        cdc = requests.get("https://api.dexscreener.com/latest/dex/tokens/0x8bab1Ef0F175F6d7EBCE79ee277BA091832F6429")
        cdcdekatron = cdc.json()
        cdcpairs = cdcdekatron["pairs"][0]
        cdcbaseToken = cdcpairs["baseToken"]
        cdcpriceNative = cdcpairs["priceNative"]
        cdcpriceUsd = cdcpairs["priceUsd"]
        cdcvolume = cdcpairs["volume"]
        cdcpriceChange = cdcpairs["priceChange"]
        cdcfdv = cdcpairs["fdv"]
        
        data = requests.get("https://api.dexscreener.com/latest/dex/tokens/0xc0E49f8C615d3d4c245970F6Dc528E4A47d69a44").json()
        pairs = data['pairs']
        token_list = []
        for pair in pairs:
            if pair['baseToken']['name'].lower() != 'icecream':
                token_list.append({
                    'name': pair['baseToken']['name'],
                    'address': pair['baseToken']['address'],
                    'price': pair['priceUsd'],
                    'symbol': pair['baseToken']['symbol'],
                    'volume': pair['volume']
                    })
        
        
        
        
        resp = requests.get("https://app.geckoterminal.com/api/p1/bitgert/pools/0x558077e98aeceeb1d616d18c144c15909d4ab744")
        getValue = resp.json()
        from_volume_in_usd = getValue["data"]["attributes"]["from_volume_in_usd"]

        context = {
            
            
            'token_list': token_list,
            
            "coredaobaseToken":coredaobaseToken, 
            "coredaovolume":coredaovolume, 
            "coredaopriceChange":coredaopriceChange, 
            "coredaopriceUsd":coredaopriceUsd, 
            "coredaofdv":coredaofdv, 
            
            "ice":ice, 
            "icebaseToken":icebaseToken, 
            "icepriceNative":icepriceNative, 
            "icepriceUsd":icepriceUsd, 
            "icevolume":icevolume, 
            "icepriceChange":icepriceChange, 
            "icefdv":icefdv, 
            
            "bitrise":bitrise, 
            "bitrisebaseToken":bitrisebaseToken, 
            "bitrisepriceNative":bitrisepriceNative, 
            "bitrisepriceUsd":bitrisepriceUsd, 
            "bitrisevolume":bitrisevolume, 
            "bitrisepriceChange":bitrisepriceChange, 
            "bitrisefdv":bitrisefdv,
            
            "from_volume_in_usd":from_volume_in_usd, 
            
            
            

            
            "navis":navis, 
            "navisbaseToken":navisbaseToken, 
            "navispriceNative":navispriceNative, 
            "navispriceUsd":navispriceUsd, 
            "navisvolume":navisvolume, 
            "navispriceChange":navispriceChange, 
            "navisfdv":navisfdv,
            
            "bow":bow, 
            "bowbaseToken":bowbaseToken, 
            "bowpriceNative":bowpriceNative, 
            "bowpriceUsd":bowpriceUsd, 
            "bowvolume":bowvolume, 
            "bowpriceChange":bowpriceChange, 
            "bowfdv":bowfdv,
            
            "shadow":shadow, 
            "shadowbaseToken":shadowbaseToken, 
            "shadowpriceNative":shadowpriceNative, 
            "shadowpriceUsd":shadowpriceUsd, 
            "shadowvolume":shadowvolume, 
            "shadowpriceChange":shadowpriceChange, 
            "shadowfdv":shadowfdv,
            
            "happy":happy, 
            "happybaseToken":happybaseToken, 
            "happypriceNative":happypriceNative, 
            "happypriceUsd":happypriceUsd, 
            "happyvolume":happyvolume, 
            "happypriceChange":happypriceChange, 
            "happyfdv":happyfdv,
            
            "coreid":coreid, 
            "coreidbaseToken":coreidbaseToken, 
            "coreidpriceNative":coreidpriceNative, 
            "coreidpriceUsd":coreidpriceUsd, 
            "coreidvolume":coreidvolume, 
            "coreidpriceChange":coreidpriceChange, 
            "coreidfdv":coreidfdv,
            
            "yields":yields, 
            "yieldsbaseToken":yieldsbaseToken, 
            "yieldspriceNative":yieldspriceNative, 
            "yieldspriceUsd":yieldspriceUsd, 
            "yieldsvolume":yieldsvolume, 
            "yieldspriceChange":yieldspriceChange, 
            "yieldsfdv":yieldsfdv,
            
            "crest":crest, 
            "crestbaseToken":crestbaseToken, 
            "crestpriceNative":crestpriceNative, 
            "crestpriceUsd":crestpriceUsd, 
            "crestvolume":crestvolume, 
            "crestpriceChange":crestpriceChange, 
            "crestfdv":crestfdv,
            
            "lfgswap":lfgswap, 
            "lfgswapbaseToken":lfgswapbaseToken, 
            "lfgswappriceNative":lfgswappriceNative, 
            "lfgswappriceUsd":lfgswappriceUsd, 
            "lfgswapvolume":lfgswapvolume, 
            "lfgswappriceChange":lfgswappriceChange, 
            "lfgswapfdv":lfgswapfdv,
            
            "lung":lung, 
            "lungbaseToken":lungbaseToken, 
            "lungpriceNative":lungpriceNative, 
            "lungpriceUsd":lungpriceUsd, 
            "lungvolume":lungvolume, 
            "lungpriceChange":lungpriceChange, 
            "lungfdv":lungfdv,
            
            "ignorefud":ignorefud, 
            "ignorefudbaseToken":ignorefudbaseToken, 
            "ignorefudpriceNative":ignorefudpriceNative, 
            "ignorefudpriceUsd":ignorefudpriceUsd, 
            "ignorefudvolume":ignorefudvolume, 
            "ignorefudpriceChange":ignorefudpriceChange, 
            "ignorefudfdv":ignorefudfdv,
            
            "ypc":ypc, 
            "ypcbaseToken":ypcbaseToken, 
            "ypcpriceNative":ypcpriceNative, 
            "ypcpriceUsd":ypcpriceUsd, 
            "ypcvolume":ypcvolume, 
            "ypcpriceChange":ypcpriceChange, 
            "ypcfdv":ypcfdv,
            
            "woof":woof, 
            "woofbaseToken":woofbaseToken, 
            "woofpriceNative":woofpriceNative, 
            "woofpriceUsd":woofpriceUsd, 
            "woofvolume":woofvolume, 
            "woofpriceChange":woofpriceChange, 
            "wooffdv":wooffdv,
            
            "score":score, 
            "scorebaseToken":scorebaseToken, 
            "scorepriceNative":scorepriceNative, 
            "scorepriceUsd":scorepriceUsd, 
            "scorevolume":scorevolume, 
            "scorepriceChange":scorepriceChange, 
            "scorefdv":scorefdv,
            
            "dc":dc, 
            "dcbaseToken":dcbaseToken, 
            "dcpriceNative":dcpriceNative, 
            "dcpriceUsd":dcpriceUsd, 
            "dcvolume":dcvolume, 
            "dcpriceChange":dcpriceChange, 
            "dcfdv":dcfdv,
            
            "hobo":hobo, 
            "hobobaseToken":hobobaseToken, 
            "hobopriceNative":hobopriceNative, 
            "hobopriceUsd":hobopriceUsd, 
            "hobovolume":hobovolume, 
            "hobopriceChange":hobopriceChange, 
            "hobofdv":hobofdv,
            
            "miidas":miidas, 
            "miidasbaseToken":miidasbaseToken, 
            "miidaspriceNative":miidaspriceNative, 
            "miidaspriceUsd":miidaspriceUsd, 
            "miidasvolume":miidasvolume, 
            "miidaspriceChange":miidaspriceChange, 
            "miidasfdv":miidasfdv,
            
            "unity":unity, 
            "unitybaseToken":unitybaseToken, 
            "unitypriceNative":unitypriceNative, 
            "unitypriceUsd":unitypriceUsd, 
            "unityvolume":unityvolume, 
            "unitypriceChange":unitypriceChange, 
            "unityfdv":unityfdv,
            
            "aicore":aicore, 
            "aicorebaseToken":aicorebaseToken, 
            "aicorepriceNative":aicorepriceNative, 
            "aicorepriceUsd":aicorepriceUsd, 
            "aicorevolume":aicorevolume, 
            "aicorepriceChange":aicorepriceChange, 
            "aicorefdv":aicorefdv,
            
            "spoon":spoon, 
            "spoonbaseToken":spoonbaseToken, 
            "spoonpriceNative":spoonpriceNative, 
            "spoonpriceUsd":spoonpriceUsd, 
            "spoonvolume":spoonvolume, 
            "spoonpriceChange":spoonpriceChange, 
            "spoonfdv":spoonfdv,
            
            #"cdc":cdc, 
            #"cdcbaseToken":cdcbaseToken, 
            #"cdcpriceNative":cdcpriceNative, 
            #"cdcpriceUsd":cdcpriceUsd, 
            #"cdcvolume":cdcvolume, 
            #"cdcpriceChange":cdcpriceChange, 
            #"cdcfdv":cdcfdv,
        }
        return render(request, "main/none.html", context)

def GetUrlViaAddress(address):
        
    if address == "0x27b45bCC26e01Ed50B4080A405D1c492FEe89d63":
        url = "doken"
    elif address == "0xce186ad6430e2fe494a22c9edbd4c68794a28b35":
        url = "loop"
    #elif address == "0xeA8686a739550d9C88FaEfb39aC6cb78B6288767":
        #url = "candy"
    elif address == "0xb999ea90607a826a3e6e6646b404c3c7d11fa39d":
        url = "ice"
    #
    elif address == "0x8fff93e810a2edaafc326edee51071da9d398e83":
        url = "bitgert"
    elif address == "0x826551890dc65655a0aceca109ab11abdbd7a07b":
        url = "canto"
    
    elif address == "0x43a8a925c1930A313D283359184A64c51a2bc0E9":
        url = "navis"
    elif address == "0x28b9aed756de31b6b362aa0f23211d13093ebb79":
        url = "lung"
    elif address == "0x40375C92d9FAf44d2f9db9Bd9ba41a3317a2404f":
        url = "core"
    elif address == "0xddBa66C1eBA873e26Ac0215Ca44892a07d83aDF5":
        url = "shadowswap"
    elif address == "0x1a639e150d2210A4BE4a5F0857A9151B241E7AE4":
        url = "bow"
    elif address == "0xb999ea90607a826a3e6e6646b404c3c7d11fa39d":
        url = "ice"
    elif address == "0x000000000e1d682cc39abe9b32285fdea1255374":
        url = "coreid"
    elif address == "0xcFE4C0783d103C44f403Bb287d29af0bAE5D4E84":
        url = "crest"
    elif address == "0xe191a4d47A6be111C75139757CDDBb61BEEd88FB":
        url = "yieldz"
    elif address == "0xF7a0b80681eC935d6dd9f3Af9826E68B99897d6D":
        url = "lfgswap"
    elif address == "0xAc9B3614Dd28c4ca72853CA996Ab76F03Db73Fb4":
        url = "happy"
    elif address == "0xDC2393dc10734BF153153038943a5deB42b209cd":
        url = "ypc"
    elif address == "0x98564E70c7fCC6d947fFE6d9EfeD5ba68b306F2E":
        url = "4token"
    elif address == "0x979A34f98b9a1bF2B38fD18f5c038423e4902db9":
        url = "3dc"
    elif address == "0x7621c97683A3b0499EC156bD257E44175e793bb1":
        url = "aicore"
    elif address == "0x7469bae0b0bc80a208eb0946121b5aff686a6ac2":
        url = "ainu"
    elif address == "0xBb790D1e8A2d34e9d846bb00EA0b0380813375EE":
        url = "akio"
    elif address == "0xBFa14641bf0fE84dE3fcf3Bf227900af445f09C3":
        url = "bcore"
    elif address == "0xbFf24592345094DFA4d6f75aFF5BE79AbCbC9bD9":
        url = "block"
    elif address == "0xE8dEC1bFC7BF572D60403c609d6589715d2a23fC":
        url = "bitvexa"
    elif address == "0x25100C0083e8E53b1cb264E978522bd477011A0d":
        url = "hobo"
    elif address == "0x5C44d3D2312AbA4d5F2406A98Bf374Bc76455092":
        url = "woof"
    elif address == "0xAA7912C028E058e4bD90Bcbb9fB41C27DbcC3245":
        url = "word"
    elif address == "0xA20b3B97df3a02f9185175760300a06B4e0A2C05":
        url = "score"
    elif address == "0x6F8BF0Ca89b8936AA498c7A2C75815Eecca328F3":
        url = "cbunny"
    elif address == "0x6501cca79ca8d6f68784f2345c9a379951e30a05":
        url = "cshare"
    elif address == "0xC830a752eef79F2D66a36645A70fB0bA176b4Cea":
        url = "ctomb"
    elif address == "0x8afb52de791a19873c3097195ef04d48ed93fe14":
        url = "emperor"
    elif address == "0x5aE225fa6573903CA58E26Cd4171B87060CeEAA2":
        url = "flash"
    elif address == "0xDBa57074B81CD0630D7960dFAA370972C5E1A6D9":
        url = "green"
    elif address == "0xA7c0B19645B653B4373E3592C84fce8C64D89E8F":
        url = "royale"
    elif address == "0xcfd38184c30832917A2871695F91e5e61bBD41fF":
        url = "miidas"
    elif address == "0x496Bb259D0117E89B2e73433524e9838c3073e60":
        url = "unity"
    elif address == "0x66B96135d0c639D53e1f23b7a5849F6022883b41":
        url = "spoon"
    elif address == "0x8bab1Ef0F175F6d7EBCE79ee277BA091832F6429":
        url = "coredoge"
    elif address == "0x9B944a707cfDE49b7c0a9593f88b17Dc2C05DB78":
        url = "pepe"
    elif address == "0xAB82f8b18ea7929815076F152b8Fd24F8b267274":
        url = "map"
    elif address == "0x9c765C62ad538011c2aAd815CaAeEc94551fbE9D":
        url = "yfi"

    else:
        url = "none"


    return url

def GetUrlViaName(name):

    if name == "Doken Super Chain (DSC)":
        url = "doken"
    elif name == "LoopNetwork (LOOP)":
        url = "loop"
    #elif name == "CandySwap (CANDY)":
        #url = "candy"
    elif name == "IceCreamSwap (ICE)":
        url = "ice"
    elif name == "Bitgert (Brise)":
        url = "bitgert"
    elif name == "Canto (CANTO)":
        url = "canto"
    elif name == "Navis (NVS)":
        url = "navis"
    elif name == "Lunagens (LUNG)":
        url = "lung"
    elif name == "Coredao (CORE)":
        url = "core"
    elif name == "ShadowSwap (SHADOW)":
        url = 'shadowswap'
    elif name == "Archerswap (BOW)":
        url = "bow"
    elif name == "Icecreamswap (ICE)":
        url = "ice"
    elif name == "Coreid (COREID)":
        url = "coreid"
    elif name == "Crest Protocol (CPT)":
        url = "crest"
    elif name == "Yieldz (YZ)":
        url = "yieldz"
    elif name == "LFGSwap (LFG)":
        url = "lfgswap"
    elif name == "Happy Token (HAPPY)":
        url = "happy"
    elif name == "Young Parrot (YPC)":
        url = "ypc"
    elif name == "Ignore Fud (4Token)":
        url = "4token"
    elif name == "3DCity (3dc)":
        url = "3dc"
    elif name == "AI Core Token (Aicore)":
        url = "aicore"
    elif name == "Aiinu (Aiinu)":
        url = "ainu"
    elif name == "Akio Inu (Akio)":
        url = "akio"
    elif name == "Big Core (BCore)":
        url = "bcore"
    elif name == "Block Verse (Block)":
        url = "block"
    elif name == "Bitvexa (Btv)":
        url = "bitvexa"
    elif name == "Hobo Universe (Hobo)":
        url = "hobo"
    elif name == "Woof (Woof)":
        url = "woof"
    elif name == "Starlybooks (Word)":
        url = "word"
    elif name == "Staked Core (SCore)":
        url = "score"
    elif name == "Core Bunny (cbunny)":
        url = "cbunny"
    elif name == "Core Share (cshare)":
        url = "cshare"
    elif name == "CoreTomb (ctomb)":
        url = "ctomb"
    elif name == "Emperor (emperor)":
        url = "emperor"
    elif name == "FlashX Max (FSXM)":
        url = "flash"
    elif name == "Green Ranger (GR)":
        url = "green"
    elif name == "MemeRoyale (Royale)":
        url = "royale"
    elif name == "Miidas (miidas)":
        url = "miidas"
    elif name == "Unity Core (Unity)":
        url = "unity"
    elif name == "Spoon (Poon)":
        url = "spoon"
    elif name == "Coredoge (CDC)":
        url = "coredoge"
    elif name == "Pepe Token (pepe)":
        url = "pepe"
    elif name == "4D Twin Maps (Map)":
        url = "map"
    elif name == "YFI (YFI)":
        url = "yfi"
    
        
    else:
        url = "none"

    return url


def IndexView(request):
    if request.method == "POST":
        address_db = [
        "0x27b45bCC26e01Ed50B4080A405D1c492FEe89d63",
        "0xce186ad6430e2fe494a22c9edbd4c68794a28b35",
        "0xb999ea90607a826a3e6e6646b404c3c7d11fa39d",
        "0x8fff93e810a2edaafc326edee51071da9d398e83",
        "0x826551890dc65655a0aceca109ab11abdbd7a07b",
        "0x43a8a925c1930A313D283359184A64c51a2bc0E9",
        "0x28b9aed756de31b6b362aa0f23211d13093ebb79",
        "0x81bCEa03678D1CEF4830942227720D542Aa15817",
        "0xddBa66C1eBA873e26Ac0215Ca44892a07d83aDF5",
        "0x1a639e150d2210A4BE4a5F0857A9151B241E7AE4",
        "0xb999ea90607a826a3e6e6646b404c3c7d11fa39d",
        "0x000000000e1d682cc39abe9b32285fdea1255374",
        "0xcFE4C0783d103C44f403Bb287d29af0bAE5D4E84",
        "0xe191a4d47A6be111C75139757CDDBb61BEEd88FB",
        "0xF7a0b80681eC935d6dd9f3Af9826E68B99897d6D",
        "0xAc9B3614Dd28c4ca72853CA996Ab76F03Db73Fb4",
        "0xDC2393dc10734BF153153038943a5deB42b209cd",
        "0x98564E70c7fCC6d947fFE6d9EfeD5ba68b306F2E",
        "0x979A34f98b9a1bF2B38fD18f5c038423e4902db9",
        "0x7621c97683A3b0499EC156bD257E44175e793bb1",
        "0x7469bae0b0bc80a208eb0946121b5aff686a6ac2",
        "0xBb790D1e8A2d34e9d846bb00EA0b0380813375EE",
        "0xBFa14641bf0fE84dE3fcf3Bf227900af445f09C3",
        "0xbFf24592345094DFA4d6f75aFF5BE79AbCbC9bD9",
        "0xE8dEC1bFC7BF572D60403c609d6589715d2a23fC",
        "0x25100C0083e8E53b1cb264E978522bd477011A0d",
        "0x5C44d3D2312AbA4d5F2406A98Bf374Bc76455092",
        "0xAA7912C028E058e4bD90Bcbb9fB41C27DbcC3245",
        "0xA20b3B97df3a02f9185175760300a06B4e0A2C05",
        "0x6F8BF0Ca89b8936AA498c7A2C75815Eecca328F3",
        "0x6501cca79ca8d6f68784f2345c9a379951e30a05",
        "0xC830a752eef79F2D66a36645A70fB0bA176b4Cea",
        "0x8afb52de791a19873c3097195ef04d48ed93fe14",
        "0x5aE225fa6573903CA58E26Cd4171B87060CeEAA2",
        "0xDBa57074B81CD0630D7960dFAA370972C5E1A6D9",
        "0xA7c0B19645B653B4373E3592C84fce8C64D89E8F",
        "0xcfd38184c30832917A2871695F91e5e61bBD41fF",
        "0x496Bb259D0117E89B2e73433524e9838c3073e60",
        "0x40375C92d9FAf44d2f9db9Bd9ba41a3317a2404f",
        "0x66B96135d0c639D53e1f23b7a5849F6022883b41",
        "0x8bab1Ef0F175F6d7EBCE79ee277BA091832F6429",
        "0x9B944a707cfDE49b7c0a9593f88b17Dc2C05DB78",
        "0xAB82f8b18ea7929815076F152b8Fd24F8b267274",
        "0x9c765C62ad538011c2aAd815CaAeEc94551fbE9D",
        ]

        name_db = ["Doken Super Chain (DSC)", "LoopNetwork (LOOP)", "IceCreamSwap (ICE)", "Bitgert (BRISE)", "Canto (Canto)", "Navis (NVS)", "Lunagens (LUNG)", "ShadowSwap (SHADOW)", "Coredao (CORE)", "Archerswap (BOW)", "Icecreamswap (ICE)", "Coreid (coreid)", "Crest Protocol (CPT)", "Yieldz (YZ)", "LFGSwap (LFG)", "Happy Token (HAPPY)", "Young Parrot (YPC)", "Ignore Fud (4Token)", "3DCity (3dc)", "AI Core Token (Aicore)", "Aiinu (Aiinu)", "Akio Inu (Akio)", "Big Core (BCore)", "BlockVerse (Block)", "Bitvexa (Btv)", "Hobo Universe (Hobo)", "Woof (Woof)", "Starlybooks (Word)", "Staked Core (SCore)", "Core Bunny (cbunny)", "Core Share (cshare)", "CoreTomb (ctomb)", "Emperor (emperor)", "FlashX Max (FSXM)", "Green Ranger (GR)", "MemeRoyale (Royale)", "Miidas (miidas)", "Unity Core (Unity)", "Spoon (Poon)", "Coredoge (CDC)", "Pepe Token (pepe)", "4D Twin Map (Map)", "YFI (YFI)"]

        status = False
        result = None
        url = "none"

        query = request.POST.get("query")

        if query[0]+query[1] == "0x":
            for item in address_db:
                if query == item:
                    result = item
                    url = GetUrlViaAddress(result)


        for item in name_db:
            if query == item or query in item:
                result = item

                url = GetUrlViaName(result)
                
        
        if url == "none":
            #return HttpResponse(str(query))
            url = f"https://app.geckoterminal.com/api/p1/core/pools/%s" % (query)
            response = requests.get(url)
            if response.status_code == 404:
                return HttpResponseRedirect(reverse("main:token_detail",args=[query,]))
            else:
                return HttpResponseRedirect(reverse("main:token_details",args=[query,]))
                
            


        return HttpResponseRedirect(reverse("main:%s" % (url)))
        


    else:
        #data = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=game-fantasy-token&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
        
        #trend = trending.json()
        #coins = trend["coins"][:4]
        #mcap = market.json()
        #m_data = mcap["data"]
        
        #candy = requests.get("https://api.dexscreener.com/latest/dex/tokens/0xeA8686a739550d9C88FaEfb39aC6cb78B6288767")
        
        #candydekatron = candy.json()
        #candypairs = candydekatron["pairs"][0]
        #candybaseToken = candypairs["baseToken"]
        #candypriceNative = candypairs["priceNative"]
        #candypriceUsd = candypairs["priceUsd"]
        #candyvolume = candypairs["volume"]
        #candypriceChange = candypairs["priceChange"]
        #candyfdv = candypairs["fdv"]
        
        
        futures = [DekatronShadow(), DekatronBow(), DekatronIce(), DekatronCoredao(), DekatronCoreid(), DekatronWoof(), DekatronSpoon(), DekatronData(), DekatronPepe(), DekatronMiidas(), DekatronIgnore()]
        
        try:
            loop = asyncio.get_event_loop()
        
        except RuntimeError as ex:
            if "There is no current event loop in thread" in str(ex):
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                loop = asyncio.get_event_loop()
        
        results, pending = loop.run_until_complete(asyncio.wait(futures))
        
        

        token_list = []
        for item in results:
            
            
        
            if (item.result()[0]["address"]) == "0x5C44d3D2312AbA4d5F2406A98Bf374Bc76455092":
        
                #woof = requests.get("https://api.dexscreener.com/latest/dex/tokens/0x5C44d3D2312AbA4d5F2406A98Bf374Bc76455092")
                woofbaseToken = item.result()[0]
                woofpriceNative = item.result()[1]
                woofpriceUsd = item.result()[2]
                woofvolume = item.result()[3]
                woofpriceChange = item.result()[4]
                wooffdv = item.result()[5]
                try:
                    wooflogo = item.result()[6]
                except:
                    wooflogo = None
        
            if (item.result()[0]["address"]) == "0xB999Ea90607a826A3E6E6646B404c3C7d11fa39D":
                #ice = requests.get("https://api.dexscreener.com/latest/dex/tokens/0xb999ea90607a826a3e6e6646b404c3c7d11fa39d")
                icebaseToken = item.result()[0]
                icepriceNative = item.result()[1]
                icepriceUsd = item.result()[2]
                icevolume = item.result()[3]
                icepriceChange = item.result()[4]
                icefdv = item.result()[5]
                try:
                    icelogo = item.result()[6]
                except:
                    icelogo = None
                    
            if (item.result()[0]["address"]) == "0x000000000E1D682Cc39ABe9B32285fdEa1255374":
                #coreid = requests.get("https://api.dexscreener.com/latest/dex/tokens/0x000000000e1d682cc39abe9b32285fdea1255374")
                coreidbaseToken = item.result()[0]
                coreidpriceNative = item.result()[1]
                coreidpriceUsd = item.result()[2]
                coreidvolume = item.result()[3]
                coreidpriceChange = item.result()[4]
                coreidfdv = item.result()[5]
                try:
                    coreidlogo = item.result()[6]
                except:
                    coreidlogo = None
        
            
        
        
            if len(item.result()) > 7:
                token_list = item.result() 
        
            
            if (item.result()[0]["address"]) == "0x66B96135d0c639D53e1f23b7a5849F6022883b41":
                #spoon = requests.get("https://api.dexscreener.com/latest/dex/tokens/0x66B96135d0c639D53e1f23b7a5849F6022883b41")
                spoonbaseToken = item.result()[0]
                spoonpriceNative = item.result()[1]
                spoonpriceUsd = item.result()[2]
                spoonvolume = item.result()[3]
                spoonpriceChange = item.result()[4]
                spoonfdv = item.result()[5]
                try:
                    spoonlogo = item.result()[6]
                except:
                    spoonlogo = None
        
            if (item.result()[0]["address"]) == "0x1a639e150d2210A4BE4a5F0857A9151B241E7AE4":
                #bow = requests.get("https://api.dexscreener.com/latest/dex/tokens/0x1a639e150d2210A4BE4a5F0857A9151B241E7AE4")
                bowbaseToken = item.result()[0]
                bowpriceNative = item.result()[1]
                bowpriceUsd = item.result()[2]
                bowvolume = item.result()[3]
                bowpriceChange = item.result()[4]
                bowfdv = item.result()[5]
                try:
                    bowlogo = item.result()[6]
                except:
                    bowlogo = None
        
            if (item.result()[0]["address"]) == "0x8bab1Ef0F175F6d7EBCE79ee277BA091832F6429":
                #cdc = requests.get("https://api.dexscreener.com/latest/dex/tokens/0x8bab1Ef0F175F6d7EBCE79ee277BA091832F6429")
                cdcbaseToken = item.result()[0]
                cdcpriceNative = item.result()[1]
                cdcpriceUsd = item.result()[2]
                cdcvolume = item.result()[3]
                cdcpriceChange = item.result()[4]
                cdcfdv = item.result()[5]
                try:
                    cdclogo = item.result()[6]
                except:
                    cdclogo = None
            
            
            
            if (item.result()[0]["address"]) == "0x9B944a707cfDE49b7c0a9593f88b17Dc2C05DB78":
                #pepe = requests.get("https://api.dexscreener.com/latest/dex/tokens/0x9B944a707cfDE49b7c0a9593f88b17Dc2C05DB78")
                pepebaseToken = item.result()[0]
                pepepriceNative = item.result()[1]
                pepepriceUsd = item.result()[2]
                pepevolume = item.result()[3]
                pepepriceChange = item.result()[4]
                pepefdv = item.result()[5]
                try:
                    pepelogo = item.result()[6]
                except:
                    pepelogo = None
            
            if (item.result()[0]["address"]) == "0xcfd38184c30832917A2871695F91e5e61bBD41fF":
                #miidas = requests.get("https://api.dexscreener.com/latest/dex/tokens/0xcfd38184c30832917A2871695F91e5e61bBD41fF")
                miidasbaseToken = item.result()[0]
                miidaspriceNative = item.result()[1]
                miidaspriceUsd = item.result()[2]
                miidasvolume = item.result()[3]
                miidaspriceChange = item.result()[4]
                miidasfdv = item.result()[5]
                try:
                    pepelogo = item.result()[6]
                except:
                    pepelogo = None
                    
            if (item.result()[0]["address"]) == "0x98564E70c7fCC6d947fFE6d9EfeD5ba68b306F2E":
                #ignorefud = requests.get("https://api.dexscreener.com/latest/dex/tokens/0x98564E70c7fCC6d947fFE6d9EfeD5ba68b306F2E")
                ignorefudbaseToken = item.result()[0]
                ignorefudpriceNative = item.result()[1]
                ignorefudpriceUsd = item.result()[2]
                ignorefudvolume = item.result()[3]
                ignorefudpriceChange = item.result()[4]
                ignorefudfdv = item.result()[5]
                try:
                    ignorefudlogo = item.result()[6]
                except:
                    ignorefudlogo = None
                    
            
        
            if (item.result()[0]["address"]) == "0xddBa66C1eBA873e26Ac0215Ca44892a07d83aDF5":
                #shadow = requests.get("https://api.dexscreener.com/latest/dex/tokens/0xddBa66C1eBA873e26Ac0215Ca44892a07d83aDF5")
                shadowbaseToken = item.result()[0]
                shadowpriceNative = item.result()[1]
                shadowpriceUsd = item.result()[2]
                shadowvolume = item.result()[3]
                shadowpriceChange = item.result()[4]
                shadowfdv = item.result()[5]
                try:
                    shadowlogo = item.result()[6]
                except:
                    shadowlogo = item.result()[6] 
        
            else:
                pass
        
        
        
        
        
                

        context = {
            
            
            'token_list': token_list,
            
             
            
            #"ice":ice, 
            "icebaseToken":icebaseToken, 
            "icepriceNative":icepriceNative, 
            "icepriceUsd":icepriceUsd, 
            "icevolume":icevolume, 
            "icepriceChange":icepriceChange, 
            "icefdv":icefdv, 

            #"woof":woof, 
            "woofbaseToken":woofbaseToken, 
            "woofpriceNative":woofpriceNative, 
            "woofpriceUsd":woofpriceUsd, 
            "woofvolume":woofvolume, 
            "woofpriceChange":woofpriceChange, 
            "wooffdv":wooffdv,

            #"bow":bow, 
            "bowbaseToken":bowbaseToken, 
            "bowpriceNative":bowpriceNative, 
            "bowpriceUsd":bowpriceUsd, 
            "bowvolume":bowvolume, 
            "bowpriceChange":bowpriceChange, 
            "bowfdv":bowfdv,
            
            #"shadow":shadow, 
            "shadowbaseToken":shadowbaseToken, 
            "shadowpriceNative":shadowpriceNative, 
            "shadowpriceUsd":shadowpriceUsd, 
            "shadowvolume":shadowvolume, 
            "shadowpriceChange":shadowpriceChange, 
            "shadowfdv":shadowfdv,
            "shadowlogo":shadowlogo,

            #"coreid":coreid, 
            "coreidbaseToken":coreidbaseToken, 
            "coreidpriceNative":coreidpriceNative, 
            "coreidpriceUsd":coreidpriceUsd, 
            "coreidvolume":coreidvolume, 
            "coreidpriceChange":coreidpriceChange, 
            "coreidfdv":coreidfdv,

            

            #"spoon":spoon, 
            "spoonbaseToken":spoonbaseToken, 
            "spoonpriceNative":spoonpriceNative, 
            "spoonpriceUsd":spoonpriceUsd, 
            "spoonvolume":spoonvolume, 
            "spoonpriceChange":spoonpriceChange, 
            "spoonfdv":spoonfdv,
            
            #"cdc":cdc, 
            #"cdcbaseToken":cdcbaseToken, 
            #"cdcpriceNative":cdcpriceNative, 
            #"cdcpriceUsd":cdcpriceUsd, 
            #"cdcvolume":cdcvolume, 
            #"cdcpriceChange":cdcpriceChange, 
            #"cdcfdv":cdcfdv,
            
            #"pepe":pepe, 
            "pepebaseToken":pepebaseToken, 
            "pepepriceNative":pepepriceNative, 
            "pepepriceUsd":pepepriceUsd, 
            "pepevolume":pepevolume, 
            "pepepriceChange":pepepriceChange, 
            "pepefdv":pepefdv,
            
            #"miidas":miidas, 
            "miidasbaseToken":miidasbaseToken, 
            "miidaspriceNative":miidaspriceNative, 
            "miidaspriceUsd":miidaspriceUsd, 
            "miidasvolume":miidasvolume, 
            "miidaspriceChange":miidaspriceChange, 
            "miidasfdv":miidasfdv,
            
            #"ignorefud":ignorefud, 
            "ignorefudbaseToken":ignorefudbaseToken, 
            "ignorefudpriceNative":ignorefudpriceNative, 
            "ignorefudpriceUsd":ignorefudpriceUsd, 
            "ignorefudvolume":ignorefudvolume, 
            "ignorefudpriceChange":ignorefudpriceChange, 
            "ignorefudfdv":ignorefudfdv,
            
            
        }
        return render(request, "main/index.html", context )
 
 
def MoreView(request):
    if request.method == "POST":
        address_db = [
        "0x27b45bCC26e01Ed50B4080A405D1c492FEe89d63",
        "0xce186ad6430e2fe494a22c9edbd4c68794a28b35",
        "0xb999ea90607a826a3e6e6646b404c3c7d11fa39d",
        "0x8fff93e810a2edaafc326edee51071da9d398e83",
        "0x826551890dc65655a0aceca109ab11abdbd7a07b",
        "0x43a8a925c1930A313D283359184A64c51a2bc0E9",
        "0x28b9aed756de31b6b362aa0f23211d13093ebb79",
        "0x81bCEa03678D1CEF4830942227720D542Aa15817",
        "0xddBa66C1eBA873e26Ac0215Ca44892a07d83aDF5",
        "0x1a639e150d2210A4BE4a5F0857A9151B241E7AE4",
        "0xb999ea90607a826a3e6e6646b404c3c7d11fa39d",
        "0x000000000e1d682cc39abe9b32285fdea1255374",
        "0xcFE4C0783d103C44f403Bb287d29af0bAE5D4E84",
        "0xe191a4d47A6be111C75139757CDDBb61BEEd88FB",
        "0xF7a0b80681eC935d6dd9f3Af9826E68B99897d6D",
        "0xAc9B3614Dd28c4ca72853CA996Ab76F03Db73Fb4",
        "0xDC2393dc10734BF153153038943a5deB42b209cd",
        "0x98564E70c7fCC6d947fFE6d9EfeD5ba68b306F2E",
        "0x979A34f98b9a1bF2B38fD18f5c038423e4902db9",
        "0x7621c97683A3b0499EC156bD257E44175e793bb1",
        "0x7469bae0b0bc80a208eb0946121b5aff686a6ac2",
        "0xBb790D1e8A2d34e9d846bb00EA0b0380813375EE",
        "0xBFa14641bf0fE84dE3fcf3Bf227900af445f09C3",
        "0xbFf24592345094DFA4d6f75aFF5BE79AbCbC9bD9",
        "0xE8dEC1bFC7BF572D60403c609d6589715d2a23fC",
        "0x25100C0083e8E53b1cb264E978522bd477011A0d",
        "0x5C44d3D2312AbA4d5F2406A98Bf374Bc76455092",
        "0xAA7912C028E058e4bD90Bcbb9fB41C27DbcC3245",
        "0xA20b3B97df3a02f9185175760300a06B4e0A2C05",
        "0x6F8BF0Ca89b8936AA498c7A2C75815Eecca328F3",
        "0x6501cca79ca8d6f68784f2345c9a379951e30a05",
        "0xC830a752eef79F2D66a36645A70fB0bA176b4Cea",
        "0x8afb52de791a19873c3097195ef04d48ed93fe14",
        "0x5aE225fa6573903CA58E26Cd4171B87060CeEAA2",
        "0xDBa57074B81CD0630D7960dFAA370972C5E1A6D9",
        "0xA7c0B19645B653B4373E3592C84fce8C64D89E8F",
        "0xcfd38184c30832917A2871695F91e5e61bBD41fF",
        "0x496Bb259D0117E89B2e73433524e9838c3073e60",
        "0x40375C92d9FAf44d2f9db9Bd9ba41a3317a2404f",
        "0x66B96135d0c639D53e1f23b7a5849F6022883b41",
        "0x8bab1Ef0F175F6d7EBCE79ee277BA091832F6429",
        "0x9B944a707cfDE49b7c0a9593f88b17Dc2C05DB78",
        "0xAB82f8b18ea7929815076F152b8Fd24F8b267274",
        "0x9c765C62ad538011c2aAd815CaAeEc94551fbE9D",
        ]

        name_db = ["Doken Super Chain (DSC)", "LoopNetwork (LOOP)", "IceCreamSwap (ICE)", "Bitgert (BRISE)", "Canto (Canto)", "Navis (NVS)", "Lunagens (LUNG)", "ShadowSwap (SHADOW)", "Coredao (CORE)", "Archerswap (BOW)", "Icecreamswap (ICE)", "Coreid (coreid)", "Crest Protocol (CPT)", "Yieldz (YZ)", "LFGSwap (LFG)", "Happy Token (HAPPY)", "Young Parrot (YPC)", "Ignore Fud (4Token)", "3DCity (3dc)", "AI Core Token (Aicore)", "Aiinu (Aiinu)", "Akio Inu (Akio)", "Big Core (BCore)", "BlockVerse (Block)", "Bitvexa (Btv)", "Hobo Universe (Hobo)", "Woof (Woof)", "Starlybooks (Word)", "Staked Core (SCore)", "Core Bunny (cbunny)", "Core Share (cshare)", "CoreTomb (ctomb)", "Emperor (emperor)", "FlashX Max (FSXM)", "Green Ranger (GR)", "MemeRoyale (Royale)", "Miidas (miidas)", "Unity Core (Unity)", "Spoon (Poon)", "Coredoge (CDC)", "Pepe Token (pepe)", "4D Twin Map (Map)", "YFI (YFI)"]

        status = False
        result = None
        url = "none"

        query = request.POST.get("query")

        if query[0]+query[1] == "0x":
            for item in address_db:
                if query == item:
                    result = item
                    url = GetUrlViaAddress(result)


        for item in name_db:
            if query == item or query in item:
                result = item

                url = GetUrlViaName(result)
                
        
        if url == "none":
            #return HttpResponse(str(query))
            url = f"https://app.geckoterminal.com/api/p1/core/pools/%s" % (query)
            response = requests.get(url)
            if response.status_code == 404:
                return HttpResponseRedirect(reverse("main:token_detail",args=[query,]))
            else:
                return HttpResponseRedirect(reverse("main:token_details",args=[query,]))
                
            


        return HttpResponseRedirect(reverse("main:%s" % (url)))
        


    else:
        #data = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=game-fantasy-token&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
        
        #trend = trending.json()
        #coins = trend["coins"][:4]
        #mcap = market.json()
        #m_data = mcap["data"]
        
        #candy = requests.get("https://api.dexscreener.com/latest/dex/tokens/0xeA8686a739550d9C88FaEfb39aC6cb78B6288767")
        
        #candydekatron = candy.json()
        #candypairs = candydekatron["pairs"][0]
        #candybaseToken = candypairs["baseToken"]
        #candypriceNative = candypairs["priceNative"]
        #candypriceUsd = candypairs["priceUsd"]
        #candyvolume = candypairs["volume"]
        #candypriceChange = candypairs["priceChange"]
        #candyfdv = candypairs["fdv"]
        
        
        futures = [DekatronShadow(), DekatronBow(), DekatronIce(), DekatronCoredao(), DekatronCoreid(), DekatronWoof(), DekatronUnity(), DekatronSpoon(), DekatronData(), DekatronPepe(), DekatronMiidas(), DekatronScore(), DekatronBlock(), DekatronDc(), DekatronMap(), DekatronYpc(), DekatronHobo(), DekatronIgnore(), DekatronLfg(), DekatronCrest(), DekatronCshare(), DekatronCtomb(), DekatronWord(), DekatronRoyale(), DekatronYfi(),]
        loop = asyncio.get_event_loop()
        
        results, pending = loop.run_until_complete(asyncio.wait(futures))
        
        coredao = requests.get("https://api.dexscreener.com/latest/dex/tokens/0x40375C92d9FAf44d2f9db9Bd9ba41a3317a2404f")
        coredaobaseToken = None
        coredaopriceNative = None
        coredaopriceUsd = None
        coredaovolume = None
        coredaopriceChange = None
        coredaofdv = None
        coredaologo = None

        
        for item in results:
            
            
        
            if (item.result()[0]["address"]) == "0x5C44d3D2312AbA4d5F2406A98Bf374Bc76455092":
        
                woof = requests.get("https://api.dexscreener.com/latest/dex/tokens/0x5C44d3D2312AbA4d5F2406A98Bf374Bc76455092")
                woofbaseToken = item.result()[0]
                woofpriceNative = item.result()[1]
                woofpriceUsd = item.result()[2]
                woofvolume = item.result()[3]
                woofpriceChange = item.result()[4]
                wooffdv = item.result()[5]
                try:
                    wooflogo = item.result()[6]
                except:
                    wooflogo = None
        
            if (item.result()[0]["address"]) == "0xB999Ea90607a826A3E6E6646B404c3C7d11fa39D":
                ice = requests.get("https://api.dexscreener.com/latest/dex/tokens/0xb999ea90607a826a3e6e6646b404c3c7d11fa39d")
                icebaseToken = item.result()[0]
                icepriceNative = item.result()[1]
                icepriceUsd = item.result()[2]
                icevolume = item.result()[3]
                icepriceChange = item.result()[4]
                icefdv = item.result()[5]
                try:
                    icelogo = item.result()[6]
                except:
                    icelogo = None
                    
            if (item.result()[0]["address"]) == "0x000000000E1D682Cc39ABe9B32285fdEa1255374":
                coreid = requests.get("https://api.dexscreener.com/latest/dex/tokens/0x000000000e1d682cc39abe9b32285fdea1255374")
                coreidbaseToken = item.result()[0]
                coreidpriceNative = item.result()[1]
                coreidpriceUsd = item.result()[2]
                coreidvolume = item.result()[3]
                coreidpriceChange = item.result()[4]
                coreidfdv = item.result()[5]
                try:
                    coreidlogo = item.result()[6]
                except:
                    coreidlogo = None
        
            if (item.result()[0]["address"]) == "0x40375C92d9FAf44d2f9db9Bd9ba41a3317a2404f":
                coredao = requests.get("https://api.dexscreener.com/latest/dex/tokens/0x40375C92d9FAf44d2f9db9Bd9ba41a3317a2404f")
                coredaobaseToken = item.result()[0]
                coredaopriceNative = item.result()[1]
                coredaopriceUsd = item.result()[2]
                coredaovolume = item.result()[3]
                coredaopriceChange = item.result()[4]
                coredaofdv = item.result()[5]
                try:
                    coredaologo = item.result()[6]
                except:
                    coredaologo = None
        
        
            if len(item.result()) > 7:
                token_list = item.result()
        
            
            if (item.result()[0]["address"]) == "0x66B96135d0c639D53e1f23b7a5849F6022883b41":
                spoon = requests.get("https://api.dexscreener.com/latest/dex/tokens/0x66B96135d0c639D53e1f23b7a5849F6022883b41")
                spoonbaseToken = item.result()[0]
                spoonpriceNative = item.result()[1]
                spoonpriceUsd = item.result()[2]
                spoonvolume = item.result()[3]
                spoonpriceChange = item.result()[4]
                spoonfdv = item.result()[5]
                try:
                    spoonlogo = item.result()[6]
                except:
                    spoonlogo = None
        
            if (item.result()[0]["address"]) == "0x1a639e150d2210A4BE4a5F0857A9151B241E7AE4":
                bow = requests.get("https://api.dexscreener.com/latest/dex/tokens/0x1a639e150d2210A4BE4a5F0857A9151B241E7AE4")
                bowbaseToken = item.result()[0]
                bowpriceNative = item.result()[1]
                bowpriceUsd = item.result()[2]
                bowvolume = item.result()[3]
                bowpriceChange = item.result()[4]
                bowfdv = item.result()[5]
                try:
                    bowlogo = item.result()[6]
                except:
                    bowlogo = None
        
            if (item.result()[0]["address"]) == "0x8bab1Ef0F175F6d7EBCE79ee277BA091832F6429":
                cdc = requests.get("https://api.dexscreener.com/latest/dex/tokens/0x8bab1Ef0F175F6d7EBCE79ee277BA091832F6429")
                cdcbaseToken = item.result()[0]
                cdcpriceNative = item.result()[1]
                cdcpriceUsd = item.result()[2]
                cdcvolume = item.result()[3]
                cdcpriceChange = item.result()[4]
                cdcfdv = item.result()[5]
                try:
                    cdclogo = item.result()[6]
                except:
                    cdclogo = None
                    
            if (item.result()[0]["address"]) == "0x979A34f98b9a1bF2B38fD18f5c038423e4902db9":
                dc = requests.get("https://api.dexscreener.com/latest/dex/tokens/0x979A34f98b9a1bF2B38fD18f5c038423e4902db9")
                dcbaseToken = item.result()[0]
                dcpriceNative = item.result()[1]
                dcpriceUsd = item.result()[2]
                dcvolume = item.result()[3]
                dcpriceChange = item.result()[4]
                dcfdv = item.result()[5]
                try:
                    dclogo = item.result()[6]
                except:
                    dclogo = None
                    
            if (item.result()[0]["address"]) == "0xA7c0B19645B653B4373E3592C84fce8C64D89E8F":
                royale = requests.get("https://api.dexscreener.com/latest/dex/tokens/0xA7c0B19645B653B4373E3592C84fce8C64D89E8F")
                royalebaseToken = item.result()[0]
                royalepriceNative = item.result()[1]
                royalepriceUsd = item.result()[2]
                royalevolume = item.result()[3]
                royalepriceChange = item.result()[4]
                royalefdv = item.result()[5]
                try:
                    royalelogo = item.result()[6]
                except:
                    royalelogo = None
            
            if (item.result()[0]["address"]) == "0x496Bb259D0117E89B2e73433524e9838c3073e60":
                unity = requests.get("https://api.dexscreener.com/latest/dex/tokens/0x496Bb259D0117E89B2e73433524e9838c3073e60")
                unitybaseToken = item.result()[0]
                unitypriceNative = item.result()[1]
                unitypriceUsd = item.result()[2]
                unityvolume = item.result()[3]
                unitypriceChange = item.result()[4]
                unityfdv = item.result()[5]
                try:
                    unitylogo = item.result()[6]
                except:
                    unitylogo = None
            
            if (item.result()[0]["address"]) == "0x9B944a707cfDE49b7c0a9593f88b17Dc2C05DB78":
                pepe = requests.get("https://api.dexscreener.com/latest/dex/tokens/0x9B944a707cfDE49b7c0a9593f88b17Dc2C05DB78")
                pepebaseToken = item.result()[0]
                pepepriceNative = item.result()[1]
                pepepriceUsd = item.result()[2]
                pepevolume = item.result()[3]
                pepepriceChange = item.result()[4]
                pepefdv = item.result()[5]
                try:
                    pepelogo = item.result()[6]
                except:
                    pepelogo = None
            
            if (item.result()[0]["address"]) == "0xcfd38184c30832917A2871695F91e5e61bBD41fF":
                miidas = requests.get("https://api.dexscreener.com/latest/dex/tokens/0xcfd38184c30832917A2871695F91e5e61bBD41fF")
                miidasbaseToken = item.result()[0]
                miidaspriceNative = item.result()[1]
                miidaspriceUsd = item.result()[2]
                miidasvolume = item.result()[3]
                miidaspriceChange = item.result()[4]
                miidasfdv = item.result()[5]
                try:
                    miidaslogo = item.result()[6]
                except:
                    miidaslogo = None
            
            if (item.result()[0]["address"]) == "0xAB82f8b18ea7929815076F152b8Fd24F8b267274":
                map = requests.get("https://api.dexscreener.com/latest/dex/tokens/0xAB82f8b18ea7929815076F152b8Fd24F8b267274")
                mapbaseToken = item.result()[0]
                mappriceNative = item.result()[1]
                mappriceUsd = item.result()[2]
                mapvolume = item.result()[3]
                mappriceChange = item.result()[4]
                mapfdv = item.result()[5]
                try:
                    maplogo = item.result()[6]
                except:
                    maplogo = None
                    
            if (item.result()[0]["address"]) == "0xDC2393dc10734BF153153038943a5deB42b209cd":
                ypc = requests.get("https://api.dexscreener.com/latest/dex/tokens/0xDC2393dc10734BF153153038943a5deB42b209cd")
                ypcbaseToken = item.result()[0]
                ypcpriceNative = item.result()[1]
                ypcpriceUsd = item.result()[2]
                ypcvolume = item.result()[3]
                ypcpriceChange = item.result()[4]
                ypcfdv = item.result()[5]
                try:
                    ypclogo = item.result()[6]
                except:
                    ypclogo = None 
            
            if (item.result()[0]["address"]) == "0x25100C0083e8E53b1cb264E978522bd477011A0d":
                hobo = requests.get("https://api.dexscreener.com/latest/dex/tokens/0x25100C0083e8E53b1cb264E978522bd477011A0d")
                hobobaseToken = item.result()[0]
                hobopriceNative = item.result()[1]
                hobopriceUsd = item.result()[2]
                hobovolume = item.result()[3]
                hobopriceChange = item.result()[4]
                hobofdv = item.result()[5]
                try:
                    hobologo = item.result()[6]
                except:
                    hobologo = None
                    
            if (item.result()[0]["address"]) == "0xF7a0b80681eC935d6dd9f3Af9826E68B99897d6D":
                lfgswap = requests.get("https://api.dexscreener.com/latest/dex/tokens/0xF7a0b80681eC935d6dd9f3Af9826E68B99897d6D")
                lfgswapbaseToken = item.result()[0]
                lfgswappriceNative = item.result()[1]
                lfgswappriceUsd = item.result()[2]
                lfgswapvolume = item.result()[3]
                lfgswappriceChange = item.result()[4]
                lfgswapfdv = item.result()[5]
                try:
                    lfgswaplogo = item.result()[6]
                except:
                    lfgswaplogo = None
                    
            if (item.result()[0]["address"]) == "0xe191a4d47A6be111C75139757CDDBb61BEEd88FB":
                score = requests.get("https://api.dexscreener.com/latest/dex/tokens/0xe191a4d47A6be111C75139757CDDBb61BEEd88FB")
                scorebaseToken = item.result()[0]
                scorepriceNative = item.result()[1]
                scorepriceUsd = item.result()[2]
                scorevolume = item.result()[3]
                scorepriceChange = item.result()[4]
                scorefdv = item.result()[5]
                try:
                    scorelogo = item.result()[6]
                except:
                    scorelogo = None
                    
            if (item.result()[0]["address"]) == "0xbFf24592345094DFA4d6f75aFF5BE79AbCbC9bD9":
                block = requests.get("https://api.dexscreener.com/latest/dex/tokens/0xbFf24592345094DFA4d6f75aFF5BE79AbCbC9bD9")
                blockbaseToken = item.result()[0]
                blockpriceNative = item.result()[1]
                blockpriceUsd = item.result()[2]
                blockvolume = item.result()[3]
                blockpriceChange = item.result()[4]
                blockfdv = item.result()[5]
                try:
                    scorelogo = item.result()[6]
                except:
                    scorelogo = None
                    
            if (item.result()[0]["address"]) == "0x98564E70c7fCC6d947fFE6d9EfeD5ba68b306F2E":
                ignorefud = requests.get("https://api.dexscreener.com/latest/dex/tokens/0x98564E70c7fCC6d947fFE6d9EfeD5ba68b306F2E")
                ignorefudbaseToken = item.result()[0]
                ignorefudpriceNative = item.result()[1]
                ignorefudpriceUsd = item.result()[2]
                ignorefudvolume = item.result()[3]
                ignorefudpriceChange = item.result()[4]
                ignorefudfdv = item.result()[5]
                try:
                    ignorefudlogo = item.result()[6]
                except:
                    ignorefudlogo = None
                    
            if (item.result()[0]["address"]) == "0xcFE4C0783d103C44f403Bb287d29af0bAE5D4E84":
                crest = requests.get("https://api.dexscreener.com/latest/dex/tokens/0xcFE4C0783d103C44f403Bb287d29af0bAE5D4E84")
                crestbaseToken = item.result()[0]
                crestpriceNative = item.result()[1]
                crestpriceUsd = item.result()[2]
                crestvolume = item.result()[3]
                crestpriceChange = item.result()[4]
                crestfdv = item.result()[5]
                try:
                    crestlogo = item.result()[6]
                except:
                    crestlogo = None
                    
            if (item.result()[0]["address"]) == "0x6501cCA79ca8D6F68784f2345c9a379951e30A05":
                cshare = requests.get("https://api.dexscreener.com/latest/dex/tokens/0x6501cCA79ca8D6F68784f2345c9a379951e30A05")
                csharebaseToken = item.result()[0]
                csharepriceNative = item.result()[1]
                csharepriceUsd = item.result()[2]
                csharevolume = item.result()[3]
                csharepriceChange = item.result()[4]
                csharefdv = item.result()[5]
                try:
                    csharelogo = item.result()[6]
                except:
                    csharelogo = None
                    
            if (item.result()[0]["address"]) == "0xC830a752eef79F2D66a36645A70fB0bA176b4Cea":
                ctomb = requests.get("https://api.dexscreener.com/latest/dex/tokens/0xC830a752eef79F2D66a36645A70fB0bA176b4Cea")
                ctombbaseToken = item.result()[0]
                ctombpriceNative = item.result()[1]
                ctombpriceUsd = item.result()[2]
                ctombvolume = item.result()[3]
                ctombpriceChange = item.result()[4]
                ctombfdv = item.result()[5]
                try:
                    ctomblogo = item.result()[6]
                except:
                    ctomblogo = None
                    
            if (item.result()[0]["address"]) == "0xAA7912C028E058e4bD90Bcbb9fB41C27DbcC3245":
                word = requests.get("https://api.dexscreener.com/latest/dex/tokens/0xAA7912C028E058e4bD90Bcbb9fB41C27DbcC3245")
                wordbaseToken = item.result()[0]
                wordpriceNative = item.result()[1]
                wordpriceUsd = item.result()[2]
                wordvolume = item.result()[3]
                wordpriceChange = item.result()[4]
                wordfdv = item.result()[5]
                try:
                    wordlogo = item.result()[6]
                except:
                    wordlogo = None
                    
            if (item.result()[0]["address"]) == "0x9c765C62ad538011c2aAd815CaAeEc94551fbE9D":
                yfi = requests.get("https://api.dexscreener.com/latest/dex/tokens/0x9c765C62ad538011c2aAd815CaAeEc94551fbE9D")
                yfibaseToken = item.result()[0]
                yfipriceNative = item.result()[1]
                yfipriceUsd = item.result()[2]
                yfivolume = item.result()[3]
                yfipriceChange = item.result()[4]
                yfifdv = item.result()[5]
                try:
                    yfilogo = item.result()[6]
                except:
                    yfilogo = None
        
            if (item.result()[0]["address"]) == "0xddBa66C1eBA873e26Ac0215Ca44892a07d83aDF5":
                shadow = requests.get("https://api.dexscreener.com/latest/dex/tokens/0xddBa66C1eBA873e26Ac0215Ca44892a07d83aDF5")
                shadowbaseToken = item.result()[0]
                shadowpriceNative = item.result()[1]
                shadowpriceUsd = item.result()[2]
                shadowvolume = item.result()[3]
                shadowpriceChange = item.result()[4]
                shadowfdv = item.result()[5]
                try:
                    shadowlogo = item.result()[6]
                except:
                    shadowlogo = item.result()[6]
                    
                    
        
            else:
                pass
        
        
        
        
        
                

        context = {
            
            
            'token_list': token_list,
            
            "coredaobaseToken":coredaobaseToken, 
            "coredaovolume":coredaovolume, 
            "coredaopriceChange":coredaopriceChange, 
            "coredaopriceUsd":coredaopriceUsd, 
            "coredaofdv":coredaofdv, 
            
            "ice":ice, 
            "icebaseToken":icebaseToken, 
            "icepriceNative":icepriceNative, 
            "icepriceUsd":icepriceUsd, 
            "icevolume":icevolume, 
            "icepriceChange":icepriceChange, 
            "icefdv":icefdv, 
            
            "block":block, 
            "blockbaseToken":blockbaseToken, 
            "blockpriceNative":blockpriceNative, 
            "blockpriceUsd":blockpriceUsd, 
            "blockvolume":blockvolume, 
            "blockpriceChange":blockpriceChange, 
            "blockfdv":blockfdv,

            "woof":woof, 
            "woofbaseToken":woofbaseToken, 
            "woofpriceNative":woofpriceNative, 
            "woofpriceUsd":woofpriceUsd, 
            "woofvolume":woofvolume, 
            "woofpriceChange":woofpriceChange, 
            "wooffdv":wooffdv,

            "bow":bow, 
            "bowbaseToken":bowbaseToken, 
            "bowpriceNative":bowpriceNative, 
            "bowpriceUsd":bowpriceUsd, 
            "bowvolume":bowvolume, 
            "bowpriceChange":bowpriceChange, 
            "bowfdv":bowfdv,
            
            "word":word, 
            "wordbaseToken":wordbaseToken, 
            "wordpriceNative":wordpriceNative, 
            "wordpriceUsd":wordpriceUsd, 
            "wordvolume":wordvolume, 
            "wordpriceChange":wordpriceChange, 
            "wordfdv":wordfdv,
            
            "shadow":shadow, 
            "shadowbaseToken":shadowbaseToken, 
            "shadowpriceNative":shadowpriceNative, 
            "shadowpriceUsd":shadowpriceUsd, 
            "shadowvolume":shadowvolume, 
            "shadowpriceChange":shadowpriceChange, 
            "shadowfdv":shadowfdv,
            "shadowlogo":shadowlogo,

            "coreid":coreid, 
            "coreidbaseToken":coreidbaseToken, 
            "coreidpriceNative":coreidpriceNative, 
            "coreidpriceUsd":coreidpriceUsd, 
            "coreidvolume":coreidvolume, 
            "coreidpriceChange":coreidpriceChange, 
            "coreidfdv":coreidfdv,

            "unity":unity, 
            "unitybaseToken":unitybaseToken, 
            "unitypriceNative":unitypriceNative, 
            "unitypriceUsd":unitypriceUsd, 
            "unityvolume":unityvolume, 
            "unitypriceChange":unitypriceChange, 
            "unityfdv":unityfdv,
            
            "score":score, 
            "scorebaseToken":scorebaseToken, 
            "scorepriceNative":scorepriceNative, 
            "scorepriceUsd":scorepriceUsd, 
            "scorevolume":scorevolume, 
            "scorepriceChange":scorepriceChange, 
            "scorefdv":scorefdv,

            "spoon":spoon, 
            "spoonbaseToken":spoonbaseToken, 
            "spoonpriceNative":spoonpriceNative, 
            "spoonpriceUsd":spoonpriceUsd, 
            "spoonvolume":spoonvolume, 
            "spoonpriceChange":spoonpriceChange, 
            "spoonfdv":spoonfdv,
            
            #"cdc":cdc, 
            #"cdcbaseToken":cdcbaseToken, 
            #"cdcpriceNative":cdcpriceNative, 
            #"cdcpriceUsd":cdcpriceUsd, 
            #"cdcvolume":cdcvolume, 
            #"cdcpriceChange":cdcpriceChange, 
            #"cdcfdv":cdcfdv,
            
            "cshare":cshare, 
            "csharebaseToken":csharebaseToken, 
            "csharepriceNative":csharepriceNative, 
            "csharepriceUsd":csharepriceUsd, 
            "csharevolume":csharevolume, 
            "csharepriceChange":csharepriceChange, 
            "csharefdv":csharefdv,
            
            "ctomb":ctomb, 
            "ctombbaseToken":ctombbaseToken, 
            "ctombpriceNative":ctombpriceNative, 
            "ctombpriceUsd":ctombpriceUsd, 
            "ctombvolume":ctombvolume, 
            "ctombpriceChange":ctombpriceChange, 
            "ctombfdv":ctombfdv,
            
            "dc":dc, 
            "dcbaseToken":dcbaseToken, 
            "dcpriceNative":dcpriceNative, 
            "dcpriceUsd":dcpriceUsd, 
            "dcvolume":dcvolume, 
            "dcpriceChange":dcpriceChange, 
            "dcfdv":dcfdv,
            
            "royale":royale, 
            "royalebaseToken":royalebaseToken, 
            "royalepriceNative":royalepriceNative, 
            "royalepriceUsd":royalepriceUsd, 
            "royalevolume":royalevolume, 
            "royalepriceChange":royalepriceChange, 
            "royalefdv":royalefdv,
            
            "crest":crest, 
            "crestbaseToken":crestbaseToken, 
            "crestpriceNative":crestpriceNative, 
            "crestpriceUsd":crestpriceUsd, 
            "crestvolume": crestvolume, 
            "crestpriceChange":crestpriceChange, 
            "crestfdv":crestfdv,
            
            "pepe":pepe, 
            "pepebaseToken":pepebaseToken, 
            "pepepriceNative":pepepriceNative, 
            "pepepriceUsd":pepepriceUsd, 
            "pepevolume":pepevolume, 
            "pepepriceChange":pepepriceChange, 
            "pepefdv":pepefdv,
            
            "miidas":miidas, 
            "miidasbaseToken":miidasbaseToken, 
            "miidaspriceNative":miidaspriceNative, 
            "miidaspriceUsd":miidaspriceUsd, 
            "miidasvolume":miidasvolume, 
            "miidaspriceChange":miidaspriceChange, 
            "miidasfdv":miidasfdv,
            
            "map":map, 
            "mapbaseToken":mapbaseToken, 
            "mappriceNative":mappriceNative, 
            "mappriceUsd":mappriceUsd, 
            "mapvolume":mapvolume, 
            "mappriceChange":mappriceChange, 
            "mapfdv":mapfdv,
            
            "ypc":ypc, 
            "ypcbaseToken":ypcbaseToken, 
            "ypcpriceNative":ypcpriceNative, 
            "ypcpriceUsd":ypcpriceUsd, 
            "ypcvolume":ypcvolume, 
            "ypcpriceChange":ypcpriceChange, 
            "ypcfdv":ypcfdv,
            
            "yfi":yfi, 
            "yfibaseToken":yfibaseToken, 
            "yfipriceNative":yfipriceNative, 
            "yfipriceUsd":yfipriceUsd, 
            "yfivolume":yfivolume, 
            "yfipriceChange":yfipriceChange, 
            "yfifdv":yfifdv,
            
            "hobo":hobo, 
            "hobobaseToken":hobobaseToken, 
            "hobopriceNative":hobopriceNative, 
            "hobopriceUsd":hobopriceUsd, 
            "hobovolume":hobovolume, 
            "hobopriceChange":hobopriceChange, 
            "hobofdv":hobofdv,
            
            "lfgswap":lfgswap, 
            "lfgswapbaseToken":lfgswapbaseToken, 
            "lfgswappriceNative":lfgswappriceNative, 
            "lfgswappriceUsd":lfgswappriceUsd, 
            "lfgswapvolume":lfgswapvolume, 
            "lfgswappriceChange":lfgswappriceChange, 
            "lfgswapfdv":lfgswapfdv,
            
            "ignorefud":ignorefud, 
            "ignorefudbaseToken":ignorefudbaseToken, 
            "ignorefudpriceNative":ignorefudpriceNative, 
            "ignorefudpriceUsd":ignorefudpriceUsd, 
            "ignorefudvolume":ignorefudvolume, 
            "ignorefudpriceChange":ignorefudpriceChange, 
            "ignorefudfdv":ignorefudfdv,
        }
        return render(request, "main/more.html", context )       
        
def pool_info(request, page):
    url = "https://app.geckoterminal.com/api/p1/core/pools?page=%s" % (int(page))
    response = requests.get(url)
    data = response.json()
    pool_data = []
    
    try:
        checker = data["data"]
    
        # Fetch all pages
        #next_page = data["links"]["next"]
        #while next_page is not None:
    #		response = requests.get(next_page)
        #	data["data"].extend(response.json()["data"])
        #	next_page = response.json()["links"]["next"]
        
        # Extract relevant data from each pool
        
        for pool in data["data"]:
            attributes = pool["attributes"]
            pool_data.append({
                "name": attributes["name"],
                "price": attributes["price_in_usd"],
                "address": attributes["address"],
                "price_percent_change": attributes["price_percent_change"],
                "from_volume_in_usd": attributes["from_volume_in_usd"],
                "to_volume_in_usd": attributes["to_volume_in_usd"],
            })
            
    except:
        pass
    
    if page <= 1:
        back_page = 1
    else:
        back_page = int(page)-1
        
    context = {"pool_data": pool_data, "next_page": int(page)+1, "back_page": back_page}
    return render(request, "main/pool_info.html", context)



def token_detail(request, token_id):
    try:
        url = f"https://app.geckoterminal.com/api/p1/core/pools/{token_id}"
        response = requests.get(url)
        data = response.json()
        
        # Extract relevant data from the token
        attributes = data["data"]["attributes"]
        
    
        token_data = {
            "name": attributes["name"],
            "price": attributes['price_in_usd'],
            "address": attributes["address"],
            "swap": attributes["swap_url"],
            "fdv": attributes["fully_diluted_valuation"],
            "swap_count": attributes["swap_count_24h"],
            "priceChange": attributes["price_percent_change"],
            "from_volume_in_usd": attributes["from_volume_in_usd"],
            "pool_fee": attributes["pool_fee"]
        }
    
    except:
        return HttpResponseRedirect(reverse("main:none"))
    
    context = {"token_data": token_data}
    return render(request, "main/token_detail.html", context)

def token_details(request, token_id):
    data = requests.get("https://api.dexscreener.com/latest/dex/tokens/0xc0E49f8C615d3d4c245970F6Dc528E4A47d69a44").json()
    pairs = data['pairs']
    for pair in pairs:
        if pair['baseToken']['address'] == token_id:
            token = pair['baseToken']
            price = pair ["priceUsd"]
            txns = pair ["txns"]
            priceChange = pair["priceChange"]
            liquidity = pair["liquidity"]
            fdv = pair["fdv"]
            volume = pair["volume"]
            chainId = pair["chainId"]
            dexId = pair["dexId"]
        elif pair['quoteToken']['address'] == token_id:
            token = pair['quoteToken']
            
        else:
            return HttpResponseRedirect(reverse("main:none"))
            
    context = {"token": token, "price":price, "txns":txns, "priceChange":"priceChange", "fdv":fdv, "liquidity":liquidity, "volume":volume, "chainId":chainId, "dexId":dexId}
    return render(request, 'main/token_details.html', context)
        
        
def DokenView(request):
    if request.method == "POST":
        pass
    else:
        response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=doken&vs_currencies=usd&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true&include_last_updated_at=true").json()
        data = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=doken&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
        rs = requests.get("https://api.dexscreener.io/latest/dex/tokens/0x0420eb45ac5a4f04763f679c07c3a637741e0289")
        dekatrons = rs.json()
        pairs = dekatrons["pairs"][0]
        baseToken = pairs["baseToken"]
        priceNative = pairs["priceNative"]
        priceUsd = pairs["priceUsd"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        priceChange = pairs["priceChange"]
        volume = pairs["volume"]
        fdv = pairs["fdv"]
        price = str(response["doken"]["usd"])
        market_cap = int(response["doken"]["usd_market_cap"])
        hr_vol = str(response["doken"]["usd_24h_vol"])
        hr_chg = str(response["doken"]["usd_24h_change"])
        last_updated = str(response["doken"]["last_updated_at"])
        context = {"data":data, "price":price, "market_cap":market_cap, "hr_vol":hr_vol, "hr_chg":hr_chg, "last_updated":last_updated,"priceNative":priceNative, "priceChange":priceChange, "volume":volume, "fdv":fdv, "volume":volume, "txns":txns, "priceUsd":priceUsd}
        return render(request, "main/doken.html", context)
        
def CoreView(request):
    if request.method == "POST":
        pass
    else:
        rs = requests.get("https://api.dexscreener.com/latest/dex/tokens/0x40375C92d9FAf44d2f9db9Bd9ba41a3317a2404f")
        resp = requests.get("https://app.geckoterminal.com/api/p1/bsc/pools/0xeb667758145bf8b9358f536284efa549f1d4d0cb")
        getValue = resp.json()
        price_in_usd = getValue["data"]["attributes"]["price_in_usd"]
        fully_diluted_valuation = getValue["data"]["attributes"]["fully_diluted_valuation"]
        price_percent_change = getValue["data"]["attributes"]["price_percent_change"]
        from_volume_in_usd = getValue["data"]["attributes"]["from_volume_in_usd"]
        dekatrons = rs.json()
        pairs = dekatrons["pairs"][15]
        baseToken = pairs["baseToken"]
        priceNative = pairs["priceNative"]
        priceUsd = pairs["priceUsd"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        priceChange = pairs["priceChange"]
        liquidity = pairs["liquidity"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        fdv = pairs["fdv"]
        
        context = {"baseToken":baseToken,"priceNative":priceNative, "priceChange":priceChange, "volume":volume, "fdv":fdv, "volume":volume, "txns":txns, "priceUsd":priceUsd, "liquidity":liquidity, "txns":txns, "price_in_usd":price_in_usd, "fully_diluted_valuation":fully_diluted_valuation, "price_percent_change":price_percent_change, "from_volume_in_usd":from_volume_in_usd}
        return render(request, "main/core.html", context)


def LoopView(request):
    if request.method == "POST":
        pass
    else:
        response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=loopnetwork&vs_currencies=usd&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true&include_last_updated_at=true").json()
        data = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=loopnetwork&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
        rs = requests.get("https://api.dexscreener.io/latest/dex/tokens/0xce186ad6430e2fe494a22c9edbd4c68794a28b35")
        dekatrons = rs.json()
        pairs = dekatrons["pairs"][0]
        baseToken = pairs["baseToken"]
        priceNative = pairs["priceNative"]
        priceUsd = pairs["priceUsd"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        priceChange = pairs["priceChange"]
        volume = pairs["volume"]
        fdv = pairs["fdv"]
        price = str(response["loopnetwork"]["usd"])
        market_cap = int(response["loopnetwork"]["usd_market_cap"])
        hr_vol = str(response["loopnetwork"]["usd_24h_vol"])
        hr_chg = str(response["loopnetwork"]["usd_24h_change"])
        last_updated = str(response["loopnetwork"]["last_updated_at"])
        context = {"data":data, "price":price, "market_cap":market_cap, "hr_vol":hr_vol, "hr_chg":hr_chg, "last_updated":last_updated,"priceNative":priceNative, "priceChange":priceChange, "volume":volume, "fdv":fdv, "volume":volume, "txns":txns, "priceUsd":priceUsd}
        return render(request, "main/loop.html", context)
        
def CandyView(request):
    if request.method == "POST":
        pass
    else:
        
        
        rs = requests.get("https://api.dexscreener.io/latest/dex/tokens/0xeA8686a739550d9C88FaEfb39aC6cb78B6288767")
        dekatrons = rs.json()
        pairs = dekatrons["pairs"][0]
        baseToken = pairs["baseToken"]
        priceNative = pairs["priceNative"]
        priceUsd = pairs["priceUsd"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        priceChange = pairs["priceChange"]
        liquidity = pairs["liquidity"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        fdv = pairs["fdv"]
        
        context = {"baseToken":baseToken,"priceNative":priceNative, "priceChange":priceChange, "volume":volume, "fdv":fdv, "volume":volume, "txns":txns, "priceUsd":priceUsd, "liquidity":liquidity, "txns":txns}
        return render(request, "main/candy.html", context)
        
def IceView(request):
    if request.method == "POST":
        pass
    else:
        
        
        rs = requests.get("https://api.dexscreener.com/latest/dex/tokens/0xb999ea90607a826a3e6e6646b404c3c7d11fa39d")
        resp = requests.get("https://app.geckoterminal.com/api/p1/bitgert/pools/0x558077e98aeceeb1d616d18c144c15909d4ab744")
        getValue = resp.json()
        price_in_usd = getValue["data"]["attributes"]["price_in_usd"]
        fully_diluted_valuation = getValue["data"]["attributes"]["fully_diluted_valuation"]
        price_percent_change = getValue["data"]["attributes"]["price_percent_change"]
        from_volume_in_usd = getValue["data"]["attributes"]["from_volume_in_usd"]
        dekatrons = rs.json()
        pairs = dekatrons["pairs"][0]
        baseToken = pairs["baseToken"]
        priceNative = pairs["priceNative"]
        priceUsd = pairs["priceUsd"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        priceChange = pairs["priceChange"]
        liquidity = pairs["liquidity"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        fdv = pairs["fdv"]
        
        context = {"baseToken":baseToken,"priceNative":priceNative, "priceChange":priceChange, "volume":volume, "fdv":fdv, "volume":volume, "txns":txns, "priceUsd":priceUsd, "liquidity":liquidity, "txns":txns, "price_in_usd":price_in_usd, "fully_diluted_valuation":fully_diluted_valuation, "price_percent_change":price_percent_change, "from_volume_in_usd":from_volume_in_usd}
        return render(request, "main/ice.html", context)
        
def NavisView(request):
    if request.method == "POST":
        pass
    else:
        
        
        rs = requests.get("https://api.dexscreener.com/latest/dex/tokens/0x43a8a925c1930A313D283359184A64c51a2bc0E9")
        resp = requests.get("https://app.geckoterminal.com/api/p1/bsc/pools/0xeb667758145bf8b9358f536284efa549f1d4d0cb")
        getValue = resp.json()
        price_in_usd = getValue["data"]["attributes"]["price_in_usd"]
        fully_diluted_valuation = getValue["data"]["attributes"]["fully_diluted_valuation"]
        price_percent_change = getValue["data"]["attributes"]["price_percent_change"]
        from_volume_in_usd = getValue["data"]["attributes"]["from_volume_in_usd"]
        dekatrons = rs.json()
        pairs = dekatrons["pairs"][0]
        baseToken = pairs["baseToken"]
        priceNative = pairs["priceNative"]
        priceUsd = pairs["priceUsd"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        priceChange = pairs["priceChange"]
        liquidity = pairs["liquidity"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        fdv = pairs["fdv"]
        
        context = {"baseToken":baseToken,"priceNative":priceNative, "priceChange":priceChange, "volume":volume, "fdv":fdv, "volume":volume, "txns":txns, "priceUsd":priceUsd, "liquidity":liquidity, "txns":txns, "price_in_usd":price_in_usd, "fully_diluted_valuation":fully_diluted_valuation, "price_percent_change":price_percent_change, "from_volume_in_usd":from_volume_in_usd}
        return render(request, "main/navis.html", context)
    
def BowView(request):
    if request.method == "POST":
        pass
    else:
        
        
        rs = requests.get("https://api.dexscreener.com/latest/dex/tokens/0x1a639e150d2210A4BE4a5F0857A9151B241E7AE4")
        resp = requests.get("https://app.geckoterminal.com/api/p1/core/pools/0xbb8502132c87ee31be0e2bc1cb8cc69374488261")
        getValue = resp.json()
        price_in_usd = getValue["data"]["attributes"]["price_in_usd"]
        fully_diluted_valuation = getValue["data"]["attributes"]["fully_diluted_valuation"]
        price_percent_change = getValue["data"]["attributes"]["price_percent_change"]
        from_volume_in_usd = getValue["data"]["attributes"]["from_volume_in_usd"]
        dekatrons = rs.json()
        pairs = dekatrons["pairs"][0]
        baseToken = pairs["baseToken"]
        priceNative = pairs["priceNative"]
        priceUsd = pairs["priceUsd"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        priceChange = pairs["priceChange"]
        liquidity = pairs["liquidity"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        fdv = pairs["fdv"]
        
        context = {"baseToken":baseToken,"priceNative":priceNative, "priceChange":priceChange, "volume":volume, "fdv":fdv, "volume":volume, "txns":txns, "priceUsd":priceUsd, "liquidity":liquidity, "txns":txns, "price_in_usd":price_in_usd, "fully_diluted_valuation":fully_diluted_valuation, "price_percent_change":price_percent_change, "from_volume_in_usd":from_volume_in_usd}
        return render(request, "main/bow.html", context) 
        
def ShadowView(request):
    if request.method == "POST":
        pass
    else:
        
        
        rs = requests.get("https://api.dexscreener.com/latest/dex/tokens/0xddBa66C1eBA873e26Ac0215Ca44892a07d83aDF5")
        resp = requests.get("https://app.geckoterminal.com/api/p1/core/pools/0xbb8502132c87ee31be0e2bc1cb8cc69374488261")
        getValue = resp.json()
        price_in_usd = getValue["data"]["attributes"]["price_in_usd"]
        fully_diluted_valuation = getValue["data"]["attributes"]["fully_diluted_valuation"]
        price_percent_change = getValue["data"]["attributes"]["price_percent_change"]
        from_volume_in_usd = getValue["data"]["attributes"]["from_volume_in_usd"]
        dekatrons = rs.json()
        pairs = dekatrons["pairs"][0]
        baseToken = pairs["baseToken"]
        priceNative = pairs["priceNative"]
        priceUsd = pairs["priceUsd"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        priceChange = pairs["priceChange"]
        liquidity = pairs["liquidity"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        fdv = pairs["fdv"]
        
        context = {"baseToken":baseToken,"priceNative":priceNative, "priceChange":priceChange, "volume":volume, "fdv":fdv, "volume":volume, "txns":txns, "priceUsd":priceUsd, "liquidity":liquidity, "txns":txns, "price_in_usd":price_in_usd, "fully_diluted_valuation":fully_diluted_valuation, "price_percent_change":price_percent_change, "from_volume_in_usd":from_volume_in_usd}
        return render(request, "main/shadow.html", context)
        

        
def CoreidView(request):
    if request.method == "POST":
        pass
    else:
        
        
        rs = requests.get("https://api.dexscreener.com/latest/dex/tokens/0x000000000e1d682cc39abe9b32285fdea1255374")
        resp = requests.get("https://app.geckoterminal.com/api/p1/core/pools/0xbb8502132c87ee31be0e2bc1cb8cc69374488261")
        getValue = resp.json()
        price_in_usd = getValue["data"]["attributes"]["price_in_usd"]
        fully_diluted_valuation = getValue["data"]["attributes"]["fully_diluted_valuation"]
        price_percent_change = getValue["data"]["attributes"]["price_percent_change"]
        from_volume_in_usd = getValue["data"]["attributes"]["from_volume_in_usd"]
        dekatrons = rs.json()
        pairs = dekatrons["pairs"][0]
        baseToken = pairs["baseToken"]
        priceNative = pairs["priceNative"]
        priceUsd = pairs["priceUsd"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        priceChange = pairs["priceChange"]
        liquidity = pairs["liquidity"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        fdv = pairs["fdv"]
        
        context = {"baseToken":baseToken,"priceNative":priceNative, "priceChange":priceChange, "volume":volume, "fdv":fdv, "volume":volume, "txns":txns, "priceUsd":priceUsd, "liquidity":liquidity, "txns":txns, "price_in_usd":price_in_usd, "fully_diluted_valuation":fully_diluted_valuation, "price_percent_change":price_percent_change, "from_volume_in_usd":from_volume_in_usd}
        return render(request, "main/coreid.html", context)
        
def CrestView(request):
    if request.method == "POST":
        pass
    else:
        
        
        rs = requests.get("https://api.dexscreener.com/latest/dex/tokens/0xcFE4C0783d103C44f403Bb287d29af0bAE5D4E84")
        resp = requests.get("https://app.geckoterminal.com/api/p1/core/pools/0xbb8502132c87ee31be0e2bc1cb8cc69374488261")
        getValue = resp.json()
        price_in_usd = getValue["data"]["attributes"]["price_in_usd"]
        fully_diluted_valuation = getValue["data"]["attributes"]["fully_diluted_valuation"]
        price_percent_change = getValue["data"]["attributes"]["price_percent_change"]
        from_volume_in_usd = getValue["data"]["attributes"]["from_volume_in_usd"]
        dekatrons = rs.json()
        pairs = dekatrons["pairs"][0]
        baseToken = pairs["baseToken"]
        priceNative = pairs["priceNative"]
        priceUsd = pairs["priceUsd"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        priceChange = pairs["priceChange"]
        liquidity = pairs["liquidity"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        fdv = pairs["fdv"]
        
        context = {"baseToken":baseToken,"priceNative":priceNative, "priceChange":priceChange, "volume":volume, "fdv":fdv, "volume":volume, "txns":txns, "priceUsd":priceUsd, "liquidity":liquidity, "txns":txns, "price_in_usd":price_in_usd, "fully_diluted_valuation":fully_diluted_valuation, "price_percent_change":price_percent_change, "from_volume_in_usd":from_volume_in_usd}
        return render(request, "main/crest.html", context)
        
def YieldsView(request):
    if request.method == "POST":
        pass
    else:
        
        
        rs = requests.get("https://api.dexscreener.com/latest/dex/tokens/0xe191a4d47A6be111C75139757CDDBb61BEEd88FB")
        resp = requests.get("https://app.geckoterminal.com/api/p1/core/pools/0xbb8502132c87ee31be0e2bc1cb8cc69374488261")
        getValue = resp.json()
        price_in_usd = getValue["data"]["attributes"]["price_in_usd"]
        fully_diluted_valuation = getValue["data"]["attributes"]["fully_diluted_valuation"]
        price_percent_change = getValue["data"]["attributes"]["price_percent_change"]
        from_volume_in_usd = getValue["data"]["attributes"]["from_volume_in_usd"]
        dekatrons = rs.json()
        pairs = dekatrons["pairs"][0]
        baseToken = pairs["baseToken"]
        priceNative = pairs["priceNative"]
        priceUsd = pairs["priceUsd"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        priceChange = pairs["priceChange"]
        liquidity = pairs["liquidity"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        fdv = pairs["fdv"]
        
        context = {"baseToken":baseToken,"priceNative":priceNative, "priceChange":priceChange, "volume":volume, "fdv":fdv, "volume":volume, "txns":txns, "priceUsd":priceUsd, "liquidity":liquidity, "txns":txns, "price_in_usd":price_in_usd, "fully_diluted_valuation":fully_diluted_valuation, "price_percent_change":price_percent_change, "from_volume_in_usd":from_volume_in_usd}
        return render(request, "main/yieldz.html", context)
        
def HappyView(request):
    if request.method == "POST":
        pass
    else:
        
        
        rs = requests.get("https://api.dexscreener.com/latest/dex/tokens/0xAc9B3614Dd28c4ca72853CA996Ab76F03Db73Fb4")
        resp = requests.get("https://app.geckoterminal.com/api/p1/core/pools/0xbb8502132c87ee31be0e2bc1cb8cc69374488261")
        getValue = resp.json()
        price_in_usd = getValue["data"]["attributes"]["price_in_usd"]
        fully_diluted_valuation = getValue["data"]["attributes"]["fully_diluted_valuation"]
        price_percent_change = getValue["data"]["attributes"]["price_percent_change"]
        from_volume_in_usd = getValue["data"]["attributes"]["from_volume_in_usd"]
        dekatrons = rs.json()
        pairs = dekatrons["pairs"][0]
        baseToken = pairs["baseToken"]
        priceNative = pairs["priceNative"]
        priceUsd = pairs["priceUsd"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        priceChange = pairs["priceChange"]
        liquidity = pairs["liquidity"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        fdv = pairs["fdv"]
        
        context = {"baseToken":baseToken,"priceNative":priceNative, "priceChange":priceChange, "volume":volume, "fdv":fdv, "volume":volume, "txns":txns, "priceUsd":priceUsd, "liquidity":liquidity, "txns":txns, "price_in_usd":price_in_usd, "fully_diluted_valuation":fully_diluted_valuation, "price_percent_change":price_percent_change, "from_volume_in_usd":from_volume_in_usd}
        return render(request, "main/happy.html", context)
        
def IgnoreFudView(request):
    if request.method == "POST":
        pass
    else:
        
        
        rs = requests.get("https://api.dexscreener.com/latest/dex/tokens/0x98564E70c7fCC6d947fFE6d9EfeD5ba68b306F2E")
        resp = requests.get("https://app.geckoterminal.com/api/p1/core/pools/0xbb8502132c87ee31be0e2bc1cb8cc69374488261")
        getValue = resp.json()
        price_in_usd = getValue["data"]["attributes"]["price_in_usd"]
        fully_diluted_valuation = getValue["data"]["attributes"]["fully_diluted_valuation"]
        price_percent_change = getValue["data"]["attributes"]["price_percent_change"]
        from_volume_in_usd = getValue["data"]["attributes"]["from_volume_in_usd"]
        dekatrons = rs.json()
        pairs = dekatrons["pairs"][0]
        baseToken = pairs["baseToken"]
        priceNative = pairs["priceNative"]
        priceUsd = pairs["priceUsd"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        priceChange = pairs["priceChange"]
        liquidity = pairs["liquidity"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        fdv = pairs["fdv"]
        
        context = {"baseToken":baseToken,"priceNative":priceNative, "priceChange":priceChange, "volume":volume, "fdv":fdv, "volume":volume, "txns":txns, "priceUsd":priceUsd, "liquidity":liquidity, "txns":txns, "price_in_usd":price_in_usd, "fully_diluted_valuation":fully_diluted_valuation, "price_percent_change":price_percent_change, "from_volume_in_usd":from_volume_in_usd}
        return render(request, "main/4token.html", context)
        
def YpcView(request):
    if request.method == "POST":
        pass
    else:
        
        
        rs = requests.get("https://api.dexscreener.com/latest/dex/tokens/0xDC2393dc10734BF153153038943a5deB42b209cd")
        resp = requests.get("https://app.geckoterminal.com/api/p1/core/pools/0xbb8502132c87ee31be0e2bc1cb8cc69374488261")
        getValue = resp.json()
        price_in_usd = getValue["data"]["attributes"]["price_in_usd"]
        fully_diluted_valuation = getValue["data"]["attributes"]["fully_diluted_valuation"]
        price_percent_change = getValue["data"]["attributes"]["price_percent_change"]
        from_volume_in_usd = getValue["data"]["attributes"]["from_volume_in_usd"]
        dekatrons = rs.json()
        pairs = dekatrons["pairs"][0]
        baseToken = pairs["baseToken"]
        priceNative = pairs["priceNative"]
        priceUsd = pairs["priceUsd"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        priceChange = pairs["priceChange"]
        liquidity = pairs["liquidity"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        fdv = pairs["fdv"]
        
        context = {"baseToken":baseToken,"priceNative":priceNative, "priceChange":priceChange, "volume":volume, "fdv":fdv, "volume":volume, "txns":txns, "priceUsd":priceUsd, "liquidity":liquidity, "txns":txns, "price_in_usd":price_in_usd, "fully_diluted_valuation":fully_diluted_valuation, "price_percent_change":price_percent_change, "from_volume_in_usd":from_volume_in_usd}
        return render(request, "main/ypc.html", context)
        
def DcView(request):
    if request.method == "POST":
        pass
    else:
        
        
        rs = requests.get("https://api.dexscreener.com/latest/dex/tokens/0x979A34f98b9a1bF2B38fD18f5c038423e4902db9")
        resp = requests.get("https://app.geckoterminal.com/api/p1/core/pools/0xbb8502132c87ee31be0e2bc1cb8cc69374488261")
        getValue = resp.json()
        price_in_usd = getValue["data"]["attributes"]["price_in_usd"]
        fully_diluted_valuation = getValue["data"]["attributes"]["fully_diluted_valuation"]
        price_percent_change = getValue["data"]["attributes"]["price_percent_change"]
        from_volume_in_usd = getValue["data"]["attributes"]["from_volume_in_usd"]
        dekatrons = rs.json()
        pairs = dekatrons["pairs"][0]
        baseToken = pairs["baseToken"]
        priceNative = pairs["priceNative"]
        priceUsd = pairs["priceUsd"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        priceChange = pairs["priceChange"]
        liquidity = pairs["liquidity"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        fdv = pairs["fdv"]
        
        context = {"baseToken":baseToken,"priceNative":priceNative, "priceChange":priceChange, "volume":volume, "fdv":fdv, "volume":volume, "txns":txns, "priceUsd":priceUsd, "liquidity":liquidity, "txns":txns, "price_in_usd":price_in_usd, "fully_diluted_valuation":fully_diluted_valuation, "price_percent_change":price_percent_change, "from_volume_in_usd":from_volume_in_usd}
        return render(request, "main/3dc.html", context)
        
def AicoreView(request):
    if request.method == "POST":
        pass
    else:
        
        
        rs = requests.get("https://api.dexscreener.com/latest/dex/tokens/0x7621c97683a3b0499ec156bd257e44175e793bb1")
        resp = requests.get("https://app.geckoterminal.com/api/p1/core/pools/0xbb8502132c87ee31be0e2bc1cb8cc69374488261")
        getValue = resp.json()
        price_in_usd = getValue["data"]["attributes"]["price_in_usd"]
        fully_diluted_valuation = getValue["data"]["attributes"]["fully_diluted_valuation"]
        price_percent_change = getValue["data"]["attributes"]["price_percent_change"]
        from_volume_in_usd = getValue["data"]["attributes"]["from_volume_in_usd"]
        dekatrons = rs.json()
        pairs = dekatrons["pairs"][0]
        baseToken = pairs["baseToken"]
        priceNative = pairs["priceNative"]
        priceUsd = pairs["priceUsd"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        priceChange = pairs["priceChange"]
        liquidity = pairs["liquidity"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        fdv = pairs["fdv"]
        
        context = {"baseToken":baseToken,"priceNative":priceNative, "priceChange":priceChange, "volume":volume, "fdv":fdv, "volume":volume, "txns":txns, "priceUsd":priceUsd, "liquidity":liquidity, "txns":txns, "price_in_usd":price_in_usd, "fully_diluted_valuation":fully_diluted_valuation, "price_percent_change":price_percent_change, "from_volume_in_usd":from_volume_in_usd}
        return render(request, "main/aicore.html", context)
        
def AinuView(request):
    if request.method == "POST":
        pass
    else:
        
        
        rs = requests.get("https://api.dexscreener.com/latest/dex/tokens/0x7469bae0b0bc80a208eb0946121b5aff686a6ac2")
        resp = requests.get("https://app.geckoterminal.com/api/p1/core/pools/0xbb8502132c87ee31be0e2bc1cb8cc69374488261")
        getValue = resp.json()
        price_in_usd = getValue["data"]["attributes"]["price_in_usd"]
        fully_diluted_valuation = getValue["data"]["attributes"]["fully_diluted_valuation"]
        price_percent_change = getValue["data"]["attributes"]["price_percent_change"]
        from_volume_in_usd = getValue["data"]["attributes"]["from_volume_in_usd"]
        dekatrons = rs.json()
        pairs = dekatrons["pairs"][0]
        baseToken = pairs["baseToken"]
        priceNative = pairs["priceNative"]
        priceUsd = pairs["priceUsd"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        priceChange = pairs["priceChange"]
        liquidity = pairs["liquidity"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        fdv = pairs["fdv"]
        
        context = {"baseToken":baseToken,"priceNative":priceNative, "priceChange":priceChange, "volume":volume, "fdv":fdv, "volume":volume, "txns":txns, "priceUsd":priceUsd, "liquidity":liquidity, "txns":txns, "price_in_usd":price_in_usd, "fully_diluted_valuation":fully_diluted_valuation, "price_percent_change":price_percent_change, "from_volume_in_usd":from_volume_in_usd}
        return render(request, "main/ainu.html", context)
        
def AkioView(request):
    if request.method == "POST":
        pass
    else:
        
        
        rs = requests.get("https://api.dexscreener.com/latest/dex/tokens/0xBb790D1e8A2d34e9d846bb00EA0b0380813375EE")
        resp = requests.get("https://app.geckoterminal.com/api/p1/core/pools/0xbb8502132c87ee31be0e2bc1cb8cc69374488261")
        getValue = resp.json()
        price_in_usd = getValue["data"]["attributes"]["price_in_usd"]
        fully_diluted_valuation = getValue["data"]["attributes"]["fully_diluted_valuation"]
        price_percent_change = getValue["data"]["attributes"]["price_percent_change"]
        from_volume_in_usd = getValue["data"]["attributes"]["from_volume_in_usd"]
        dekatrons = rs.json()
        pairs = dekatrons["pairs"][0]
        baseToken = pairs["baseToken"]
        priceNative = pairs["priceNative"]
        priceUsd = pairs["priceUsd"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        priceChange = pairs["priceChange"]
        liquidity = pairs["liquidity"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        fdv = pairs["fdv"]
        
        context = {"baseToken":baseToken,"priceNative":priceNative, "priceChange":priceChange, "volume":volume, "fdv":fdv, "volume":volume, "txns":txns, "priceUsd":priceUsd, "liquidity":liquidity, "txns":txns, "price_in_usd":price_in_usd, "fully_diluted_valuation":fully_diluted_valuation, "price_percent_change":price_percent_change, "from_volume_in_usd":from_volume_in_usd}
        return render(request, "main/akio.html", context)
        
def BcoreView(request):
    if request.method == "POST":
        pass
    else:
        
        
        rs = requests.get("https://api.dexscreener.com/latest/dex/tokens/0xBFa14641bf0fE84dE3fcf3Bf227900af445f09C3")
        resp = requests.get("https://app.geckoterminal.com/api/p1/core/pools/0xbb8502132c87ee31be0e2bc1cb8cc69374488261")
        getValue = resp.json()
        price_in_usd = getValue["data"]["attributes"]["price_in_usd"]
        fully_diluted_valuation = getValue["data"]["attributes"]["fully_diluted_valuation"]
        price_percent_change = getValue["data"]["attributes"]["price_percent_change"]
        from_volume_in_usd = getValue["data"]["attributes"]["from_volume_in_usd"]
        dekatrons = rs.json()
        pairs = dekatrons["pairs"][0]
        baseToken = pairs["baseToken"]
        priceNative = pairs["priceNative"]
        priceUsd = pairs["priceUsd"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        priceChange = pairs["priceChange"]
        liquidity = pairs["liquidity"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        fdv = pairs["fdv"]
        
        context = {"baseToken":baseToken,"priceNative":priceNative, "priceChange":priceChange, "volume":volume, "fdv":fdv, "volume":volume, "txns":txns, "priceUsd":priceUsd, "liquidity":liquidity, "txns":txns, "price_in_usd":price_in_usd, "fully_diluted_valuation":fully_diluted_valuation, "price_percent_change":price_percent_change, "from_volume_in_usd":from_volume_in_usd}
        return render(request, "main/bcore.html", context)
        
def BlockView(request):
    if request.method == "POST":
        pass
    else:
        
        
        rs = requests.get("https://api.dexscreener.com/latest/dex/tokens/0xbFf24592345094DFA4d6f75aFF5BE79AbCbC9bD9")
        resp = requests.get("https://app.geckoterminal.com/api/p1/core/pools/0xbb8502132c87ee31be0e2bc1cb8cc69374488261")
        getValue = resp.json()
        price_in_usd = getValue["data"]["attributes"]["price_in_usd"]
        fully_diluted_valuation = getValue["data"]["attributes"]["fully_diluted_valuation"]
        price_percent_change = getValue["data"]["attributes"]["price_percent_change"]
        from_volume_in_usd = getValue["data"]["attributes"]["from_volume_in_usd"]
        dekatrons = rs.json()
        pairs = dekatrons["pairs"][0]
        baseToken = pairs["baseToken"]
        priceNative = pairs["priceNative"]
        priceUsd = pairs["priceUsd"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        priceChange = pairs["priceChange"]
        liquidity = pairs["liquidity"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        fdv = pairs["fdv"]
        
        context = {"baseToken":baseToken,"priceNative":priceNative, "priceChange":priceChange, "volume":volume, "fdv":fdv, "volume":volume, "txns":txns, "priceUsd":priceUsd, "liquidity":liquidity, "txns":txns, "price_in_usd":price_in_usd, "fully_diluted_valuation":fully_diluted_valuation, "price_percent_change":price_percent_change, "from_volume_in_usd":from_volume_in_usd}
        return render(request, "main/block.html", context)
        
def MapView(request):
    if request.method == "POST":
        pass
    else:
        
        
        rs = requests.get("https://api.dexscreener.com/latest/dex/tokens/0xAB82f8b18ea7929815076F152b8Fd24F8b267274")
        resp = requests.get("https://app.geckoterminal.com/api/p1/core/pools/0xbb8502132c87ee31be0e2bc1cb8cc69374488261")
        getValue = resp.json()
        price_in_usd = getValue["data"]["attributes"]["price_in_usd"]
        fully_diluted_valuation = getValue["data"]["attributes"]["fully_diluted_valuation"]
        price_percent_change = getValue["data"]["attributes"]["price_percent_change"]
        from_volume_in_usd = getValue["data"]["attributes"]["from_volume_in_usd"]
        dekatrons = rs.json()
        pairs = dekatrons["pairs"][0]
        baseToken = pairs["baseToken"]
        priceNative = pairs["priceNative"]
        priceUsd = pairs["priceUsd"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        priceChange = pairs["priceChange"]
        liquidity = pairs["liquidity"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        fdv = pairs["fdv"]
        
        context = {"baseToken":baseToken,"priceNative":priceNative, "priceChange":priceChange, "volume":volume, "fdv":fdv, "volume":volume, "txns":txns, "priceUsd":priceUsd, "liquidity":liquidity, "txns":txns, "price_in_usd":price_in_usd, "fully_diluted_valuation":fully_diluted_valuation, "price_percent_change":price_percent_change, "from_volume_in_usd":from_volume_in_usd}
        return render(request, "main/map.html", context)
        
def BitvexaView(request):
    if request.method == "POST":
        pass
    else:
        
        
        rs = requests.get("https://api.dexscreener.com/latest/dex/tokens/0xE8dEC1bFC7BF572D60403c609d6589715d2a23fC")
        resp = requests.get("https://app.geckoterminal.com/api/p1/core/pools/0xbb8502132c87ee31be0e2bc1cb8cc69374488261")
        getValue = resp.json()
        price_in_usd = getValue["data"]["attributes"]["price_in_usd"]
        fully_diluted_valuation = getValue["data"]["attributes"]["fully_diluted_valuation"]
        price_percent_change = getValue["data"]["attributes"]["price_percent_change"]
        from_volume_in_usd = getValue["data"]["attributes"]["from_volume_in_usd"]
        dekatrons = rs.json()
        pairs = dekatrons["pairs"][0]
        baseToken = pairs["baseToken"]
        priceNative = pairs["priceNative"]
        priceUsd = pairs["priceUsd"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        priceChange = pairs["priceChange"]
        liquidity = pairs["liquidity"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        fdv = pairs["fdv"]
        
        context = {"baseToken":baseToken,"priceNative":priceNative, "priceChange":priceChange, "volume":volume, "fdv":fdv, "volume":volume, "txns":txns, "priceUsd":priceUsd, "liquidity":liquidity, "txns":txns, "price_in_usd":price_in_usd, "fully_diluted_valuation":fully_diluted_valuation, "price_percent_change":price_percent_change, "from_volume_in_usd":from_volume_in_usd}
        return render(request, "main/bitvexa.html", context)

def HoboView(request):
    if request.method == "POST":
        pass
    else:
        
        
        rs = requests.get("https://api.dexscreener.com/latest/dex/tokens/0x25100C0083e8E53b1cb264E978522bd477011A0d")
        resp = requests.get("https://app.geckoterminal.com/api/p1/core/pools/0xbb8502132c87ee31be0e2bc1cb8cc69374488261")
        getValue = resp.json()
        price_in_usd = getValue["data"]["attributes"]["price_in_usd"]
        fully_diluted_valuation = getValue["data"]["attributes"]["fully_diluted_valuation"]
        price_percent_change = getValue["data"]["attributes"]["price_percent_change"]
        from_volume_in_usd = getValue["data"]["attributes"]["from_volume_in_usd"]
        dekatrons = rs.json()
        pairs = dekatrons["pairs"][0]
        baseToken = pairs["baseToken"]
        priceNative = pairs["priceNative"]
        priceUsd = pairs["priceUsd"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        priceChange = pairs["priceChange"]
        liquidity = pairs["liquidity"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        fdv = pairs["fdv"]
        
        context = {"baseToken":baseToken,"priceNative":priceNative, "priceChange":priceChange, "volume":volume, "fdv":fdv, "volume":volume, "txns":txns, "priceUsd":priceUsd, "liquidity":liquidity, "txns":txns, "price_in_usd":price_in_usd, "fully_diluted_valuation":fully_diluted_valuation, "price_percent_change":price_percent_change, "from_volume_in_usd":from_volume_in_usd}
        return render(request, "main/hobo.html", context)
        
def WoofView(request):
    if request.method == "POST":
        pass
    else:
        
        
        rs = requests.get("https://api.dexscreener.com/latest/dex/tokens/0x5C44d3D2312AbA4d5F2406A98Bf374Bc76455092")
        resp = requests.get("https://app.geckoterminal.com/api/p1/core/pools/0xbb8502132c87ee31be0e2bc1cb8cc69374488261")
        getValue = resp.json()
        price_in_usd = getValue["data"]["attributes"]["price_in_usd"]
        fully_diluted_valuation = getValue["data"]["attributes"]["fully_diluted_valuation"]
        price_percent_change = getValue["data"]["attributes"]["price_percent_change"]
        from_volume_in_usd = getValue["data"]["attributes"]["from_volume_in_usd"]
        dekatrons = rs.json()
        pairs = dekatrons["pairs"][0]
        baseToken = pairs["baseToken"]
        priceNative = pairs["priceNative"]
        priceUsd = pairs["priceUsd"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        priceChange = pairs["priceChange"]
        liquidity = pairs["liquidity"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        fdv = pairs["fdv"]
        
        context = {"baseToken":baseToken,"priceNative":priceNative, "priceChange":priceChange, "volume":volume, "fdv":fdv, "volume":volume, "txns":txns, "priceUsd":priceUsd, "liquidity":liquidity, "txns":txns, "price_in_usd":price_in_usd, "fully_diluted_valuation":fully_diluted_valuation, "price_percent_change":price_percent_change, "from_volume_in_usd":from_volume_in_usd}
        return render(request, "main/woof.html", context)
        

        
def WordView(request):
    if request.method == "POST":
        pass
    else:
        
        
        rs = requests.get("https://api.dexscreener.com/latest/dex/tokens/0xAA7912C028E058e4bD90Bcbb9fB41C27DbcC3245")
        resp = requests.get("https://app.geckoterminal.com/api/p1/core/pools/0xbb8502132c87ee31be0e2bc1cb8cc69374488261")
        getValue = resp.json()
        price_in_usd = getValue["data"]["attributes"]["price_in_usd"]
        fully_diluted_valuation = getValue["data"]["attributes"]["fully_diluted_valuation"]
        price_percent_change = getValue["data"]["attributes"]["price_percent_change"]
        from_volume_in_usd = getValue["data"]["attributes"]["from_volume_in_usd"]
        dekatrons = rs.json()
        pairs = dekatrons["pairs"][0]
        baseToken = pairs["baseToken"]
        priceNative = pairs["priceNative"]
        priceUsd = pairs["priceUsd"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        priceChange = pairs["priceChange"]
        liquidity = pairs["liquidity"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        fdv = pairs["fdv"]
        
        context = {"baseToken":baseToken,"priceNative":priceNative, "priceChange":priceChange, "volume":volume, "fdv":fdv, "volume":volume, "txns":txns, "priceUsd":priceUsd, "liquidity":liquidity, "txns":txns, "price_in_usd":price_in_usd, "fully_diluted_valuation":fully_diluted_valuation, "price_percent_change":price_percent_change, "from_volume_in_usd":from_volume_in_usd}
        return render(request, "main/word.html", context)

def ScoreView(request):
    if request.method == "POST":
        pass
    else:
        
        
        rs = requests.get("https://api.dexscreener.com/latest/dex/tokens/0xA20b3B97df3a02f9185175760300a06B4e0A2C05")
        resp = requests.get("https://app.geckoterminal.com/api/p1/core/pools/0xbb8502132c87ee31be0e2bc1cb8cc69374488261")
        getValue = resp.json()
        price_in_usd = getValue["data"]["attributes"]["price_in_usd"]
        fully_diluted_valuation = getValue["data"]["attributes"]["fully_diluted_valuation"]
        price_percent_change = getValue["data"]["attributes"]["price_percent_change"]
        from_volume_in_usd = getValue["data"]["attributes"]["from_volume_in_usd"]
        dekatrons = rs.json()
        pairs = dekatrons["pairs"][0]
        baseToken = pairs["baseToken"]
        priceNative = pairs["priceNative"]
        priceUsd = pairs["priceUsd"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        priceChange = pairs["priceChange"]
        liquidity = pairs["liquidity"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        fdv = pairs["fdv"]
        
        context = {"baseToken":baseToken,"priceNative":priceNative, "priceChange":priceChange, "volume":volume, "fdv":fdv, "volume":volume, "txns":txns, "priceUsd":priceUsd, "liquidity":liquidity, "txns":txns, "price_in_usd":price_in_usd, "fully_diluted_valuation":fully_diluted_valuation, "price_percent_change":price_percent_change, "from_volume_in_usd":from_volume_in_usd}
        return render(request, "main/score.html", context)
        
def CbunnyView(request):
    if request.method == "POST":
        pass
    else:
        
        
        rs = requests.get("https://api.dexscreener.com/latest/dex/tokens/0x6F8BF0Ca89b8936AA498c7A2C75815Eecca328F3 ")
        resp = requests.get("https://app.geckoterminal.com/api/p1/core/pools/0xbb8502132c87ee31be0e2bc1cb8cc69374488261")
        getValue = resp.json()
        price_in_usd = getValue["data"]["attributes"]["price_in_usd"]
        fully_diluted_valuation = getValue["data"]["attributes"]["fully_diluted_valuation"]
        price_percent_change = getValue["data"]["attributes"]["price_percent_change"]
        from_volume_in_usd = getValue["data"]["attributes"]["from_volume_in_usd"]
        dekatrons = rs.json()
        pairs = dekatrons["pairs"][0]
        baseToken = pairs["baseToken"]
        priceNative = pairs["priceNative"]
        priceUsd = pairs["priceUsd"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        priceChange = pairs["priceChange"]
        liquidity = pairs["liquidity"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        fdv = pairs["fdv"]
        
        context = {"baseToken":baseToken,"priceNative":priceNative, "priceChange":priceChange, "volume":volume, "fdv":fdv, "volume":volume, "txns":txns, "priceUsd":priceUsd, "liquidity":liquidity, "txns":txns, "price_in_usd":price_in_usd, "fully_diluted_valuation":fully_diluted_valuation, "price_percent_change":price_percent_change, "from_volume_in_usd":from_volume_in_usd}
        return render(request, "main/cbunny.html", context)
        
def CshareView(request):
    if request.method == "POST":
        pass
    else:
        
        
        rs = requests.get("https://api.dexscreener.com/latest/dex/tokens/0x6501cCA79ca8D6F68784f2345c9a379951e30A05 ")
        resp = requests.get("https://app.geckoterminal.com/api/p1/core/pools/0xbb8502132c87ee31be0e2bc1cb8cc69374488261")
        getValue = resp.json()
        price_in_usd = getValue["data"]["attributes"]["price_in_usd"]
        fully_diluted_valuation = getValue["data"]["attributes"]["fully_diluted_valuation"]
        price_percent_change = getValue["data"]["attributes"]["price_percent_change"]
        from_volume_in_usd = getValue["data"]["attributes"]["from_volume_in_usd"]
        dekatrons = rs.json()
        pairs = dekatrons["pairs"][0]
        baseToken = pairs["baseToken"]
        priceNative = pairs["priceNative"]
        priceUsd = pairs["priceUsd"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        priceChange = pairs["priceChange"]
        liquidity = pairs["liquidity"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        fdv = pairs["fdv"]
        
        context = {"baseToken":baseToken,"priceNative":priceNative, "priceChange":priceChange, "volume":volume, "fdv":fdv, "volume":volume, "txns":txns, "priceUsd":priceUsd, "liquidity":liquidity, "txns":txns, "price_in_usd":price_in_usd, "fully_diluted_valuation":fully_diluted_valuation, "price_percent_change":price_percent_change, "from_volume_in_usd":from_volume_in_usd}
        return render(request, "main/cshare.html", context)
        
def CtombView(request):
    if request.method == "POST":
        pass
    else:
        
        
        rs = requests.get("https://api.dexscreener.com/latest/dex/tokens/0xC830a752eef79F2D66a36645A70fB0bA176b4Cea ")
        resp = requests.get("https://app.geckoterminal.com/api/p1/core/pools/0xbb8502132c87ee31be0e2bc1cb8cc69374488261")
        getValue = resp.json()
        price_in_usd = getValue["data"]["attributes"]["price_in_usd"]
        fully_diluted_valuation = getValue["data"]["attributes"]["fully_diluted_valuation"]
        price_percent_change = getValue["data"]["attributes"]["price_percent_change"]
        from_volume_in_usd = getValue["data"]["attributes"]["from_volume_in_usd"]
        dekatrons = rs.json()
        pairs = dekatrons["pairs"][0]
        baseToken = pairs["baseToken"]
        priceNative = pairs["priceNative"]
        priceUsd = pairs["priceUsd"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        priceChange = pairs["priceChange"]
        liquidity = pairs["liquidity"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        fdv = pairs["fdv"]
        
        context = {"baseToken":baseToken,"priceNative":priceNative, "priceChange":priceChange, "volume":volume, "fdv":fdv, "volume":volume, "txns":txns, "priceUsd":priceUsd, "liquidity":liquidity, "txns":txns, "price_in_usd":price_in_usd, "fully_diluted_valuation":fully_diluted_valuation, "price_percent_change":price_percent_change, "from_volume_in_usd":from_volume_in_usd}
        return render(request, "main/ctomb.html", context)

def FlashView(request):
    if request.method == "POST":
        pass
    else:
        
        
        rs = requests.get("https://api.dexscreener.com/latest/dex/tokens/0x5aE225fa6573903CA58E26Cd4171B87060CeEAA2 ")
        resp = requests.get("https://app.geckoterminal.com/api/p1/core/pools/0xbb8502132c87ee31be0e2bc1cb8cc69374488261")
        getValue = resp.json()
        price_in_usd = getValue["data"]["attributes"]["price_in_usd"]
        fully_diluted_valuation = getValue["data"]["attributes"]["fully_diluted_valuation"]
        price_percent_change = getValue["data"]["attributes"]["price_percent_change"]
        from_volume_in_usd = getValue["data"]["attributes"]["from_volume_in_usd"]
        dekatrons = rs.json()
        pairs = dekatrons["pairs"][0]
        baseToken = pairs["baseToken"]
        priceNative = pairs["priceNative"]
        priceUsd = pairs["priceUsd"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        priceChange = pairs["priceChange"]
        liquidity = pairs["liquidity"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        fdv = pairs["fdv"]
        
        context = {"baseToken":baseToken,"priceNative":priceNative, "priceChange":priceChange, "volume":volume, "fdv":fdv, "volume":volume, "txns":txns, "priceUsd":priceUsd, "liquidity":liquidity, "txns":txns, "price_in_usd":price_in_usd, "fully_diluted_valuation":fully_diluted_valuation, "price_percent_change":price_percent_change, "from_volume_in_usd":from_volume_in_usd}
        return render(request, "main/flash.html", context)
        


def GreenView(request):
    if request.method == "POST":
        pass
    else:
        
        
        rs = requests.get("https://api.dexscreener.com/latest/dex/tokens/0xDBa57074B81CD0630D7960dFAA370972C5E1A6D9 ")
        resp = requests.get("https://app.geckoterminal.com/api/p1/core/pools/0xbb8502132c87ee31be0e2bc1cb8cc69374488261")
        getValue = resp.json()
        price_in_usd = getValue["data"]["attributes"]["price_in_usd"]
        fully_diluted_valuation = getValue["data"]["attributes"]["fully_diluted_valuation"]
        price_percent_change = getValue["data"]["attributes"]["price_percent_change"]
        from_volume_in_usd = getValue["data"]["attributes"]["from_volume_in_usd"]
        dekatrons = rs.json()
        pairs = dekatrons["pairs"][0]
        baseToken = pairs["baseToken"]
        priceNative = pairs["priceNative"]
        priceUsd = pairs["priceUsd"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        priceChange = pairs["priceChange"]
        liquidity = pairs["liquidity"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        fdv = pairs["fdv"]
        
        context = {"baseToken":baseToken,"priceNative":priceNative, "priceChange":priceChange, "volume":volume, "fdv":fdv, "volume":volume, "txns":txns, "priceUsd":priceUsd, "liquidity":liquidity, "txns":txns, "price_in_usd":price_in_usd, "fully_diluted_valuation":fully_diluted_valuation, "price_percent_change":price_percent_change, "from_volume_in_usd":from_volume_in_usd}
        return render(request, "main/green.html", context)
        
def EmperorView(request):
    if request.method == "POST":
        pass
    else:
        
        
        rs = requests.get("https://api.dexscreener.com/latest/dex/tokens/0x8afb52de791a19873c3097195ef04d48ed93fe14 ")
        resp = requests.get("https://app.geckoterminal.com/api/p1/core/pools/0xbb8502132c87ee31be0e2bc1cb8cc69374488261")
        getValue = resp.json()
        price_in_usd = getValue["data"]["attributes"]["price_in_usd"]
        fully_diluted_valuation = getValue["data"]["attributes"]["fully_diluted_valuation"]
        price_percent_change = getValue["data"]["attributes"]["price_percent_change"]
        from_volume_in_usd = getValue["data"]["attributes"]["from_volume_in_usd"]
        dekatrons = rs.json()
        pairs = dekatrons["pairs"][0]
        baseToken = pairs["baseToken"]
        priceNative = pairs["priceNative"]
        priceUsd = pairs["priceUsd"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        priceChange = pairs["priceChange"]
        liquidity = pairs["liquidity"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        fdv = pairs["fdv"]
        
        context = {"baseToken":baseToken,"priceNative":priceNative, "priceChange":priceChange, "volume":volume, "fdv":fdv, "volume":volume, "txns":txns, "priceUsd":priceUsd, "liquidity":liquidity, "txns":txns, "price_in_usd":price_in_usd, "fully_diluted_valuation":fully_diluted_valuation, "price_percent_change":price_percent_change, "from_volume_in_usd":from_volume_in_usd}
        return render(request, "main/emperor.html", context)

def RoyaleView(request):
    if request.method == "POST":
        pass
    else:
        
        
        rs = requests.get("https://api.dexscreener.com/latest/dex/tokens/0xA7c0B19645B653B4373E3592C84fce8C64D89E8F")
        resp = requests.get("https://app.geckoterminal.com/api/p1/core/pools/0xbb8502132c87ee31be0e2bc1cb8cc69374488261")
        getValue = resp.json()
        price_in_usd = getValue["data"]["attributes"]["price_in_usd"]
        fully_diluted_valuation = getValue["data"]["attributes"]["fully_diluted_valuation"]
        price_percent_change = getValue["data"]["attributes"]["price_percent_change"]
        from_volume_in_usd = getValue["data"]["attributes"]["from_volume_in_usd"]
        dekatrons = rs.json()
        pairs = dekatrons["pairs"][0]
        baseToken = pairs["baseToken"]
        priceNative = pairs["priceNative"]
        priceUsd = pairs["priceUsd"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        priceChange = pairs["priceChange"]
        liquidity = pairs["liquidity"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        fdv = pairs["fdv"]
        
        context = {"baseToken":baseToken,"priceNative":priceNative, "priceChange":priceChange, "volume":volume, "fdv":fdv, "volume":volume, "txns":txns, "priceUsd":priceUsd, "liquidity":liquidity, "txns":txns, "price_in_usd":price_in_usd, "fully_diluted_valuation":fully_diluted_valuation, "price_percent_change":price_percent_change, "from_volume_in_usd":from_volume_in_usd}
        return render(request, "main/royale.html", context)
        
def MiidasView(request):
    if request.method == "POST":
        pass
    else:
        
        
        rs = requests.get("https://api.dexscreener.com/latest/dex/tokens/0xcfd38184c30832917A2871695F91e5e61bBD41fF")
        resp = requests.get("https://app.geckoterminal.com/api/p1/core/pools/0xbb8502132c87ee31be0e2bc1cb8cc69374488261")
        getValue = resp.json()
        price_in_usd = getValue["data"]["attributes"]["price_in_usd"]
        fully_diluted_valuation = getValue["data"]["attributes"]["fully_diluted_valuation"]
        price_percent_change = getValue["data"]["attributes"]["price_percent_change"]
        from_volume_in_usd = getValue["data"]["attributes"]["from_volume_in_usd"]
        dekatrons = rs.json()
        pairs = dekatrons["pairs"][0]
        baseToken = pairs["baseToken"]
        priceNative = pairs["priceNative"]
        priceUsd = pairs["priceUsd"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        priceChange = pairs["priceChange"]
        liquidity = pairs["liquidity"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        fdv = pairs["fdv"]
        
        context = {"baseToken":baseToken,"priceNative":priceNative, "priceChange":priceChange, "volume":volume, "fdv":fdv, "volume":volume, "txns":txns, "priceUsd":priceUsd, "liquidity":liquidity, "txns":txns, "price_in_usd":price_in_usd, "fully_diluted_valuation":fully_diluted_valuation, "price_percent_change":price_percent_change, "from_volume_in_usd":from_volume_in_usd}
        return render(request, "main/miidas.html", context)
        
def UnityView(request):
    if request.method == "POST":
        pass
    else:
        
        
        rs = requests.get("https://api.dexscreener.com/latest/dex/tokens/0x496Bb259D0117E89B2e73433524e9838c3073e60")
        resp = requests.get("https://app.geckoterminal.com/api/p1/core/pools/0xbb8502132c87ee31be0e2bc1cb8cc69374488261")
        getValue = resp.json()
        price_in_usd = getValue["data"]["attributes"]["price_in_usd"]
        fully_diluted_valuation = getValue["data"]["attributes"]["fully_diluted_valuation"]
        price_percent_change = getValue["data"]["attributes"]["price_percent_change"]
        from_volume_in_usd = getValue["data"]["attributes"]["from_volume_in_usd"]
        dekatrons = rs.json()
        pairs = dekatrons["pairs"][0]
        baseToken = pairs["baseToken"]
        priceNative = pairs["priceNative"]
        priceUsd = pairs["priceUsd"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        priceChange = pairs["priceChange"]
        liquidity = pairs["liquidity"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        fdv = pairs["fdv"]
        
        context = {"baseToken":baseToken,"priceNative":priceNative, "priceChange":priceChange, "volume":volume, "fdv":fdv, "volume":volume, "txns":txns, "priceUsd":priceUsd, "liquidity":liquidity, "txns":txns, "price_in_usd":price_in_usd, "fully_diluted_valuation":fully_diluted_valuation, "price_percent_change":price_percent_change, "from_volume_in_usd":from_volume_in_usd}
        return render(request, "main/unity.html", context)
        
def YfiView(request):
    if request.method == "POST":
        pass
    else:
        
        
        rs = requests.get("https://api.dexscreener.com/latest/dex/tokens/0x9c765C62ad538011c2aAd815CaAeEc94551fbE9D")
        resp = requests.get("https://app.geckoterminal.com/api/p1/core/pools/0xbb8502132c87ee31be0e2bc1cb8cc69374488261")
        getValue = resp.json()
        price_in_usd = getValue["data"]["attributes"]["price_in_usd"]
        fully_diluted_valuation = getValue["data"]["attributes"]["fully_diluted_valuation"]
        price_percent_change = getValue["data"]["attributes"]["price_percent_change"]
        from_volume_in_usd = getValue["data"]["attributes"]["from_volume_in_usd"]
        dekatrons = rs.json()
        pairs = dekatrons["pairs"][0]
        baseToken = pairs["baseToken"]
        priceNative = pairs["priceNative"]
        priceUsd = pairs["priceUsd"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        priceChange = pairs["priceChange"]
        liquidity = pairs["liquidity"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        fdv = pairs["fdv"]
        
        context = {"baseToken":baseToken,"priceNative":priceNative, "priceChange":priceChange, "volume":volume, "fdv":fdv, "volume":volume, "txns":txns, "priceUsd":priceUsd, "liquidity":liquidity, "txns":txns, "price_in_usd":price_in_usd, "fully_diluted_valuation":fully_diluted_valuation, "price_percent_change":price_percent_change, "from_volume_in_usd":from_volume_in_usd}
        return render(request, "main/yfi.html", context)

def SpoonView(request):
    if request.method == "POST":
        pass
    else:
        
        
        rs = requests.get("https://api.dexscreener.com/latest/dex/tokens/0x66B96135d0c639D53e1f23b7a5849F6022883b41")
        resp = requests.get("https://app.geckoterminal.com/api/p1/core/pools/0xbb8502132c87ee31be0e2bc1cb8cc69374488261")
        getValue = resp.json()
        price_in_usd = getValue["data"]["attributes"]["price_in_usd"]
        fully_diluted_valuation = getValue["data"]["attributes"]["fully_diluted_valuation"]
        price_percent_change = getValue["data"]["attributes"]["price_percent_change"]
        from_volume_in_usd = getValue["data"]["attributes"]["from_volume_in_usd"]
        dekatrons = rs.json()
        pairs = dekatrons["pairs"][0]
        baseToken = pairs["baseToken"]
        priceNative = pairs["priceNative"]
        priceUsd = pairs["priceUsd"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        priceChange = pairs["priceChange"]
        liquidity = pairs["liquidity"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        fdv = pairs["fdv"]
        
        context = {"baseToken":baseToken,"priceNative":priceNative, "priceChange":priceChange, "volume":volume, "fdv":fdv, "volume":volume, "txns":txns, "priceUsd":priceUsd, "liquidity":liquidity, "txns":txns, "price_in_usd":price_in_usd, "fully_diluted_valuation":fully_diluted_valuation, "price_percent_change":price_percent_change, "from_volume_in_usd":from_volume_in_usd}
        return render(request, "main/spoon.html", context)
        
def CoredogeView(request):
    if request.method == "POST":
        pass
    else:
        
        
        rs = requests.get("https://api.dexscreener.com/latest/dex/tokens/0x8bab1Ef0F175F6d7EBCE79ee277BA091832F6429")
        resp = requests.get("https://app.geckoterminal.com/api/p1/core/pools/0xbb8502132c87ee31be0e2bc1cb8cc69374488261")
        getValue = resp.json()
        price_in_usd = getValue["data"]["attributes"]["price_in_usd"]
        fully_diluted_valuation = getValue["data"]["attributes"]["fully_diluted_valuation"]
        price_percent_change = getValue["data"]["attributes"]["price_percent_change"]
        from_volume_in_usd = getValue["data"]["attributes"]["from_volume_in_usd"]
        dekatrons = rs.json()
        pairs = dekatrons["pairs"][0]
        baseToken = pairs["baseToken"]
        priceNative = pairs["priceNative"]
        priceUsd = pairs["priceUsd"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        priceChange = pairs["priceChange"]
        liquidity = pairs["liquidity"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        fdv = pairs["fdv"]
        
        context = {"baseToken":baseToken,"priceNative":priceNative, "priceChange":priceChange, "volume":volume, "fdv":fdv, "volume":volume, "txns":txns, "priceUsd":priceUsd, "liquidity":liquidity, "txns":txns, "price_in_usd":price_in_usd, "fully_diluted_valuation":fully_diluted_valuation, "price_percent_change":price_percent_change, "from_volume_in_usd":from_volume_in_usd}
        return render(request, "main/coredoge.html", context)
    
def LfgswapView(request):
    if request.method == "POST":
        pass
    else:
        
        
        rs = requests.get("https://api.dexscreener.com/latest/dex/tokens/0xF7a0b80681eC935d6dd9f3Af9826E68B99897d6D")
        resp = requests.get("https://app.geckoterminal.com/api/p1/core/pools/0xbb8502132c87ee31be0e2bc1cb8cc69374488261")
        getValue = resp.json()
        price_in_usd = getValue["data"]["attributes"]["price_in_usd"]
        fully_diluted_valuation = getValue["data"]["attributes"]["fully_diluted_valuation"]
        price_percent_change = getValue["data"]["attributes"]["price_percent_change"]
        from_volume_in_usd = getValue["data"]["attributes"]["from_volume_in_usd"]
        dekatrons = rs.json()
        pairs = dekatrons["pairs"][0]
        baseToken = pairs["baseToken"]
        priceNative = pairs["priceNative"]
        priceUsd = pairs["priceUsd"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        priceChange = pairs["priceChange"]
        liquidity = pairs["liquidity"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        fdv = pairs["fdv"]
        
        context = {"baseToken":baseToken,"priceNative":priceNative, "priceChange":priceChange, "volume":volume, "fdv":fdv, "volume":volume, "txns":txns, "priceUsd":priceUsd, "liquidity":liquidity, "txns":txns, "price_in_usd":price_in_usd, "fully_diluted_valuation":fully_diluted_valuation, "price_percent_change":price_percent_change, "from_volume_in_usd":from_volume_in_usd}
        return render(request, "main/lfgswap.html", context)


def PepeView(request):
    if request.method == "POST":
        pass
    else:
        
        
        rs = requests.get("https://api.dexscreener.com/latest/dex/tokens/0x9B944a707cfDE49b7c0a9593f88b17Dc2C05DB78")
        resp = requests.get("https://app.geckoterminal.com/api/p1/core/pools/0xbb8502132c87ee31be0e2bc1cb8cc69374488261")
        getValue = resp.json()
        price_in_usd = getValue["data"]["attributes"]["price_in_usd"]
        fully_diluted_valuation = getValue["data"]["attributes"]["fully_diluted_valuation"]
        price_percent_change = getValue["data"]["attributes"]["price_percent_change"]
        from_volume_in_usd = getValue["data"]["attributes"]["from_volume_in_usd"]
        dekatrons = rs.json()
        pairs = dekatrons["pairs"][0]
        baseToken = pairs["baseToken"]
        priceNative = pairs["priceNative"]
        priceUsd = pairs["priceUsd"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        priceChange = pairs["priceChange"]
        liquidity = pairs["liquidity"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        fdv = pairs["fdv"]
        
        context = {"baseToken":baseToken,"priceNative":priceNative, "priceChange":priceChange, "volume":volume, "fdv":fdv, "volume":volume, "txns":txns, "priceUsd":priceUsd, "liquidity":liquidity, "txns":txns, "price_in_usd":price_in_usd, "fully_diluted_valuation":fully_diluted_valuation, "price_percent_change":price_percent_change, "from_volume_in_usd":from_volume_in_usd}
        return render(request, "main/pepe.html", context)
        
def LungView(request):
    if request.method == "POST":
        pass
    else:
        
        
        rs = requests.get("https://api.dexscreener.com/latest/dex/tokens/0x28b9aed756de31b6b362aa0f23211d13093ebb79")
        resp = requests.get("https://app.geckoterminal.com/api/p1/bsc/pools/0x0f008480ddc18b6bac65863dcd4ebbea0716e572")
        getValue = resp.json()
        price_in_usd = getValue["data"]["attributes"]["price_in_usd"]
        fully_diluted_valuation = getValue["data"]["attributes"]["fully_diluted_valuation"]
        price_percent_change = getValue["data"]["attributes"]["price_percent_change"]
        from_volume_in_usd = getValue["data"]["attributes"]["from_volume_in_usd"]
        dekatrons = rs.json()
        pairs = dekatrons["pairs"][0]
        baseToken = pairs["baseToken"]
        priceNative = pairs["priceNative"]
        priceUsd = pairs["priceUsd"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        priceChange = pairs["priceChange"]
        liquidity = pairs["liquidity"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        fdv = pairs["fdv"]
        
        context = {"baseToken":baseToken,"priceNative":priceNative, "priceChange":priceChange, "volume":volume, "fdv":fdv, "volume":volume, "txns":txns, "priceUsd":priceUsd, "liquidity":liquidity, "txns":txns, "price_in_usd":price_in_usd, "fully_diluted_valuation":fully_diluted_valuation, "price_percent_change":price_percent_change, "from_volume_in_usd":from_volume_in_usd}
        return render(request, "main/lung.html", context)
        
def BitgertView(request):
    if request.method == "POST":
        pass
    else:
        rs = requests.get("https://api.dexscreener.com/latest/dex/tokens/	0x8fff93e810a2edaafc326edee51071da9d398e83")
        resp = requests.get("https://app.geckoterminal.com/api/p1/bsc/pools/0x0f008480ddc18b6bac65863dcd4ebbea0716e572")
        getValue = resp.json()
        price_in_usd = getValue["data"]["attributes"]["price_in_usd"]
        fully_diluted_valuation = getValue["data"]["attributes"]["fully_diluted_valuation"]
        price_percent_change = getValue["data"]["attributes"]["price_percent_change"]
        from_volume_in_usd = getValue["data"]["attributes"]["from_volume_in_usd"]
        dekatrons = rs.json()
        pairs = dekatrons["pairs"][0]
        baseToken = pairs["baseToken"]
        priceNative = pairs["priceNative"]
        priceUsd = pairs["priceUsd"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        priceChange = pairs["priceChange"]
        liquidity = pairs["liquidity"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        fdv = pairs["fdv"]
        
        context = {"baseToken":baseToken,"priceNative":priceNative, "priceChange":priceChange, "volume":volume, "fdv":fdv, "volume":volume, "txns":txns, "priceUsd":priceUsd, "liquidity":liquidity, "txns":txns, "price_in_usd":price_in_usd, "fully_diluted_valuation":fully_diluted_valuation, "price_percent_change":price_percent_change, "from_volume_in_usd":from_volume_in_usd}
        return render(request, "main/bitgert.html", context)
        
def CantoView(request):
    if request.method == "POST":
        pass
    else:
        response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=canto&vs_currencies=usd&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true&include_last_updated_at=true").json()
        data = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=canto&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
        rs = requests.get("https://api.dexscreener.io/latest/dex/tokens/0x826551890dc65655a0aceca109ab11abdbd7a07b")
        dekatrons = rs.json()
        pairs = dekatrons["pairs"][0]
        baseToken = pairs["baseToken"]
        priceNative = pairs["priceNative"]
        priceUsd = pairs["priceUsd"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        priceChange = pairs["priceChange"]
        volume = pairs["volume"]
        fdv = pairs["fdv"]
        price = str(response["canto"]["usd"])
        market_cap = int(response["canto"]["usd_market_cap"])
        hr_vol = str(response["canto"]["usd_24h_vol"])
        hr_chg = str(response["canto"]["usd_24h_change"])
        last_updated = str(response["canto"]["last_updated_at"])
        context = {"data":data, "price":price, "market_cap":market_cap, "hr_vol":hr_vol, "hr_chg":hr_chg, "last_updated":last_updated,"priceNative":priceNative, "priceChange":priceChange, "volume":volume, "fdv":fdv, "volume":volume, "txns":txns, "priceUsd":priceUsd}
        return render(request, "main/canto.html", context)
        

        
def ComingView(request):
    if request.method == "POST":
        pass
        

    else:

        context = {}
        return render(request, "main/comingsoon.html", context)
        
def error_404(request, exception):
    return render(request,'app_user/400.html')
    
def error_500(request):
    return render(request,'app_user/500.html')

        
        
