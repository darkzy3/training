# Utiliser une image de base Python officielle
FROM python:3.8

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers dans le conteneur
COPY . /app

# Installer les dépendances de l'application
RUN pip install -r requirements.txt

# Exposer le port sur lequel l'application s'exécute
EXPOSE 5000

# Définir la commande pour exécuter l'application
CMD ["python", "app.py"]