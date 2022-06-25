from django.db import models

# Create your models here.

class MySite(models.Model):
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    rasm = models.ImageField(upload_to='title/')

    def __str__(self):
          return self.title

class Welcome(models.Model):
    hello = models.CharField(max_length=255)

    def __str__(self):
        return self.hello

class Me(models.Model):
    about = models.CharField(max_length=255)
    text = models.TextField()


    def __str__(self):
        return self.about

class Home(models.Model):
    house = models.CharField(max_length=255)

    def __str__(self):
        return self.house
class About(models.Model):
    haqida = models.CharField(max_length=255)

    def __str__(self):
        return self.haqida

class Service(models.Model):
    hizmatlar = models.CharField(max_length=255)

    def __str__(self):
        return self.hizmatlar

class Price(models.Model):
    narhlar = models.CharField(max_length=255)

    def __str__(self):
        return self.narhlar

class Team(models.Model):
    jamoa = models.CharField(max_length=255)

    def __str__(self):
        return self.jamoa

class Clients(models.Model):
    klient = models.CharField(max_length=255)

    def __str__(self):
        return self.klient

class Contact(models.Model):
    boglanish = models.CharField(max_length=255)

    def __str__(self):
        return self.boglanish
class SignIn(models.Model):
    kirish = models.CharField(max_length=255)

class LogIn(models.Model):
    ulanish = models.CharField(max_length=255)

class SignUp(models.Model):
    ulanish1 = models.CharField(max_length=255)

class StartNow(models.Model):
    boshlash = models.CharField(max_length=255)

class Haqida(models.Model):
    biz_haqimizda = models.CharField(max_length=255)
    tekst = models.CharField(max_length=355)

class Servis(models.Model):
    hizmat = models.CharField(max_length=255)
    tekst1 = models.CharField(max_length=355)

class Simple(models.Model):
    oson = models.CharField(max_length=255)
    text1 = models.CharField(max_length=255)
    

class Powerful(models.Model):
    kuchli = models.CharField(max_length=255)
    text2 = models.CharField(max_length=255)

class Easy(models.Model):
    qulay = models.CharField(max_length=355)
    text3 = models.CharField(max_length=355)

class Muvaffaqiyat(models.Model):
    yuksalishimiz_siri = models.CharField(max_length=355)
    tekst2 = models.CharField(max_length=355)

class Learn(models.Model):
    organish = models.CharField(max_length=355)

class Great(models.Model):
    zor = models.CharField(max_length=355)
    tekst3 = models.CharField(max_length=500)

class Best(models.Model):
    alo = models.CharField(max_length=355)
    tab = models.CharField(max_length=500)

class Support(models.Model):
    qollash = models.CharField(max_length=355)
    tekst4 = models.CharField(max_length=500)

class Learning(models.Model):
    oqish = models.CharField(max_length=355)
    talim_olish = models.CharField(max_length=500)

class Awesome(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()

class Contact1(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()

class Wallet(models.Model):
    tittle_1 = models.CharField(max_length=255)
    text_1 = models.TextField()
    tittle_2 = models.CharField(max_length=255)
    text_2 = models.TextField()
    tittle_3 = models.CharField(max_length=255)
    text_3 = models.TextField()

class RealClients(models.Model):
    name = models.CharField(max_length=255)
    text = models.TextField()

class RealClientsImages(models.Model):
    image = models.ImageField(upload_to='RealClientsImages/')

class RealPrices(models.Model):
    tittle = models.CharField(max_length=255)
    text = models.TextField()

class Prices(models.Model):
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    text = models.TextField()
    button = models.CharField(max_length=255)

class Comanda(models.Model):
    tittle = models.CharField(max_length=255)
    text = models.CharField(max_length=300)

class ComandaInfo(models.Model):
    name = models.CharField(max_length=255)
    text_2 = models.TextField()
    image = models.ImageField(upload_to='Comanda/')
    fb_icon = models.CharField(max_length=255)
    tw_icon = models.CharField(max_length=255)
    linkedIn_icon = models.CharField(max_length=255)
    inst_icon = models.CharField(max_length=255)
class Section(models.Model):
    name = models.CharField(max_length=255)
    text = models.TextField()
    
class Section1(models.Model):
    adress_tittle = models.CharField(max_length=355)
    adress_name = models.CharField(max_length=255)
    call_tittle = models.CharField(max_length=255)
    call_phone = models.IntegerField()
    email_name = models.CharField(max_length=255)
    email = models.EmailField()
    
class Telegram_ids(models.Model):
    ids = models.IntegerField()
    