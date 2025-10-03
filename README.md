🎟️ EventHub — Guide de démarrage



App Django d’événements (utilisateurs/roles, participations, avis) + Postgres en Docker + import d’un dump.sql.

🚀 TL;DR
# 1) Lancer Postgres (importe automatiquement dump.sql au 1er run)
docker compose up -d

# 2) Créer l’env Python
python -m venv .venv && source .venv/bin/activate  # Win: .venv\Scripts\Activate.ps1

# 3) Installer les deps
pip install -r requirements.txt

# 4) Appliquer les migrations (schéma déjà présent via dump)
python manage.py migrate --fake-initial

# 5) Démarrer Django
python manage.py runserver


Appli dispo sur http://127.0.0.1:8000/

# Démarrage
docker compose up -d

# Suivre les logs (utile pour voir l’import du dump au premier run)
docker logs -f postgres-db

🔁 Réimporter dump.sql

Importer manuellement dans la base en cours d’exécution :

# depuis la racine du projet
cat dump.sql | docker exec -i postgres-db psql -U jessy -d events

🐍 Application Django (local)
1) Environnement
python -m venv .venv
# macOS / Linux
source .venv/bin/activate
# Windows PowerShell
.venv\Scripts\Activate.ps1

pip install --upgrade pip
pip install -r requirements.txt

2) Configuration DB

Par défaut, la connexion pointe vers Postgres local (Docker) :

# settings.py (extrait)
DATABASES = {
  "default": {
    "ENGINE": "django.db.backends.postgresql",
    "NAME": "events",
    "USER": "jessy",
    "PASSWORD": "event",
    "HOST": "127.0.0.1",
    "PORT": "5432",
  }
}


Ces valeurs correspondent au docker-compose.yml. Modifie-les si tu changes le compose. 

docker-compose

3) Migrations

Si le schéma/table existe déjà via dump.sql : aligne l’état des migrations sans recréer les tables :

python manage.py migrate --fake-initial


Si tu pars d’une base vide :

python manage.py migrate

4) Lancer le serveur
python manage.py runserver

(Optionnel) Superuser
python manage.py createsuperuser

🗂️ Arborescence
.
├─ account/               # app users
├─ eventhub/              # projet Django (settings)
├─ events/                # app événements
├─ participation/         # app participations
├─ reviews/               # app avis
├─ templates/             # templates Django
├─ theme/                 # styles / assets
├─ docker-compose.yml     # Postgres (+ import auto dump.sql)  ← important
├─ dump.sql               # schéma + données
├─ manage.py
└─ requirements.txt

📜 Licence

Usage interne / éducatif (adapte selon tes besoins).
