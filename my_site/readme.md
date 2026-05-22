# Django Blog Project 🚀

## Introducció
Este proyecto consiste en el desarrollo de una aplicación web de Blog utilizando el framework **Django**. El objetivo principal es poner en práctica los conocimientos de programación web, diseño de bases de datos relacionales y la arquitectura MVT (Modelo-Vista-Plantilla).

### Objetivos principales:
* Gestionar un sistema dinámico de publicaciones (Posts) asociados a Autores y Etiquetas (Tags).
* Implementar un sistema de rutas limpias y amigables (URLs dinámicas y Slugs).
* Modularizar las vistas para ofrecer listados y detalles específicos de cada entidad.
* Poblar la base de datos de forma eficiente mediante el uso de *Fixtures*.

---

## Instal·lació ràpida

Sigue esta secuencia única de comandos en tu terminal para clonar el proyecto, instalar las dependencias necesarias, configurar la base de datos y cargar los datos de prueba de golpe:

```bash
# Pas 1: Clonar el repositori y entrar a la carpeta del proyecto
git clone https://github.com/edsonPC20/django-blog-project.git
cd my_site

# Pas 2: Instal·lar la dependencia de Django
pip install django

# Pas 3: Executar les migracions per crear la base de datos local (db.sqlite3)
python manage.py makemigrations
python manage.py migrate

# Pas 4: Poblar la Base de Dades carregant el fitxer JSON de les Fixtures
python manage.py loaddata blog/fixtures/initial_data.json

# Execució del projecte: Para arrancar el servidor de desarrollo local de Django, ejecuta el siguiente comando en tu terminal
python manage.py runserver

# Rutas disponibles en el Blog:
Página de Inicio: http://127.0.0.1:8000/ — "Muestra los 3 últimos posts publicados."

Todos los Posts: http://127.0.0.1:8000/posts — "Listado completo de todas las publicaciones."

Listado de Autores: http://127.0.0.1:8000/authors — "Tabla estilizada con los autores registrados."

Listado de Etiquetas: http://127.0.0.1:8000/tags — "Sección con filtros dinámicos para ver posts según su etiqueta."

Panel de Administración: http://127.0.0.1:8000/admin — "Gestión interna de los modelos de datos de Django."

## Documentació del projecte (Pydoc & GitHub Actions)

La documentación técnica de los archivos de código fuente (`.py`) se genera automáticamente mediante **Pydoc** en cada subida de código, gracias a un flujo de trabajo automatizado configurado con **GitHub Actions**.

Puedes visualizar de manera interactiva la documentación técnica del proyecto haciendo clic en el siguiente enlace:

📄 Rutas: https://edsonpc20.github.io/proyecto_Django/blog.urls.html

📄 Vistas: https://edsonpc20.github.io/proyecto_Django/blog.views.html

📄 Administrador: https://edsonpc20.github.io/proyecto_Django/manage.html