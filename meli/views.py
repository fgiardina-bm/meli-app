from django.shortcuts import render
from meli.lib.Mercadolibre import Mercadolibre
from meli.lib.Storage import Storage

# Create your views here.
def index(request):

    # storage=Storage()

    # url = storage.upload(
    #     filepath='/Users/fernandogiardina/Desktop/IMG_0001.jpeg',
    #     destination_name='IMG_0001.jpeg', 
    #     publica=False)
    # print(url)




    last_query = ''
    if request.method == 'POST':
        q = request.POST.get('search')
        last_query = q
        mercadolibre = Mercadolibre()
        response = mercadolibre.buscar(q)
        results = response.json()
        return render(request, 'index.html', {
            'response': results['results'],
            'paging': results['paging'],
            'last_query': last_query
        })
    else:
        return render(request, 'index.html', {
            'response': '',
            'paging': '',
            'last_query': last_query
        })

