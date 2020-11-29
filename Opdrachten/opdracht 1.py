import requests

opdracht =  {
        "nr1"   :   "Eerste regel",
        "nr2"   :   "Tweede regel",
        "nr3"   :   "Derde regel"
    }

x = requests.post('http://192.168.0.222:8000/opdracht2', json=opdracht)

print(x.text)