# Utiliser une image Python officielle comme base
FROM python:3.10-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers du projet
COPY pyproject.toml .
COPY README.md .
COPY src/ src/

# Installer les dépendances du projet
RUN pip install --no-cache-dir hatchling && \
    pip install --no-cache-dir .

# Définir le volume pour monter le code source
VOLUME ["/app"]

# Maintenir le conteneur en vie sans consommer de ressources
CMD ["tail", "-f", "/dev/null"] 