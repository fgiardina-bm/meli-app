import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage, db, firestore
import datetime

# https://storage.googleapis.com/meli-b67df.appspot.com/
# meli-b67df-firebase-adminsdk-295cy-13fb469e45.json

class Storage():
    def __init__(self, collection_name):
        cred = credentials.Certificate('meli/lib/meli-b67df-firebase-adminsdk-295cy-13fb469e45.json')
        firebase_admin.initialize_app(cred, {
            'storageBucket': 'meli-b67df.appspot.com',
            'databaseURL': 'https://meli-b67df-default-rtdb.firebaseio.com/'
        })
        self.base_url = 'https://storage.googleapis.com/meli-b67df.appspot.com/'
        self.bucket = storage.bucket()
        self.ref = db.reference(collection_name)
        self.firestore = firestore.client()

    def upload(self,filepath,destination_name, publica=False):
        archivo_local = filepath
        archivo_remoto = destination_name
        blob = self.bucket.blob(archivo_remoto)
        blob.upload_from_filename(archivo_local)

        if publica == True:
            url_publica = blob.public_url
            blob.make_public()
            return url_publica
        else:    
            ttl = datetime.timedelta(hours=1)
            url_temporal = blob.generate_signed_url(expiration=ttl)
            return url_temporal
        

    def get_data_by_key(self, key):
        return self.ref.child(key).get()
    
    def get_data_by_key_value(self, key, value):
        return self.ref.order_by_child(key).equal_to(value).get()

    def add_data(self, data, key=None):
        if key is None:
            return self.ref.push(data)
        else:
            return self.ref.child(key).set(data)        
        
    def update_data(self, data, datos_filtrados):
        for key, value in datos_filtrados.items():
            self.ref.child(key).update(data)

    def add_data_firestore(self,data, id):
        doc_ref = self.firestore.collection('meli').document(id)
        doc_ref.set(data)

    def update_data_firestore(self,data, id):
        doc_ref = self.firestore.collection('meli').document(id)
        doc_ref.set(data)

    def get_check_exists_firestore(self,id):
        doc_ref = self.firestore.collection('meli').document(id)
        doc = doc_ref.get()
        return doc

    def get_all_cnt_firestore(self):
        docs = self.firestore.collection("meli")
        count_query = docs.count()
        query_result = count_query.get()
        # stream_query = docs.stream()
        return {
            'count':query_result[0][0].value,
            # 'data': stream_query
        }
        
        
