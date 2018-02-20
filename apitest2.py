import urllib2
import json
import time


READ_API_KEY='PW3KP1EUN4Y8GI0X' #Hier den read api key hineinfügen
CHANNEL_ID='427711'  #Hier die Channel Id einfügen


while True: #Schleifen beginn
    TS = urllib2.urlopen("http://api.thingspeak.com/channels/%s/feeds/last.json?api_key=%s" \
                       % (CHANNEL_ID,READ_API_KEY))     #Definition der URL des API's, wo auch gleichzeitig die Werte von oben eingefügt werden.

    response = TS.read() #Befehl zum Lesen der Datei
    data=json.loads(response) #Auswerten der Ausgabe 


    a = data['created_at'] #Hier wird beschrieben wann der Stream erstellt wurde
    b = data['field1'] #Hier wird das feld eins, also der erste Messwert beschrieben
    c = data['field2'] #Hier kann man einfach die reihe der Messfelder fortsetzen
    print a + " Temperatur : " + b + "C" + "  Luftfeuchtigkeit : " + c + "%" + "    " #Das hier ist die Ausgabe der JSON und wird hiwer gedruckt
    time.sleep(5) #Hier wird beschrieben wie lange, in sekunden, gewartet wird bis zum nächsten Abfragen  

    TS.close() #Hier wird der Loop also die Schleife geschlossen.

#https://api.thingspeak.com/channels/427711/feeds.json?api_key=PW3KP1EUN4Y8GI0X
