import schedule
import time
import datetime
import requests
import io
import os
from PIL import Image
from Mercadolibre import Mercadolibre
from Storage import Storage

mercadolibre=Mercadolibre()
storage=Storage('meli')

def task():
    print(f"Inicio de la tarea: {datetime.datetime.now()}")
    cnt_col = storage.get_all_cnt_firestore()
    print(f"Cnt COLLECTION: {cnt_col['count']}")
    temas = ['iPhone 14 Pro Max','chevrolet cruze','chevrolet tracker','macbook pro m2', 'sommier','colchon']
    for q in temas:
        offset = 0
        limit = 50
        loop = 3 #int(1000 / limit)
        print(q)
        for i in range(0,loop):
            # time.sleep(1)
            resutlados = mercadolibre.buscar(q,limit,offset)
            resutlados_json = resutlados.json()
            for item in resutlados_json['results']:
                dbitem = storage.get_check_exists_firestore(item['id'])
                dic = {
                    'id': item['id'],
                    'title': item['title'],
                    'price': item['price'],
                    'link': item['permalink'],
                    'condition': item['condition'],
                    'currency_id': item['currency_id'],
                    'available_quantity': item['available_quantity'],
                    'stop_time': item['stop_time'],
                    'address': item['address'],
                    'seller_address': item['seller_address'],
                    'attributes': item['attributes'],
                    'search': q,
                    'updated_at': datetime.datetime.now().isoformat()
                }

                if dbitem.exists == False:
                    dic['created_at'] = datetime.datetime.now().isoformat()
                    storage.add_data_firestore(dic,item['id'])
                    print(q, f"saved {item['id']}")

                    # imagen = Image.open(io.BytesIO(response.content))
                    # filename = item['id'] + '.jpg'
                    # imagen.save(filename)
                    # s = storage.upload(filename,filename)
                    # os.remove(filename)
                    # print(q, f"uploaded {filename}")

                else:
                    update_item = dbitem.to_dict()
                    try:
                        dic['created_at'] = update_item['created_at']
                    except:
                        pass

                    storage.update_data_firestore(dic,item['id'])
                    print(q, f"updated {item['id']}")

            print(len(resutlados_json['results']), i, offset)
            offset += limit

    print(f"Fin de la tarea: {datetime.datetime.now()}")
    print()

# Programar la tarea para que se ejecute cada hora
schedule.every(5).seconds.do(task)

while True:
    # Ejecutar la tarea programada
    schedule.run_pending()
    time.sleep(1)
