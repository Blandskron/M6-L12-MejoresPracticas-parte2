# **Mejores Prácticas en Django**

Este proyecto implementa un ejemplo práctico basado en las mejores prácticas de Django, con un enfoque en la organización del código, el manejo de errores y la implementación de entornos virtuales, variables de entorno, y estructuras organizadas para plantillas y vistas.

---

## **Características del Proyecto**

1. **Redirección Automática**:
   - La URL base (`/`) redirige automáticamente a `/home/`.

2. **Manejo de Errores**:
   - Implementación de una página personalizada para el error 404 con un mensaje amigable: **"Creo que te perdiste esto"**.

3. **Gestión de Entornos y Configuración Segura**:
   - Uso de entornos virtuales y configuración mediante `django-environ`.
   - Separación de configuraciones sensibles a través de variables de entorno.

4. **Buenas Prácticas**:
   - Estructura clara de plantillas y vistas.
   - Uso de `ALLOWED_HOSTS` y manejo de configuraciones para entornos de producción.

---

## **Requisitos Previos**

- Python 3.8 o superior.
- Django 5.1.4 o superior.
- django-environ para manejar variables de entorno.

---

## **Instalación**

### **1. Clonar el Repositorio**
```bash
git clone https://github.com/tu-usuario/mejores-practicas-django.git
cd mejores-practicas-django
```

### **2. Crear un Entorno Virtual**
```bash
python -m venv env
source env/bin/activate  # En Windows: env\Scripts\activate
```

### **3. Instalar Dependencias**
```bash
pip install -r requirements.txt
```

### **4. Configurar Variables de Entorno**
Crea un archivo `.env` en la raíz del proyecto con el siguiente contenido:

```
SECRET_KEY=super-secret-key
DEBUG=False
ALLOWED_HOSTS=127.0.0.1,localhost
DATABASE_URL=sqlite:///db.sqlite3
```

### **5. Migrar la Base de Datos**
```bash
python manage.py makemigrations
python manage.py migrate
```

### **6. Crear un Superusuario**
```bash
python manage.py createsuperuser
```

### **7. Ejecutar el Servidor**
```bash
python manage.py runserver
```

---

## **Uso**

### **Página Principal**
- Accede a la página principal en [http://127.0.0.1:8000/home/](http://127.0.0.1:8000/home/).

### **Manejo del Error 404**
- Intenta acceder a una URL inexistente, como [http://127.0.0.1:8000/xyz](http://127.0.0.1:8000/xyz), y verás la página personalizada con el mensaje **"Creo que te perdiste esto"**.

### **Gestión de Usuarios y Datos**
- Accede al sitio administrativo en [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) para gestionar datos y usuarios.

---

## **Estructura del Proyecto**

```
mejores-practicas-django/
├── config/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── main/
│   ├── migrations/
│   ├── templates/
│   │   ├── main/
│   │   │   └── home.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   ├── urls.py
├── error404/
│   ├── templates/
│   │   ├── error404/
│   │   │   └── 404.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── views.py
│   ├── tests.py
├── manage.py
├── env/
└── requirements.txt
```

---

## **Funciones Implementadas**

### **1. Manejo de Errores**
- Personalización del error 404 con una página amigable.

### **2. Redirección Automática**
- La URL base (`/`) redirige automáticamente a `/home/`.

### **3. Configuración Segura**
- Uso de variables de entorno para manejar configuraciones sensibles, como `SECRET_KEY` y `ALLOWED_HOSTS`.

---

## **Pruebas**

1. **Página Principal**:
   - Asegúrate de que `/` redirige correctamente a `/home/`.

2. **Error 404**:
   - Intenta acceder a una ruta no existente para validar la página personalizada.

3. **Modo de Producción**:
   - Configura `DEBUG=False` y verifica que `ALLOWED_HOSTS` está correctamente configurado.

---

## **Archivo `requirements.txt`**

```plaintext
django==5.1.4
django-environ==0.10.0
```

---

## **Contribuciones**

¡Las contribuciones son bienvenidas! Si deseas colaborar:
1. Haz un fork del repositorio.
2. Crea una rama para tus cambios.
3. Envía un pull request con una descripción detallada.

---
