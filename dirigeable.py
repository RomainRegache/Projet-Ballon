from network import WLAN
import time
import socket
import utime
import os
import json
import ure
import machine


"""
Déclaration de la classe Dirigeable
"""
class Dirigeable:
    """
    Déclaration des attributs de la classe dirigeable:
        -wlan : correspond à l'objet permettant de piloter la Wi-Fi
        -data : liste contenant les différents messages à envoyer
        -WIFI_SSID : correspond au nom du SSID auquel nous allons nous connecter
        -WIFI_USER : correspond au username utilisé pour se connecter au Wi-Fi (non utilisé dans cette version)
        -WIFI_PSWD : correspond au mot de passe utilisé pour se connecter au Wi-Fi
        -URL_POST_DATA : correspond à l'URL à laquelle est envoyée les données par défaut
    """
    wlan = WLAN(mode=WLAN.STA)
    data = []
    WIFI_SSID = ""
    WIFI_USER = ""
    WIFI_PSWD = ""
    URL_POST_DATA = ""

    """
    Nom : __init__(self)
    But : Initialisation de l'objet créé
    Description : Les variables sont initialisés à partir du fichier CONF qui doit se situer dans le même répertoire que le programme
    """
    def __init__(self):
        f = open("CONF","r")
        regex = ure.compile("[\;]")
        r = regex.split(f.read())
        self.WIFI_SSID = r[1]
        self.WIFI_USER = r[3]
        self.WIFI_PSWD = r[5]
        self.URL_POST_DATA = r[7]
        f.close()

    """
    Nom : wifi_start(self)
    But : Connexion au réseau Wi-Fi
    Description : Connecte le microcontrôleur au réseau Wi-Fi
    Met également à jour l'horloge du microcontrôleur.
    """
    def wifi_start(self):
        self.wlan.init()
        self.wlan.connect(self.WIFI_SSID, auth=(WLAN.WPA2, self.WIFI_PSWD))
        while not self.wlan.isconnected():
            time.sleep_ms(50)
        print(self.wlan.ifconfig())
        machine.RTC().ntp_sync("delphi.phys.univ-tours.fr")


    """
    Nom : wifi_stop(self)
    But : Déconnexion du réseau Wi-Fi
    Description : Déconnecte le microcontrôleur du réseau Wi-Fi
    """
    def wifi_stop(self):
        self.wlan.disconnect()
        self.wlan.deinit() #si cette ligne n'est pas présente, il y aura un conflit lors de la reconnexion au réseau

    """
    Nom : http_get(self,url)
    But : Effectuer une requête HTTP GET sur une URL
    Description : Cette fonction permet d'initialiser un socket afin d'effectuer une requête GET sur une adresse web passée en paramètre
    Le résultat de la requête est affichée.
    """
    def http_get(self,url):
        _, _, host, path = url.split('/', 3)
        addr = socket.getaddrinfo(host, 80)[0][-1]
        s = socket.socket()
        s.connect(addr)
        s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
        while True:
            data = s.recv(100)
            if data:
                print(str(data, 'utf8'))
            else:
                break
        s.close()


    """
    Nom : http_post(self,url,data)
    But : Effectuer une requête HTTP POST sur une URL
    Description : Cette fonction permet d'intiailiser un socket et d'envoyer les données passés en paramètre
    de la variable data sur l'URL passé en paramètre de la variable url.
    """
    def http_post(self,url,data):
        _, _, host, path = url.split('/', 3)
        addr = socket.getaddrinfo(host, 80)[0][-1]
        s = socket.socket()
        s.connect(addr)
        s.send(bytes('POST /%s HTTP/1.1\nHost: %s\nContent-Type: text/plain\nContent-Length: 2\n\n%s' % (path, host, data), 'utf8'))
        data = s.recv(100)
        if data:
            print(str(data, 'utf8'))
        s.close()

    from network import WLAN
import time
import socket
import utime
import os
import json
import ure
import machine

