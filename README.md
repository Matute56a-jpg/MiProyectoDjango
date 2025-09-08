# 🍷 Proyecto Django: Vino Argentino

Este es un proyecto web desarrollado en Python con Django como entrega final de curso. La aplicación simula un blog temático dedicado al vino argentino, con secciones de publicaciones, gestión de bodegas, enólogos y vinos.

---

## 🚀 Funcionalidades principales

- **Página de inicio** con banner e introducción al proyecto.
- **Sección "Acerca de mí"** donde se presenta el autor.
- **Blog** con CRUD (crear, leer, actualizar y borrar posts).  
- **Gestión de vinos** (modelo principal):
  - Crear, listar, buscar y editar vinos.
  - Asociar bodegas y enólogos.
- **Autenticación de usuarios**:
  - Registro de nuevos usuarios.
  - Inicio y cierre de sesión.
  - Perfil con datos editables.
- **Mensajería interna** entre usuarios.
- **Panel de administración** para gestionar todo el contenido.
- **Uso de CKEditor 5** para edición enriquecida de texto.

---

## 📦 Requisitos previos

- Python 3.10+  
- Django 5.2+  
- Virtualenv (opcional, recomendado)

---

## ⚙️ Instalación

1. Clona el repositorio:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd MiProyectoDjango
   ```

2. Crea y activa el entorno virtual:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate   # En Windows
   source .venv/bin/activate  # En Linux/Mac
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Ejecuta las migraciones:
   ```bash
   python manage.py migrate
   ```

5. Crea un superusuario:
   ```bash
   python manage.py createsuperuser
   ```

6. Inicia el servidor:
   ```bash
   python manage.py runserver
   ```

---

## 📂 Estructura básica del proyecto

```
MiProyectoDjango/
│── accounts/        # App para manejo de usuarios
│── blog/            # App para posts y artículos
│── core/            # Páginas principales (home, about)
│── messenger/       # App de mensajería interna
│── mi_app1/         # App de vinos (modelo principal)
│── media/           # Archivos subidos por usuarios (ignorado en git)
│── static/          # Archivos estáticos (CSS, JS, imágenes)
│── templates/       # Plantillas HTML con herencia
│── db.sqlite3       # Base de datos (ignorada en git)
│── manage.py        # Comando principal de Django
│── requirements.txt # Dependencias
│── .gitignore       # Archivos y carpetas ignoradas en git
```

---

## 🔑 Credenciales iniciales

Después de crear el superusuario con `createsuperuser`, podrás acceder a:

👉 **Admin**: http://127.0.0.1:8000/admin/  
👉 **Login**: http://127.0.0.1:8000/accounts/login/

---

## ✨ Funcionalidades extra

- Uso de **mixins y decoradores** en vistas.  
- Validaciones en formularios.  
- Herencia de templates para mantener diseño uniforme.  

---

## 📹 Entrega final

La entrega incluye:

- Código en GitHub (sin `db.sqlite3`, `media/` ni `__pycache__/`).  
- Archivo **README.md** con instrucciones claras.  
- Video de máximo 10 minutos mostrando la aplicación y sus funciones.  

---

## 👨‍💻 Autor

- **Matías Pérez**  
  Proyecto desarrollado como entrega final en Django.  
