 Gestor de Tareas

⚡ Descripción

Una aplicación web sencilla de gestión de tareas, desarrollada con **Django** en Python, diseñada para facilitar la organización y el seguimiento de proyectos en un entorno de servidor. Este proyecto proporciona herramientas para crear, gestionar y controlar tareas de forma eficiente a través de una interfaz intuitiva y fácil de usar.

## Características Principales

- ✅ Crear nuevas tareas
- ✅ Editar tareas existentes
- ✅ Eliminar tareas
- ✅ Listar todas las tareas
- ✅ Interfaz web intuitiva y responsive
- ✅ Base de datos persistente

## Tecnologías Utilizadas

- **Python 3.8+** - Lenguaje de programación
- **Django 3.2+** - Framework web backend
- **SQLite** - Base de datos (por defecto)
- **HTML/CSS** - Frontend

💻 Requisitos del Sistema

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Dependencias listadas en `requirements.txt`

  🚀 Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/rvssian666/Entorno_Servidor.git
cd Entorno_Servidor
```

### 2. Crear un entorno virtual (recomendado)

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Aplicar migraciones

```bash
python manage.py migrate
```

### 5. Crear un superusuario (administrador)

```bash
python manage.py createsuperuser
```

Sigue las instrucciones en pantalla para crear tu cuenta de administrador.

📦Estructura del Proyecto

```
Entorno_Servidor/
├── task_manager/              # Aplicación principal de Django
│   ├── migrations/            # Migraciones de base de datos
│   ├── templates/             # Plantillas HTML
│   ├── static/                # Archivos CSS, JS, imágenes
│   ├── models.py              # Modelos de datos
│   ├── views.py               # Vistas de la aplicación
│   ├── urls.py                # Rutas URL
│   └── admin.py               # Configuración del panel de administración
├── proyecto/                  # Configuración del proyecto Django
│   ├── settings.py            # Configuración del proyecto
│   ├── urls.py                # Rutas principales
│   ├── wsgi.py                # Configuración WSGI
│   └── asgi.py                # Configuración ASGI
├── manage.py                  # Script de gestión de Django
├── requirements.txt           # Dependencias del proyecto
└── README.md                  # Este archivo
```

## Uso

### Iniciar el servidor de desarrollo

```bash
python manage.py runserver
```

La aplicación estará disponible en `http://127.0.0.1:8000/`

### Acceder al panel de administración

```
http://127.0.0.1:8000/admin/
```

Inicia sesión con las credenciales del superusuario creado.

### Crear una nueva tarea

1. Accede a la página principal de la aplicación
2. Haz clic en "Crear nueva tarea"
3. Completa los campos requeridos
4. Haz clic en "Guardar"

### Editar una tarea

1. Selecciona una tarea de la lista
2. Haz clic en "Editar"
3. Realiza los cambios necesarios
4. Haz clic en "Actualizar"

### Eliminar una tarea

1. Selecciona una tarea de la lista
2. Haz clic en "Eliminar"
3. Confirma la acción

## Archivo requirements.txt

Asegúrate de que tu `requirements.txt` incluya las siguientes dependencias:

```
Django>=3.2,<4.0
```

O si necesitas versiones más recientes:

```
Django>=4.0
```

## Configuración de la Base de Datos

Por defecto, este proyecto utiliza **SQLite** como base de datos. Para cambiar a otra base de datos como PostgreSQL o MySQL:

1. Instala el adaptador correspondiente:
   - PostgreSQL: `pip install psycopg2-binary`
   - MySQL: `pip install mysqlclient`

2. Modifica `proyecto/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  # o 'django.db.backends.mysql'
        'NAME': 'nombre_base_datos',
        'USER': 'usuario',
        'PASSWORD': 'contraseña',
        'HOST': 'localhost',
        'PORT': '5432',  # 3306 para MySQL
    }
}
```

## Contribuir

Las contribuciones son bienvenidas. Si deseas mejorar este proyecto:

1. Haz un fork del repositorio
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

💳 Licencia

Este proyecto está bajo la licencia MIT. Ver el archivo `LICENSE` para más detalles.

 🙍‍♂️Autor

- Alexander Fuentes - Desarrollo inicial

## Contacto

Si tienes preguntas o sugerencias sobre el proyecto, no dudes en abrir un issue en el repositorio.

## Estado del Proyecto

Este es un proyecto académico/educativo en desarrollo. Las mejoras y nuevas características se añadirán de forma continua.

## Notas Importantes

- Asegúrate de nunca compartir tu archivo `settings.py` con credenciales reales. Usa variables de entorno para información sensible.
- Para producción, establece `DEBUG = False` en `settings.py`
- Utiliza un servidor web como Gunicorn o uWSGI en lugar del servidor de desarrollo

---

**Última actualización:** 2026-02-14