"""
Déclaration de la classe Dirigeable
"""
class Dirigeable:
    """
    Déclaration des attributs de la classe dirigeable:
        -wlan : correspond à l'objet permettant de piloter la Wi-Fi
        -data : liste contenant les différents messages à envoyer
        -WIFI_SSID : correspond au nom du SSID auquel nous allons nous connecter
        -WIFI_USER : correspond au username utilisé pour se connecter au Wi-Fi (non utilisé dans cette version)
        -I_PSWD : correspond au mot de passe utilisé pour se connecter au Wi-Fi
        -URL_POST_DATA : correspond à l'URL à laquelle est envoyée les données par défaut
    """
    wlan = WLAN(mode=WLAN.STA)
    data = []
    WIFI_SSID = ""
    WIFI_USER = ""
    WIFI_PSWD = ""
    URL_POST_DATA = ""

    """
    Nom : __init__(self)
    But : Initialisation de l'objet créé
    Description : Les variables sont initialisés à partir du fichier CONF qui doit se situer dans le même répertoire que le programme
    """
    def __init__(self):
        f = open("CONF","r")
        regex = ure.compile("[\;]")
        r = regex.split(f.read())
        self.WIFI_SSID = r[1]
        self.WIFI_USER = r[3]
        self.WIFI_PSWD = r[5]
        self.URL_POST_DATA = r[7]
        f.close()

    """
    Nom : wifi_start(self)
    But : Connexion au réseau Wi-Fi
    Description : Connecte le microcontrôleur au réseau Wi-Fi
    Met également à jour l'horloge du microcontrôleur.
    """
    def wifi_start(self):
        self.wlan.init()
        self.wlan.connect(self.WIFI_SSID, auth=(WLAN.WPA2, self.WIFI_PSWD))
        while not self.wlan.isconnected():
            time.sleep_ms(50)
        print(self.wlan.ifconfig())
        machine.RTC().ntp_sync("delphi.phys.univ-tours.fr")


    """
    Nom : wifi_stop(self)
    But : Déconnexion du réseau Wi-Fi
    Description : Déconnecte le microcontrôleur du réseau Wi-Fi
    """
    def wifi_stop(self):
        self.wlan.disconnect()
        self.wlan.deinit() #si cette ligne n'est pas présente, il y aura un conflit lors de la reconnexion au réseau

    """
    Nom : http_get(self,url)
    But : Effectuer une requête HTTP GET sur une URL
    Description : Cette fonction permet d'initialiser un socket afin d'effectuer une requête GET sur une adresse web passée en paramètre
    Le résultat de la requête est affichée.
    """
    def http_get(self,url):
        _, _, host, path = url.split('/', 3)
        addr = socket.getaddrinfo(host, 80)[0][-1]
        s = socket.socket()
        s.connect(addr)
        s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
        while True:
            data = s.recv(100)
            if data:
                print(str(data, 'utf8'))
            else:
                break
        s.close()


    """
    Nom : http_post(self,url,data)
    But : Effectuer une requête HTTP POST sur une URL
    Description : Cette fonction permet d'intiailiser un socket et d'envoyer les données passés en paramètre
    de la variable data sur l'URL passé en paramètre de la variable url.
    """
    def http_post(self,url,data):
        _, _, host, path = url.split('/', 3)
        print(host)
        print(_)
        print()
        addr = socket.getaddrinfo(host, 80)[0][-1]
        s = socket.socket()
        s.connect(addr)
        s.send(bytes('POST /%s HTTP/1.1\nHost: %s\nContent-Type: text/plain\nContent-Length: 2\n\n%s' % (path, host, data), 'utf8'))
        data = s.recv(100)
        if data:
            print(str(data, 'utf8'))
        s.close()

    """
    Nom : http_post_json(self,url,data)
    But : Effectuer une requête HTTP POST sur une URL avec des données json
    Description : Cette fonction permet d'envoyer des données formaliser en json vers une adresse passée en paramètre.
    """
    def http_post_json(self,url,data):
        _, _, host, path = url.split('/', 3)
        print(url.split('/', 3))
        print(host)
        print(path)
        addr = socket.getaddrinfo(host, 80)[0][-1]
        print(addr)
        s = socket.socket()
        s.connect(addr)
        json_str = json.dumps(data)
        #print(json_str)
        print(s.send(bytes('POST /%s HTTP/1.1\nHost: %s\nContent-Type: application/json\nContent-Length: %s\n\n%s' % (path, host,len(json_str), json_str), 'utf8')))
        s.send(bytes('POST /%s HTTP/1.1\nHost: %s\nContent-Type: application/json\nContent-Length: %s\n\n%s' % (path, host,len(json_str), json_str), 'utf8'))
        data = s.recv(100)
        if data:
            print(str(data, 'utf8'))
        s.close()

    """
    Nom : data_reset(self)
    But : Remettre à zéro les données stocker à envoyer
    Description : Supprime les données mise en attente pour l'envoi de la variable "data"
    """
    def data_reset(self):
        self.data = []

    """
    Nom : data_add(self,new)
    But : Ajouter des données à la file d'attente des envois
    Description : Ajoute la donnée "new" dans la liste "data" comprenant les données à envoyer.
    "new" doit être de type dictionnaire, afin de le formaliser par la suite en json
    """
    def data_add(self,new):
        self.data.append(new)

    """
    Nom : data_send(self,url)
    But : Envoyer les données de "data" vers "url"
    Description : Envoi des données de type json, mises en attente dans la variable "data".
    """
    def data_send(self,url):
        for d in self.data:
            self.http_post_json(url, d)

    """
    Nom : data_send_default(self)
    But : Envoyer les données de "data" à l'adresse par défaut
    Description : Envoi les données de la liste "data" vers l'adresse par défaut définis dans le fichier
    CONF ou modifié par la suite dans la variable "URL_POST_DATA"
    """
    def data_send_default(self):
        self.data_send(self.URL_POST_DATA)

    """
    Nom : data_add_test(self)
    But : Ajout de données par défaut dans le but de tester un envoi
    """
    def data_add_test(self):
        d = {
            "time": "2021-12-10 16:03:07.193915",
            "dirigeable": "ptTours1",
            "MCP9808": "ok"
        }
        self.data_add(d)

    """
    Nom : sleep(self,time)
    But : Met en veille le microcontrôleur
    Description : Cette fonction a pour but de mettre en veille le microcontrôleur afin d'économiser de l'énergie.
    Contrairement à la fonction sleep classique, on pourra ici se déconnecter et reconnecter proprement au réseau WiFi.
    """
    def sleep(self,time):
        self.wifi_stop()
        machine.sleep(time)
        self.wifi_start()
