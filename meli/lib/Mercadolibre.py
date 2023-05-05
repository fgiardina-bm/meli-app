import requests

class Mercadolibre():
    def __init__(self):
        self.url = f"https://api.mercadolibre.com/sites/MLA/search?q="
        self.headers = {
            'Content-type': 'application/jsoon',
            'Authorization': 'Bearer XXXXXXXXXX'
        }

    def buscar(self,q,limit=10,offset=0):
        return requests.get(self.url+q+'&limit='+str(limit)+'&offset='+str(offset), headers=self.headers)