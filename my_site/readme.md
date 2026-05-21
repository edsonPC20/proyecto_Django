# Django Blog Project 

## 1. Introducció
Aquest projecte consisteix en el desenvolupament d'una aplicació web de Blog utilitzant el framework **Django**. L'objectiu principal és posar en pràctica els coneixements de programació web, disseny de bases de dades relacionals i arquitectura MVT (Model-Vista-Plantilla).

### Objectius principals:
* Gestionar un sistema dinàmic de publicacions (Posts) associats a Autors i Etiquetes (Tags).
* Implementar un sistema de rutes netes i amigables (URLs dinàmiques i Slugs).
* Modularitzar les vistes per oferir llistats i detalls específics de cada entitat.
* Poblar la base de dades de forma eficient mitjançant l'ús de *Fixtures*.

---

## 2. Instal·lació ràpida

Segueix aquests passos per configurar el projecte en el teu entorn local.

### Pas 1: Clonar el repositori
Clona el projecte des de GitHub a la teva màquina local:
```bash
git clone <URL_DE_TEU_REPOSITORI_AQUÍ>
cd my_site```

### Pas 2: Instal·lar dependències
Assegura't de tenir Python instal·lat. Després, instal·la Django i les dependències del projecte:
pip install django

### Pas 3: Executar migracions
Crea i aplica l'estructura de la base de dades local (db.sqlite3):
python manage.py makemigrations
python manage.py migrate

### Pas 4: Poblar la Base de Dades (Opcional - Fixtures)
Per carregar les dades de mostra del Blog (autors, posts i etiquetes inicials), executa:
python manage.py loaddata initial_data.json

## 3. Execució del projecte
Per arrancar el servidor de desenvolupament local de Django, executa el següent comando a la terminal:
python manage.py runserver

URL per accedir-hi
Un cop el servidor estigui en marxa, pots accedir a l'aplicació mitjançant les següents adreces al teu navegador:

Pàgina d'Inici (Home): http://127.0.0.1:8000/ — Mostra els últims posts.

Llistat d'Autors: http://127.0.0.1:8000/authors — Taula amb els autors del blog.

Llistat d'Etiquetes (Tags): http://127.0.0.1:8000/tags — Filtre de posts per temàtica.
