# MELI WEB APP

- Dentro de la carpeta del proyecto
 
```sh
pip install virtualenv
virtualenv venv 
source venv/bin/activate
code .
```

- Crear un proyecto con django
```sh
pip install django
pip install requests
pip install firebase
pip install firebase_admin
pip install schedule
pip install pillow

django-admin --version

django-admin startproject webapp .
python manage.py runserver
```

- Crear una app dentro del proyecto
```sh
django-admin startapp meli

```

- reinstalar entorno virtual
```sh 
borrar la carpeta venv
virtualenv venv 
source venv/bin/activate
pip install django
pip install requests
pip install firebase
pip install firebase_admin
pip install schedule
pip install pillow
```