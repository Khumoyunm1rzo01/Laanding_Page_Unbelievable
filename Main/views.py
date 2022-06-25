from django.shortcuts import render, redirect
import requests 
from .models import *

def Index(request):
    title = MySite.objects.last()
    hello = Welcome.objects.last()
    house = Home.objects.last()
    haqida = About.objects.last()
    hizmatlar = Service.objects.last()
    narhlar = Price.objects.last()
    jamoa = Team.objects.last()
    klient = Clients.objects.last()
    boglanish = Contact.objects.last()
    kirish = SignIn.objects.last()
    ulanish = LogIn.objects.last()
    ulanish1 = SignUp.objects.last()
    boshlash = StartNow.objects.last()
    biz_haqimizda = Haqida.objects.last()
    hizmat = Servis.objects.last()
    oson = Simple.objects.last()
    text1 = Simple.objects.last()
    kuchli = Powerful.objects.last()
    text2 = Powerful.objects.last()
    tekst = Haqida.objects.last()
    qulay = Easy.objects.last()
    text3 = Easy.objects.last()
    tekst1 = Servis.objects.last()
    yuksalish_siri = Muvaffaqiyat.objects.last()
    tekst2 = Muvaffaqiyat.objects.last()
    organish = Learn.objects.last()
    zor = Great.objects.last()
    tekst3 = Great.objects.last()
    alo = Best.objects.last()
    tab = Best.objects.last()
    qollash = Support.objects.last()
    tekst4 = Support.objects.last()
    oqish = Learning.objects.last()
    talim_olish = Learning.objects.last()
    title = Awesome.objects.last()
    text = Awesome.objects.last()
    tittle_1 = Wallet.objects.all()
    text_1 = Wallet.objects.all()
    tittle_2 = Wallet.objects.all()
    text_2 = Wallet.objects.all()
    tittle_3 = Wallet.objects.all()
    text_3 = Wallet.objects.all()
    text = Me.objects.all()
    context = {
        'section1': Section1.objects.all(),
        'comandainfo': ComandaInfo.objects.all(),
        'section': Section.objects.all(),
        'comanda': Comanda.objects.all(),
        'prices': Prices.objects.all(),
        'clients': RealClients.objects.all(),
        'image': RealClientsImages.objects.all(),
        'real': RealPrices.objects.all(),
        'tittle_1': tittle_1,
        'text_1': text_1,
        'tittle_2': tittle_2,
        'text_2': text_2,
        'tittle_3': tittle_3,
        'text_3': text_3,
        'oqish': oqish,
        'talim_olish': talim_olish,
        'qollash': qollash,
        'tekst4': tekst4,
        'alo': alo,
        'tab': tab,
        'tekst3': tekst3,
        'zor': zor, 
        'organish': organish,
        'yuksalish_siri': yuksalish_siri,
        'tekst2': tekst2,
        'tekst1': tekst1,
        'qulay': qulay,
        'text3': text3,
        'tekst': tekst,
        'text2': text2,
        'text1': text1,
        'kuchli': kuchli,
        'oson': oson,
        'hizmat': hizmat,
        'biz_haqimizda': biz_haqimizda,
        'boshlash': boshlash,
        'ulanish1': ulanish1,
        'ulanish': ulanish, 
        'kirish': kirish,
        'boglanish': boglanish,
        'klient': klient,
        'jamoa': jamoa,
        'narhlar': narhlar,
        'hizmatlar': hizmatlar,
        'haqida': haqida,
        'house': house,
        'title': title,
        'hello': hello,
        'about': Me.objects.all(),
        'title': title, 
        'text': text,
    }
    return render(request, 'index.html', context)

def AddContact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST.get('email')
        message = request.POST.get('message')

        Contact1.objects.create(name=name, email=email, message=message)
        ids = Telegram_ids.objects.all()
        token = "5288291380:AAEZ2SvY0bfasXyK0x_qm1uRcsg527SifEg"
        for id in ids:
            text = 'Yangi obuna: \n\nMijoz: ' + name + '\nEmail: ' + email + '\nMessage: ' + message
            url = 'https://api.telegram.org/bot' + token + '/sendMessage?chat_id='
            requests.get(url + str(id.ids) + '&text=' + text)
    return redirect('index')