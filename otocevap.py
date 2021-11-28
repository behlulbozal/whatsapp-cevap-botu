# Tarayıcıyı açıp son mesajı yakala
from selenium import webdriver
# Kodu 3 saniyede bir çalıştır
import time
# Zamanlanmış mesaj için saati belirle
from datetime import datetime
# Klavyeyi bizim yerimize kullanır
import pyautogui
# Türkçe karakterlere izin verir
import locale
locale.setlocale(locale.LC_ALL, '')


def calistir():
    # Tarayıcıyı açıyoruz
    browser = tarayiciyi_ac()
    # Her 3 saniyede bir aynı mesaja cevap atılmasın diye böyle bir değişken tutuyoruz
    sonIslemYapilanMesaj = 'Herhangi bir mesaja cevap verilmedi'
    # QR kodu okuttuktan sonra terminalde ENTER'a basıyoruz
    input("QR kodu okut ve Enter'e bas")
    # While True ile sürekli dönen bir döngüye aldık
    while True:
        # Son gelen mesajı belirler
        sonGelenMesaj = son_gelen_mesaj(browser)
        # Eğer son gelen mesaj daha önce işlem yaptığımız mesaj değilse
        if(sonIslemYapilanMesaj != sonGelenMesaj):
            # Gelen mesaja cevap olarak belirlenmiş mesajı getir
            gonderilecek_mesaj = gonderilecek_mesaj_belirle(sonGelenMesaj)
            # Mesajı Gönder
            msg_send(gonderilecek_mesaj)
            # Bu mesaja bir daha işlem yapılmasın diye değişkenimize atama yap
            sonIslemYapilanMesaj = gonderilecek_mesaj

        # Otomatik zamanlanmış mesajın süresini ve içeriğini ayarla
        mesaj_zamanla_gonder('19', 'Günaydıın')
        # 3 saniye bekler ve sonra tekrar çalışır
        time.sleep(3)


def tarayiciyi_ac():
    browser = webdriver.Chrome(executable_path='./chromedriver')
    browser.implicitly_wait(3)
    browser.get('https://web.whatsapp.com')
    return browser


def mesaj_zamanla_gonder(gonderilecek_saat, gonderilecek_mesaj):
    saat = datetime.now().hour
    if(gonderilecek_saat == saat):
        msg_send(gonderilecek_mesaj)


def msg_send(gonderilecek_mesaj):
    pyautogui.press(gonderilecek_mesaj)
    pyautogui.press('enter')


def son_gelen_mesaj(browser):
    tumMesajlar = browser.find_elements_by_css_selector(
        "div[class='Nm1g1 _22AX6']")
    return tumMesajlar[len(tumMesajlar)-1].find_elements_by_css_selector(
        'div > div > div.copyable-text > div > span.emoji-texttt.i0jNr.selectable-text.copyable-text > span').text


def gonderilecek_mesaj_belirle(msg):
    if(msg == 'Nasılsın'):
        return 'İyiyim teşekkürler sen nasılsın'
    if(msg == 'Bugün işin var mı'):
        return 'Ya tamda bugün işim var biliyo musun, sonra görüşelim mi'


calistir()
