# Utiliser une image de base qui inclut les outils de compilation
FROM python:3.9-slim-buster

# Installation des dépendances système nécessaires
RUN apt-get update && apt-get install -y \
    build-essential \
    gfortran \
    libopenblas-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Définition du répertoire de travail
WORKDIR /app

# Copie et installation des dépendances Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Le code sera monté depuis l'hôte
CMD ["python", "main.py"] 