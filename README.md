...# **Django Best Practices Project**

Este proyecto implementa una aplicación Django utilizando las mejores prácticas descritas en el documento de referencia. Se enfoca en la creación de entornos virtuales, el uso de variables de entorno, la configuración adecuada de plantillas, la implementación de modelos abstractos, el uso de campos booleanos y choices, y una estructura organizada del proyecto.

---

## **Características del Proyecto**

1. **Redirección Automática**:
   - La URL base (`/`) redirige automáticamente a `/home/`.

2. **Gestión de Artículos**:
   - CRUD completo para gestionar artículos con estados predefinidos utilizando choices.
   - Implementación de modelos abstractos para evitar repetición de código.

3. **Buenas Prácticas de Django**:
   - Uso de entornos virtuales para un entorno aislado.
   - Configuración de variables sensibles con `django-environ`.
   - Organización y orden recomendado para imports y modelos.

4. **Estructura de Plantillas**:
   - Plantillas organizadas a nivel de aplicación y proyecto.

---

## **Requisitos Previos**

- Python 3.8 o superior.
- Django 4.0 o superior.
- django-environ.

---

## **Instalación**

### **1. Clonar el Repositorio**
```bash
git clone https://github.com/tu-usuario/django-best-practices.git
cd django-best-practices
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
DEBUG=True
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

### **Redirección Automática**
- Cuando accedes a la URL base (`/`), serás redirigido automáticamente a `/home/`.

### **Gestión de Artículos**
- Accede al sitio administrativo en [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) para gestionar artículos.
- Los artículos tienen estados predefinidos (`NEW`, `VERIFIED`, `PUBLISHED`) que se manejan con choices.

### **Página Principal**
- Accede a la página principal en [http://127.0.0.1:8000/home/](http://127.0.0.1:8000/home/).

---

## **Estructura del Proyecto**

```
config/
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
├── manage.py
├── env/
└── requirements.txt
```

---

## **Funciones Implementadas**

### **1. Modelos**
- **BaseModel**:
  - Modelo abstracto que incluye campos comunes (`state`, `created`, `modified`).
- **Article**:
  - Modelo que representa un artículo con estados definidos por choices (`NEW`, `VERIFIED`, `PUBLISHED`).

### **2. Sitio Administrativo**
- Personalización del sitio administrativo para buscar, filtrar y listar artículos.

### **3. Variables de Entorno**
- Uso de `django-environ` para separar configuraciones sensibles.

### **4. Redirección**
- Redirección automática desde `/` a `/home/`.

---

## **Pruebas y Depuración**

1. Verifica que las redirecciones funcionan correctamente:
   - Accede a [http://127.0.0.1:8000/](http://127.0.0.1:8000/) y asegúrate de ser redirigido a `/home/`.

2. Asegúrate de que los modelos aparecen en el sitio administrativo:
   - Crea y edita artículos desde el sitio administrativo.

3. Valida que los estados de los artículos (`NEW`, `VERIFIED`, `PUBLISHED`) se manejan correctamente.

---

## **Archivo `requirements.txt`**

```plaintext
django==4.2.5
django-environ==0.10.0
```

---

## **Contribuciones**

¡Las contribuciones son bienvenidas! Si deseas colaborar:
1. Haz un fork del repositorio.
2. Crea una rama para tus cambios.
3. Envía un pull request con una descripción detallada.

---
